// Compiled by ClojureScript 1.7.228 {:static-fns true, :optimize-constants true}
goog.provide('org.numenta.sanity.demos.q_learning_2d');
goog.require('cljs.core');
goog.require('org.numenta.sanity.plots_canvas');
goog.require('goog.dom');
goog.require('reagent.core');
goog.require('org.numenta.sanity.helpers');
goog.require('org.numenta.sanity.main');
goog.require('org.nfrac.comportex.demos.q_learning_2d');
goog.require('org.numenta.sanity.util');
goog.require('org.numenta.sanity.comportex.data');
goog.require('goog.string');
goog.require('cljs.core.async');
goog.require('org.numenta.sanity.bridge.marshalling');
goog.require('reagent_forms.core');
goog.require('org.nfrac.comportex.core');
goog.require('org.numenta.sanity.bridge.browser');
goog.require('org.numenta.sanity.demos.q_learning_1d');
goog.require('org.numenta.sanity.demos.comportex_common');
goog.require('org.nfrac.comportex.util');
goog.require('goog.string.format');
goog.require('monet.canvas');
org.numenta.sanity.demos.q_learning_2d.config = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$n_DASH_regions,(1)], null));
org.numenta.sanity.demos.q_learning_2d.world_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$2(cljs.core.async.buffer((1)),cljs.core.map.cljs$core$IFn$_invoke$arity$1((function (p1__72881_SHARP_){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(p1__72881_SHARP_,cljs.core.cst$kw$label,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$x.cljs$core$IFn$_invoke$arity$1(p1__72881_SHARP_),cljs.core.cst$kw$y.cljs$core$IFn$_invoke$arity$1(p1__72881_SHARP_)], null));
})));
org.numenta.sanity.demos.q_learning_2d.into_sim = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
org.numenta.sanity.demos.q_learning_2d.model = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
org.numenta.sanity.demos.q_learning_2d.draw_world = (function org$numenta$sanity$demos$q_learning_2d$draw_world(ctx,inval,htm){
var surface = org.nfrac.comportex.demos.q_learning_2d.surface;
var x_max = cljs.core.count(surface);
var y_max = cljs.core.count(cljs.core.first(surface));
var x_lim = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(0),x_max], null);
var y_lim = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(0),y_max], null);
var width_px = ctx.canvas.width;
var height_px = ctx.canvas.height;
var edge_px = (function (){var x__6491__auto__ = width_px;
var y__6492__auto__ = height_px;
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})();
var plot_size = new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$w,edge_px,cljs.core.cst$kw$h,edge_px], null);
var plot = org.numenta.sanity.plots_canvas.xy_plot(ctx,plot_size,x_lim,y_lim);
monet.canvas.clear_rect(ctx,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$x,(0),cljs.core.cst$kw$y,(0),cljs.core.cst$kw$w,width_px,cljs.core.cst$kw$h,height_px], null));

org.numenta.sanity.plots_canvas.frame_BANG_(plot);

var seq__72914_72946 = cljs.core.seq(cljs.core.range.cljs$core$IFn$_invoke$arity$1(cljs.core.count(surface)));
var chunk__72921_72947 = null;
var count__72922_72948 = (0);
var i__72923_72949 = (0);
while(true){
if((i__72923_72949 < count__72922_72948)){
var y_72950 = chunk__72921_72947.cljs$core$IIndexed$_nth$arity$2(null,i__72923_72949);
var seq__72924_72951 = cljs.core.seq(cljs.core.range.cljs$core$IFn$_invoke$arity$1(cljs.core.count(cljs.core.first(surface))));
var chunk__72926_72952 = null;
var count__72927_72953 = (0);
var i__72928_72954 = (0);
while(true){
if((i__72928_72954 < count__72927_72953)){
var x_72955 = chunk__72926_72952.cljs$core$IIndexed$_nth$arity$2(null,i__72928_72954);
var v_72956 = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(surface,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x_72955,y_72950], null));
if((v_72956 >= (10))){
monet.canvas.fill_style(ctx,"#66ff66");

org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_72955,y_72950,(1),(1));
} else {
if((v_72956 <= (-10))){
monet.canvas.fill_style(ctx,"black");

org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_72955,y_72950,(1),(1));
} else {
}
}

