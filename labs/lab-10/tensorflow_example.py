# TensorFlow and tf.keras
import tensorflow as tf
from PIL import Image

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images = train_images / 255.0
test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)
def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i+9000, predictions[i+9000], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i+9000, predictions[i+9000], test_labels)
plt.tight_layout()
#plt.show()


pants = 1-(np.asarray(Image.open("./test-images/cropped/pants.png"))/255)
pants = (np.expand_dims(pants, 0))
shirt = 1-(np.asarray(Image.open("./test-images/cropped/shirt.png"))/255)
shirt = (np.expand_dims(shirt, 0))
shoes = 1-(np.asarray(Image.open("./test-images/cropped/shoes.png"))/255)
shoes = (np.expand_dims(shoes, 0))

predictions_pant= probability_model.predict(pants)
print(predictions_pant)
print(np.argmax(predictions_pant))
predictions_shirt = probability_model.predict(shirt)
print(predictions_shirt)
print(np.argmax(predictions_shirt))
predictions_shoes = probability_model.predict(shoes)
print(predictions_shoes)
print(np.argmax(predictions_shoes))
#print(test_images[1])
#dataset = [pants, shirt, shoes]
#predictions = probability_model.predict(pants)

