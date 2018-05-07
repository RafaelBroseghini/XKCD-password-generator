var clipboard = new ClipboardJS('.btn2');

$(function () {
  $('[data-toggle="popover"]').popover({
    delay: {"show":500}
  });
})

clipboard.on('success', function(e) {
    console.log(clipboard);
    console.info('Action:', e.action);
    console.info('Text:', e.text);
    console.info('Trigger:', e.trigger);
    e.clearSelection();
});

clipboard.on('error', function(e) {
    console.error('Action:', e.action);
    console.error('Trigger:', e.trigger);
});

function refresh() {
  location.reload();
}