var G__72957 = seq__72924_72951;
var G__72958 = chunk__72926_72952;
var G__72959 = count__72927_72953;
var G__72960 = (i__72928_72954 + (1));
seq__72924_72951 = G__72957;
chunk__72926_72952 = G__72958;
count__72927_72953 = G__72959;
i__72928_72954 = G__72960;
continue;
} else {
var temp__4657__auto___72961 = cljs.core.seq(seq__72924_72951);
if(temp__4657__auto___72961){
var seq__72924_72962__$1 = temp__4657__auto___72961;
if(cljs.core.chunked_seq_QMARK_(seq__72924_72962__$1)){
var c__6956__auto___72963 = cljs.core.chunk_first(seq__72924_72962__$1);
var G__72964 = cljs.core.chunk_rest(seq__72924_72962__$1);
var G__72965 = c__6956__auto___72963;
var G__72966 = cljs.core.count(c__6956__auto___72963);
var G__72967 = (0);
seq__72924_72951 = G__72964;
chunk__72926_72952 = G__72965;
count__72927_72953 = G__72966;
i__72928_72954 = G__72967;
continue;
} else {
var x_72968 = cljs.core.first(seq__72924_72962__$1);
var v_72969 = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(surface,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x_72968,y_72950], null));
if((v_72969 >= (10))){
monet.canvas.fill_style(ctx,"#66ff66");

org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_72968,y_72950,(1),(1));
} else {
if((v_72969 <= (-10))){
monet.canvas.fill_style(ctx,"black");

org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_72968,y_72950,(1),(1));
} else {
}
}

var G__72970 = cljs.core.next(seq__72924_72962__$1);
var G__72971 = null;
var G__72972 = (0);
var G__72973 = (0);
seq__72924_72951 = G__72970;
chunk__72926_72952 = G__72971;
count__72927_72953 = G__72972;
i__72928_72954 = G__72973;
continue;
}
} else {
}
}
break;
}

var G__72974 = seq__72914_72946;
var G__72975 = chunk__72921_72947;
var G__72976 = count__72922_72948;
var G__72977 = (i__72923_72949 + (1));
seq__72914_72946 = G__72974;
chunk__72921_72947 = G__72975;
count__72922_72948 = G__72976;
i__72923_72949 = G__72977;
continue;
} else {
var temp__4657__auto___72978 = cljs.core.seq(seq__72914_72946);
if(temp__4657__auto___72978){
var seq__72914_72979__$1 = temp__4657__auto___72978;
if(cljs.core.chunked_seq_QMARK_(seq__72914_72979__$1)){
var c__6956__auto___72980 = cljs.core.chunk_first(seq__72914_72979__$1);
var G__72981 = cljs.core.chunk_rest(seq__72914_72979__$1);
var G__72982 = c__6956__auto___72980;
var G__72983 = cljs.core.count(c__6956__auto___72980);
var G__72984 = (0);
seq__72914_72946 = G__72981;
chunk__72921_72947 = G__72982;
count__72922_72948 = G__72983;
i__72923_72949 = G__72984;
continue;
} else {
var y_72985 = cljs.core.first(seq__72914_72979__$1);
var seq__72915_72986 = cljs.core.seq(cljs.core.range.cljs$core$IFn$_invoke$arity$1(cljs.core.count(cljs.core.first(surface))));
var chunk__72917_72987 = null;
var count__72918_72988 = (0);
var i__72919_72989 = (0);
while(true){
if((i__72919_72989 < count__72918_72988)){
var x_72990 = chunk__72917_72987.cljs$core$IIndexed$_nth$arity$2(null,i__72919_72989);
var v_72991 = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(surface,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x_72990,y_72985], null));
if((v_72991 >= (10))){
monet.canvas.fill_style(ctx,"#66ff66");

org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_72990,y_72985,(1),(1));
} else {
if((v_72991 <= (-10))){
monet.canvas.fill_style(ctx,"black");

org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_72990,y_72985,(1),(1));
} else {
}
}

var G__72992 = seq__72915_72986;
var G__72993 = chunk__72917_72987;
var G__72994 = count__72918_72988;
var G__72995 = (i__72919_72989 + (1));
seq__72915_72986 = G__72992;
chunk__72917_72987 = G__72993;
count__72918_72988 = G__72994;
i__72919_72989 = G__72995;
continue;
} else {
var temp__4657__auto___72996__$1 = cljs.core.seq(seq__72915_72986);
if(temp__4657__auto___72996__$1){
var seq__72915_72997__$1 = temp__4657__auto___72996__$1;
if(cljs.core.chunked_seq_QMARK_(seq__72915_72997__$1)){
var c__6956__auto___72998 = cljs.core.chunk_first(seq__72915_72997__$1);
var G__72999 = cljs.core.chunk_rest(seq__72915_72997__$1);
var G__73000 = c__6956__auto___72998;
var G__73001 = cljs.core.count(c__6956__auto___72998);
var G__73002 = (0);
seq__72915_72986 = G__72999;
chunk__72917_72987 = G__73000;
count__72918_72988 = G__73001;
i__72919_72989 = G__73002;
continue;
} else {
var x_73003 = cljs.core.first(seq__72915_72997__$1);
var v_73004 = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(surface,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x_73003,y_72985], null));
if((v_73004 >= (10))){
monet.canvas.fill_style(ctx,"#66ff66");

org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_73003,y_72985,(1),(1));
} else {
if((v_73004 <= (-10))){
monet.canvas.fill_style(ctx,"black");

org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_73003,y_72985,(1),(1));
} else {
}
}

