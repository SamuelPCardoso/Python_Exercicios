import qrcode

imagem_qrcode = qrcode.make('Parafuso 6/2 - Preço R$0.25')
imagem_qrcode.save('Parafuso.png')
