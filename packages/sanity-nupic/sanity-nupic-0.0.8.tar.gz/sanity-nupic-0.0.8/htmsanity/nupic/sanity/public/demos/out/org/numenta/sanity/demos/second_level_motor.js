// Compiled by ClojureScript 1.7.228 {:static-fns true, :optimize-constants true}
goog.provide('org.numenta.sanity.demos.second_level_motor');
goog.require('cljs.core');
goog.require('org.numenta.sanity.plots_canvas');
goog.require('goog.dom.forms');
goog.require('goog.dom');
goog.require('reagent.core');
goog.require('org.numenta.sanity.helpers');
goog.require('org.numenta.sanity.main');
goog.require('org.nfrac.comportex.demos.second_level_motor');
goog.require('org.numenta.sanity.util');
goog.require('org.numenta.sanity.comportex.data');
goog.require('cljs.core.async');
goog.require('reagent_forms.core');
goog.require('org.nfrac.comportex.core');
goog.require('org.numenta.sanity.bridge.browser');
goog.require('org.numenta.sanity.demos.comportex_common');
goog.require('monet.canvas');
goog.require('org.numenta.sanity.demos.sensorimotor_1d');
goog.require('clojure.string');
org.numenta.sanity.demos.second_level_motor.config = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$text,org.nfrac.comportex.demos.second_level_motor.test_text,cljs.core.cst$kw$edit_DASH_text,org.nfrac.comportex.demos.second_level_motor.test_text], null));
org.numenta.sanity.demos.second_level_motor.world_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$2(cljs.core.async.buffer((1)),cljs.core.map.cljs$core$IFn$_invoke$arity$1((function (p1__73491_SHARP_){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(p1__73491_SHARP_,cljs.core.cst$kw$label,cljs.core.cst$kw$value.cljs$core$IFn$_invoke$arity$1(p1__73491_SHARP_));
})));
org.numenta.sanity.demos.second_level_motor.control_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
org.numenta.sanity.demos.second_level_motor.into_sim = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
org.numenta.sanity.demos.second_level_motor.model = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
org.numenta.sanity.demos.second_level_motor.draw_world = (function org$numenta$sanity$demos$second_level_motor$draw_world(ctx,inval){
var map__73509 = inval;
var map__73509__$1 = ((((!((map__73509 == null)))?((((map__73509.cljs$lang$protocol_mask$partition0$ & (64))) || (map__73509.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__73509):map__73509);
var sentences = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__73509__$1,cljs.core.cst$kw$sentences);
var position = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__73509__$1,cljs.core.cst$kw$position);
var vec__73510 = position;
var i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73510,(0),null);
var j = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73510,(1),null);
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73510,(2),null);
var sentence = cljs.core.get.cljs$core$IFn$_invoke$arity$2(sentences,i);
var word_n_letters = cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.comp.cljs$core$IFn$_invoke$arity$2(cljs.core.inc,cljs.core.count),sentence);
var sentence_flat = cljs.core.concat.cljs$core$IFn$_invoke$arity$2(cljs.core.flatten(cljs.core.interpose.cljs$core$IFn$_invoke$arity$2(" ",sentence)),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, ["."], null));
var n_letters = cljs.core.reduce.cljs$core$IFn$_invoke$arity$2(cljs.core._PLUS_,word_n_letters);
var x_lim = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(0),(1)], null);
var y_lim = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(0),n_letters], null);
var width_px = ctx.canvas.width;
var height_px = ctx.canvas.height;
var plot_size = new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$w,width_px,cljs.core.cst$kw$h,height_px], null);
var plot = org.numenta.sanity.plots_canvas.xy_plot(ctx,plot_size,x_lim,y_lim);
var x_scale = org.numenta.sanity.plots_canvas.scale_fn(x_lim,cljs.core.cst$kw$w.cljs$core$IFn$_invoke$arity$1(plot_size));
var y_scale = org.numenta.sanity.plots_canvas.scale_fn(y_lim,cljs.core.cst$kw$h.cljs$core$IFn$_invoke$arity$1(plot_size));
monet.canvas.clear_rect(ctx,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$x,(0),cljs.core.cst$kw$y,(0),cljs.core.cst$kw$w,width_px,cljs.core.cst$kw$h,height_px], null));

