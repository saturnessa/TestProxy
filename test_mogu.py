from public import get_page, test_proxy, max, stats_result, is_proxy
import time

api_url = 'http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=03aaeef6cf0e41289cb54e630c605847&count=1&expiryDate=0&format=2'
wait = 6


def main():
    print('Testing mogu')
    used_time_list = []
    valid_count = 0
    total_count = 0
    while True:
        flag, result = get_page(api_url)
        if flag:
            proxy = result.strip()
            if is_proxy(proxy):
                total_count += 1
                print('Testing proxy', proxy)
                test_flag, test_result = test_proxy(proxy=proxy)
                if test_flag:
                    valid_count += 1
                    used_time_list.append(test_result)
                stats_result(used_time_list, valid_count, total_count)
        time.sleep(wait)
        if total_count == max:
            break


if __name__ == '__main__':
    main()
