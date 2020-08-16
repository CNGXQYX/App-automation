from selenium.webdriver.common.by import By

# -------------about_out-----------
update_version_button=By.XPATH,'//*[@text="版本更新"]'

# -------------ad----------------------

skip_button=By.ID,'com.yunmall.lc:id/view_mask'

# -----------address_administration----------------
new_address_butotn=By.XPATH,"//*[@text='新增地址']"
receipt_and_name=By.ID,'com.yunmall.lc:id/receipt_name'

# ---------home---------------------------------------------

'''大写B小写y，大写ID
用的By的时候要记得导包。大写，这是一个类？
中文下的逗号容易出问题'''

my_button=By.ID,'com.yunmall.lc:id/tab_me'

# ----------login_or_register----------------------------------------------------

haved_account=By.ID,'com.yunmall.lc:id/textView1'

# --------login-------------------------------

# 注意 XPATH表达式，后面这样是id 和class的写法，一不注意就写成这样！！username=By.XPATH,'请输入手机/昵称'
username=By.XPATH,"//*[@text='请输入手机/昵称']"
password=By.ID,'com.yunmall.lc:id/logon_password_textview'
login_button=By.XPATH,"//*[@text='登录']"

# ------------my--------------------------

nick_name_text_view=By.ID,'com.yunmall.lc:id/tv_user_nikename'
setting_button=By.ID,'com.yunmall.lc:id/ymtitlebar_left_btn_image'
join_super_vip=By.XPATH,"//*[@text='加入超级VIP']"

# ----------------new_address--------------
receipt_name=By.ID,'com.yunmall.lc:id/address_receipt_name'
phone_address=By.ID,"com.yunmall.lc:id/address_add_phone"
detailed_address=By.ID,'com.yunmall.lc:id/address_detail_addr_info'
post_code=By.ID,'com.yunmall.lc:id/address_post_code'
defaul_address=By.ID,'com.yunmall.lc:id/address_default'
new_address_activity='com.yunmall.ymctoc.ui.activity.AddressAddActivity'
choose_region=By.ID,'com.yunmall.lc:id/address_province'
area_feature = By.ID, "com.yunmall.lc:id/area_title"
save_button=By.ID,'com.yunmall.lc:id/button_send'

# -------------setting---------------

about_out_button=By.ID,'com.yunmall.lc:id/setting_about_yunmall'
clear_cache_button=By.ID,'com.yunmall.lc:id/setting_clear_cache'
address_administration_button=By.XPATH,"//*[@text='地址管理']"

# -----------------vip-----------------------

# input是标签名，说明之前的*就是代替了标签名。 这是一个webview内容，元素特征不是通过automatorview获取的，是通过chrome输入chrome://inspect 里面有工具获取
# 注意这里是tpye和value了，不是之前经常写的text了，xpath的内容多变
invite_frame=By.XPATH,"//input[@placeholder='邀请码必填']"
be_vip_button=By.XPATH,"//input[@value='立即成为会员']"



