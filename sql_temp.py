
sql_template = '''
           INSERT INTO `resource_manager`.`tb_position_resource_data` (`position_id`, `type`, `mode`, `daily_pv`, `average_ctr`, `cut_off_ctr`, `cpm`, `update_time` ) 
           VALUES	( %d, 1, 1, 0, 0.000000, 0.000000, 0.000000,now() ),( %d, 1, 2, 0, 0.000000, 0.000000, 0.000000, now() );
       '''

def format_sql(position_id, time_str) :
    sql = sql_template % (position_id, position_id)
    return sql

if __name__ == '__main__':
    position_id_list = [66000016, 66000017, 66000018]
    for position_id in position_id_list:
        print(format_sql(position_id,'2022-08-22 17:38:12' ))
