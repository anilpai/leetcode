class Solution(object):
    '''
    Question : https://www.codewars.com/kata/sort-the-columns-of-a-csv-file/
    '''
    def sort_csv_columns(self, csv_file_content, sep=';', end='\n'):
        '''Sort a CSV file by column name.'''
        csv_columns = zip(*(row.split(sep) for row in csv_file_content.split(end)))
        sorted_columns = sorted(csv_columns, key=lambda col: col[0].lower())
        return end.join(sep.join(row) for row in zip(*sorted_columns))


if __name__=='__main__':

    pre_sorting = (
            "myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n"
            "17945;10091;10088;3907;10132\n"
            "2;12;13;48;11"
        )

    post_sorting = (
             "Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n"
             "3907;17945;10091;10088;10132\n"
             "48;2;12;13;11"
        )

    s = Solution()
    print(s.sort_csv_columns(pre_sorting) == post_sorting)