var G__73005 = cljs.core.next(seq__72915_72997__$1);
var G__73006 = null;
var G__73007 = (0);
var G__73008 = (0);
seq__72915_72986 = G__73005;
chunk__72917_72987 = G__73006;
count__72918_72988 = G__73007;
i__72919_72989 = G__73008;
continue;
}
} else {
}
}
break;
}

var G__73009 = cljs.core.next(seq__72914_72979__$1);
var G__73010 = null;
var G__73011 = (0);
var G__73012 = (0);
seq__72914_72946 = G__73009;
chunk__72921_72947 = G__73010;
count__72922_72948 = G__73011;
i__72923_72949 = G__73012;
continue;
}
} else {
}
}
break;
}

var seq__72930_73013 = cljs.core.seq(cljs.core.cst$kw$Q_DASH_map.cljs$core$IFn$_invoke$arity$1(inval));
var chunk__72932_73014 = null;
var count__72933_73015 = (0);
var i__72934_73016 = (0);
while(true){
if((i__72934_73016 < count__72933_73015)){
var vec__72936_73017 = chunk__72932_73014.cljs$core$IIndexed$_nth$arity$2(null,i__72934_73016);
var state_action_73018 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72936_73017,(0),null);
var q_73019 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72936_73017,(1),null);
var map__72937_73020 = state_action_73018;
var map__72937_73021__$1 = ((((!((map__72937_73020 == null)))?((((map__72937_73020.cljs$lang$protocol_mask$partition0$ & (64))) || (map__72937_73020.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__72937_73020):map__72937_73020);
var x_73022 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72937_73021__$1,cljs.core.cst$kw$x);
var y_73023 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72937_73021__$1,cljs.core.cst$kw$y);
var action_73024 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72937_73021__$1,cljs.core.cst$kw$action);
var map__72938_73025 = action_73024;
var map__72938_73026__$1 = ((((!((map__72938_73025 == null)))?((((map__72938_73025.cljs$lang$protocol_mask$partition0$ & (64))) || (map__72938_73025.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__72938_73025):map__72938_73025);
var dx_73027 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72938_73026__$1,cljs.core.cst$kw$dx);
var dy_73028 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72938_73026__$1,cljs.core.cst$kw$dy);
monet.canvas.fill_style(ctx,(((q_73019 > (0)))?"green":"red"));

monet.canvas.alpha(ctx,org.nfrac.comportex.util.abs(q_73019));

if((dx_73027 > (0))){
org.numenta.sanity.plots_canvas.rect_BANG_(plot,(x_73022 - 0.25),y_73023,0.25,(1));
} else {
if((dx_73027 < (0))){
org.numenta.sanity.plots_canvas.rect_BANG_(plot,(x_73022 + (1)),y_73023,0.25,(1));
} else {
if((dy_73028 > (0))){
org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_73022,(y_73023 - 0.25),(1),0.25);
} else {
if((dy_73028 < (0))){
org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_73022,(y_73023 + (1)),(1),0.25);
} else {
}
}
}
}

var G__73029 = seq__72930_73013;
var G__73030 = chunk__72932_73014;
var G__73031 = count__72933_73015;
var G__73032 = (i__72934_73016 + (1));
seq__72930_73013 = G__73029;
chunk__72932_73014 = G__73030;
count__72933_73015 = G__73031;
i__72934_73016 = G__73032;
continue;
} else {
var temp__4657__auto___73033 = cljs.core.seq(seq__72930_73013);
if(temp__4657__auto___73033){
var seq__72930_73034__$1 = temp__4657__auto___73033;
if(cljs.core.chunked_seq_QMARK_(seq__72930_73034__$1)){
var c__6956__auto___73035 = cljs.core.chunk_first(seq__72930_73034__$1);
var G__73036 = cljs.core.chunk_rest(seq__72930_73034__$1);
var G__73037 = c__6956__auto___73035;
var G__73038 = cljs.core.count(c__6956__auto___73035);
var G__73039 = (0);
seq__72930_73013 = G__73036;
chunk__72932_73014 = G__73037;
count__72933_73015 = G__73038;
i__72934_73016 = G__73039;
continue;
} else {
var vec__72941_73040 = cljs.core.first(seq__72930_73034__$1);
var state_action_73041 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72941_73040,(0),null);
var q_73042 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72941_73040,(1),null);
var map__72942_73043 = state_action_73041;
var map__72942_73044__$1 = ((((!((map__72942_73043 == null)))?((((map__72942_73043.cljs$lang$protocol_mask$partition0$ & (64))) || (map__72942_73043.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__72942_73043):map__72942_73043);
var x_73045 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72942_73044__$1,cljs.core.cst$kw$x);
var y_73046 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72942_73044__$1,cljs.core.cst$kw$y);
var action_73047 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72942_73044__$1,cljs.core.cst$kw$action);
var map__72943_73048 = action_73047;
var map__72943_73049__$1 = ((((!((map__72943_73048 == null)))?((((map__72943_73048.cljs$lang$protocol_mask$partition0$ & (64))) || (map__72943_73048.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__72943_73048):map__72943_73048);
var dx_73050 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72943_73049__$1,cljs.core.cst$kw$dx);
var dy_73051 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__72943_73049__$1,cljs.core.cst$kw$dy);
monet.canvas.fill_style(ctx,(((q_73042 > (0)))?"green":"red"));

monet.canvas.alpha(ctx,org.nfrac.comportex.util.abs(q_73042));

if((dx_73050 > (0))){
org.numenta.sanity.plots_canvas.rect_BANG_(plot,(x_73045 - 0.25),y_73046,0.25,(1));
} else {
if((dx_73050 < (0))){
org.numenta.sanity.plots_canvas.rect_BANG_(plot,(x_73045 + (1)),y_73046,0.25,(1));
} else {
if((dy_73051 > (0))){
org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_73045,(y_73046 - 0.25),(1),0.25);
} else {
if((dy_73051 < (0))){
org.numenta.sanity.plots_canvas.rect_BANG_(plot,x_73045,(y_73046 + (1)),(1),0.25);
} else {
}
}
}
}

var G__73052 = cljs.core.next(seq__72930_73034__$1);
var G__73053 = null;
var G__73054 = (0);
var G__73055 = (0);
seq__72930_73013 = G__73052;
chunk__72932_73014 = G__73053;
count__72933_73015 = G__73054;
i__72934_73016 = G__73055;
continue;
}
} else {
}
}
break;
}

