/* globals requestAnimationFrame */

const images = document.querySelectorAll('img')
images.forEach(image => {
  image.onclick = () => rotateImage(image)
})

const rotateImage = (image, degrees = 0) => {
  degrees += 10
  image.style.transform = 'rotate(' + degrees + 'deg)'
  if (degrees >= 360) return
  requestAnimationFrame(() => rotateImage(image, degrees))
}