org.numenta.sanity.plots_canvas.frame_BANG_(plot);

monet.canvas.font_style(ctx,[cljs.core.str((function (){var x__6491__auto__ = (30);
var y__6492__auto__ = ((height_px / n_letters) | (0));
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})()),cljs.core.str("px monospace")].join(''));

monet.canvas.text_baseline(ctx,cljs.core.cst$kw$middle);

monet.canvas.fill_style(ctx,"black");

var seq__73512_73526 = cljs.core.seq(cljs.core.map_indexed.cljs$core$IFn$_invoke$arity$2(cljs.core.vector,sentence_flat));
var chunk__73513_73527 = null;
var count__73514_73528 = (0);
var i__73515_73529 = (0);
while(true){
if((i__73515_73529 < count__73514_73528)){
var vec__73516_73530 = chunk__73513_73527.cljs$core$IIndexed$_nth$arity$2(null,i__73515_73529);
var y_73531 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73516_73530,(0),null);
var letter_73532 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73516_73530,(1),null);
monet.canvas.text(ctx,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$x,(5),cljs.core.cst$kw$y,(function (){var G__73517 = (y_73531 + 0.5);
return (y_scale.cljs$core$IFn$_invoke$arity$1 ? y_scale.cljs$core$IFn$_invoke$arity$1(G__73517) : y_scale.call(null,G__73517));
})(),cljs.core.cst$kw$text,[cljs.core.str(letter_73532)].join('')], null));

var G__73533 = seq__73512_73526;
var G__73534 = chunk__73513_73527;
var G__73535 = count__73514_73528;
var G__73536 = (i__73515_73529 + (1));
seq__73512_73526 = G__73533;
chunk__73513_73527 = G__73534;
count__73514_73528 = G__73535;
i__73515_73529 = G__73536;
continue;
} else {
var temp__4657__auto___73537 = cljs.core.seq(seq__73512_73526);
if(temp__4657__auto___73537){
var seq__73512_73538__$1 = temp__4657__auto___73537;
if(cljs.core.chunked_seq_QMARK_(seq__73512_73538__$1)){
var c__6956__auto___73539 = cljs.core.chunk_first(seq__73512_73538__$1);
var G__73540 = cljs.core.chunk_rest(seq__73512_73538__$1);
var G__73541 = c__6956__auto___73539;
var G__73542 = cljs.core.count(c__6956__auto___73539);
var G__73543 = (0);
seq__73512_73526 = G__73540;
chunk__73513_73527 = G__73541;
count__73514_73528 = G__73542;
i__73515_73529 = G__73543;
continue;
} else {
var vec__73518_73544 = cljs.core.first(seq__73512_73538__$1);
var y_73545 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73518_73544,(0),null);
var letter_73546 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73518_73544,(1),null);
monet.canvas.text(ctx,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$x,(5),cljs.core.cst$kw$y,(function (){var G__73519 = (y_73545 + 0.5);
return (y_scale.cljs$core$IFn$_invoke$arity$1 ? y_scale.cljs$core$IFn$_invoke$arity$1(G__73519) : y_scale.call(null,G__73519));
})(),cljs.core.cst$kw$text,[cljs.core.str(letter_73546)].join('')], null));

var G__73547 = cljs.core.next(seq__73512_73538__$1);
var G__73548 = null;
var G__73549 = (0);
var G__73550 = (0);
seq__73512_73526 = G__73547;
chunk__73513_73527 = G__73548;
count__73514_73528 = G__73549;
i__73515_73529 = G__73550;
continue;
}
} else {
}
}
break;
}

