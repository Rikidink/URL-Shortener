// Copy to clipboard button
const copyToClipboard = () => {
    const copiedText = document.getElementById("shortened_url").innerHTML;
    navigator.clipboard.writeText(copiedText);
}

// Save image button
const saveImage = (destination="rickly") => {
    const image = document.getElementById("qrCode");
    const link = document.createElement('a');

    link.href = image.src;
    link.download = destination.concat(".png");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}


// Hamburger dropdown menu
const toggleHamburger = () => {
    document.getElementById('navbar-default').classList.toggle('hidden');
}
