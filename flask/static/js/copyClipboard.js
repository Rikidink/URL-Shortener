const copyToClipboard = () => {
    const copiedText = document.getElementById("shortened_url").innerHTML;
    navigator.clipboard.writeText(copiedText);
}
