from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time
import utilities.custom_logger as cl
import logging

# here we write a code to access all the LHS components
class lhsPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # General Locators
    _create_pay_link = "//div[contains(text(),'Create Payment Link')]"
    _add_product = "//div[contains(text(),'Add Product')]"
    _dashboard = "//span[contains(text(),'Dashboard')]"

    # Payments locators
    _payment_links = "//span[contains(text(),'Payment Links')]"
    _refunds = "//span[contains(text(),'Refunds')]"
    _spends = "//span[contains(text(),'Spends')]"
    _api_plugins = "//span[contains(text(),'API & Plugins')]"
    _reseller = "//span[contains(text(),'API & Plugins')]"
    _bank_transfer = "//span[contains(text(),'Bank transfer')]"
    _payment_apps = "//span[contains(text(),'Payment Apps')]"

    # Order locators
    _orders = "//span[contains(text(),'Orders')]"
    _all_orders = "//span[contains(text(),'All Orders')]"
    _abandoned_carts = "//span[contains(text(),'Abandoned Carts')]"
    _enquiries = "//span[contains(text(),'Enquiries')]"

    # Inventory locators
    _products = "//span[contains(text(),'Products')]"
    _all_products = "//span[contains(text(),'All Products')]"
    _categories = "//span[contains(text(),'Categories')]"
    _attributes = "//span[contains(text(),'Attributes')]"
    _product_option = "//span[contains(text(),'Product Options')]"
    _review = "//span[contains(text(),'Reviews')]"

    # Discount locators
    _discounts = "//span[contains(text(),'Discounts')]"
    _coupons = "//span[contains(text(),'Coupons')]"
    _wholesale_discount = "//span[contains(text(),'Wholesale Discounts')]"
    _referral_discount = "//span[contains(text(),'Referral Discounts')]"

    # Store locators
    _store = "//span[text()='Store']"
    _manage_store = "//span[contains(text(),'Manage Store')]"
    _my_logo = "//span[contains(text(),'My Logo')]"
    _select_theme = "//span[contains(text(),'Select Theme')]"
    _banner_image = "//span[contains(text(),'Banner Images')]"
    _social_pages = "//span[contains(text(),'Social Media Pages')]"
    _domain_mailbox = "//span[contains(text(),'Domains & Mailbox')]"
    _shipping_setting = "//span[contains(text(),'Shipping Settings')]"
    _tax_setting = "//span[contains(text(),'Tax Settings')]"

    # CRM locators
    _customers = "//span[contains(text(),'Customers')]"
    _all_customers = "//span[contains(text(),'All Customers')]"
    _subscribed_users = "//span[contains(text(),'Subscribed Users')]"
    _membership = "//span[contains(text(),'Memberships')]"
    _contact_us_queries = "//span[contains(text(),'Contact Us Queries')]"

    # Campaign locators
    _campaigns = "//span[contains(text(),'Campaigns')]"
    _all_campaigns = "//span[contains(text(),'All Campaigns')]"
    _sms_emails = "//span[contains(text(),'SMS and Emails')]"
    _subscription_popup = "//span[contains(text(),'Subscription popup')]"
    _push_notifications = "//span[contains(text(),'Push notifications')]"

    # SEO locators
    _seo = "//span[contains(text(),'SEO')]"
    _basic_seo = "//span[contains(text(),'Basic SEO')]"
    _custom_metatags = "//span[contains(text(),'Custom Metatags')]"
    _google_webmaster = "//span[contains(text(),'Google Webmaster')]"
    _url_redirection = "//span[contains(text(),'URL redirection')]"

    # Profile menu locators
    _profile_menu = "//a[contains(@class,'show-for-medium-up push-half--left')]"
    _user_payment_link = ""
    _store_link = "//a[text()='Your Online Store']"
    _setting = "//a[text()='Settings']"
    _subscription_plan = "//a[text()='Subscription Plan']"
    _manage_members = "//a[text()='Manage Members']"
    _faster_payout = "//a[text()='Faster Payouts']"
    _invite_earn = "//a[text()='Invite & Earn']"
    _gst_invoices = "//a[text()='GST Invoices']"
    _give_feedback = "//span[contains(text(),'Give Feedback')]"
    _help_support = "//span[contains(@class,'soft-quarter--left')]"
    _logout_link = "//a[text()='Log Out']"

    # By defaults we use locatorType="xpath", specify it if u use any other

    # Click method for General
    def click_create_pay_link(self):
        self.elementClick(self._create_pay_link)

    def click_add_product(self):
        self.elementClick(self._add_product)

    def click_dashboard(self):
        self.elementClick(self._dashboard)

    # Click method for Payments module
    def click_payment_links(self):
        self.elementClick(self._payment_links)

    def click_refunds(self):
        self.elementClick(self._refunds)

    def click_spends(self):
        self.elementClick(self._spends)

    def click_api_plugins(self):
        self.elementClick(self._api_plugins)

    def click_reseller(self):
        self.elementClick(self._reseller)

    def click_bank_transfer(self):
        self.elementClick(self._bank_transfer)

    def click_payment_apps(self):
        self.elementClick(self._payment_apps)

    # Click method for Order module
    def click_orders(self):
        self.elementClick(self._orders)

    def click_all_orders(self):
        self.elementClick(self._all_orders)

    def click_abandoned_carts(self):
        self.elementClick(self._abandoned_carts)

    def click_enquiries(self):
        self.elementClick(self._enquiries)

    # Click method for Inventory/Products
    def click_products(self):
        self.elementClick(self._products)

    def click_all_products(self):
        self.elementClick(self._all_products)

    def click_categories(self):
        self.elementClick(self._categories)

    def click_attributes(self):
        self.elementClick(self._attributes)

    def click_product_option(self):
        self.elementClick(self._product_option)

    def click_review(self):
        self.elementClick(self._review)

    # Click method for Discounts Module
    def click_discounts(self):
        self.elementClick(self._discounts)

    def click_coupons(self):
        self.elementClick(self._coupons)

    def click_wholesale_discount(self):
        self.elementClick(self._wholesale_discount)

    def click_referral_discount(self):
        self.elementClick(self._referral_discount)

    # Click method for Store Module
    def click_store(self):
        self.elementClick(self._store)

    def click_manage_store(self):
        self.elementClick(self._manage_store)

    def click_my_logo(self):
        self.elementClick(self._my_logo)

    def click_select_theme(self):
        self.elementClick(self._select_theme)

    def click_banner_image(self):
        self.elementClick(self._banner_image)

    def click__social_pages(self):
        self.elementClick(self._social_pages)

    def click_domain_mailbox(self):
        self.elementClick(self._domain_mailbox)

    def click_shipping_setting(self):
        self.elementClick(self._shipping_setting)

    def click_tax_setting(self):
        self.elementClick(self._tax_setting)

    # Click method for Customers/CRM Module
    def click_customers(self):
        self.elementClick(self._customers)

    def click_all_customers(self):
        self.elementClick(self._all_customers)

    def click_subscribed_users(self):
        self.elementClick(self._subscribed_users)

    def click_membership(self):
        self.elementClick(self._membership)

    def click_contact_us_queries(self):
        self.elementClick(self._contact_us_queries)

    # Click method for Campaigns Module
    def click_campaigns(self):
        self.elementClick(self._campaigns)

    def click_all_campaigns(self):
        self.elementClick(self._all_campaigns)

    def click_sms_emails(self):
        self.elementClick(self._sms_emails)

    def click_subscription_popup(self):
        self.elementClick(self._subscription_popup)

    def click_push_notifications(self):
        self.elementClick(self._push_notifications)

    # Click method for SEO Module
    def click_seo(self):
        self.elementClick(self._seo)

    def click_basic_seo(self):
        self.elementClick(self._basic_seo)

    def click_custom_metatags(self):
        self.elementClick(self._custom_metatags)

    def click_google_webmaster(self):
        self.elementClick(self._google_webmaster)

    def click_url_redirection(self):
        self.elementClick(self._url_redirection)

    # Click method for Profile menu
    def click_profile_menu(self):
        self.elementClick(self._profile_menu)

    def click_user_payment_link(self):
        self.elementClick(self._user_payment_link)

    def click_store_link(self):
        self.elementClick(self._store_link)

    def click_setting(self):
        self.elementClick(self._setting)

    def click_subscription_plan(self):
        self.elementClick(self._subscription_plan)

    def click_manage_members(self):
        self.elementClick(self._manage_members)

    def click_faster_payout(self):
        self.elementClick(self._faster_payout)

    def click_invite_earn(self):
        self.elementClick(self._invite_earn)

    def click_gst_invoices(self):
        self.elementClick(self._gst_invoices)

    def click_give_feedback(self):
        self.elementClick(self._give_feedback)

    def click_help_support(self):
        self.elementClick(self._help_support)

    def click_logout_link(self):
        self.elementClick(self._logout_link)
