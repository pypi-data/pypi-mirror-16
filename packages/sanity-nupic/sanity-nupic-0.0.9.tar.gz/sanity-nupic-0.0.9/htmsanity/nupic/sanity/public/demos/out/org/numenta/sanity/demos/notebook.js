// Compiled by ClojureScript 1.7.228 {:static-fns true, :optimize-constants true}
goog.provide('org.numenta.sanity.demos.notebook');
goog.require('cljs.core');
goog.require('reagent.core');
goog.require('org.numenta.sanity.viz_canvas');
goog.require('org.numenta.sanity.demos.runner');
goog.require('org.nfrac.comportex.protocols');
goog.require('org.numenta.sanity.bridge.remote');
goog.require('org.numenta.sanity.util');
goog.require('cljs.core.async');
goog.require('org.numenta.sanity.bridge.marshalling');
goog.require('org.numenta.sanity.selection');
goog.require('cognitect.transit');
goog.require('org.nfrac.comportex.util');
goog.require('clojure.walk');
cljs.core.enable_console_print_BANG_();
org.numenta.sanity.demos.notebook.pipe_to_remote_target_BANG_ = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
org.numenta.sanity.demos.notebook.remote_target__GT_chan = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(cljs.core.PersistentArrayMap.EMPTY);
org.numenta.sanity.demos.notebook.connect = (function org$numenta$sanity$demos$notebook$connect(url){
var G__72306 = org.numenta.sanity.demos.notebook.pipe_to_remote_target_BANG_;
var G__72307 = org.numenta.sanity.bridge.remote.init(url);
return (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(G__72306,G__72307) : cljs.core.reset_BANG_.call(null,G__72306,G__72307));
});
goog.exportSymbol('org.numenta.sanity.demos.notebook.connect', org.numenta.sanity.demos.notebook.connect);
org.numenta.sanity.demos.notebook.read_transit_str = (function org$numenta$sanity$demos$notebook$read_transit_str(s){
return cognitect.transit.read(cognitect.transit.reader.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$json),s);
});
org.numenta.sanity.demos.notebook.display_inbits = (function org$numenta$sanity$demos$notebook$display_inbits(el,serialized){
var vec__72309 = org.numenta.sanity.demos.notebook.read_transit_str(serialized);
var dims = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72309,(0),null);
var state__GT_bits = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72309,(1),null);
var d_opts = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72309,(2),null);
return reagent.core.render.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.viz_canvas.inbits_display,dims,state__GT_bits,cljs.core.merge.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([cljs.core.cst$kw$drawing.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.viz_canvas.default_viz_options),d_opts], 0))], null),el);
});
goog.exportSymbol('org.numenta.sanity.demos.notebook.display_inbits', org.numenta.sanity.demos.notebook.display_inbits);
org.numenta.sanity.demos.notebook.release_inbits = (function org$numenta$sanity$demos$notebook$release_inbits(el){
return reagent.core.unmount_component_at_node(el);
});
goog.exportSymbol('org.numenta.sanity.demos.notebook.release_inbits', org.numenta.sanity.demos.notebook.release_inbits);
org.numenta.sanity.demos.notebook.add_viz = (function org$numenta$sanity$demos$notebook$add_viz(el,serialized){
var vec__72440 = org.numenta.sanity.demos.notebook.read_transit_str(serialized);
var journal_target = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72440,(0),null);
var opts = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__72440,(1),null);
var into_journal = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var into_viz = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var response_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(org.numenta.sanity.demos.notebook.remote_target__GT_chan,cljs.core.assoc,journal_target,into_journal);

(cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.notebook.pipe_to_remote_target_BANG_) : cljs.core.deref.call(null,org.numenta.sanity.demos.notebook.pipe_to_remote_target_BANG_)).call(null,journal_target,into_journal);

cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(into_journal,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, ["get-network-shape",org.numenta.sanity.bridge.marshalling.channel.cljs$core$IFn$_invoke$arity$2(response_c,true)], null));

