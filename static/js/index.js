document.addEventListener('DOMContentLoaded', () => {
  const imageUpload = document.getElementById('imageUpload');
  const fileUploadError = document.getElementById('fileUploadError');
  const uploadLabel = document.getElementById('uploadLabel');

  imageUpload.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (!file) return;

    fileUploadError.style.display = 'none';
    if (file.size > 5 * 1024 * 1024) {
      fileUploadError.textContent = 'File size should not exceed 5MB.';
      fileUploadError.style.display = 'block';
      return;
    }

    if (!file.type.match('image.*')) {
      fileUploadError.textContent = 'Please select an image file.';
      fileUploadError.style.display = 'block';
      return;
    }

    const fileUrl = URL.createObjectURL(file);
    displayFileUrl(fileUrl);
  });

  function displayFileUrl(fileUrl) {
    // Truncate URL if it's too long
    let displayUrl = fileUrl.length > 50 ? fileUrl.substring(0, 47) + '...' : fileUrl;
    uploadLabel.textContent = `Uploaded file URL: ${displayUrl}`;
  }

  window.triggerUpload = () => imageUpload.click();

  const displayButton = document.getElementById('displayButton');
  if (displayButton) {
    displayButton.addEventListener('click', () => {
      window.location.href = '/display';
    });
  }
});