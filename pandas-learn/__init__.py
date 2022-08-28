from matplotlib import pyplot as plt
if __name__ == '__main__':
    # vprofile_data = pd.read_csv("data/vprofile-2021-11.csv",index_col=['createdAt'],parse_dates=True)
    # vprofile_data_count = vprofile_data.groupby(['vType'])['vType'].count()
    # print(vprofile_data_count)
    # # vprofile_data_count.plot.bar()
    # # plt.show()
    #
    # person_data = vprofile_data[vprofile_data['vType']==1]
    # org_data = vprofile_data[vprofile_data['vType'] == 2][['uid','vType','companyType','companySubType','status']]
    # org_data = org_data.sort_index()
    # org_data = org_data['companyType']
    # print(org_data)
    # org_data.plot.area(figsize=(12, 4), subplots=True)
    # plt.show()
    uids = '247994913,205755977,103491001,25109527,381562037,126478630,221399689,221624198,101743730,83877026,182305663,381566849,139451296,381539191,58580173,85221679,328053583,296905422,380331794'
    uid_list = uids.split(',')
    for uid in uid_list:
        print(uid)









