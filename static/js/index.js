document.addEventListener('DOMContentLoaded', function() {
  // JavaScript to trigger the file input click when the label is clicked
  function triggerUpload() {
    document.getElementById('imageUpload').click();
  }

  // Event listener to handle the file upload
  document.getElementById('imageUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
      // Handle the file upload here
      console.log('File selected:', file.name);
      // You can add code here to display the image or upload it to a server
    }
  });

  // Assign triggerUpload to the global scope so it can be called from the onclick attribute
  window.triggerUpload = triggerUpload;
});