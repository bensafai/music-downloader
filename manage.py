from src.Controller.SearchController import SearchController

if __name__ == '__main__':
    search_controller = SearchController('spotify')
    request = search_controller.request_action()
    print(request)