var curr_index = cljs.core.apply.cljs$core$IFn$_invoke$arity$3(cljs.core._PLUS_,k,cljs.core.take.cljs$core$IFn$_invoke$arity$2(j,word_n_letters));
var vec__73520 = org.nfrac.comportex.demos.second_level_motor.next_position(position,cljs.core.cst$kw$action.cljs$core$IFn$_invoke$arity$1(inval));
var ni = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73520,(0),null);
var nj = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73520,(1),null);
var nk = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73520,(2),null);
var sentence_sacc = cljs.core.cst$kw$next_DASH_sentence_DASH_saccade.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$action.cljs$core$IFn$_invoke$arity$1(inval));
var next_index = (((sentence_sacc < (0)))?(-1):(((sentence_sacc > (0)))?(n_letters + (1)):cljs.core.apply.cljs$core$IFn$_invoke$arity$3(cljs.core._PLUS_,nk,cljs.core.take.cljs$core$IFn$_invoke$arity$2(nj,word_n_letters))
));
var focus_x = (10);
var focus_y = (function (){var G__73521 = (0.5 + curr_index);
return (y_scale.cljs$core$IFn$_invoke$arity$1 ? y_scale.cljs$core$IFn$_invoke$arity$1(G__73521) : y_scale.call(null,G__73521));
})();
var next_focus_y = (function (){var G__73522 = (0.5 + next_index);
return (y_scale.cljs$core$IFn$_invoke$arity$1 ? y_scale.cljs$core$IFn$_invoke$arity$1(G__73522) : y_scale.call(null,G__73522));
})();
var eye_x = cljs.core.cst$kw$w.cljs$core$IFn$_invoke$arity$1(plot_size);
var eye_y = cljs.core.quot(cljs.core.cst$kw$h.cljs$core$IFn$_invoke$arity$1(plot_size),(2));
var G__73523 = ctx;
monet.canvas.begin_path(G__73523);

monet.canvas.move_to(G__73523,eye_x,eye_y);

monet.canvas.line_to(G__73523,focus_x,next_focus_y);

monet.canvas.stroke_style(G__73523,"lightgrey");

monet.canvas.stroke(G__73523);

monet.canvas.begin_path(G__73523);

monet.canvas.move_to(G__73523,eye_x,eye_y);

monet.canvas.line_to(G__73523,focus_x,focus_y);

monet.canvas.stroke_style(G__73523,"black");

monet.canvas.stroke(G__73523);

org.numenta.sanity.demos.sensorimotor_1d.draw_eye(G__73523,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$x,eye_x,cljs.core.cst$kw$y,eye_y,cljs.core.cst$kw$angle,(function (){var G__73524 = (focus_y - eye_y);
var G__73525 = (focus_x - eye_x);
return Math.atan2(G__73524,G__73525);
})(),cljs.core.cst$kw$radius,(30)], null));

