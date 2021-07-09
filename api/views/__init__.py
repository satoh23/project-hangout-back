

from .blog import (CreateBlogView, EditBlogView, CreateBlogNotThumbnailView,
                   ListGenreView, ListBlogView, DetailBlogView, BuyBlogView)

from .point import (test_payment, save_stripe_info)

from .message import (CreateMessageFromMaleView, CreateMessageFromFemaleView, ListMessageBoxView)
