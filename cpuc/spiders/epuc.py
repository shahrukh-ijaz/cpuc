import re

import scrapy
from scrapy import FormRequest
from datetime import datetime, timedelta

from scrapy.loader import ItemLoader

from cpuc.items import ProceedingDetail


class CpucSpider(scrapy.Spider):
    name = "epuc"
    allowed_domains = ['epuc.vermont.gov']
    start_urls = ['https://epuc.vermont.gov/?q=User']

    def parse(self, response):
        """ This function will do login ."""
        form_build_id = response.xpath("//*[@name='form_build_id']/@value").get()
        formdata = {
            'name': 'shahrukh.ijaz@arbisoft.com',
            'pass': 'shahrukh31',
            'form_id': 'user_login',
            'form_build_id': form_build_id,
            'op': 'Log in'
        }
        cookiejar = form_build_id
        return scrapy.FormRequest(
            url='https://epuc.vermont.gov/?q=User',
            formdata=formdata,
            meta={
                'cookiejar': cookiejar
            },
            method='POST',
            callback=self.redirect_to_search
            )

    def redirect_to_search(self, response):
        """ This function will redirect to the search case page."""
        return response.follow(
            url='https://epuc.vermont.gov/?q=node/101',
            callback=self.search_case,
            meta={'cookiejar': response.meta['cookiejar']}
        )

    def search_case(self, response):
        """This function make search for last two days dockets"""
        search_start_date = datetime.now().date()
        search_end_date = (datetime.now() - timedelta(days=2)).date()
        search_end_date = search_end_date.strftime("%m/%d/%Y")
        search_start_date = search_start_date.strftime("%m/%d/%Y")
        ecp_form_id = response.xpath("//input[@name='ecpFormId']/@value").get()

        formdata = {
            'formId': response.xpath("//*[@name='formId']/@value").get(),
            'data(181445)': str(search_end_date),
            'data(181445_right)': str(search_start_date),
            'eCourtFormCode': 'S-Document-Orders-Portal',
            'ecpFormId': ecp_form_id,
            'op': 'Search',
            'form_build_id': response.xpath("//input[@name='form_build_id']/@value").get(),
            'form_id': 'ecp_searchform_form'
        }

        return FormRequest.from_response(
            response=response,
            formdata=formdata,
            callback=self.parse_proceeding_numbers,
            meta={
                'cookiejar': response.meta['cookiejar']
            },
            dont_filter=True
        )

    def parse_proceeding_numbers(self, response):
        list_of_proceeding_numbers = list()
        list_of_proceeding_url = list()
        row_count = 0
        for row in response.xpath("//table[contains(@class, 'searchResultsPage')]/tr[@style='height:17px']"):
            list_of_proceeding_numbers.append(row.xpath("td[1]/span/@title").get().strip())
            row_count += 1
            list_of_proceeding_url.append(response.urljoin(row.xpath("td[1]/span/a/@href").get()))

        total_proceeding_numbers = int((response.xpath("//*[@id='edit-tablepager-bottom']//table//tr/td[1]"
                                                       "/text()").get()).split(" ")[0])

        current_page = response.xpath("//ul[@class='pagination']//li[@class=' active ']/a/text()").get()
        # current_page = response.xpath("//ul[@class='pagination']//li[@class=' active ']/a/text()").get()

        next_page = response.xpath("//ul[@class='pagination']/following-sibling::li[@class=' active ']").get()
        print("hello")