return G__73523;
});
org.numenta.sanity.demos.second_level_motor.signed_str = (function org$numenta$sanity$demos$second_level_motor$signed_str(x){
return [cljs.core.str((((x < (0)))?"":"+")),cljs.core.str(x)].join('');
});
org.numenta.sanity.demos.second_level_motor.sentence_string = (function org$numenta$sanity$demos$second_level_motor$sentence_string(sentence){
return cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.str,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(cljs.core.flatten(cljs.core.interpose.cljs$core$IFn$_invoke$arity$2(" ",sentence)),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, ["."], null)));
});
org.numenta.sanity.demos.second_level_motor.world_pane = (function org$numenta$sanity$demos$second_level_motor$world_pane(){
var temp__4657__auto__ = org.numenta.sanity.main.selected_step.cljs$core$IFn$_invoke$arity$0();
if(cljs.core.truth_(temp__4657__auto__)){
var step = temp__4657__auto__;
var inval = cljs.core.cst$kw$input_DASH_value.cljs$core$IFn$_invoke$arity$1(step);
var map__73554 = inval;
var map__73554__$1 = ((((!((map__73554 == null)))?((((map__73554.cljs$lang$protocol_mask$partition0$ & (64))) || (map__73554.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__73554):map__73554);
var sentences = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__73554__$1,cljs.core.cst$kw$sentences);
var position = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__73554__$1,cljs.core.cst$kw$position);
var action = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__73554__$1,cljs.core.cst$kw$action);
var vec__73555 = position;
var i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73555,(0),null);
var j = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73555,(1),null);
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__73555,(2),null);
var letter_sacc = cljs.core.cst$kw$next_DASH_letter_DASH_saccade.cljs$core$IFn$_invoke$arity$1(action);
var word_sacc = cljs.core.cst$kw$next_DASH_word_DASH_saccade.cljs$core$IFn$_invoke$arity$1(action);
var sentence_sacc = cljs.core.cst$kw$next_DASH_sentence_DASH_saccade.cljs$core$IFn$_invoke$arity$1(action);
return new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p$muted,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"Input on selected timestep."], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$table$table,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$tr,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$th,"value"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,[cljs.core.str(cljs.core.cst$kw$value.cljs$core$IFn$_invoke$arity$1(inval))].join('')], null)], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$tr,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$th,"next move"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,((!((sentence_sacc === (0))))?"sentence":((!((word_sacc === (0))))?"word":((!((letter_sacc === (0))))?"letter":null)))], null)], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$tr,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$th,"direction"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$td,(((((sentence_sacc + word_sacc) + letter_sacc) > (0)))?"fwd":"back")], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$pre,clojure.string.join.cljs$core$IFn$_invoke$arity$2("\n",cljs.core.map.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.demos.second_level_motor.sentence_string,cljs.core.take.cljs$core$IFn$_invoke$arity$2(i,sentences)))], null),new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.helpers.resizing_canvas,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$width,"100%",cljs.core.cst$kw$height,"75vh"], null)], null),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.main.selection], null),((function (inval,map__73554,map__73554__$1,sentences,position,action,vec__73555,i,j,k,letter_sacc,word_sacc,sentence_sacc,step,temp__4657__auto__){
return (function (ctx){
var step__$1 = org.numenta.sanity.main.selected_step.cljs$core$IFn$_invoke$arity$0();
var inval__$1 = cljs.core.cst$kw$input_DASH_value.cljs$core$IFn$_invoke$arity$1(step__$1);
return org.numenta.sanity.demos.second_level_motor.draw_world(ctx,inval__$1);
});})(inval,map__73554,map__73554__$1,sentences,position,action,vec__73555,i,j,k,letter_sacc,word_sacc,sentence_sacc,step,temp__4657__auto__))
,null], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$pre,clojure.string.join.cljs$core$IFn$_invoke$arity$2("\n",cljs.core.map.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.demos.second_level_motor.sentence_string,cljs.core.drop.cljs$core$IFn$_invoke$arity$2((i + (1)),sentences)))], null)], null);
} else {
return null;
}
});
org.numenta.sanity.demos.second_level_motor.set_model_BANG_ = (function org$numenta$sanity$demos$second_level_motor$set_model_BANG_(){
return org.numenta.sanity.helpers.with_ui_loading_message((function (){
var init_QMARK_ = ((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.second_level_motor.model) : cljs.core.deref.call(null,org.numenta.sanity.demos.second_level_motor.model)) == null);
var c__38109__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto__,init_QMARK_){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto__,init_QMARK_){
return (function (state_73624){
var state_val_73625 = (state_73624[(1)]);
if((state_val_73625 === (1))){
var state_73624__$1 = state_73624;
if(init_QMARK_){
var statearr_73626_73643 = state_73624__$1;
(statearr_73626_73643[(1)] = (2));

} else {
var statearr_73627_73644 = state_73624__$1;
(statearr_73627_73644[(1)] = (3));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_73625 === (2))){
var state_73624__$1 = state_73624;
var statearr_73628_73645 = state_73624__$1;
(statearr_73628_73645[(2)] = null);

(statearr_73628_73645[(1)] = (4));


return cljs.core.cst$kw$recur;
} else {
if((state_val_73625 === (3))){
var state_73624__$1 = state_73624;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_73624__$1,(5),org.numenta.sanity.demos.second_level_motor.world_c);
} else {
if((state_val_73625 === (4))){
var inst_73605 = (state_73624[(2)]);
var inst_73606 = org.nfrac.comportex.demos.second_level_motor.two_region_model.cljs$core$IFn$_invoke$arity$0();
var inst_73607 = (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.demos.second_level_motor.model,inst_73606) : cljs.core.reset_BANG_.call(null,org.numenta.sanity.demos.second_level_motor.model,inst_73606));
var state_73624__$1 = (function (){var statearr_73629 = state_73624;
(statearr_73629[(7)] = inst_73605);

(statearr_73629[(8)] = inst_73607);

return statearr_73629;
})();
if(init_QMARK_){
var statearr_73630_73646 = state_73624__$1;
(statearr_73630_73646[(1)] = (6));

} else {
var statearr_73631_73647 = state_73624__$1;
(statearr_73631_73647[(1)] = (7));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_73625 === (5))){
var inst_73603 = (state_73624[(2)]);
var state_73624__$1 = state_73624;
var statearr_73632_73648 = state_73624__$1;
(statearr_73632_73648[(2)] = inst_73603);

(statearr_73632_73648[(1)] = (4));


return cljs.core.cst$kw$recur;
} else {
if((state_val_73625 === (6))){
var inst_73609 = org.nfrac.comportex.demos.second_level_motor.htm_step_with_action_selection(org.numenta.sanity.demos.second_level_motor.world_c,org.numenta.sanity.demos.second_level_motor.control_c);
var inst_73610 = org.numenta.sanity.bridge.browser.init.cljs$core$IFn$_invoke$arity$5(org.numenta.sanity.demos.second_level_motor.model,org.numenta.sanity.demos.second_level_motor.world_c,org.numenta.sanity.main.into_journal,org.numenta.sanity.demos.second_level_motor.into_sim,inst_73609);
var state_73624__$1 = state_73624;
var statearr_73633_73649 = state_73624__$1;
(statearr_73633_73649[(2)] = inst_73610);

(statearr_73633_73649[(1)] = (8));


return cljs.core.cst$kw$recur;
} else {
if((state_val_73625 === (7))){
var inst_73612 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.second_level_motor.model) : cljs.core.deref.call(null,org.numenta.sanity.demos.second_level_motor.model));
var inst_73613 = org.numenta.sanity.comportex.data.network_shape(inst_73612);
var inst_73614 = org.numenta.sanity.util.translate_network_shape(inst_73613);
var inst_73615 = (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.main.network_shape,inst_73614) : cljs.core.reset_BANG_.call(null,org.numenta.sanity.main.network_shape,inst_73614));
var state_73624__$1 = state_73624;
var statearr_73634_73650 = state_73624__$1;
(statearr_73634_73650[(2)] = inst_73615);

(statearr_73634_73650[(1)] = (8));


return cljs.core.cst$kw$recur;
} else {
if((state_val_73625 === (8))){
var inst_73617 = (state_73624[(2)]);
var inst_73618 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.second_level_motor.config) : cljs.core.deref.call(null,org.numenta.sanity.demos.second_level_motor.config));
var inst_73619 = cljs.core.cst$kw$text.cljs$core$IFn$_invoke$arity$1(inst_73618);
var inst_73620 = org.nfrac.comportex.demos.second_level_motor.parse_sentences(inst_73619);
var inst_73621 = org.nfrac.comportex.demos.second_level_motor.initial_inval(inst_73620);
var inst_73622 = cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.demos.second_level_motor.world_c,inst_73621);
var state_73624__$1 = (function (){var statearr_73635 = state_73624;
(statearr_73635[(9)] = inst_73617);

return statearr_73635;
})();
return cljs.core.async.impl.ioc_helpers.return_chan(state_73624__$1,inst_73622);
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
var org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto____0 = (function (){
var statearr_73639 = [null,null,null,null,null,null,null,null,null,null];
(statearr_73639[(0)] = org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto__);

(statearr_73639[(1)] = (1));

return statearr_73639;
});
var org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto____1 = (function (state_73624){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_73624);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e73640){if((e73640 instanceof Object)){
var ex__37999__auto__ = e73640;
var statearr_73641_73651 = state_73624;
(statearr_73641_73651[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_73624);

return cljs.core.cst$kw$recur;
} else {
throw e73640;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__73652 = state_73624;
state_73624 = G__73652;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto__ = function(state_73624){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto____1.call(this,state_73624);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto____0;
org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$second_level_motor$set_model_BANG__$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto__,init_QMARK_))
})();
var state__38111__auto__ = (function (){var statearr_73642 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_73642[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto__);

return statearr_73642;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto__,init_QMARK_))
);

return c__38109__auto__;
}));
});
org.numenta.sanity.demos.second_level_motor.set_text_BANG_ = (function org$numenta$sanity$demos$second_level_motor$set_text_BANG_(){
var text = cljs.core.cst$kw$edit_DASH_text.cljs$core$IFn$_invoke$arity$1((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.second_level_motor.config) : cljs.core.deref.call(null,org.numenta.sanity.demos.second_level_motor.config)));
var sentences = org.nfrac.comportex.demos.second_level_motor.parse_sentences(text);
cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.demos.second_level_motor.control_c,((function (text,sentences){
return (function (_){
return org.nfrac.comportex.demos.second_level_motor.initial_inval(sentences);
});})(text,sentences))
);

return cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(org.numenta.sanity.demos.second_level_motor.config,cljs.core.assoc,cljs.core.cst$kw$text,text);
});
org.numenta.sanity.demos.second_level_motor.config_template = new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$h3,"Input ",new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"Letters in words in sentences"], null)], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_horizontal,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_12,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$textarea$form_DASH_control,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$field,cljs.core.cst$kw$textarea,cljs.core.cst$kw$id,cljs.core.cst$kw$edit_DASH_text,cljs.core.cst$kw$rows,(8)], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_8,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$button$btn$btn_DASH_primary,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$field,cljs.core.cst$kw$container,cljs.core.cst$kw$visible_QMARK_,(function (p1__73653_SHARP_){
return cljs.core.not_EQ_.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$edit_DASH_text.cljs$core$IFn$_invoke$arity$1(p1__73653_SHARP_),cljs.core.cst$kw$text.cljs$core$IFn$_invoke$arity$1(p1__73653_SHARP_));
}),cljs.core.cst$kw$on_DASH_click,(function (e){
org.numenta.sanity.demos.second_level_motor.set_text_BANG_();

return e.preventDefault();
})], null),"Set sentences"], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$h3,"HTM model"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_horizontal,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_offset_DASH_5$col_DASH_sm_DASH_7,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$button$btn$btn_DASH_default,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$on_DASH_click,(function (e){
org.numenta.sanity.demos.second_level_motor.set_model_BANG_();

return e.preventDefault();
})], null),"Restart with new model"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p$text_DASH_danger,"This resets all parameters."], null)], null)], null)], null)], null);
org.numenta.sanity.demos.second_level_motor.model_tab = (function org$numenta$sanity$demos$second_level_motor$model_tab(){
return new cljs.core.PersistentVector(null, 7, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"A two-region example of temporal pooling over sensorimotor input."], null),new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"The world is a string of letters divided into words and\n   sentences. Only one letter is received as direct sensory input at\n   any one time. Motor actions (saccades) shift the focus to a new\n   letter. These motor actions are encoded in two separate senses: ",new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$code,"letter-motor"], null)," and ",new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$code,"word-motor"], null),". The former is distal input to the first level region, while the\n    latter is distal input to the second-level region."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Within a word, letter saccades always move forward one\n   letter. At the end of a word, we check whether the first region's\n   columns are bursting (indicating it has not yet learned the word's\n   letter sequence). If it is bursting, a letter saccade moves back to\n   the start of the same word. Otherwise, a word saccade is\n   generated."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Within a sentence, word saccades always move forward one\n   word. At the end of a sentence, we check whether the second\n   region's columns are bursting (indicating it has not yet learned\n   the sentence's word sequence). If it is bursting, a word saccade\n   moves back to the start of the same sentence."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"And similarly for sentence saccades."], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [reagent_forms.core.bind_fields,org.numenta.sanity.demos.second_level_motor.config_template,org.numenta.sanity.demos.second_level_motor.config], null)], null);
});
org.numenta.sanity.demos.second_level_motor.init = (function org$numenta$sanity$demos$second_level_motor$init(){
reagent.core.render.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.main.sanity_app,"Comportex",new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.second_level_motor.model_tab], null),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.second_level_motor.world_pane], null),org.numenta.sanity.demos.comportex_common.all_features,org.numenta.sanity.demos.second_level_motor.into_sim], null),goog.dom.getElement("sanity-app"));

return org.numenta.sanity.demos.second_level_motor.set_model_BANG_();
});
goog.exportSymbol('org.numenta.sanity.demos.second_level_motor.init', org.numenta.sanity.demos.second_level_motor.init);