monet.canvas.alpha(ctx,(1));

var x_EQ__73056 = (0.5 + cljs.core.cst$kw$x.cljs$core$IFn$_invoke$arity$1(inval));
var y_EQ__73057 = (0.5 + cljs.core.cst$kw$y.cljs$core$IFn$_invoke$arity$1(inval));
var dx_1_73058 = cljs.core.cst$kw$dx.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$prev_DASH_action.cljs$core$IFn$_invoke$arity$1(inval));
var dy_1_73059 = cljs.core.cst$kw$dy.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$prev_DASH_action.cljs$core$IFn$_invoke$arity$1(inval));
var dx_73060 = cljs.core.cst$kw$dx.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$action.cljs$core$IFn$_invoke$arity$1(inval));
var dy_73061 = cljs.core.cst$kw$dy.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$action.cljs$core$IFn$_invoke$arity$1(inval));
monet.canvas.stroke_style(ctx,"black");

org.numenta.sanity.plots_canvas.line_BANG_(plot,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(x_EQ__73056 - dx_1_73058),(y_EQ__73057 - dy_1_73059)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x_EQ__73056,y_EQ__73057], null)], null));

monet.canvas.stroke_style(ctx,"#888");

org.numenta.sanity.plots_canvas.line_BANG_(plot,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x_EQ__73056,y_EQ__73057], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(x_EQ__73056 + dx_73060),(y_EQ__73057 + dy_73061)], null)], null));