var c__38109__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c){
return (function (state_72548){
var state_val_72549 = (state_72548[(1)]);
if((state_val_72549 === (1))){
var state_72548__$1 = state_72548;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_72548__$1,(2),response_c);
} else {
if((state_val_72549 === (2))){
var inst_72445 = (state_72548[(7)]);
var inst_72442 = (state_72548[(2)]);
var inst_72443 = org.numenta.sanity.util.translate_network_shape(inst_72442);
var inst_72444 = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(inst_72443);
var inst_72445__$1 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var inst_72446 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72447 = org.numenta.sanity.bridge.marshalling.channel.cljs$core$IFn$_invoke$arity$2(inst_72445__$1,true);
var inst_72448 = ["get-steps",inst_72447];
var inst_72449 = (new cljs.core.PersistentVector(null,2,(5),inst_72446,inst_72448,null));
var inst_72450 = cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(into_journal,inst_72449);
var state_72548__$1 = (function (){var statearr_72550 = state_72548;
(statearr_72550[(7)] = inst_72445__$1);

(statearr_72550[(8)] = inst_72450);

(statearr_72550[(9)] = inst_72444);

return statearr_72550;
})();
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_72548__$1,(3),inst_72445__$1);
} else {
if((state_val_72549 === (3))){
var inst_72445 = (state_72548[(7)]);
var inst_72459 = (state_72548[(10)]);
var inst_72453 = (state_72548[(11)]);
var inst_72444 = (state_72548[(9)]);
var inst_72453__$1 = (state_72548[(2)]);
var inst_72454 = (function (){var network_shape = inst_72444;
var response_c__$1 = inst_72445;
var all_steps = inst_72453__$1;
return ((function (network_shape,response_c__$1,all_steps,inst_72445,inst_72459,inst_72453,inst_72444,inst_72453__$1,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c){
return (function (step){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(step,cljs.core.cst$kw$network_DASH_shape,(cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(network_shape) : cljs.core.deref.call(null,network_shape)));
});
;})(network_shape,response_c__$1,all_steps,inst_72445,inst_72459,inst_72453,inst_72444,inst_72453__$1,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c))
})();
var inst_72455 = clojure.walk.keywordize_keys(inst_72453__$1);
var inst_72456 = cljs.core.map.cljs$core$IFn$_invoke$arity$2(inst_72454,inst_72455);
var inst_72457 = cljs.core.reverse(inst_72456);
var inst_72458 = cljs.core.vec(inst_72457);
var inst_72459__$1 = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(inst_72458);
var inst_72460 = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.selection.blank_selection);
var inst_72462 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(inst_72459__$1) : cljs.core.deref.call(null,inst_72459__$1));
var inst_72463 = cljs.core.count(inst_72462);
var inst_72464 = cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2((1),inst_72463);
var state_72548__$1 = (function (){var statearr_72551 = state_72548;
(statearr_72551[(10)] = inst_72459__$1);

(statearr_72551[(11)] = inst_72453__$1);

(statearr_72551[(12)] = inst_72460);

return statearr_72551;
})();
if(inst_72464){
var statearr_72552_72568 = state_72548__$1;
(statearr_72552_72568[(1)] = (4));

} else {
var statearr_72553_72569 = state_72548__$1;
(statearr_72553_72569[(1)] = (5));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_72549 === (4))){
var inst_72466 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72467 = [cljs.core.cst$kw$drawing,cljs.core.cst$kw$display_DASH_mode];
var inst_72468 = (new cljs.core.PersistentVector(null,2,(5),inst_72466,inst_72467,null));
var inst_72469 = cljs.core.assoc_in(org.numenta.sanity.viz_canvas.default_viz_options,inst_72468,cljs.core.cst$kw$two_DASH_d);
var state_72548__$1 = state_72548;
var statearr_72554_72570 = state_72548__$1;
(statearr_72554_72570[(2)] = inst_72469);

(statearr_72554_72570[(1)] = (6));


return cljs.core.cst$kw$recur;
} else {
if((state_val_72549 === (5))){
var state_72548__$1 = state_72548;
var statearr_72555_72571 = state_72548__$1;
(statearr_72555_72571[(2)] = org.numenta.sanity.viz_canvas.default_viz_options);

(statearr_72555_72571[(1)] = (6));


return cljs.core.cst$kw$recur;
} else {
if((state_val_72549 === (6))){
var inst_72445 = (state_72548[(7)]);
var inst_72459 = (state_72548[(10)]);
var inst_72453 = (state_72548[(11)]);
var inst_72460 = (state_72548[(12)]);
var inst_72475 = (state_72548[(13)]);
var inst_72444 = (state_72548[(9)]);
var inst_72472 = (state_72548[(2)]);
var inst_72473 = (function (){var network_shape = inst_72444;
var response_c__$1 = inst_72445;
var all_steps = inst_72453;
var steps = inst_72459;
var selection = inst_72460;
var base_opts = inst_72472;
return ((function (network_shape,response_c__$1,all_steps,steps,selection,base_opts,inst_72445,inst_72459,inst_72453,inst_72460,inst_72475,inst_72444,inst_72472,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c){
return (function() { 
var G__72572__delegate = function (xs){
var last_non_nil = cljs.core.first(cljs.core.filter.cljs$core$IFn$_invoke$arity$2(cljs.core.complement(cljs.core.nil_QMARK_),cljs.core.reverse(xs)));
if(cljs.core.coll_QMARK_(last_non_nil)){
return last_non_nil;
} else {
return cljs.core.last(xs);
}
};
var G__72572 = function (var_args){
var xs = null;
if (arguments.length > 0) {
var G__72573__i = 0, G__72573__a = new Array(arguments.length -  0);
while (G__72573__i < G__72573__a.length) {G__72573__a[G__72573__i] = arguments[G__72573__i + 0]; ++G__72573__i;}
  xs = new cljs.core.IndexedSeq(G__72573__a,0);
} 
return G__72572__delegate.call(this,xs);};
G__72572.cljs$lang$maxFixedArity = 0;
G__72572.cljs$lang$applyTo = (function (arglist__72574){
var xs = cljs.core.seq(arglist__72574);
return G__72572__delegate(xs);
});
G__72572.cljs$core$IFn$_invoke$arity$variadic = G__72572__delegate;
return G__72572;
})()
;
;})(network_shape,response_c__$1,all_steps,steps,selection,base_opts,inst_72445,inst_72459,inst_72453,inst_72460,inst_72475,inst_72444,inst_72472,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c))
})();
var inst_72474 = org.nfrac.comportex.util.deep_merge_with.cljs$core$IFn$_invoke$arity$variadic(inst_72473,cljs.core.array_seq([inst_72472,opts], 0));
var inst_72475__$1 = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(inst_72474);
var inst_72476 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(inst_72444) : cljs.core.deref.call(null,inst_72444));
var inst_72477 = cljs.core.cst$kw$regions.cljs$core$IFn$_invoke$arity$1(inst_72476);
var inst_72478 = cljs.core.seq(inst_72477);
var inst_72479 = cljs.core.first(inst_72478);
var inst_72480 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_72479,(0),null);
var inst_72481 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_72479,(1),null);
var inst_72482 = cljs.core.keys(inst_72481);
var inst_72483 = cljs.core.first(inst_72482);
var inst_72485 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(inst_72444) : cljs.core.deref.call(null,inst_72444));
var inst_72486 = cljs.core.cst$kw$regions.cljs$core$IFn$_invoke$arity$1(inst_72485);
var inst_72487 = cljs.core.seq(inst_72486);
var inst_72488 = cljs.core.first(inst_72487);
var inst_72489 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_72488,(0),null);
var inst_72490 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_72488,(1),null);
var inst_72491 = cljs.core.keys(inst_72490);
var inst_72492 = cljs.core.first(inst_72491);
var inst_72493 = (function (){var selection = inst_72460;
var network_shape = inst_72444;
var base_opts = inst_72472;
var response_c__$1 = inst_72445;
var all_steps = inst_72453;
var steps = inst_72459;
var viz_options = inst_72475__$1;
var layer_id = inst_72492;
var rgn = inst_72490;
var vec__72484 = inst_72488;
var vec__72451 = inst_72479;
var region_key = inst_72489;
return ((function (selection,network_shape,base_opts,response_c__$1,all_steps,steps,viz_options,layer_id,rgn,vec__72484,vec__72451,region_key,inst_72445,inst_72459,inst_72453,inst_72460,inst_72475,inst_72444,inst_72472,inst_72473,inst_72474,inst_72475__$1,inst_72476,inst_72477,inst_72478,inst_72479,inst_72480,inst_72481,inst_72482,inst_72483,inst_72485,inst_72486,inst_72487,inst_72488,inst_72489,inst_72490,inst_72491,inst_72492,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c){
return (function (p1__72310_SHARP_){
return cljs.core.conj.cljs$core$IFn$_invoke$arity$2(cljs.core.empty(p1__72310_SHARP_),new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$dt,(0),cljs.core.cst$kw$region,region_key,cljs.core.cst$kw$layer,layer_id,cljs.core.cst$kw$snapshot_DASH_id,cljs.core.cst$kw$snapshot_DASH_id.cljs$core$IFn$_invoke$arity$1(cljs.core.first((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(steps) : cljs.core.deref.call(null,steps))))], null));
});
;})(selection,network_shape,base_opts,response_c__$1,all_steps,steps,viz_options,layer_id,rgn,vec__72484,vec__72451,region_key,inst_72445,inst_72459,inst_72453,inst_72460,inst_72475,inst_72444,inst_72472,inst_72473,inst_72474,inst_72475__$1,inst_72476,inst_72477,inst_72478,inst_72479,inst_72480,inst_72481,inst_72482,inst_72483,inst_72485,inst_72486,inst_72487,inst_72488,inst_72489,inst_72490,inst_72491,inst_72492,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c))
})();
var inst_72494 = cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(inst_72460,inst_72493);
var inst_72495 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72496 = [cljs.core.cst$kw$on_DASH_click,cljs.core.cst$kw$on_DASH_key_DASH_down,cljs.core.cst$kw$tabIndex];
var inst_72497 = (function (){var selection = inst_72460;
var network_shape = inst_72444;
var base_opts = inst_72472;
var response_c__$1 = inst_72445;
var all_steps = inst_72453;
var steps = inst_72459;
var viz_options = inst_72475__$1;
var layer_id = inst_72483;
var rgn = inst_72481;
var vec__72451 = inst_72479;
var region_key = inst_72480;
return ((function (selection,network_shape,base_opts,response_c__$1,all_steps,steps,viz_options,layer_id,rgn,vec__72451,region_key,inst_72445,inst_72459,inst_72453,inst_72460,inst_72475,inst_72444,inst_72472,inst_72473,inst_72474,inst_72475__$1,inst_72476,inst_72477,inst_72478,inst_72479,inst_72480,inst_72481,inst_72482,inst_72483,inst_72485,inst_72486,inst_72487,inst_72488,inst_72489,inst_72490,inst_72491,inst_72492,inst_72493,inst_72494,inst_72495,inst_72496,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c){
return (function (){
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(into_viz,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$background_DASH_clicked], null));
});
;})(selection,network_shape,base_opts,response_c__$1,all_steps,steps,viz_options,layer_id,rgn,vec__72451,region_key,inst_72445,inst_72459,inst_72453,inst_72460,inst_72475,inst_72444,inst_72472,inst_72473,inst_72474,inst_72475__$1,inst_72476,inst_72477,inst_72478,inst_72479,inst_72480,inst_72481,inst_72482,inst_72483,inst_72485,inst_72486,inst_72487,inst_72488,inst_72489,inst_72490,inst_72491,inst_72492,inst_72493,inst_72494,inst_72495,inst_72496,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c))
})();
var inst_72498 = (function (){var selection = inst_72460;
var network_shape = inst_72444;
var base_opts = inst_72472;
var response_c__$1 = inst_72445;
var all_steps = inst_72453;
var steps = inst_72459;
var viz_options = inst_72475__$1;
var layer_id = inst_72483;
var rgn = inst_72481;
var vec__72451 = inst_72479;
var region_key = inst_72480;
return ((function (selection,network_shape,base_opts,response_c__$1,all_steps,steps,viz_options,layer_id,rgn,vec__72451,region_key,inst_72445,inst_72459,inst_72453,inst_72460,inst_72475,inst_72444,inst_72472,inst_72473,inst_72474,inst_72475__$1,inst_72476,inst_72477,inst_72478,inst_72479,inst_72480,inst_72481,inst_72482,inst_72483,inst_72485,inst_72486,inst_72487,inst_72488,inst_72489,inst_72490,inst_72491,inst_72492,inst_72493,inst_72494,inst_72495,inst_72496,inst_72497,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c){
return (function (p1__72311_SHARP_){
return org.numenta.sanity.viz_canvas.viz_key_down(p1__72311_SHARP_,into_viz);
});
;})(selection,network_shape,base_opts,response_c__$1,all_steps,steps,viz_options,layer_id,rgn,vec__72451,region_key,inst_72445,inst_72459,inst_72453,inst_72460,inst_72475,inst_72444,inst_72472,inst_72473,inst_72474,inst_72475__$1,inst_72476,inst_72477,inst_72478,inst_72479,inst_72480,inst_72481,inst_72482,inst_72483,inst_72485,inst_72486,inst_72487,inst_72488,inst_72489,inst_72490,inst_72491,inst_72492,inst_72493,inst_72494,inst_72495,inst_72496,inst_72497,state_val_72549,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c))
})();
var inst_72499 = [inst_72497,inst_72498,(1)];
var inst_72500 = cljs.core.PersistentHashMap.fromArrays(inst_72496,inst_72499);
var inst_72501 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(inst_72459) : cljs.core.deref.call(null,inst_72459));
var inst_72502 = cljs.core.count(inst_72501);
var inst_72503 = (inst_72502 > (1));
var state_72548__$1 = (function (){var statearr_72556 = state_72548;
(statearr_72556[(13)] = inst_72475__$1);

(statearr_72556[(14)] = inst_72495);

(statearr_72556[(15)] = inst_72500);

(statearr_72556[(16)] = inst_72494);

return statearr_72556;
})();
if(cljs.core.truth_(inst_72503)){
var statearr_72557_72575 = state_72548__$1;
(statearr_72557_72575[(1)] = (7));

} else {
var statearr_72558_72576 = state_72548__$1;
(statearr_72558_72576[(1)] = (8));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_72549 === (7))){
var inst_72459 = (state_72548[(10)]);
var inst_72460 = (state_72548[(12)]);
var inst_72475 = (state_72548[(13)]);
var inst_72505 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72506 = [org.numenta.sanity.viz_canvas.viz_timeline,inst_72459,inst_72460,inst_72475];
var inst_72507 = (new cljs.core.PersistentVector(null,4,(5),inst_72505,inst_72506,null));
var state_72548__$1 = state_72548;
var statearr_72559_72577 = state_72548__$1;
(statearr_72559_72577[(2)] = inst_72507);

(statearr_72559_72577[(1)] = (9));


return cljs.core.cst$kw$recur;
} else {
if((state_val_72549 === (8))){
var state_72548__$1 = state_72548;
var statearr_72560_72578 = state_72548__$1;
(statearr_72560_72578[(2)] = null);

(statearr_72560_72578[(1)] = (9));


return cljs.core.cst$kw$recur;
} else {
if((state_val_72549 === (9))){
var inst_72459 = (state_72548[(10)]);
var inst_72460 = (state_72548[(12)]);
var inst_72475 = (state_72548[(13)]);
var inst_72495 = (state_72548[(14)]);
var inst_72444 = (state_72548[(9)]);
var inst_72500 = (state_72548[(15)]);
var inst_72510 = (state_72548[(2)]);
var inst_72511 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72512 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72513 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72514 = [cljs.core.cst$kw$style];
var inst_72515 = [cljs.core.cst$kw$border,cljs.core.cst$kw$vertical_DASH_align];
var inst_72516 = ["none","top"];
var inst_72517 = cljs.core.PersistentHashMap.fromArrays(inst_72515,inst_72516);
var inst_72518 = [inst_72517];
var inst_72519 = cljs.core.PersistentHashMap.fromArrays(inst_72514,inst_72518);
var inst_72520 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72521 = [org.numenta.sanity.demos.runner.world_pane,inst_72459,inst_72460];
var inst_72522 = (new cljs.core.PersistentVector(null,3,(5),inst_72520,inst_72521,null));
var inst_72523 = [cljs.core.cst$kw$td,inst_72519,inst_72522];
var inst_72524 = (new cljs.core.PersistentVector(null,3,(5),inst_72513,inst_72523,null));
var inst_72525 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72526 = [cljs.core.cst$kw$style];
var inst_72527 = [cljs.core.cst$kw$border,cljs.core.cst$kw$vertical_DASH_align];
var inst_72528 = ["none","top"];
var inst_72529 = cljs.core.PersistentHashMap.fromArrays(inst_72527,inst_72528);
var inst_72530 = [inst_72529];
var inst_72531 = cljs.core.PersistentHashMap.fromArrays(inst_72526,inst_72530);
var inst_72532 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_72533 = [cljs.core.cst$kw$tabIndex];
var inst_72534 = [(0)];
var inst_72535 = cljs.core.PersistentHashMap.fromArrays(inst_72533,inst_72534);
var inst_72536 = [org.numenta.sanity.viz_canvas.viz_canvas,inst_72535,inst_72459,inst_72460,inst_72444,inst_72475,into_viz,null,into_journal];
var inst_72537 = (new cljs.core.PersistentVector(null,9,(5),inst_72532,inst_72536,null));
var inst_72538 = [cljs.core.cst$kw$td,inst_72531,inst_72537];
var inst_72539 = (new cljs.core.PersistentVector(null,3,(5),inst_72525,inst_72538,null));
var inst_72540 = [cljs.core.cst$kw$tr,inst_72524,inst_72539];
var inst_72541 = (new cljs.core.PersistentVector(null,3,(5),inst_72512,inst_72540,null));
var inst_72542 = [cljs.core.cst$kw$table,inst_72541];
var inst_72543 = (new cljs.core.PersistentVector(null,2,(5),inst_72511,inst_72542,null));
var inst_72544 = [cljs.core.cst$kw$div,inst_72500,inst_72510,inst_72543];
var inst_72545 = (new cljs.core.PersistentVector(null,4,(5),inst_72495,inst_72544,null));
var inst_72546 = reagent.core.render.cljs$core$IFn$_invoke$arity$2(inst_72545,el);
var state_72548__$1 = state_72548;
return cljs.core.async.impl.ioc_helpers.return_chan(state_72548__$1,inst_72546);
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
});})(c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c))
;
return ((function (switch__37995__auto__,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c){
return (function() {
var org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto____0 = (function (){
var statearr_72564 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_72564[(0)] = org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto__);

(statearr_72564[(1)] = (1));

return statearr_72564;
});
var org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto____1 = (function (state_72548){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_72548);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e72565){if((e72565 instanceof Object)){
var ex__37999__auto__ = e72565;
var statearr_72566_72579 = state_72548;
(statearr_72566_72579[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_72548);

return cljs.core.cst$kw$recur;
} else {
throw e72565;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__72580 = state_72548;
state_72548 = G__72580;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto__ = function(state_72548){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto____1.call(this,state_72548);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto____0;
org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$notebook$add_viz_$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c))
})();
var state__38111__auto__ = (function (){var statearr_72567 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_72567[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto__);

return statearr_72567;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto__,vec__72440,journal_target,opts,into_journal,into_viz,response_c))
);

return c__38109__auto__;
});
goog.exportSymbol('org.numenta.sanity.demos.notebook.add_viz', org.numenta.sanity.demos.notebook.add_viz);
org.numenta.sanity.demos.notebook.release_viz = (function org$numenta$sanity$demos$notebook$release_viz(el,serialized){
reagent.core.unmount_component_at_node(el);

var journal_target = org.numenta.sanity.demos.notebook.read_transit_str(serialized);
cljs.core.async.close_BANG_(cljs.core.get.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.notebook.remote_target__GT_chan) : cljs.core.deref.call(null,org.numenta.sanity.demos.notebook.remote_target__GT_chan)),journal_target));

return cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(org.numenta.sanity.demos.notebook.remote_target__GT_chan,cljs.core.dissoc,journal_target);
});
goog.exportSymbol('org.numenta.sanity.demos.notebook.release_viz', org.numenta.sanity.demos.notebook.release_viz);
org.numenta.sanity.demos.notebook.exported_viz = (function org$numenta$sanity$demos$notebook$exported_viz(el){
var cnvs = cljs.core.array_seq.cljs$core$IFn$_invoke$arity$1(el.getElementsByTagName("canvas"));
var copy_el = document.createElement("div");
copy_el.innerHTML = el.innerHTML;

var seq__72587_72593 = cljs.core.seq(cnvs);
var chunk__72589_72594 = null;
var count__72590_72595 = (0);
var i__72591_72596 = (0);
while(true){
if((i__72591_72596 < count__72590_72595)){
var cnv_72597 = chunk__72589_72594.cljs$core$IIndexed$_nth$arity$2(null,i__72591_72596);
var victim_el_72598 = (copy_el.getElementsByTagName("canvas")[(0)]);
var img_el_72599 = document.createElement("img");
img_el_72599.setAttribute("src",cnv_72597.toDataURL("image/png"));

var temp__4657__auto___72600 = victim_el_72598.getAttribute("style");
if(cljs.core.truth_(temp__4657__auto___72600)){
var style_72601 = temp__4657__auto___72600;
img_el_72599.setAttribute("style",style_72601);
} else {
}

victim_el_72598.parentNode.replaceChild(img_el_72599,victim_el_72598);

var G__72602 = seq__72587_72593;
var G__72603 = chunk__72589_72594;
var G__72604 = count__72590_72595;
var G__72605 = (i__72591_72596 + (1));
seq__72587_72593 = G__72602;
chunk__72589_72594 = G__72603;
count__72590_72595 = G__72604;
i__72591_72596 = G__72605;
continue;
} else {
var temp__4657__auto___72606 = cljs.core.seq(seq__72587_72593);
if(temp__4657__auto___72606){
var seq__72587_72607__$1 = temp__4657__auto___72606;
if(cljs.core.chunked_seq_QMARK_(seq__72587_72607__$1)){
var c__6956__auto___72608 = cljs.core.chunk_first(seq__72587_72607__$1);
var G__72609 = cljs.core.chunk_rest(seq__72587_72607__$1);
var G__72610 = c__6956__auto___72608;
var G__72611 = cljs.core.count(c__6956__auto___72608);
var G__72612 = (0);
seq__72587_72593 = G__72609;
chunk__72589_72594 = G__72610;
count__72590_72595 = G__72611;
i__72591_72596 = G__72612;
continue;
} else {
var cnv_72613 = cljs.core.first(seq__72587_72607__$1);
var victim_el_72614 = (copy_el.getElementsByTagName("canvas")[(0)]);
var img_el_72615 = document.createElement("img");
img_el_72615.setAttribute("src",cnv_72613.toDataURL("image/png"));

var temp__4657__auto___72616__$1 = victim_el_72614.getAttribute("style");
if(cljs.core.truth_(temp__4657__auto___72616__$1)){
var style_72617 = temp__4657__auto___72616__$1;
img_el_72615.setAttribute("style",style_72617);
} else {
}

victim_el_72614.parentNode.replaceChild(img_el_72615,victim_el_72614);

var G__72618 = cljs.core.next(seq__72587_72607__$1);
var G__72619 = null;
var G__72620 = (0);
var G__72621 = (0);
seq__72587_72593 = G__72618;
chunk__72589_72594 = G__72619;
count__72590_72595 = G__72620;
i__72591_72596 = G__72621;
continue;
}
} else {
}
}
break;
}

return copy_el.innerHTML;
});
goog.exportSymbol('org.numenta.sanity.demos.notebook.exported_viz', org.numenta.sanity.demos.notebook.exported_viz);
