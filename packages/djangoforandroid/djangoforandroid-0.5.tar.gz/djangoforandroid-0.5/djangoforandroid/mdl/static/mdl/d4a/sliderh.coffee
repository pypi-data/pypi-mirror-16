

########################################################################
class SliderH

    #----------------------------------------------------------------------
    constructor: (sliderh, parent) ->
        @DIRTY = false
        @WIDTH_SLIDER = $(sliderh).width()
        @WIDTH_SLIDER_THRESHOLD = @WIDTH_SLIDER/2
        @WIDTH_MAX_SLIDER = $(parent).width() - @WIDTH_SLIDER



    #----------------------------------------------------------------------
    start_pand_single: (event) =>
        cls = @
        parent = $(event.srcEvent.path[1])

        cls.OFFSET = parseInt(parent.css("transform").split(',')[4])
        if not cls.OFFSET
            cls.OFFSET = 0

        if cls.OFFSET > 0
            cls.OFFSET = 0

        cls.DIRTY = true


    #----------------------------------------------------------------------
    start_pand_end: (event) =>
        cls = @
        parent = $(event.srcEvent.path[1])

        if cls.DIRTY
            parent.css({"-webkit-transition-duration": "0.2s"})
            parent.css({"-webkit-transform": "translateX(#{cls.OFFSET}px)"})

        console.log("j")

    #----------------------------------------------------------------------
    start_pand: (event) =>
        cls = @
        parent = $(event.srcEvent.path[1])

        X = cls.OFFSET + event.deltaX

        if cls.OFFSET is 0 and event.deltaX > 0
            return

        if cls.OFFSET is -cls.WIDTH_MAX_SLIDER and event.deltaX < 0
            return

        parent.css({"-webkit-transition-duration": "0s"})
        parent.css({"-webkit-transform": "translateX(#{X}px)"})

        if event.deltaX < -cls.WIDTH_SLIDER_THRESHOLD
            W = cls.OFFSET - cls.WIDTH_SLIDER
            parent.css({"-webkit-transition-duration": "0.2s"})
            parent.css({"-webkit-transform": "translateX(#{W}px)"})
            cls.DIRTY = false
            return

        if event.deltaX > cls.WIDTH_SLIDER_THRESHOLD
            W = cls.OFFSET + cls.WIDTH_SLIDER
            parent.css({"-webkit-transition-duration": "0.2s"})
            parent.css({"-webkit-transform": "translateX(#{W}px)"})
            cls.DIRTY = false
            return


$(document).ready ->





#Contructor
#----------------------------------------------------------------------

    for element in $(".d4a-sliderh-parent")
        SliderH_ = new SliderH($(element).children(".d4a-sliderh"), element)
        ASH_slider = new Hammer(element)
        ASH_slider.get("pan").set({velocity: 0, pointers: 1, threshold: 0})
        ASH_slider.on "panleft panright", SliderH_.start_pand
        ASH_slider.on "panstart", SliderH_.start_pand_single
        ASH_slider.on "panend", SliderH_.start_pand_end

    #ASH_slider2 = new Hammer($(".ash-slider")[1])
    #ASH_slider2.get("pan").set({velocity: 0, pointers: 1, threshold: 0})
    #ASH_slider2.on "panleft panright", SliderH.start_pand


    #ASH_slider.on "panright", SliderH.start_pand_right
