from django.urls import path
# from django.contrib.auth.decorators import login_required

# from useracc.views import ApprovalView, IndexView, UserProfileView, UserUpdateView, \
#     ShopSignupFormView, ShopUpdateView, RequestsView, ShopProfileView, UserListView, AddUserFormView, UserUpdateByAdminView, UserDeleteByAdmin,  ProductListView, ProductDeleteView, ProductDetailView, ProductUpdateView, AddProductFormView, BuyProductView, AddToWishlistView, WishListView, DeleteFromWishListView, AddToCartView, CartView, DeleteFromCartView

from useracc.views import ApprovalView, IndexView, UserProfileView, UserUpdateView, \
    ShopSignupFormView, ShopUpdateView, RequestsView, ShopProfileView, \
    UserListView, AddUserFormView, UserUpdateByAdminView, ProductListView,\
    UserDeleteByAdmin, AddProductFormView, ProductUpdateView, ProductDeleteView, \
    ProductDetailView, BuyNowView, AddToWishlistView, WishListView,\
    DeleteFromWishListView, AddToCartView, CartView, DeleteFromCartView, CheckoutView, \
    MyOrdersView, CancelOrderView, OrderDetailView, RemoveItemView, ShopOrderView, \
    ItemStatusUpdateView, SalesReportView, UserOrderView, OrderDetailForAdminView, \
    ProductDetailForAdminView, ShopListView, ShopDetailView, ProductListForAdminView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('approval/<int:id>', ApprovalView.as_view(), name='approval'),
    path('userprofile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('shopprofile/<int:pk>', ShopProfileView.as_view(), name='shopprofile'),
    path('editshopdetails/<int:pk>',
         ShopUpdateView.as_view(), name='shopupdate_view'),
    path('edituserdetails/<int:pk>',
         UserUpdateView.as_view(), name='userupdate_view'),
    path('signupasshop/', ShopSignupFormView.as_view(), name="shopsignup"),
    path('requests/', RequestsView.as_view(), name="getallrequests"),
    path('listusers/', UserListView.as_view(), name="userlist"),
    path('adduser/', AddUserFormView.as_view(), name="adduser"),
    path(
        'userupdatebyadmin/<int:pk>', UserUpdateByAdminView.as_view(),
        name="userupdatebyadmin"
    ),
    path('userupdatebyadmin/', UserUpdateByAdminView.as_view(),
         name="userupdatebyadmin"),
    path('userdeletebyadmin/', UserDeleteByAdmin.as_view(),
         name='userdeletebyadmin'),
    path('addproduct/', AddProductFormView.as_view(), name='addproduct'),
    path('listproducts/', ProductListView.as_view(), name="productlist"),
    path('productupdate/<int:pk>',
         ProductUpdateView.as_view(), name="productupdate"),
    path('deleteproduct/', ProductDeleteView.as_view(), name="deleteproduct"),
    path('productdetail/<int:pk>', ProductDetailView.as_view(), name='profile'),
    path('addtowishlist/<int:pk>',
         AddToWishlistView.as_view(), name='addtowishlist'),
    path('mywishlist/<int:pk>', WishListView.as_view(), name="mywishlist"),
    path('deletefromwishlist/', DeleteFromWishListView.as_view(),
         name="deletefromwishlist"),
    path('addtocart/<int:pk>', AddToCartView.as_view(), name="addtocart"),
    path('mycart/<int:pk>', CartView.as_view(), name="mycart"),
    path('deletefromcart/', DeleteFromCartView.as_view(), name="deletefromcart"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('myorders/', MyOrdersView.as_view(), name="myorders"),
    path('cancelorder/<int:pk>', CancelOrderView.as_view(), name="cancelorder"),
    path('orderdetail/<int:pk>', OrderDetailView.as_view(), name="orderdetail"),
    path('removeitem/<int:pk>', RemoveItemView.as_view(), name="removeitem"),
    path("buynow/<int:pk>", BuyNowView.as_view(), name="buynow"),
    path('shoporder/', ShopOrderView.as_view(), name="shoporder"),
    path('itemstatusupdate/<int:pk>',
         ItemStatusUpdateView.as_view(), name="itemstatusupdate"),
    path('salesreport/', SalesReportView.as_view(), name="salesreport"),
    path('userorders', UserOrderView.as_view(), name="userorders"),
    path('orderdetailforadmin/<int:pk>',
         OrderDetailForAdminView.as_view(), name="orderdetailforadmin"),
    path('productdetailforadmin/<int:pk>',
         ProductDetailForAdminView.as_view(), name="productdetailforadmin"),
    path('shoplist', ShopListView.as_view(), name="shoplist"),
    path('shopdetail/<int:pk>', ShopDetailView.as_view(), name="shopdetail"),
    path('productlist/<int:pk>',
         ProductListForAdminView.as_view(), name="productlist")

]
