// Compiled by ClojureScript 1.7.228 {:static-fns true, :optimize-constants true}
goog.provide('org.numenta.sanity.demos.simple_sentences');
goog.require('cljs.core');
goog.require('goog.dom.forms');
goog.require('goog.dom');
goog.require('reagent.core');
goog.require('org.numenta.sanity.helpers');
goog.require('org.numenta.sanity.main');
goog.require('org.nfrac.comportex.demos.simple_sentences');
goog.require('org.numenta.sanity.util');
goog.require('org.numenta.sanity.comportex.data');
goog.require('cljs.core.async');
goog.require('org.numenta.sanity.bridge.marshalling');
goog.require('reagent_forms.core');
goog.require('org.nfrac.comportex.core');
goog.require('org.numenta.sanity.bridge.browser');
goog.require('org.numenta.sanity.demos.comportex_common');
goog.require('org.nfrac.comportex.util');
org.numenta.sanity.demos.simple_sentences.config = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$n_DASH_regions,(1),cljs.core.cst$kw$repeats,(1),cljs.core.cst$kw$text,org.nfrac.comportex.demos.simple_sentences.input_text,cljs.core.cst$kw$world_DASH_buffer_DASH_count,(0)], null));
org.numenta.sanity.demos.simple_sentences.world_buffer = cljs.core.async.buffer((5000));
org.numenta.sanity.demos.simple_sentences.world_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.demos.simple_sentences.world_buffer,cljs.core.comp.cljs$core$IFn$_invoke$arity$2(cljs.core.map.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.util.keep_history_middleware((100),cljs.core.cst$kw$word,cljs.core.cst$kw$history)),cljs.core.map.cljs$core$IFn$_invoke$arity$1((function (p1__70581_SHARP_){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(p1__70581_SHARP_,cljs.core.cst$kw$label,cljs.core.cst$kw$word.cljs$core$IFn$_invoke$arity$1(p1__70581_SHARP_));
}))));
org.numenta.sanity.demos.simple_sentences.into_sim = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
org.numenta.sanity.demos.simple_sentences.model = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
cljs.core.add_watch(org.numenta.sanity.demos.simple_sentences.model,cljs.core.cst$kw$org$numenta$sanity$demos$simple_DASH_sentences_SLASH_count_DASH_world_DASH_buffer,(function (_,___$1,___$2,___$3){
return cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(org.numenta.sanity.demos.simple_sentences.config,cljs.core.assoc,cljs.core.cst$kw$world_DASH_buffer_DASH_count,cljs.core.count(org.numenta.sanity.demos.simple_sentences.world_buffer));
}));
org.numenta.sanity.demos.simple_sentences.max_shown = (100);
org.numenta.sanity.demos.simple_sentences.scroll_every = (50);
org.numenta.sanity.demos.simple_sentences.world_pane = (function org$numenta$sanity$demos$simple_sentences$world_pane(){
var show_predictions = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(false);
var selected_htm = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
cljs.core.add_watch(org.numenta.sanity.main.selection,cljs.core.cst$kw$org$numenta$sanity$demos$simple_DASH_sentences_SLASH_fetch_DASH_selected_DASH_htm,((function (show_predictions,selected_htm){
return (function (_,___$1,___$2,p__70597){
var vec__70598 = p__70597;
var sel1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70598,(0),null);
var temp__4657__auto__ = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(sel1,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$step,cljs.core.cst$kw$snapshot_DASH_id], null));
if(cljs.core.truth_(temp__4657__auto__)){
var snapshot_id = temp__4657__auto__;
var out_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.main.into_journal,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, ["get-model",snapshot_id,org.numenta.sanity.bridge.marshalling.channel.cljs$core$IFn$_invoke$arity$2(out_c,true)], null));

var c__38109__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__70598,sel1,show_predictions,selected_htm){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__70598,sel1,show_predictions,selected_htm){
return (function (state_70603){
var state_val_70604 = (state_70603[(1)]);
if((state_val_70604 === (1))){
var state_70603__$1 = state_70603;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_70603__$1,(2),out_c);
} else {
if((state_val_70604 === (2))){
var inst_70600 = (state_70603[(2)]);
var inst_70601 = (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(selected_htm,inst_70600) : cljs.core.reset_BANG_.call(null,selected_htm,inst_70600));
var state_70603__$1 = state_70603;
return cljs.core.async.impl.ioc_helpers.return_chan(state_70603__$1,inst_70601);
} else {
return null;
}
}
});})(c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__70598,sel1,show_predictions,selected_htm))
;
return ((function (switch__37995__auto__,c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__70598,sel1,show_predictions,selected_htm){
return (function() {
var org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto____0 = (function (){
var statearr_70608 = [null,null,null,null,null,null,null];
(statearr_70608[(0)] = org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto__);

(statearr_70608[(1)] = (1));

return statearr_70608;
});
var org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto____1 = (function (state_70603){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_70603);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e70609){if((e70609 instanceof Object)){
var ex__37999__auto__ = e70609;
var statearr_70610_70612 = state_70603;
(statearr_70610_70612[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_70603);

return cljs.core.cst$kw$recur;
} else {
throw e70609;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__70613 = state_70603;
state_70603 = G__70613;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto__ = function(state_70603){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto____1.call(this,state_70603);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto____0;
org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$simple_sentences$world_pane_$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__70598,sel1,show_predictions,selected_htm))
})();
var state__38111__auto__ = (function (){var statearr_70611 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_70611[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto__);

return statearr_70611;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto__,out_c,snapshot_id,temp__4657__auto__,vec__70598,sel1,show_predictions,selected_htm))
);

return c__38109__auto__;
} else {
return null;
}
});})(show_predictions,selected_htm))
);

