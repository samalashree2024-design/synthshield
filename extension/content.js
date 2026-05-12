function addLabel() {
  if (!document.querySelector(".synthshield-label")) {
    const label = document.createElement("div");
    label.innerText = "⚠ Likely AI-generated";
    label.className = "synthshield-label";

   label.style.position = "fixed";
label.style.top = "80px";
label.style.right = "20px";
label.style.left = "auto";
    label.style.backgroundColor = "yellow";
    label.style.color = "black";
    label.style.padding = "8px";
    label.style.fontSize = "12px";
    label.style.fontWeight = "bold";
    label.style.zIndex = "999999";

    document.body.appendChild(label);
  }
}

const observer = new MutationObserver(addLabel);
observer.observe(document.body, {
  childList: true,
  subtree: true
});

addLabel();