'''
Scrape Texas_deathRow_executed_table AND last_words data
Python 3.5+
'''


import os
import csv
import asyncio
import aiohttp
import logging
from hashlib import md5
from functools import wraps
from lxml.html import parse
from urllib.parse import urljoin
from urllib.error import HTTPError
from collections import OrderedDict


if not os.path.exists('.cache'):
    os.makedirs('.cache')


# 'get_total' is the cumulative count of GET requests
get_total = 0
# 'get_count' has the number of running GET requests
get_count = 0
# Never run more than 'get_limit' GET requests at a time
get_limit = 2


async def get(url):
    '''Returns the lxml tree of a URL, loading from a cache'''

    # Cache the file in .cache/<md5(URL)>
    path = os.path.join('.cache', md5(url.encode('utf-8')).hexdigest())

    # If the URL is not already cached, get it and cache it
    if not os.path.exists(path):
        global get_count, get_total

        # Keep releasing control and re-cheking periodically until we are below 'get_limit' running GET requests
        while get_count >= get_limit:
            await asyncio.sleep(0.1)

        # Get the URL
        get_count += 1
        get_total += 1

        logging.info('Task# %d (total: %d). %s', get_count, get_total, url)
        async with aiohttp.request('GET', url) as response:
            get_count -= 1

            # Save the response fully (without decoding) into the cache
            if response.status == 200:
                result = await response.text()
                with open(path, 'w') as handle:
                    handle.write(result)
            else:
                raise HTTPError(response.status)

    # URL is cached in path. Return the lxml tree
    return parse(path)


async def scrape():
    '''Scrape the Texas_DeathRow_Executed_List'''

    # Get all the data from the main index page
    url = 'https://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
    tree = await get(url)
    rows = []

    for row in tree.findall('.//tr')[1:]:
        cells = row.findall('td')
        rows.append(OrderedDict((
            ('id', cells[0].text),
            ('offender_info_link', urljoin(url, cells[1].find('a').get('href'))),
            ('last_words_link', urljoin(url, cells[2].find('a').get('href'))),
            ('last_name', cells[3].text),
            ('first_name', cells[4].text),
            ('tdcj_number', cells[5].text),
            ('age', cells[6].text),
            ('date', cells[7].text),
            ('race', cells[8].text),
            ('county', cells[9].text)
        )))

    # Get all the last word links -- asynchronously.
    last_words = await asyncio.gather(*(get(row['last_words_link']) for row in rows))

    # Parse each last words page and add last words into rows['last_words']
    for tree, row in zip(last_words, rows):
        paragraphs = tree.find('.//div[@id="body"]').findall('p')
        for i, para in enumerate(paragraphs):
            if para.get('class') == 'text_bold' and para.text.lower().strip().startswith('last statement'):
                row['last_words'] = '\n'.join(para.text_content() or '' for para in paragraphs[i + 1:])
                break

    # Save the file with UTF-8 encoding
    with open('DeathRowExecuted_scraped.csv', 'w', encoding='utf8') as handle:
        out = csv.DictWriter(handle, rows[0].keys(), lineterminator='\n')
        out.writeheader()
        out.writerows(rows)


### ### ###

# Log all information requests
logging.basicConfig(level=logging.INFO)

# main
loop = asyncio.get_event_loop()
loop.run_until_complete(scrape())
loop.close
