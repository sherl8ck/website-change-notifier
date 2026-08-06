def is_new_notice(faculty, latest_notice, saved_data):

    if faculty not in saved_data:
        return True

    old_notice = saved_data[faculty]

    return latest_notice["link"] != old_notice["link"]