import boto3

# Bu kod bloğu, AWS hesabınızın oturum açma bilgilerini kullanarak bir AWS hesabı oluşturur
# AWS hesabı oluşturma işlemlerini tamamlamak için daha fazla bilgi için AWS dokümantasyonunu inceleyebilirsiniz
client = boto3.client('mws',
                      aws_access_key_id='<YOUR_AWS_ACCESS_KEY_ID>',
                      aws_secret_access_key='<YOUR_AWS_SECRET_ACCESS_KEY>',
                      seller_id='<YOUR_SELLER_ID>',
                      region_name='<REGION_NAME>')

# Bu kod bloğu, Amazon hesabınızın işlem geçmişine erişmek için bir istek gönderir
response = client.list_orders(
    CreatedAfter='<DATE_TIME>',
    OrderStatus='Shipped'
)

# Bu kod bloğu, döndürülen cevaplardaki siparişleri ve siparişlerin ödeme tutarlarını alır
orders = response['Orders']['Order']
total_spent = 0
for order in orders:
    total_spent += float(order['OrderTotal']['Amount'])

print(f'Toplam harcama: {total_spent:.2f}')
