/* Project specific Javascript goes here. */

$("button.copy-to-clipboard").click((e) => {
  const ingredientElements = $(e.target).parent().children("li");
  const ingredientStr = ingredientElements
    .map((_, el) => el.textContent)
    .toArray()
    .join("\n");
  copyStringToClipboard(ingredientStr);
});

function copyStringToClipboard(text) {
  var input = $("<textarea>");
  $("body").append(input);
  input.val(text).select();
  document.execCommand("copy");
  input.remove();
}
