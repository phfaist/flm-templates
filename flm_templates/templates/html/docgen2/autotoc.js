installAutoToc = (function(){
    var clickCallback = function(targetHeaderElement, event) {
        targetHeaderElement.scrollIntoView();
    };
    return function(contentsElement, tocElement)
    {
        var headerElements = contentsElement.querySelectorAll('h1');

        //var tocContentsHtml = '';
        var ulElement = document.createElement('ul');

        for (var j = 0; j < headerElements.length; ++j) {
            var hEl = headerElements[j];
            
            var liElement = document.createElement('li');
            liElement.innerHTML = hEl.innerHTML;

            liElement.addEventListener(
                'click',
                (function(hEl){ // capture hEl here
                    return function(event) {
                       clickCallback(hEl, event); 
                    };
                })(hEl)
            );

            ulElement.appendChild(liElement);
        }

        tocElement.innerHTML = '';

        var captionElement = document.createElement('div');
        captionElement.classList.add('toc-caption');
        captionElement.innerHTML = 'Contents';

        tocElement.appendChild(captionElement);
        tocElement.appendChild(ulElement);
    }
})();

window.addEventListener('load', function() {
    installAutoToc(document.getElementById('article_main'),
                   document.getElementById('toc'));
});
