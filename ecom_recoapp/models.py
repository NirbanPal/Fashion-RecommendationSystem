from django.db import models

# Create your models here.
GENDER_CHOICES=(
    ('Men' , 'Men'),
    ('Women' , 'Women'),
    ('Boys' , 'Boys'),
    ('Girls' , 'Girls'),
    ('Unisex' , 'Unisex'),
)

M_CATAGOTY_CHOICES=(
    ('Apparel' , 'Apparel'),
    ('Accessories' , 'Accessories'),
    ('Footwear' , 'Footwear'),
    ('Personal Care' , 'Personal Care'),
    ('Free Items' , 'Free Items'),
    ('Sporting Goods' , 'Sporting Goods'),
    ('Home' , 'Home'),
)

S_CATAGOTY_CHOICES=(
    ('Topwear','Topwear'),
    ('Bottomwear','Bottomwear'),
    ('Watches','Watches'),
    ('Socks','Socks'),
    ('Shoes','Shoes'),
    ('Belts','Belts'),
    ('Flip Flops','Flip Flops'),
    ('Bags','Bags'),
    ('Innerwear','Innerwear'),
    ('Sandal','Sandal'),
    ('Shoe Accessories','Shoe Accessories'),
    ('Fragrance','Fragrance'),
    ('Jewellery','Jewellery'),
    ('Lips','Lips'),
    ('Saree','Saree'),
    ('Eyewear','Eyewear'),
    ('Nails','Nails'),
    ('Scarves','Scarves'),
    ('Dress','Dress'),
    ('Loungewear and Nightwear','Loungewear and Nightwear'),
    ('Wallets','Wallets'),
    ('Apparel Set','Apparel Set'),
    ('Headwear','Headwear'),
    ('Mufflers','Mufflers'),
    ('Skin Care','Skin Care'),
    ('Makeup','Makeup'),
    ('Free Gifts','Free Gifts'),
    ('Ties','Ties'),
    ('Accessories','Accessories'),
    ('Skin','Skin'),
    ('Beauty Accessories','Beauty Accessories'),
    ('Water Bottle','Water Bottle'),
    ('Eyes','Eyes'),
    ('Bath and Body','Bath and Body'),
    ('Gloves','Gloves'),
    ('Sports Accessories','Sports Accessories'),
    ('Cufflinks','Cufflinks'),
    ('Sports Equipment','Sports Equipment'),
    ('Stoles','Stoles'),
    ('Hair','Hair'),
    ('Perfumes','Perfumes'),
    ('Home Furnishing','Home Furnishing'),
    ('Umbrellas','Umbrellas'),
    ('Wristbands','Wristbands'),
    ('Vouchers','Vouchers'),
)


