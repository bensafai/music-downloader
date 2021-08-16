from src.Controller import DownloadController as controller

if __name__ == '__main__':
    controller = controller.DownloadController('spotify')
    request = controller.request_action()
    print(request)