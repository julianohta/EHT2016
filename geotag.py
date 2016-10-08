from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# reference: https://gist.github.com/erans/983821

def convert_deg(value):
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

def get_if_exist(data, key):
    if key in data:
        return data[key]
        
    return None

def get_lat_lng(filename):
    data = {}
    im = Image.open(filename)
    info = im._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps[sub_decoded] = value[t]

                data[decoded] = gps
            else:
                data[decoded] = value
    lat = None
    lng = None
    if "GPSInfo" in data:
        gps = data["GPSInfo"]
        gps_lat = get_if_exist(gps, "GPSLatitude")
        gps_lat_r = get_if_exist(gps, "GPSLatitudeRef")
        gps_lng = get_if_exist(gps, "GPSLongitude")
        gps_lng_r = get_if_exist(gps, "GPSLongitudeRef")

        if gps_lat and gps_lng_r and gps_lng and gps_lng_r:
            lat = convert_deg(gps_lat)
            if gps_lat_r != "N":
                lat = 0 - lat
            lng = convert_deg(gps_lng)
            if gps_lng_r != "E":
                lng = 0 - lng

    return lat, lng
