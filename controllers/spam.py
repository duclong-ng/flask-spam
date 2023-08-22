import requests
def tv360(phone):
    cookies = {
        'img-ext': 'avif',
        'acw_tc': 'af93860b014c10e47943828a4465454296c08ecb6890d13d915efb4d82c47d22',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_bac9e40a-428b-48f4-bfa2-90d6f3dedae3.xatMpLy%2F02fwATJ370k5AXdykbaPvGWUu6s2nkEeahc',
        'shared-device-id': 'web_bac9e40a-428b-48f4-bfa2-90d6f3dedae3',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        '_gid': 'GA1.2.2101359280.1692360676',
        '_gat_UA-180935206-1': '1',
        '_ga': 'GA1.1.338574088.1692360676',
        'G_ENABLED_IDPS': 'google',
        '_ga_E5YP28Y8EF': 'GS1.1.1692360675.1.1.1692360698.0.0.0',
        '_ga_D7L53J0JMS': 'GS1.1.1692360675.1.1.1692360698.37.0.0',
        'session-id': 's%3A6ad273c9-3b9b-435f-9761-b172188a34d0.6cj%2FiDb7X6T1LOs2hvLSlZGsBjruOrOTeY2q%2BwiVnhQ',
    }

    headers = {
        'authority': 'tv360.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://tv360.vn',
        'referer': 'https://tv360.vn/login',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1692360698646',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)

    print(response.text)

def myVT(phone):
    cookies = {
        'laravel_session': 'Jp1mjLOxH5QwDhwnlm5RGa2S6xdCMak2HW4nHL29',
        '_gcl_au': '1.1.212914999.1692361758',
        '_ga_VH8261689Q': 'GS1.1.1692361758.1.0.1692361758.60.0.0',
        '_ga': 'GA1.2.655914714.1692361758',
        '_gid': 'GA1.2.1344508402.1692361758',
        '_gat_UA-58224545-1': '1',
        '_ga_GR6VMPGW3N': 'GS1.2.1692361758.1.0.1692361758.60.0.0',
        '__zi': '3000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NSqtr_JpqH9BtdJDixxJ70wQSikvjzPG3PrqXhsvqLO0b3OpC0.1',
        'XSRF-TOKEN': 'eyJpdiI6ImxWdHIwTHFzZWMydDRsdjdrbVIrSVE9PSIsInZhbHVlIjoiUlhreEhwZGxsMTJzQnQyVXdVaUZXd3JEMzJmaU04Nm0rRm1BU0NqM1dLM0NiVzFtaVhCQVJXRWlFZmpwZFlrUCIsIm1hYyI6IjQyZDQxMTgyYmEwNTRiN2FmMDI0ZGM5NTc0MjNkYmJiZTdjMmU2Y2ZhYzRkMTYxYjdmODc4N2ZjZmM4Y2QyYjEifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=Jp1mjLOxH5QwDhwnlm5RGa2S6xdCMak2HW4nHL29; _gcl_au=1.1.212914999.1692361758; _ga_VH8261689Q=GS1.1.1692361758.1.0.1692361758.60.0.0; _ga=GA1.2.655914714.1692361758; _gid=GA1.2.1344508402.1692361758; _gat_UA-58224545-1=1; _ga_GR6VMPGW3N=GS1.2.1692361758.1.0.1692361758.60.0.0; __zi=3000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NSqtr_JpqH9BtdJDixxJ70wQSikvjzPG3PrqXhsvqLO0b3OpC0.1; XSRF-TOKEN=eyJpdiI6ImxWdHIwTHFzZWMydDRsdjdrbVIrSVE9PSIsInZhbHVlIjoiUlhreEhwZGxsMTJzQnQyVXdVaUZXd3JEMzJmaU04Nm0rRm1BU0NqM1dLM0NiVzFtaVhCQVJXRWlFZmpwZFlrUCIsIm1hYyI6IjQyZDQxMTgyYmEwNTRiN2FmMDI0ZGM5NTc0MjNkYmJiZTdjMmU2Y2ZhYzRkMTYxYjdmODc4N2ZjZmM4Y2QyYjEifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'neetHDzyCXQ124dYXDO6BHgrZbChbIdtIBURzsjI',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6ImxWdHIwTHFzZWMydDRsdjdrbVIrSVE9PSIsInZhbHVlIjoiUlhreEhwZGxsMTJzQnQyVXdVaUZXd3JEMzJmaU04Nm0rRm1BU0NqM1dLM0NiVzFtaVhCQVJXRWlFZmpwZFlrUCIsIm1hYyI6IjQyZDQxMTgyYmEwNTRiN2FmMDI0ZGM5NTc0MjNkYmJiZTdjMmU2Y2ZhYzRkMTYxYjdmODc4N2ZjZmM4Y2QyYjEifQ==',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)

    print(response.text)