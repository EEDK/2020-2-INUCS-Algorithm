import re


def solution(files):
    pattern = re.compile(r'([a-zA-Z\-\s]+)(\d{1,5})(.*)')
    sorted_files = sorted(files, key=lambda x: (
        re.match(pattern, x).group(1).lower(), int(re.match(pattern, x).group(2))))
    return sorted_files


print(solution(["F-5 Freedom Fighter", "B-50 Superfortress",
      "A-10 Thunderbolt II", "F-14 Tomcat"]))