monet.canvas.stroke_style(ctx,"#888");

monet.canvas.fill_style(ctx,"white");

org.numenta.sanity.plots_canvas.point_BANG_(plot,(x_EQ__73056 - dx_1_73058),(y_EQ__73057 - dy_1_73059),(3));

monet.canvas.stroke_style(ctx,"black");

monet.canvas.fill_style(ctx,"yellow");

org.numenta.sanity.plots_canvas.point_BANG_(plot,x_EQ__73056,y_EQ__73057,(4));

monet.canvas.stroke_style(ctx,"black");

return org.numenta.sanity.plots_canvas.grid_BANG_(plot,cljs.core.PersistentArrayMap.EMPTY);
});
org.numenta.sanity.demos.q_learning_2d.signed_str = (function org$numenta$sanity$demos$q_learning_2d$signed_str(x){
return [cljs.core.str((((x < (0)))?"":"+")),cljs.core.str(x)].join('');
});
org.numenta.sanity.demos.q_learning_2d.world_pane = (function org$numenta$sanity$demos$q_learning_2d$world_pane(){
var selected_htm = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
cljs.core.add_watch(org.numenta.sanity.main.selection,cljs.core.cst$kw$org$numenta$sanity$demos$q_DASH_learning_DASH_2d_SLASH_fetch_DASH_selected_DASH_htm,((function (selected_htm){
return (function (_,___$1,___$2,p__73077){
var vec__73078 = p__73077;
var sel1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73078,(0),null);
var temp__4657__auto__ = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(sel1,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$step,cljs.core.cst$kw$snapshot_DASH_id], null));
if(cljs.core.truth_(temp__4657__auto__)){
var snapshot_id = temp__4657__auto__;
var out_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.main.into_journal,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, ["get-model",snapshot_id,org.numenta.sanity.bridge.marshalling.channel.cljs$core$IFn$_invoke$arity$2(out_c,true)], null));

var c__38109__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__73078,sel1,selected_htm){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__73078,sel1,selected_htm){
return (function (state_73083){
var state_val_73084 = (state_73083[(1)]);
if((state_val_73084 === (1))){
var state_73083__$1 = state_73083;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_73083__$1,(2),out_c);
} else {
if((state_val_73084 === (2))){
var inst_73080 = (state_73083[(2)]);
var inst_73081 = (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(selected_htm,inst_73080) : cljs.core.reset_BANG_.call(null,selected_htm,inst_73080));
var state_73083__$1 = state_73083;
return cljs.core.async.impl.ioc_helpers.return_chan(state_73083__$1,inst_73081);
} else {
return null;
}
}
});})(c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__73078,sel1,selected_htm))
;
return ((function (switch__37995__auto__,c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__73078,sel1,selected_htm){
return (function() {
var org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto____0 = (function (){
var statearr_73088 = [null,null,null,null,null,null,null];
(statearr_73088[(0)] = org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto__);

(statearr_73088[(1)] = (1));

return statearr_73088;
});
var org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto____1 = (function (state_73083){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_73083);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e73089){if((e73089 instanceof Object)){
var ex__37999__auto__ = e73089;
var statearr_73090_73092 = state_73083;
(statearr_73090_73092[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_73083);

return cljs.core.cst$kw$recur;
} else {
throw e73089;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__73093 = state_73083;
state_73083 = G__73093;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto__ = function(state_73083){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto____1.call(this,state_73083);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto____0;
org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$q_learning_2d$world_pane_$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__73078,sel1,selected_htm))
})();
var state__38111__auto__ = (function (){var statearr_73091 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_73091[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto__);

return statearr_73091;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__73078,sel1,selected_htm))
);

return c__38109__auto__;
} else {
return null;
}
});})(selected_htm))
);

