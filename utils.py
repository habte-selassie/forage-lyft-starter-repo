def add_years_to_date(orginal_date,years_to_add):
    result = orginal_date.replace(year=original_date.year + years_to_add)
    return result