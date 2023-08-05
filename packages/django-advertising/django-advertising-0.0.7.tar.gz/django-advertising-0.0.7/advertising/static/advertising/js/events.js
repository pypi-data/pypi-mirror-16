var advertisingModule = (function()
{
    'use strict';

    /**
     * @name: Initialize
     * @descrip: Init advertising
     * @param {String} id: id advertising.
    */
    function initialize(id){
        var counter = document.querySelector("#images_advertising_" + id).childNodes.length - 1;
        var counterTotal = counter;
        var container, image;

        //This variable to load template tag
        var secondsIntervalAdvertising;
        if(window['TimeOutAdvertising_' + id])
        {
            secondsIntervalAdvertising = window['TimeOutAdvertising_' + id];
        }else
        {
            secondsIntervalAdvertising = 3000;
        }

        setInterval(function()
        {
            //Hide image index counter
            if (counter > -1)
            {
                toogle(id, counter, false);
            }

            //If the final, again show images
            if(counter <= 0)
            {
                counter = counterTotal;
                for(var i=0;i<=counter;i++)
                {
                    toogle(id, i, true);
                }
            }else
            {
                counter--;
            }
        }, secondsIntervalAdvertising);
    }

    /**
     * @name: toogle
     * @descrip: Check if is show or hide element container
     * @param {String} id: id advertising.
     * @param {Integer} counter - id element.
     * @param {Boolena} is_show - if element is show or hide
    */
    function toogle(id, counter, is_show)
    {
        var container = "#image_container_advertising_" + counter + "_" + id;
        if(is_show)
        {
            displayMe(document.querySelector(container));
        }else{
            hideMe(document.querySelector(container));
        }
    }

    /**
     * @name: displayMe
     * @descrip: Show element of the dom.
     * @param {htmlElement} element - Element to show.
    */
    function displayMe(element)
    {
        element.style.transition = "all .3s";
        element.style.display = "block";
    }

    /**
     * @name: hideMe
     * @descrip: Hide element of the dom.
     * @param {htmlElement} element - Element to hide.
    */
    function hideMe(element)
    {
        element.style.transition = "all .3s";
        element.style.display = "none";
    }

    return {
        'initialize': initialize
    }
})();