ARTYPE_CHOICES=(('Shirts','Shirts'), 
                ('Jeans','Jeans'),
                ('Watches','Watches'),
                ('Track Pants','Track Pants'),
                ('Tshirts','Tshirts'),
                ('Socks','Socks'),
                ('Casual Shoes','Casual Shoes'),
                ('Belts','Belts'),
                ('Flip Flops','Flip Flops'),
                ('Handbags','Handbags'),
                ('Tops','Tops'),
                ('Bra','Bra'),
                ('Sandals','Sandals'),
                ('Shoe Accessories','Shoe Accessories'),
                ('Sweatshirts','Sweatshirts'),
                ('Deodorant','Deodorant') ,('Formal Shoes','Formal Shoes'),('Bracelet','Bracelet') ,('Lipstick','Lipstick') , ('Flats','Flats'), ('Kurtas','Kurtas'),
       ('Waistcoat','Waistcoat'),('Sports Shoes','Sports Shoes') ,('Shorts','Shorts') ,('Briefs','Briefs') ,('Sarees','Sarees') ,('Perfume and Body Mist','Perfume and Body Mist'),('Heels','Heels') ,('Sunglasses','Sunglasses') ,('Innerwear Vests','Innerwear Vests') ,('Pendant','Pendant')
       ,('Nail Polish','Nail Polish') ,('Laptop Bag','Laptop Bag') ,('Scarves','Scarves') ,('Rain Jacket','Rain Jacket') ,('Dresses','Dresses'),('Night suits','Night suits')
       , ('Skirts','Skirts'),('Wallets','Wallets') ,('Blazers','Blazers') ,('Ring','Ring') ,('Kurta Sets','Kurta Sets')
       ,('Clutches','Clutches') ,('Shrug','Shrug') ,('Backpacks','Backpacks') ,('Caps','Caps') , ('Trousers','Trousers'),
       ('Earrings','Earrings'), ('Camisoles','Camisoles'),('Boxers','Boxers') ,('Jewellery Set','Jewellery Set') ,('Dupatta','Dupatta') ,
       ('Capris','Capris'),('Lip Gloss','Lip Gloss') ,('Bath Robe','Bath Robe') ,('Mufflers','Mufflers') , ('Tunics','Tunics'),
       ('Jackets','Jackets'),('Trunk','Trunk') , ('Lounge Pants','Lounge Pants'),('Face Wash and Cleanser','Face Wash and Cleanser') ,
       ('Necklace and Chains','Necklace and Chains'),('Duffel Bag','Duffel Bag') ,('Sports Sandals','Sports Sandals') ,('Foundation and Primer','Foundation and Primer'), ('Sweaters','Sweaters'), ('Free Gifts','Free Gifts'),('Trolley Bag','Trolley Bag') ,
       ('Tracksuits','Tracksuits'),('Swimwear','Swimwear') ,('Shoe Laces','Shoe Laces') ,('Fragrance Gift Set','Fragrance Gift Set') ,
       ('Bangle','Bangle'),('Nightdress','Nightdress') ,('Ties','Ties') ,('Baby Dolls','Baby Dolls') , ('Leggings','Leggings'),
       ('Highlighter and Blush','Highlighter and Blush'),('Travel Accessory','Travel Accessory') , ('Kurtis','Kurtis'),
       ('Mobile Pouch','Mobile Pouch'),('Messenger Bag','Messenger Bag') , ('Lip Care','Lip Care'),('Face Moisturisers','Face Moisturisers'),('Compact','Compact'),('Eye Cream','Eye Cream') ,('Accessory Gift Set','Accessory Gift Set') ,('Beauty Accessory','Beauty Accessory') ,('Jumpsuit','Jumpsuit'), ('Kajal and Eyeliner','Kajal and Eyeliner'), ('Water Bottle','Water Bottle'),('Suspenders','Suspenders') ,('Lip Liner','Lip Liner'),('Robe','Robe') ,('Salwar and Dupatta','Salwar and Dupatta') ,('Patiala','Patiala') ,('Stockings','Stockings') ,
       ('Eyeshadow','Eyeshadow'),('Headband','Headband') ,('Tights','Tights') ,('Nail Essentials','Nail Essentials') ,('Churidar','Churidar') ,
       ('Lounge Tshirts','Lounge Tshirts'),('Face Scrub and Exfoliator','Face Scrub and Exfoliator') , ('Lounge Shorts','Lounge Shorts'),('Gloves','Gloves'),('Mask and Peel','Mask and Peel') , ('Wristbands','Wristbands'),('Tablet Sleeve','Tablet Sleeve') ,('Ties and Cufflinks','Ties and Cufflinks'),('Footballs','Footballs') ,('Stoles','Stoles') ,('Shapewear','Shapewear') ,
       ('Nehru Jackets','Nehru Jackets'),('Salwar','Salwar') ,('Cufflinks','Cufflinks') ,('Jeggings','Jeggings') ,('Hair Colour','Hair Colour') ,
       ('Concealer','Concealer'),('Rompers','Rompers') ,('Body Lotion','Body Lotion') ,('Sunscreen','Sunscreen') ,('Booties','Booties') ,
       ('Waist Pouch','Waist Pouch'), ('Hair Accessory','Hair Accessory'),('Rucksacks','Rucksacks') ,('Basketballs','Basketballs') ,
       ('Lehenga Choli','Lehenga Choli'),('Clothing Set','Clothing Set') ,('Mascara','Mascara') ,('Toner','Toner') ,
       ('Cushion Covers','Cushion Covers'),('Key chain','Key chain') ,('Makeup Remover','Makeup Remover') ,('Lip Plumper','Lip Plumper') ,
       ('Umbrellas','Umbrellas'),('Face Serum and Gel','Face Serum and Gel') ,('Hat','Hat') ,('Mens Grooming Kit','Mens Grooming Kit') ,
       ('Rain Trousers','Rain Trousers'),('Body Wash and Scrub','Body Wash and Scrub') ,('Suits','Suits') ,('Ipad','Ipad') )

class Product(models.Model):
    id = models.IntegerField(primary_key = True)
    gender = models.CharField(choices = GENDER_CHOICES,max_length = 255)
    masterCategory = models.CharField(choices = M_CATAGOTY_CHOICES,max_length = 255)
    subCategory= models.CharField(choices = S_CATAGOTY_CHOICES,max_length = 255)
    articleType= models.CharField(choices = ARTYPE_CHOICES,max_length = 255)
    baseColour= models.CharField(max_length = 255,null=True, blank=True)
    season= models.CharField(max_length = 255,null=True, blank=True)
    year= models.IntegerField(null=True, blank=True)
    usage=models.CharField(max_length = 255,null=True, blank=True)
    productDisplayName=models.TextField(null=True, blank=True,default='')
    link=models.TextField(null=False, blank=False)
    description=models.TextField(null=True,blank=True,default='')
    product_image = models.ImageField(upload_to = 'productimg')


    def __str__(self) :
        return str(self.productDisplayName)

    



class Cart(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default =1)

    def __str__(self) :
        return str(self.product_id)
