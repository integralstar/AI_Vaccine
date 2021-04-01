#import cnn_model
import keras_cnn

'''
cnn = cnn_model.CNN_tensor()
cnn.load_images()
'''

cnn = keras_cnn.CNN()
#print(cnn)
cnn.image_preprocess()
loss, acc = cnn.do_cnn()

print("loss : %s accuracy : %s" % (loss, acc*100))
