"use strict";

const copyStatus = document.getElementById("copy-status");

document.querySelectorAll("button[data-copy-target]").forEach((button) => {
  const field = document.getElementById(button.dataset.copyTarget);
  if (!field || !copyStatus) return;

  const originalLabel = button.textContent;
  let resetTimer;

  button.addEventListener("click", async () => {
    clearTimeout(resetTimer);
    button.disabled = true;
    button.textContent = originalLabel;
    copyStatus.textContent = "";

    try {
      if (!window.isSecureContext || !navigator.clipboard?.writeText) {
        throw new Error("Clipboard access unavailable");
      }

      await navigator.clipboard.writeText(field.value);
      button.textContent = "Copied!";
      copyStatus.textContent = "Copied.";
      resetTimer = window.setTimeout(() => {
        button.textContent = originalLabel;
      }, 2000);
    } catch {
      field.focus();
      field.select();
      field.setSelectionRange(0, field.value.length);
      copyStatus.textContent = "Text selected. Press Ctrl+C or Command+C to copy.";
    } finally {
      button.disabled = false;
    }
  });

  // Keep manual selection available when JavaScript is disabled or fails to load.
  button.hidden = false;
});