return ((function (selected_htm){
return (function (){
var temp__4657__auto__ = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(selected_htm) : cljs.core.deref.call(null,selected_htm));
if(cljs.core.truth_(temp__4657__auto__)){
var htm = temp__4657__auto__;
var inval = cljs.core.cst$kw$input_DASH_value.cljs$core$IFn$_invoke$arity$1(htm);
var DELTA = goog.string.unescapeEntities("&Delta;");
var TIMES = goog.string.unescapeEntities("&times;");
return new cljs.core.PersistentVector(null, 7, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p$muted,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"Input on selected timestep."], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p$muted,new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"Reward ",new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$var,"R"], null)," = z ",TIMES," 0.01"], null)], null),new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$table$table$table_DASH_condensed,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$tr,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$th,"x,y"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"position"], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,cljs.core.cst$kw$x.cljs$core$IFn$_invoke$arity$1(inval),",",cljs.core.cst$kw$y.cljs$core$IFn$_invoke$arity$1(inval)], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$tr,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$th,[cljs.core.str(DELTA),cljs.core.str("x,"),cljs.core.str(DELTA),cljs.core.str("y")].join('')], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"action"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,[cljs.core.str(org.numenta.sanity.demos.q_learning_2d.signed_str(cljs.core.cst$kw$dx.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$prev_DASH_action.cljs$core$IFn$_invoke$arity$1(inval)))),cljs.core.str(","),cljs.core.str(org.numenta.sanity.demos.q_learning_2d.signed_str(cljs.core.cst$kw$dy.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$prev_DASH_action.cljs$core$IFn$_invoke$arity$1(inval))))].join('')], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$tr,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$th,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$var,"z"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"~reward"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,org.numenta.sanity.demos.q_learning_2d.signed_str(cljs.core.cst$kw$z.cljs$core$IFn$_invoke$arity$1(inval))], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$tr,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$th,[cljs.core.str(DELTA),cljs.core.str("x,"),cljs.core.str(DELTA),cljs.core.str("y")].join(''),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$sub,"t+1"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"action"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,[cljs.core.str(org.numenta.sanity.demos.q_learning_2d.signed_str(cljs.core.cst$kw$dx.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$action.cljs$core$IFn$_invoke$arity$1(inval)))),cljs.core.str(","),cljs.core.str(org.numenta.sanity.demos.q_learning_2d.signed_str(cljs.core.cst$kw$dy.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$action.cljs$core$IFn$_invoke$arity$1(inval))))].join('')], null)], null)], null),org.numenta.sanity.demos.q_learning_1d.q_learning_sub_pane(htm),new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.helpers.resizing_canvas,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$width,"100%",cljs.core.cst$kw$height,"240px"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.main.selection,selected_htm], null),((function (inval,DELTA,TIMES,htm,temp__4657__auto__,selected_htm){
return (function (ctx){
var step = org.numenta.sanity.main.selected_step.cljs$core$IFn$_invoke$arity$0();
var inval__$1 = cljs.core.cst$kw$input_DASH_value.cljs$core$IFn$_invoke$arity$1(step);
return org.numenta.sanity.demos.q_learning_2d.draw_world(ctx,inval__$1,(cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(selected_htm) : cljs.core.deref.call(null,selected_htm)));
});})(inval,DELTA,TIMES,htm,temp__4657__auto__,selected_htm))
,null], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Current position on the objective function surface. ","Also shows approx Q values for each position/action combination,\n            where green is positive and red is negative.\n            These are the last seen Q values including last adjustments."], null)], null)], null);
} else {
return null;
}
});
;})(selected_htm))
});
org.numenta.sanity.demos.q_learning_2d.set_model_BANG_ = (function org$numenta$sanity$demos$q_learning_2d$set_model_BANG_(){
return org.numenta.sanity.helpers.with_ui_loading_message((function (){
var init_QMARK_ = ((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.q_learning_2d.model) : cljs.core.deref.call(null,org.numenta.sanity.demos.q_learning_2d.model)) == null);
var c__38109__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto__,init_QMARK_){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto__,init_QMARK_){
return (function (state_73153){
var state_val_73154 = (state_73153[(1)]);
if((state_val_73154 === (1))){
var state_73153__$1 = state_73153;
if(init_QMARK_){
var statearr_73155_73172 = state_73153__$1;
(statearr_73155_73172[(1)] = (2));

} else {
var statearr_73156_73173 = state_73153__$1;
(statearr_73156_73173[(1)] = (3));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_73154 === (2))){
var state_73153__$1 = state_73153;
var statearr_73157_73174 = state_73153__$1;
(statearr_73157_73174[(2)] = null);

(statearr_73157_73174[(1)] = (4));


return cljs.core.cst$kw$recur;
} else {
if((state_val_73154 === (3))){
var state_73153__$1 = state_73153;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_73153__$1,(5),org.numenta.sanity.demos.q_learning_2d.world_c);
} else {
if((state_val_73154 === (4))){
var inst_73138 = (state_73153[(2)]);
var inst_73139 = org.nfrac.comportex.demos.q_learning_2d.make_model();
var inst_73140 = (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.demos.q_learning_2d.model,inst_73139) : cljs.core.reset_BANG_.call(null,org.numenta.sanity.demos.q_learning_2d.model,inst_73139));
var state_73153__$1 = (function (){var statearr_73158 = state_73153;
(statearr_73158[(7)] = inst_73140);

(statearr_73158[(8)] = inst_73138);

return statearr_73158;
})();
if(init_QMARK_){
var statearr_73159_73175 = state_73153__$1;
(statearr_73159_73175[(1)] = (6));

} else {
var statearr_73160_73176 = state_73153__$1;
(statearr_73160_73176[(1)] = (7));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_73154 === (5))){
var inst_73136 = (state_73153[(2)]);
var state_73153__$1 = state_73153;
var statearr_73161_73177 = state_73153__$1;
(statearr_73161_73177[(2)] = inst_73136);

(statearr_73161_73177[(1)] = (4));


return cljs.core.cst$kw$recur;
} else {
if((state_val_73154 === (6))){
var inst_73142 = org.nfrac.comportex.demos.q_learning_2d.htm_step_with_action_selection(org.numenta.sanity.demos.q_learning_2d.world_c);
var inst_73143 = org.numenta.sanity.bridge.browser.init.cljs$core$IFn$_invoke$arity$5(org.numenta.sanity.demos.q_learning_2d.model,org.numenta.sanity.demos.q_learning_2d.world_c,org.numenta.sanity.main.into_journal,org.numenta.sanity.demos.q_learning_2d.into_sim,inst_73142);
var state_73153__$1 = state_73153;
var statearr_73162_73178 = state_73153__$1;
(statearr_73162_73178[(2)] = inst_73143);

(statearr_73162_73178[(1)] = (8));


return cljs.core.cst$kw$recur;
} else {
if((state_val_73154 === (7))){
var inst_73145 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.q_learning_2d.model) : cljs.core.deref.call(null,org.numenta.sanity.demos.q_learning_2d.model));
var inst_73146 = org.numenta.sanity.comportex.data.network_shape(inst_73145);
var inst_73147 = org.numenta.sanity.util.translate_network_shape(inst_73146);
var inst_73148 = (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.main.network_shape,inst_73147) : cljs.core.reset_BANG_.call(null,org.numenta.sanity.main.network_shape,inst_73147));
var state_73153__$1 = state_73153;
var statearr_73163_73179 = state_73153__$1;
(statearr_73163_73179[(2)] = inst_73148);

(statearr_73163_73179[(1)] = (8));


return cljs.core.cst$kw$recur;
} else {
if((state_val_73154 === (8))){
var inst_73150 = (state_73153[(2)]);
var inst_73151 = cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.demos.q_learning_2d.world_c,org.nfrac.comportex.demos.q_learning_2d.initial_inval);
var state_73153__$1 = (function (){var statearr_73164 = state_73153;
(statearr_73164[(9)] = inst_73150);

return statearr_73164;
})();
return cljs.core.async.impl.ioc_helpers.return_chan(state_73153__$1,inst_73151);
} else {
return null;
}
}
}
}
}
}
}
}
});})(c__38109__auto__,init_QMARK_))
;
return ((function (switch__37995__auto__,c__38109__auto__,init_QMARK_){
return (function() {
var org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto____0 = (function (){
var statearr_73168 = [null,null,null,null,null,null,null,null,null,null];
(statearr_73168[(0)] = org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto__);

(statearr_73168[(1)] = (1));

return statearr_73168;
});
var org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto____1 = (function (state_73153){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_73153);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e73169){if((e73169 instanceof Object)){
var ex__37999__auto__ = e73169;
var statearr_73170_73180 = state_73153;
(statearr_73170_73180[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_73153);

return cljs.core.cst$kw$recur;
} else {
throw e73169;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__73181 = state_73153;
state_73153 = G__73181;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto__ = function(state_73153){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto____1.call(this,state_73153);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto____0;
org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$q_learning_2d$set_model_BANG__$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto__,init_QMARK_))
})();
var state__38111__auto__ = (function (){var statearr_73171 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_73171[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto__);

return statearr_73171;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto__,init_QMARK_))
);

return c__38109__auto__;
}));
});
org.numenta.sanity.demos.q_learning_2d.config_template = new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_horizontal,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$label$col_DASH_sm_DASH_5,"Number of regions:"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_7,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$input$form_DASH_control,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$field,cljs.core.cst$kw$numeric,cljs.core.cst$kw$id,cljs.core.cst$kw$n_DASH_regions], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_offset_DASH_5$col_DASH_sm_DASH_7,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$button$btn$btn_DASH_default,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$on_DASH_click,(function (e){
org.numenta.sanity.demos.q_learning_2d.set_model_BANG_();

return e.preventDefault();
})], null),"Restart with new model"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p$text_DASH_danger,"This resets all parameters."], null)], null)], null)], null);
org.numenta.sanity.demos.q_learning_2d.model_tab = (function org$numenta$sanity$demos$q_learning_2d$model_tab(){
return new cljs.core.PersistentVector(null, 14, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Highly experimental attempt at integrating ",new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$a,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$href,"http://en.wikipedia.org/wiki/Q-learning"], null),"Q learning"], null)," (reinforcement learning)."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$h4,"General approach"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"A Q value indicates the goodness of taking an action from some\n        state. We represent a Q value by the average permanence of\n        synapses activating the action from that state, minus the\n        initial permanence value."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"The action region columns are activated just like any other\n        region, but are then interpreted to produce an action."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Adjustments to a Q value, based on reward and expected future\n        reward, are applied to the permanence of synapses which\n        directly activated the action (columns). This adjustment\n        applies in the action layer only, where it replaces the usual\n        learning of proximal synapses (spatial pooling)."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Exploration arises from the usual boosting of neglected\n        columns, primarily in the action layer."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$h4,"This example"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"The agent can move up, down, left or right on a surface.\n        The reward is -3 on normal squares, -200 on hazard squares\n        and +200 on the goal square. These are divided by 100 for\n        comparison to Q values on the synaptic permanence scale."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"The action layer columns are interpreted to produce an\n        action. 10 columns are allocated to each of the four\n        directions of movement, and the direction with most active\n        columns is used to move the agent."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"The input is the location of the agent via coordinate\n        encoder, plus the last movement as distal input."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"This example is episodic: when the agent reaches either the\n        goal or a hazard it is returned to the starting point. Success\n        is indicated by the agent following a direct path to the goal\n        square."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$h3,"HTM model"], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [reagent_forms.core.bind_fields,org.numenta.sanity.demos.q_learning_2d.config_template,org.numenta.sanity.demos.q_learning_2d.config], null)], null);
});
org.numenta.sanity.demos.q_learning_2d.init = (function org$numenta$sanity$demos$q_learning_2d$init(){
reagent.core.render.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.main.sanity_app,"Comportex",new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.q_learning_2d.model_tab], null),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.q_learning_2d.world_pane], null),org.numenta.sanity.demos.comportex_common.all_features,org.numenta.sanity.demos.q_learning_2d.into_sim], null),goog.dom.getElement("sanity-app"));

cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(org.numenta.sanity.main.viz_options,cljs.core.assoc_in,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$drawing,cljs.core.cst$kw$display_DASH_mode], null),cljs.core.cst$kw$two_DASH_d);

return org.numenta.sanity.demos.q_learning_2d.set_model_BANG_();
});
goog.exportSymbol('org.numenta.sanity.demos.q_learning_2d.init', org.numenta.sanity.demos.q_learning_2d.init);