return ((function (show_predictions,selected_htm){
return (function (){
var temp__4657__auto__ = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(selected_htm) : cljs.core.deref.call(null,selected_htm));
if(cljs.core.truth_(temp__4657__auto__)){
var htm = temp__4657__auto__;
var inval = cljs.core.cst$kw$input_DASH_value.cljs$core$IFn$_invoke$arity$1(htm);
return new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p$muted,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"Input on selected timestep."], null)], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$min_DASH_height,"40vh"], null)], null),org.numenta.sanity.helpers.text_world_input_component(inval,htm,org.numenta.sanity.demos.simple_sentences.max_shown,org.numenta.sanity.demos.simple_sentences.scroll_every," ")], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$checkbox,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$label,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$input,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$type,cljs.core.cst$kw$checkbox,cljs.core.cst$kw$checked,(cljs.core.truth_((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(show_predictions) : cljs.core.deref.call(null,show_predictions)))?true:null),cljs.core.cst$kw$on_DASH_change,((function (inval,htm,temp__4657__auto__,show_predictions,selected_htm){
return (function (e){
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(show_predictions,cljs.core.not);

return e.preventDefault();
});})(inval,htm,temp__4657__auto__,show_predictions,selected_htm))
], null)], null),"Compute predictions"], null)], null),(cljs.core.truth_((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(show_predictions) : cljs.core.deref.call(null,show_predictions)))?org.numenta.sanity.helpers.text_world_predictions_component(htm,(8)):null)], null);
} else {
return null;
}
});
;})(show_predictions,selected_htm))
});
org.numenta.sanity.demos.simple_sentences.set_model_BANG_ = (function org$numenta$sanity$demos$simple_sentences$set_model_BANG_(){
return org.numenta.sanity.helpers.with_ui_loading_message((function (){
var n_regions = cljs.core.cst$kw$n_DASH_regions.cljs$core$IFn$_invoke$arity$1((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.simple_sentences.config) : cljs.core.deref.call(null,org.numenta.sanity.demos.simple_sentences.config)));
var init_QMARK_ = ((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.simple_sentences.model) : cljs.core.deref.call(null,org.numenta.sanity.demos.simple_sentences.model)) == null);
var G__70618_70622 = org.numenta.sanity.demos.simple_sentences.model;
var G__70619_70623 = org.nfrac.comportex.demos.simple_sentences.n_region_model.cljs$core$IFn$_invoke$arity$2(n_regions,org.nfrac.comportex.demos.simple_sentences.spec);
(cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(G__70618_70622,G__70619_70623) : cljs.core.reset_BANG_.call(null,G__70618_70622,G__70619_70623));

if(init_QMARK_){
return org.numenta.sanity.bridge.browser.init.cljs$core$IFn$_invoke$arity$4(org.numenta.sanity.demos.simple_sentences.model,org.numenta.sanity.demos.simple_sentences.world_c,org.numenta.sanity.main.into_journal,org.numenta.sanity.demos.simple_sentences.into_sim);
} else {
var G__70620 = org.numenta.sanity.main.network_shape;
var G__70621 = org.numenta.sanity.util.translate_network_shape(org.numenta.sanity.comportex.data.network_shape((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.simple_sentences.model) : cljs.core.deref.call(null,org.numenta.sanity.demos.simple_sentences.model))));
return (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(G__70620,G__70621) : cljs.core.reset_BANG_.call(null,G__70620,G__70621));
}
}));
});
org.numenta.sanity.demos.simple_sentences.send_text_BANG_ = (function org$numenta$sanity$demos$simple_sentences$send_text_BANG_(){
var temp__4657__auto__ = cljs.core.seq(org.nfrac.comportex.demos.simple_sentences.word_item_seq(cljs.core.cst$kw$repeats.cljs$core$IFn$_invoke$arity$1((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.simple_sentences.config) : cljs.core.deref.call(null,org.numenta.sanity.demos.simple_sentences.config))),cljs.core.cst$kw$text.cljs$core$IFn$_invoke$arity$1((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.simple_sentences.config) : cljs.core.deref.call(null,org.numenta.sanity.demos.simple_sentences.config)))));
if(temp__4657__auto__){
var xs = temp__4657__auto__;
var c__38109__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto__,xs,temp__4657__auto__){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto__,xs,temp__4657__auto__){
return (function (state_70646){
var state_val_70647 = (state_70646[(1)]);
if((state_val_70647 === (1))){
var inst_70640 = cljs.core.async.onto_chan.cljs$core$IFn$_invoke$arity$3(org.numenta.sanity.demos.simple_sentences.world_c,xs,false);
var state_70646__$1 = state_70646;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_70646__$1,(2),inst_70640);
} else {
if((state_val_70647 === (2))){
var inst_70642 = (state_70646[(2)]);
var inst_70643 = cljs.core.count(org.numenta.sanity.demos.simple_sentences.world_buffer);
var inst_70644 = cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(org.numenta.sanity.demos.simple_sentences.config,cljs.core.assoc,cljs.core.cst$kw$world_DASH_buffer_DASH_count,inst_70643);
var state_70646__$1 = (function (){var statearr_70648 = state_70646;
(statearr_70648[(7)] = inst_70642);

return statearr_70648;
})();
return cljs.core.async.impl.ioc_helpers.return_chan(state_70646__$1,inst_70644);
} else {
return null;
}
}
});})(c__38109__auto__,xs,temp__4657__auto__))
;
return ((function (switch__37995__auto__,c__38109__auto__,xs,temp__4657__auto__){
return (function() {
var org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto____0 = (function (){
var statearr_70652 = [null,null,null,null,null,null,null,null];
(statearr_70652[(0)] = org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto__);

(statearr_70652[(1)] = (1));

return statearr_70652;
});
var org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto____1 = (function (state_70646){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_70646);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e70653){if((e70653 instanceof Object)){
var ex__37999__auto__ = e70653;
var statearr_70654_70656 = state_70646;
(statearr_70654_70656[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_70646);

return cljs.core.cst$kw$recur;
} else {
throw e70653;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__70657 = state_70646;
state_70646 = G__70657;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto__ = function(state_70646){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto____1.call(this,state_70646);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto____0;
org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$simple_sentences$send_text_BANG__$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto__,xs,temp__4657__auto__))
})();
var state__38111__auto__ = (function (){var statearr_70655 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_70655[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto__);

return statearr_70655;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto__,xs,temp__4657__auto__))
);

return c__38109__auto__;
} else {
return null;
}
});
org.numenta.sanity.demos.simple_sentences.config_template = new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$h3,"Input ",new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$small,"Word sequences"], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p$text_DASH_info,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$span,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$field,cljs.core.cst$kw$label,cljs.core.cst$kw$id,cljs.core.cst$kw$world_DASH_buffer_DASH_count,cljs.core.cst$kw$postamble," queued input values."], null)], null)," ",new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$span,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$field,cljs.core.cst$kw$container,cljs.core.cst$kw$visible_QMARK_,(function (p1__70658_SHARP_){
return (cljs.core.cst$kw$world_DASH_buffer_DASH_count.cljs$core$IFn$_invoke$arity$1(p1__70658_SHARP_) > (0));
})], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$button$btn$btn_DASH_warning$btn_DASH_xs,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$on_DASH_click,(function (e){
var c__38109__auto___70701 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto___70701){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto___70701){
return (function (state_70680){
var state_val_70681 = (state_70680[(1)]);
if((state_val_70681 === (7))){
var inst_70666 = (state_70680[(2)]);
var state_70680__$1 = state_70680;
var statearr_70682_70702 = state_70680__$1;
(statearr_70682_70702[(2)] = inst_70666);

(statearr_70682_70702[(1)] = (6));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70681 === (1))){
var state_70680__$1 = state_70680;
var statearr_70683_70703 = state_70680__$1;
(statearr_70683_70703[(2)] = null);

(statearr_70683_70703[(1)] = (2));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70681 === (4))){
var state_70680__$1 = state_70680;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_70680__$1,(7),org.numenta.sanity.demos.simple_sentences.world_c);
} else {
if((state_val_70681 === (6))){
var inst_70669 = (state_70680[(2)]);
var state_70680__$1 = state_70680;
if(cljs.core.truth_(inst_70669)){
var statearr_70684_70704 = state_70680__$1;
(statearr_70684_70704[(1)] = (8));

} else {
var statearr_70685_70705 = state_70680__$1;
(statearr_70685_70705[(1)] = (9));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_70681 === (3))){
var inst_70678 = (state_70680[(2)]);
var state_70680__$1 = state_70680;
return cljs.core.async.impl.ioc_helpers.return_chan(state_70680__$1,inst_70678);
} else {
if((state_val_70681 === (2))){
var inst_70663 = (state_70680[(7)]);
var inst_70662 = cljs.core.count(org.numenta.sanity.demos.simple_sentences.world_buffer);
var inst_70663__$1 = (inst_70662 > (0));
var state_70680__$1 = (function (){var statearr_70686 = state_70680;
(statearr_70686[(7)] = inst_70663__$1);

return statearr_70686;
})();
if(cljs.core.truth_(inst_70663__$1)){
var statearr_70687_70706 = state_70680__$1;
(statearr_70687_70706[(1)] = (4));

} else {
var statearr_70688_70707 = state_70680__$1;
(statearr_70688_70707[(1)] = (5));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_70681 === (9))){
var state_70680__$1 = state_70680;
var statearr_70689_70708 = state_70680__$1;
(statearr_70689_70708[(2)] = null);

(statearr_70689_70708[(1)] = (10));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70681 === (5))){
var inst_70663 = (state_70680[(7)]);
var state_70680__$1 = state_70680;
var statearr_70690_70709 = state_70680__$1;
(statearr_70690_70709[(2)] = inst_70663);

(statearr_70690_70709[(1)] = (6));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70681 === (10))){
var inst_70676 = (state_70680[(2)]);
var state_70680__$1 = state_70680;
var statearr_70691_70710 = state_70680__$1;
(statearr_70691_70710[(2)] = inst_70676);

(statearr_70691_70710[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70681 === (8))){
var inst_70671 = cljs.core.count(org.numenta.sanity.demos.simple_sentences.world_buffer);
var inst_70672 = cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(org.numenta.sanity.demos.simple_sentences.config,cljs.core.assoc,cljs.core.cst$kw$world_DASH_buffer_DASH_count,inst_70671);
var state_70680__$1 = (function (){var statearr_70692 = state_70680;
(statearr_70692[(8)] = inst_70672);

return statearr_70692;
})();
var statearr_70693_70711 = state_70680__$1;
(statearr_70693_70711[(2)] = null);

(statearr_70693_70711[(1)] = (2));


return cljs.core.cst$kw$recur;
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
}
}
});})(c__38109__auto___70701))
;
return ((function (switch__37995__auto__,c__38109__auto___70701){
return (function() {
var org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto____0 = (function (){
var statearr_70697 = [null,null,null,null,null,null,null,null,null];
(statearr_70697[(0)] = org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto__);

(statearr_70697[(1)] = (1));

return statearr_70697;
});
var org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto____1 = (function (state_70680){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_70680);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e70698){if((e70698 instanceof Object)){
var ex__37999__auto__ = e70698;
var statearr_70699_70712 = state_70680;
(statearr_70699_70712[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_70680);

return cljs.core.cst$kw$recur;
} else {
throw e70698;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__70713 = state_70680;
state_70680 = G__70713;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto__ = function(state_70680){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto____1.call(this,state_70680);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto____0;
org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto____1;
return org$numenta$sanity$demos$simple_sentences$state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto___70701))
})();
var state__38111__auto__ = (function (){var statearr_70700 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_70700[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto___70701);

return statearr_70700;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto___70701))
);


return e.preventDefault();
})], null),"Clear"], null)], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_horizontal,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$label$col_DASH_sm_DASH_5,"Repeats of each sentence:"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_7,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$input$form_DASH_control,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$field,cljs.core.cst$kw$numeric,cljs.core.cst$kw$id,cljs.core.cst$kw$repeats], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_12,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$textarea$form_DASH_control,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$field,cljs.core.cst$kw$textarea,cljs.core.cst$kw$id,cljs.core.cst$kw$text,cljs.core.cst$kw$rows,(10)], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_8,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$button$btn$btn_DASH_primary,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$field,cljs.core.cst$kw$container,cljs.core.cst$kw$visible_QMARK_,(function (p1__70659_SHARP_){
return (cljs.core.cst$kw$world_DASH_buffer_DASH_count.cljs$core$IFn$_invoke$arity$1(p1__70659_SHARP_) === (0));
}),cljs.core.cst$kw$on_DASH_click,(function (e){
org.numenta.sanity.demos.simple_sentences.send_text_BANG_();

return e.preventDefault();
})], null),"Queue text input"], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$button$btn$btn_DASH_default,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$field,cljs.core.cst$kw$container,cljs.core.cst$kw$visible_QMARK_,(function (p1__70660_SHARP_){
return (cljs.core.cst$kw$world_DASH_buffer_DASH_count.cljs$core$IFn$_invoke$arity$1(p1__70660_SHARP_) > (0));
}),cljs.core.cst$kw$on_DASH_click,(function (e){
org.numenta.sanity.demos.simple_sentences.send_text_BANG_();

return e.preventDefault();
})], null),"Queue more text input"], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$h3,"HTM model"], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_horizontal,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$label$col_DASH_sm_DASH_5,"Number of regions:"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_7,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$input$form_DASH_control,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$field,cljs.core.cst$kw$numeric,cljs.core.cst$kw$id,cljs.core.cst$kw$n_DASH_regions], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$form_DASH_group,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div$col_DASH_sm_DASH_offset_DASH_5$col_DASH_sm_DASH_7,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$button$btn$btn_DASH_default,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$on_DASH_click,(function (e){
org.numenta.sanity.demos.simple_sentences.set_model_BANG_();

return e.preventDefault();
})], null),"Restart with new model"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p$text_DASH_danger,"This resets all parameters."], null)], null)], null)], null)], null);
org.numenta.sanity.demos.simple_sentences.model_tab = (function org$numenta$sanity$demos$simple_sentences$model_tab(){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"In this example, text is presented as a sequence of words,\n        with independent unique encodings. The text is split into\n        sentences at each period (.) and each sentence into\n        words."], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [reagent_forms.core.bind_fields,org.numenta.sanity.demos.simple_sentences.config_template,org.numenta.sanity.demos.simple_sentences.config], null)], null);
});
org.numenta.sanity.demos.simple_sentences.init = (function org$numenta$sanity$demos$simple_sentences$init(){
reagent.core.render.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.main.sanity_app,"Comportex",new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.simple_sentences.model_tab], null),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.simple_sentences.world_pane], null),org.numenta.sanity.demos.comportex_common.all_features,org.numenta.sanity.demos.simple_sentences.into_sim], null),goog.dom.getElement("sanity-app"));

org.numenta.sanity.demos.simple_sentences.send_text_BANG_();

return org.numenta.sanity.demos.simple_sentences.set_model_BANG_();
});
goog.exportSymbol('org.numenta.sanity.demos.simple_sentences.init', org.numenta.sanity.demos.simple_sentences.init);
