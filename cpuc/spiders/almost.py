import scrapy
from scrapy import FormRequest
from cpuc.items import DocumentDetail, Document, File, ProceedingDetail


class CpucSpider(scrapy.Spider):
    name = "cpuc"
    allowed_domains = ['cpuc.ca.gov']

    start_urls = ['http://docs.cpuc.ca.gov/advancedsearchform.aspx']

    def parse(self, response):
        formdata = {
                    '__EVENTARGUMENT': '',
                    '__EVENTTARGET': '',
                    'FilingDateFrom': '06/19/19',
                    'FilingDateTo': '06/20/19',
                    '__VIEWSTATEGENERATOR': '6DB12421',
                    'DocTitle': '',
                    'ddlCpuc01Types': '-1',
                    'IndustryID': '-1',
                    'ProcNum': '',
                    'MeetDate': '',
                    'PubDateFrom': '',
                    'PubDateTo': '',
                    'EfileConfirmNum': '',
                    'SearchButton': 'Search',
                    '__VIEWSTATE': '/wEPDwUKLTk2MTY0MzkwOQ9kFgICBQ9kFgYCCQ8QDxYGHg5EYXRhVmFsdWVGaWVsZAUJRG9jVHlwZUlEHg1EYXRhVGV4dEZpZWxkBQtEb2NUeXBlRGVzYx4LXyFEYXRhQm91bmRnZBAVEA4tLVNlbGVjdCBPbmUtLQZBZ2VuZGEORGFpbHkgQ2FsZW5kYXIPQWdlbmRhIERlY2lzaW9uEENvbW1lbnQgRGVjaXNpb24ORmluYWwgRGVjaXNpb24NR2VuZXJhbCBPcmRlciZJdGVtIGZvciBsZWdpc2xhdGl2ZSBzZWN0aW9uIG9mIGFnZW5kYQxOZXdzIFJlbGVhc2UGUmVwb3J0EUFnZW5kYSBSZXNvbHV0aW9uEkNvbW1lbnQgUmVzb2x1dGlvbhBGaW5hbCBSZXNvbHV0aW9uH1J1bGVzIG9mIFByYWN0aWNlIGFuZCBQcm9jZWR1cmUGUnVsaW5nFUUtRmlsZWQgRG9jdW1lbnQgVHlwZRUQAi0xATEBOQIxNwIxOAIxOQIyOQIzMgI0MAI1MAI1MwI1NAI1NQI1NwI1OAItNRQrAxBnZ2dnZ2dnZ2dnZ2dnZ2dnZGQCCw8QDxYGHwAFCURvY1R5cGVJRB8BBQtEb2NUeXBlRGVzYx8CZ2QPFk4CAQICAgMCBAIFAgYCBwIIAgkCCgILAgwCDQIOAg8CEAIRAhICEwIUAhUCFgIXAhgCGQIaAhsCHAIdAh4CHwIgAiECIgIjAiQCJQImAicCKAIpAioCKwIsAi0CLgIvAjACMQIyAjMCNAI1AjYCNwI4AjkCOgI7AjwCPQI+Aj8CQAJBAkICQwJEAkUCRgJHAkgCSQJKAksCTAJNAk4WThAFDkFMSiBSZXNvbHV0aW9uBQMxMzBnEAUJQWx0ZXJuYXRlBQI2OWcQBRNBbWVuZGVkIEFwcGxpY2F0aW9uBQI2N2cQBRFBbWVuZGVkIENvbXBsYWludAUCNjhnEAUJQW1lbmRtZW50BQI3MGcQBQZBbnN3ZXIFAjcxZxAFBkFwcGVhbAUCNzJnEAUVQXBwZWFsIENhdGVnb3JpemF0aW9uBQI3M2cQBQtBcHBsaWNhdGlvbgUCNjZnEAUVQXJiaXRyYXRpb24gQWdyZWVtZW50BQI3NWcQBRFBcmJpdHJhdG9yIFJlcG9ydAUCNzRnEAUIQXNzaWduZWQFAjc2ZxAFBUJyaWVmBQI3N2cQBQhDYWxlbmRhcgUCODBnEAUWQ2VydGlmaWNhdGUgb2YgU2VydmljZQUCODVnEAUPQ2l0YXRpb24gQXBwZWFsBQMxNDhnEAUIQ29tbWVudHMFAjgyZxAFFUNvbW1lbnRzIG9uIEFsdGVybmF0ZQUCODNnEAUYQ29tbWlzc2lvbiBJbnZlc3RpZ2F0aW9uBQI5OWcQBRVDb21taXNzaW9uIFJ1bGVtYWtpbmcFAzExMmcQBQlDb21wbGFpbnQFAjc4ZxAFEENvbXBsYWludCBBbnN3ZXIFAjc5ZxAFEUNvbXBsaWFuY2UgRmlsaW5nBQI4MWcQBRhDb25zb2xpZGF0ZWQgUHJvY2VlZGluZ3MFAjg0ZxAFCURlZmVuZGFudAUCODZnEAURRGVuaWFsIG9mIEV4cGFydGUFAjkyZxAFDkRyYWZ0IERlY2lzaW9uBQI4N2cQBQpFeGNlcHRpb25zBQI5NGcQBQdFeGhpYml0BQI5M2cQBQdFeHBhcnRlBQI5NWcQBQ5GZWUgLSBSdWxlIDIuNQUCOThnEAUERmVlcwUCOTZnEAUOSWRlbnRpZmljYXRpb24FAzEwMGcQBQdJbXBvdW5kBQMxMDFnEAUVSW5zdHJ1Y3Rpb24gdG8gQW5zd2VyBQMxMDJnEAUbSW5zdHJ1Y3Rpb24gdG8gQW5zd2VyIFNCOTYwBQMxMDNnEAUMTGF3ICYgTW90aW9uBQMxMDRnEAUKTWVtb3JhbmR1bQUDMTA1ZxAFFE1pc2NlbGxhbmVvdXMgRmlsaW5nBQMxMDZnEAUGTW90aW9uBQMxMDdnEAUXTW90aW9uIGZvciBSZWFzc2lnbm1lbnQFAzEyM2cQBQlOT0kgRmlsZWQFAzEwOGcQBQxOT0kgVGVuZGVyZWQFAzE0NGcQBQZOb3RpY2UFAzEwOWcQBRBOb3RpY2Ugb2YgRGVuaWFsBQI5MWcQBQlPYmplY3Rpb24FAzExMWcQBQpPcHBvc2l0aW9uBQMxMTNnEAUFT3JkZXIFAzExMGcQBQhQZXRpdGlvbgUDMTE4ZxAFGVBldGl0aW9uIGZvciBNb2RpZmljYXRpb24FAzEyMGcQBShQZXRpdGlvbiBUbyBBZG9wdCBBbWVuZCBPciBSZXBlYWwgUmVndWwuBQMxMjJnEAUfUHJlaGVhcmluZyBDb25mZXJlbmNlIFN0YXRlbWVudAUDMTE5ZxAFG1ByZXNpZGluZyBPZmZpY2VycyBEZWNpc2lvbgUDMTIxZxAFE1ByaW1hcnkgUGFydGljaXBhbnQFAzExNWcQBSNQcm9wb25lbnRzIEVudmlyb25tZW50YWwgQXNzZXNzbWVudAUDMTE3ZxAFEVByb3Bvc2VkIERlY2lzaW9uBQMxMTZnEAUHUHJvdGVzdAUDMTE0ZxAFClJlYXNzaWduZWQFAzEyNmcQBQxSZWNhbGVuZGFyZWQFAzEyNWcQBRFSZWhlYXJpbmcgUmVxdWVzdAUDMTI0ZxAFEFJlamVjdGlvbiBMZXR0ZXIFAzEzM2cQBQVSZXBseQUDMTI3ZxAFBlJlcG9ydAUDMTI4ZxAFB1JlcXVlc3QFAzEyOWcQBSFSZXNvbHV0aW9uIEFMSi0xNzYgQ2F0ZWdvcml6YXRpb24FAzEzMWcQBQhSZXNwb25zZQUDMTMyZxAFBlJ1bGluZwUDMTM2ZxAFDlNjb3BpbmcgUnVsaW5nBQMxMzVnEAUJU3RhdGVtZW50BQMxMzhnEAULU3RpcHVsYXRpb24FAzEzOWcQBQhTdWJwb2VuYQUDMTQwZxAFClN1cHBsZW1lbnQFAzE0MWcQBQxTdXBwbGVtZW50YWwFAzEzN2cQBSVTdXBwbGVtZW50YWwgQ29uc29saWRhdGVkIFByb2NlZWRpbmdzBQMxNDJnEAUTU3VwcG9ydGluZyBEb2N1bWVudAUDMTQ3ZxAFCVRlc3RpbW9ueQUDMTQzZxAFClRyYW5zY3JpcHQFAzE0NWcQBQpXaXRoZHJhd2FsBQMxNDZnZGQCDw8QDxYGHwAFCkluZHVzdHJ5SUQfAQUMSW5kdXN0cnlOYW1lHwJnZA8WBwIBAgICAwIEAgUCBgIHFgcQBQZFbmVyZ3kFATFnEAUOVHJhbnNwb3J0YXRpb24FATJnEAULV2F0ZXIvU2V3ZXIFATNnEAUOQ29tbXVuaWNhdGlvbnMFATRnEAUFT3RoZXIFATVnEGUFAjE0ZxAFDk11bHRpcGxlIFR5cGVzBQIxNWdkZGQrMOijrhj2nAD696/Nqu10v92XtvVvSDLWV5SpZjUXRw==',
                    '__EVENTVALIDATION': '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'
                    }
        yield FormRequest.from_response(response,
                                        formdata=formdata,
                                        method='POST',
                                        callback=self.parse_search_result
                                        )

    def parse_search_result(self, response):
        proceeding_set = set()
        table_rows = response.xpath("//table[@id='ResultTable']/tbody/tr")
        skip = False
        for row in table_rows:
            if not skip:
                proceeding_number = row.xpath("td[@class='ResultTitleTD']/text()")[1].get()
                len_str = len(proceeding_number)
                proceeding_number = proceeding_number[12: len_str]
                if len(proceeding_number) > 8:
                    proceeding_number = proceeding_number[0:8]
                proceeding_set.add(proceeding_number)
                skip = True
            else:
                skip = False
        for proceeding_number in proceeding_set:
            next_page = 'https://apps.cpuc.ca.gov/apex/f?p=401:56:6062906969229::NO:RP,57,RIR:P5_PROCEEDING_SELECT:{}'\
                .format(proceeding_number)
            yield response.follow(next_page, callback=self.parse_proceeding_number,
                                  meta={'proceeding_number': proceeding_number})
        formdata = {
            '__EVENTTARGET': 'lnkNextPage',
            '__VIEWSTATEGENERATOR': response.xpath("//input[@id='__VIEWSTATEGENERATOR']/@value").get(),
            '__VIEWSTATE': response.xpath("//input[@id='__VIEWSTATE']/@value").get(),
            '__EVENTVALIDATION': response.xpath("//input[@id='__EVENTVALIDATION']/@value").get()
        }
        yield FormRequest(
            url='http://docs.cpuc.ca.gov/SearchRes.aspx',
            formdata=formdata,
            callback=self.parse_search_result
        )

    def parse_proceeding_number(self, response):
        proceeding_details = ProceedingDetail()
        table_rows = response.xpath("//table[@id='apex_layout_1757486743389754952']/tr")
        filling_parties = list()
        for filled_party in table_rows.xpath("td[position()=2]//span[@id='P56_FILED_BY']/text()"):
            filling_parties.append(filled_party.get())

        proceeding_details['filing_parties'] = filling_parties

        industries = list()
        for industry in table_rows.xpath("td[position()=2]//span[@id='P56_INDUSTRY']/text()"):
            industries.append(industry.get())
        proceeding_details['industries'] = industries

        proceeding_details['filled_on'] = table_rows.xpath("td[position()=2]//span[@id='P56_FILING_DATE']/text()").get()
        proceeding_details['status'] = table_rows.xpath("td[position()=2]//span[@id='P56_STATUS']/text()").get()
        proceeding_details['proceeding_type'] = table_rows.xpath("td[position()=2]//span[@id='P56_CATEGORY']/text()").get()
        proceeding_details['title'] = table_rows.xpath("td[position()=2]//span[@id='P56_DESCRIPTION']/text()").get()

        assignees = list()
        for industry in table_rows.xpath("td[position()=2]//span[@id='P56_STAFF']/text()"):
            assignees.append(industry.get())
        proceeding_details['assignees'] = assignees

        cookie = response.request.headers.getlist("Cookie")

        yield scrapy.Request(
            url='https://apps.cpuc.ca.gov/apex/f?p=401:57:0::NO',
            callback=self.save_document,
            errback=self.error_back,
            headers={'Cookie': cookie},
            dont_filter=True,
            meta={'details': proceeding_details, 'dont_merge_cookies': True}
        )

    def error_back(self, failure):
        print(failure)

    def save_document(self, response):
        table_documents = response.xpath("//div[@id='apexir_DATA_PANEL']//table[@class='apexir_WORKSHEET_DATA']"
                                         "//tr")
        skip = True     # first row is empty that's why skip one time
        for data in table_documents:
            document_detail = DocumentDetail()
            if skip:
                skip = False
            else:
                column_no = 1
                for columns in data.xpath("td"):        # for fetching each column of table
                    if column_no == 1:
                        document_detail['filling_date'] = columns.xpath("text()").get()
                        column_no += 1
                    elif column_no == 2:
                        document_detail['document_link'] = columns.xpath("a/@href").get()
                        print(document_detail['document_link'])
                        document_detail['document_type'] = columns.xpath("a/span/u/text()").get()
                        column_no += 1
                    elif column_no == 3:
                        for filled_party in columns.xpath("text()"):
                            document_detail['filled_by'] = filled_party.get()

                        column_no += 1
                    elif column_no == 4:
                        document_detail['description'] = columns.xpath("text()").get()

                yield response.follow(document_detail['document_link'], callback=self.download_pdf,
                                      meta={'document': document_detail, 'dont_merge_cookies': True})

            formdata = {
                '__EVENTARGUMENT': '',
                '__EVENTTARGET': 'lnkNextPage',
                '__VIEWSTATEGENERATOR': 'F8727AE4',
                '__VIEWSTATE': '/wEPDwUKLTk4MTE4OTkyNQ9kFgICBQ9kFgwCAQ8PFgIeB1Zpc2libGVoZGQCAg8PFgIfAGhkZAIDDw8WAh8AaGRkAgQPFgIeC18hSXRlbUNvdW50AgQWCGYPZBYEAgEPDxYCHg9Db21tYW5kQXJndW1lbnQFATFkFgJmDxUBATFkAgIPFQEBIGQCAQ9kFgQCAQ8PFgIfAgUBMmQWAmYPFQEBMmQCAg8VAQEgZAICD2QWBAIBDw8WAh8CBQEzZBYCZg8VAQEzZAICDxUBASBkAgMPZBYEAgEPDxYCHwIFATRkFgJmDxUBATRkAgIPFQEBIGQCBg8PFgIfAGhkZAIIDxYCHwECFBYoAgEPZBYCZg8VBVJSdWxpbmcgZmlsZWQgYnkgQUxKL0ZJVENIL0NQVUMgb24gMDYvMTcvMjAxOSBDb25mIyAxMzU3MjggKENlcnRpZmljYXRlIE9mIFNlcnZpY2UpFFByb2NlZWRpbmc6IFIxMzExMDA1D0UtRmlsZWQ6IFJ1bGluZ088YSBocmVmPScvUHVibGlzaGVkRG9jcy9FZmlsZS9HMDAwL00zMDIvSzI0MC8zMDIyNDA3NDguUERGJz5QREY8L2E+ICg3NiBLQik8YnI+CjA2LzE4LzIwMTlkAgMPZBYCZg8VBTlSdWxpbmcgZmlsZWQgYnkgQUxKL0ZJVENIL0NQVUMgb24gMDYvMTcvMjAxOSBDb25mIyAxMzU3MjgUUHJvY2VlZGluZzogUjEzMTEwMDUPRS1GaWxlZDogUnVsaW5nUDxhIGhyZWY9Jy9QdWJsaXNoZWREb2NzL0VmaWxlL0cwMDAvTTMwMi9LMjQwLzMwMjI0MDg1Ny5QREYnPlBERjwvYT4gKDE3NSBLQik8YnI+CjA2LzE4LzIwMTlkAgUPZBYCZg8VBVNSdWxpbmcgZmlsZWQgYnkgQUxKL1NFTUNFUi9DUFVDIG9uIDA2LzE3LzIwMTkgQ29uZiMgMTM1NjgwIChDZXJ0aWZpY2F0ZSBPZiBTZXJ2aWNlKRRQcm9jZWVkaW5nOiBSMTgxMjAwNQ9FLUZpbGVkOiBSdWxpbmdPPGEgaHJlZj0nL1B1Ymxpc2hlZERvY3MvRWZpbGUvRzAwMC9NMzAzL0swNzQvMzAzMDc0MjAzLlBERic+UERGPC9hPiAoNzYgS0IpPGJyPgowNi8xOC8yMDE5ZAIHD2QWAmYPFQU6UnVsaW5nIGZpbGVkIGJ5IEFMSi9TRU1DRVIvQ1BVQyBvbiAwNi8xNy8yMDE5IENvbmYjIDEzNTY4MBRQcm9jZWVkaW5nOiBSMTgxMjAwNQ9FLUZpbGVkOiBSdWxpbmdQPGEgaHJlZj0nL1B1Ymxpc2hlZERvY3MvRWZpbGUvRzAwMC9NMzAyL0s5NDIvMzAyOTQyMjg5LlBERic+UERGPC9hPiAoMTI0IEtCKTxicj4KMDYvMTgvMjAxOWQCCQ9kFgJmDxUFUFJ1bGluZyBmaWxlZCBieSBBTEovS0FPL0NQVUMgb24gMDYvMTcvMjAxOSBDb25mIyAxMzU2NzkgKENlcnRpZmljYXRlIE9mIFNlcnZpY2UpFFByb2NlZWRpbmc6IEExODEyMDE3D0UtRmlsZWQ6IFJ1bGluZ088YSBocmVmPScvUHVibGlzaGVkRG9jcy9FZmlsZS9HMDAwL00zMDIvSzk0Mi8zMDI5NDIyODguUERGJz5QREY8L2E+ICg3NiBLQik8YnI+CjA2LzE4LzIwMTlkAgsPZBYCZg8VBTdSdWxpbmcgZmlsZWQgYnkgQUxKL0tBTy9DUFVDIG9uIDA2LzE3LzIwMTkgQ29uZiMgMTM1Njc5FFByb2NlZWRpbmc6IEExODEyMDE3D0UtRmlsZWQ6IFJ1bGluZ1A8YSBocmVmPScvUHVibGlzaGVkRG9jcy9FZmlsZS9HMDAwL00zMDIvSzI0MC8zMDIyNDA4NDguUERGJz5QREY8L2E+ICgxMzQgS0IpPGJyPgowNi8xOC8yMDE5ZAIND2QWAmYPFQUiR1JTIEF0dGFjaG1lbnQgM19SZXBvcnQgMDYuMTcuMjAxORRQcm9jZWVkaW5nOiBSMTUwMTAwOBxFLUZpbGVkOiBTdXBwb3J0aW5nIERvY3VtZW50UzxhIGhyZWY9Jy9QdWJsaXNoZWREb2NzL1N1cERvYy9SMTUwMTAwOC8yMTIxLzMwMTk0NTk4MS5wZGYnPlBERjwvYT4gKDM3MzYwMyBLQik8YnI+CjA2LzE4LzIwMTlkAg8PZBYCZg8VBTFHUlMgLSBBcHBlbmRpeCA5X0VtaXNzaW9uIEZhY3RvcnNfMDYuMTcuMjAxOS54bHN4FFByb2NlZWRpbmc6IFIxNTAxMDA4HEUtRmlsZWQ6IFN1cHBvcnRpbmcgRG9jdW1lbnRTPGEgaHJlZj0nL1B1Ymxpc2hlZERvY3MvU3VwRG9jL1IxNTAxMDA4LzIxMjEvMzAyMjk4MDM5LnBkZic+UERGPC9hPiAoMTA0NDk0IEtCKTxicj4KMDYvMTgvMjAxOWQCEQ9kFgJmDxUFMUdSUyAtIEFwcGVuZGl4IDhfVGVtcGxhdGUgU3VtbWFyeV8wNi4xNy4yMDE5Lnhsc3gUUHJvY2VlZGluZzogUjE1MDEwMDgcRS1GaWxlZDogU3VwcG9ydGluZyBEb2N1bWVudFM8YSBocmVmPScvUHVibGlzaGVkRG9jcy9TdXBEb2MvUjE1MDEwMDgvMjEyMS8zMDIyNDA4NDYucGRmJz5QREY8L2E+ICgxMTQ4ODcgS0IpPGJyPgowNi8xOC8yMDE5ZAITD2QWAmYPFQUzR1JTIC0gQXBwZW5kaXggN19TdG9yYWdlIEZhY2lsaXRpZXNfMDYuMTcuMjAxOS54bHN4FFByb2NlZWRpbmc6IFIxNTAxMDA4HEUtRmlsZWQ6IFN1cHBvcnRpbmcgRG9jdW1lbnRTPGEgaHJlZj0nL1B1Ymxpc2hlZERvY3MvU3VwRG9jL1IxNTAxMDA4LzIxMjEvMzAxOTI0OTkwLnBkZic+UERGPC9hPiAoMjAwNTYyIEtCKTxicj4KMDYvMTgvMjAxOWQCFQ9kFgJmDxUFLEdSUyAtIEFwcGVuZGl4IDZfTVNBIFN5c3RlbXNfMDYuMTcuMjAxOS54bHN4FFByb2NlZWRpbmc6IFIxNTAxMDA4HEUtRmlsZWQ6IFN1cHBvcnRpbmcgRG9jdW1lbnRTPGEgaHJlZj0nL1B1Ymxpc2hlZERvY3MvU3VwRG9jL1IxNTAxMDA4LzIxMjEvMzAyMjQwNzQwLnBkZic+UERGPC9hPiAoMTUyNzA5IEtCKTxicj4KMDYvMTgvMjAxOWQCFw9kFgJmDxUFYFNXR2FzIChVIDkwNSBHKV9SZXNwb25zZSB0byBTRUQgRGF0YSBSZXF1ZXN0IChTb3V0aHdlc3QgR2FzIFIxNS0wMS0wMDggMjAxOSBBbm51YWwgUmVwb3J0KV9GSU5BTBRQcm9jZWVkaW5nOiBSMTUwMTAwOBxFLUZpbGVkOiBTdXBwb3J0aW5nIERvY3VtZW50VTxhIGhyZWY9Jy9QdWJsaXNoZWREb2NzL1N1cERvYy9SMTUwMTAwOC8yMTIwLzMwMTkyNDk4OC5wZGYnPlBERjwvYT4gKDc1OTIzOTQxIEtCKTxicj4KMDYvMTgvMjAxOWQCGQ9kFgJmDxUFVVJ1bGluZyBmaWxlZCBieSBBTEovSlVOR1JFSVMvQ1BVQyBvbiAwNi8xNy8yMDE5IENvbmYjIDEzNTY4NSAoQ2VydGlmaWNhdGUgT2YgU2VydmljZSkUUHJvY2VlZGluZzogQTE5MDMwMDgPRS1GaWxlZDogUnVsaW5nUDxhIGhyZWY9Jy9QdWJsaXNoZWREb2NzL0VmaWxlL0cwMDAvTTMwMy9LMDc0LzMwMzA3NDIwMS5QREYnPlBERjwvYT4gKDE0NSBLQik8YnI+CjA2LzE3LzIwMTlkAhsPZBYCZg8VBTxSdWxpbmcgZmlsZWQgYnkgQUxKL0pVTkdSRUlTL0NQVUMgb24gMDYvMTcvMjAxOSBDb25mIyAxMzU2ODUUUHJvY2VlZGluZzogQTE5MDMwMDgPRS1GaWxlZDogUnVsaW5nUDxhIGhyZWY9Jy9QdWJsaXNoZWREb2NzL0VmaWxlL0cwMDAvTTMwMS9LOTQ1LzMwMTk0NTk4MC5QREYnPlBERjwvYT4gKDExNyBLQik8YnI+CjA2LzE3LzIwMTlkAh0PZBYCZg8VBSZSMTUwMTAwOC1QR0UtTkdMQS1BcHAwNi1SZWRhY3RlZC1QYXJ0MhRQcm9jZWVkaW5nOiBSMTUwMTAwOBxFLUZpbGVkOiBTdXBwb3J0aW5nIERvY3VtZW50VTxhIGhyZWY9Jy9QdWJsaXNoZWREb2NzL1N1cERvYy9SMTUwMTAwOC8yMTE5LzMwMTkyNDk4Ni5wZGYnPlBERjwvYT4gKDE2MzE4MjcxIEtCKTxicj4KMDYvMTcvMjAxOWQCHw9kFgJmDxUFJlIxNTAxMDA4LVBHRS1OR0xBLUFwcDA2LVJlZGFjdGVkLVBhcnQxFFByb2NlZWRpbmc6IFIxNTAxMDA4HEUtRmlsZWQ6IFN1cHBvcnRpbmcgRG9jdW1lbnRVPGEgaHJlZj0nL1B1Ymxpc2hlZERvY3MvU3VwRG9jL1IxNTAxMDA4LzIxMTgvMzAxOTI0OTg1LnBkZic+UERGPC9hPiAoMTcyNDE2OTYgS0IpPGJyPgowNi8xNy8yMDE5ZAIhD2QWAmYPFQUWU3VtbWFyeSBTaGVldF9KQ01fMjAyMBRQcm9jZWVkaW5nOiBBMTcwMTAxMxxFLUZpbGVkOiBTdXBwb3J0aW5nIERvY3VtZW50VDxhIGhyZWY9Jy9QdWJsaXNoZWREb2NzL1N1cERvYy9BMTcwMTAxMy8yMTE2LzMwMTkyNDk4Mi5wZGYnPlBERjwvYT4gKDExNzQ1MjYgS0IpPGJyPgowNi8xNy8yMDE5ZAIjD2QWAmYPFQU6TUNFIFBHRSBKb2ludCBDb29wZXJhdGlvbiBDZXJ0aWZpY2F0ZSBvZiBTZXJ2aWNlIDYtMTctMjAxORRQcm9jZWVkaW5nOiBBMTcwMTAxMxxFLUZpbGVkOiBTdXBwb3J0aW5nIERvY3VtZW50UzxhIGhyZWY9Jy9QdWJsaXNoZWREb2NzL1N1cERvYy9BMTcwMTAxMy8yMTE2LzMwMjI5ODAzMy5wZGYnPlBERjwvYT4gKDUxNzUzMiBLQik8YnI+CjA2LzE3LzIwMTlkAiUPZBYCZg8VBTdNQ0UgQWR2aWNlIExldHRlciAzNi1FIFBHJkUgQWR2aWNlIExldHRlciA0MTA3LUctNTU2My1FFFByb2NlZWRpbmc6IEExNzAxMDEzHEUtRmlsZWQ6IFN1cHBvcnRpbmcgRG9jdW1lbnRTPGEgaHJlZj0nL1B1Ymxpc2hlZERvY3MvU3VwRG9jL0ExNzAxMDEzLzIxMTYvMzAyMjg2MTkwLnBkZic+UERGPC9hPiAoNDg5NjQzIEtCKTxicj4KMDYvMTcvMjAxOWQCJw9kFgJmDxUFTUExODAzMDA5IFNDRS0wNC1BIEJsZWRzb2UgRVJSQVRBIFJlYXNvbmFibGVuZXNzIG9mIFNPTkdTIDEgRXhwZW5zZXMgMjAxNi0yMDE3FFByb2NlZWRpbmc6IEExODAzMDA5HEUtRmlsZWQ6IFN1cHBvcnRpbmcgRG9jdW1lbnRTPGEgaHJlZj0nL1B1Ymxpc2hlZERvY3MvU3VwRG9jL0ExODAzMDA5LzIxMTUvMzAyMjg2MTg5LnBkZic+UERGPC9hPiAoMTg3NDk5IEtCKTxicj4KMDYvMTcvMjAxOWRkgbFULY0pkImMgHBcD01P0VFUvs+M4zbGffzxJNPjwks=',
                '__EVENTVALIDATION': '/wEdAAs7/SzGrJTxWQTlgEuFeQdE+KzX0FwelcUOhBan/b5uzOgvnuFPcTGgEjLUkdWZc9Q3HyTnWxBPDserVE5AdOKMboAdnFN9V8/jdI6JisscRk4bsve4h24cI1UNeqgIUed3XcL1uN8jICMXmyKyKvRhmxqxgsKed83dLNmKlXfwAJr9MmqSrK6WW0iyGSBDO3+z+wwn6BZL4VHpTU8Tzi856xnhpwsSGQBSYSfF1dWHPbdnme2xzh8PLXfskS+CalL/7mh8OVdGW0F8+RGYNcsD'
            }
            yield FormRequest.from_response(response,
                                            formdata=formdata, method='POST', callback=self.save_document)

    def download_pdf(self, response):
        document_detail = response.meta['document']
        table_rows = response.xpath("//table[@id='ResultTable']/tbody/tr")
        skip = False
        documents = list()
        files_list = list()
        for row in table_rows:
            document = Document()
            if not skip:
                document['title'] = row.xpath("td[@class='ResultTitleTD']/text()").get()
                document['link'] = response.urljoin(row.xpath("td[@class='ResultLinkTD']/a/@href").get())
                files_list.append(document['link'])
                document['type'] = row.xpath("td[@class='ResultTypeTD']/text()").get()
                document['date'] = row.xpath("td[@class='ResultDateTD']/text()").get()
                documents.append(document)
                skip = True
            else:
                skip = False

        document_detail['documents'] = documents
        files = File()
        files['file_urls'] = files_list
        # yield files
        yield document_detail

