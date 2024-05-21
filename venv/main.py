import veiwImages

def manage():
    veiwImages.get_from_server()
    x = int(input("Press 1 to display all icons and 2 to display a selected icon\n"))
    if x == 1:
        veiwImages.print_all_icons()
    else:
        keyword = input("Enter keyword to search icons: ")
        veiwImages.search_icons_by_keyword(keyword)


def main():
    manage()

if __name__ == '__main__':
    main()
