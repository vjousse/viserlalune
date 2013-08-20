<?php


header ("Content-Type:text/css");


/** ===============================================================
 *
 *      Edit your Color Configurations below:
 *      You should only enter 6-Digits HEX Colors.
 *
 ================================================================== */


$color = "#2780AF"; // Change your Color Here


/** ===============================================================
 *
 *      Do not Edit anything below this line if you do not know
 *      what you are trying to do..!
 *
 ================================================================== */


function checkhexcolor($color) {

    return preg_match('/^#[a-f0-9]{6}$/i', $color);

}


/** ===============================================================
 *
 *      Primary Color Scheme
 *
 ================================================================== */


if( isset( $_GET[ 'color' ] ) AND $_GET[ 'color' ] != '' ):

    $color = "#" . $_GET[ 'color' ];
    
endif;

if( !$color OR !checkhexcolor( $color ) ) {
    
    $color = "#57B3DF";
    
}


?>


/* ----------------------------------------------------------------
    Colors
-----------------------------------------------------------------*/


a,
h1 span,
h2 span,
h3 span,
h4 span,
h5 span,
h6 span,
#top-menu li a:hover,
#lp-contacts li span,
#portfolio-filter li a:hover,
#portfolio-filter li.activeFilter a,
.portfolio-item:hover h3 a,
.entry_date div.post-icon,
.entry_meta li a:hover,
.ipost .ipost-title a:hover,
.comment-content .comment-author a:hover,
.promo h3 > span,
.error-404,
.tab_widget ul.tabs li.active a,
.product-feature3:hover span,
.team-skills li span,
.best-price .pricing-title h4,
.best-price .pricing-price { color: <?php echo $color; ?>; }

.pricing-style2 .pricing-price { color: #FFF !important; }


/* ----------------------------------------------------------------
    Background Colors
-----------------------------------------------------------------*/


#top-menu li.top-menu-em a,
#primary-menu > ul > li:hover,
#primary-menu ul li.current,
#primary-menu > div > ul > li:hover,
#primary-menu div ul li.current,
#primary-menu > div > ul > li.current-menu-ancestor,
#primary-menu > div > ul > li.current-menu-parent,
#primary-menu > div > ul > li.current-menu-item,
.sticky-menu-wrap > ul > li:hover,
.sticky-menu-wrap ul li.current,
.sticky-menu-wrap > ul > li.current-menu-ancestor,
.sticky-menu-wrap > ul > li.current-menu-parent,
.sticky-menu-wrap > ul > li.current-menu-item,
#primary-menu ul ul li,
.sticky-menu-wrap ul ul li,
.lp-subscribe input[type="submit"],
.portfolio-overlay,
#portfolio-navigation a:hover,
.entry_date div.month,
.entry_date div.day,
.sidenav > .active > a,
.sidenav > .active > a:hover,
.promo-action a:hover,
.error-404-meta input[type="submit"],
.product-feature img,
.product-feature > span,
.team-image span,
.icon-rounded:hover,
.icon-circled:hover,
.simple-button.inverse,
.simple-button:hover,
.pricing-style2 .best-price .pricing-price,
#twitter-panel,
#gotoTop:hover,
a.twitter-follow-me:hover,
#footer.footer-dark a.twitter-follow-me:hover,
.sposts-list .spost-image:hover,
#footer.footer-dark .sposts-list .spost-image:hover,
.tagcloud a:hover,
#footer.footer-dark .tagcloud a:hover,
.widget-scroll-prev:hover,
.widget-scroll-next:hover,
#footer.footer-dark .widget-scroll-prev,
#footer.footer-dark .widget-scroll-next { background-color: <?php echo $color; ?>; }

.ei-title h2 span,
.ei-title h3 span,
.ei-slider-thumbs li.ei-slider-element,
.flex-prev:hover,
.flex-next:hover,
.rs-prev:hover,
.rs-next:hover,
.nivo-prevNav:hover,
.nivo-nextNav:hover,
.camera_prev:hover,
.camera_next:hover,
.camera_commands:hover,
.tp-leftarrow.large:hover,
.tp-rightarrow.large:hover,
.ls-noskin .ls-nav-prev:hover,
.ls-noskin .ls-nav-next:hover { background-color: <?php echo $color; ?> !important; }

.ei-title h3 span { background-color: rgba(11,11,11,0.8) !important; }


/* ----------------------------------------------------------------
    Border Colors
-----------------------------------------------------------------*/


#top-menu li a:hover,
.comment-content .comment-author a:hover,
.our-clients li:hover { border-color: <?php echo $color; ?>; }


#header.header2,
.flex-control-thumbs li img.flex-active,
.rs-thumb-wrap a.active,
.tab_widget ul.tabs li.active,
#footer,
#copyrights { border-top-color: <?php echo $color; ?>; }


span.page-divider span,
#portfolio-filter li.activeFilter,
.portfolio-item:hover .portfolio-title,
#footer.footer-dark .portfolio-item:hover .portfolio-title { border-bottom-color: <?php echo $color; ?>; }


.slide-caption,
.rs-caption,
.nivo-caption,
.promo,
.side-tabs ul.tabs li.active { border-left-color: <?php echo $color; ?>; }

.ei-title h3 span { border-left-color: <?php echo $color; ?> !important; }


/* ----------------------------------------------------------------
    Selection Colors
-----------------------------------------------------------------*/


::selection,
::-moz-selection,
::-webkit-selection { background-color: <?php echo $color; ?>; }