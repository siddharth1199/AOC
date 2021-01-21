import pandas as pd


def surface_area(df):
    surf_area = (2 * df['len'] * df['wid']) + (2 * df['len'] * df['hei']) + (2 * df['hei'] * df['wid'])

    return surf_area


def area_smallest_side(df):
    area_smallest = ([(df['len'] * df['wid']), (df['len'] * df['hei']), (df['hei'] * df['wid'])])

    return area_smallest


def volume(df):
    volume_box = (df['len'] * df['wid'] * df['hei'])

    return volume_box


def smallest_perimeter(df):
    smallest_per = ((df['len'] + df['len'] + df['hei'] + df['hei']),
                    (df['hei'] + df['hei'] + df['wid'] + df['wid']),
                    (df['wid'] + df['wid'] + df['len'] + df['len']))

    return smallest_per


def wrapping_paper(df):
    wrapping_len = sum(surface_area(df) + pd.concat(area_smallest_side(df), axis=1).min(axis=1))
    return wrapping_len


def ribbon(df):
    ribbion_len = sum(volume(df) + (pd.concat(smallest_perimeter(df), axis=1).min(axis=1)))
    return ribbion_len


def main():
    df = pd.read_csv('../inputs/day2.txt', sep='x', names=['len', 'wid', 'hei'])
    print("Total square feet of wrapping paper: {}".format(wrapping_paper(df)))
    print("total feet of ribbon: {}".format(ribbon(df)))


if __name__ == "__main__":
    main()