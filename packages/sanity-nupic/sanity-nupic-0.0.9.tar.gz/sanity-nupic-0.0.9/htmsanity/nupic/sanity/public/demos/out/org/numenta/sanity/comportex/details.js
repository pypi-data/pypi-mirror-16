// Compiled by ClojureScript 1.7.228 {:static-fns true, :optimize-constants true}
goog.provide('org.numenta.sanity.comportex.details');
goog.require('cljs.core');
goog.require('clojure.string');
goog.require('org.nfrac.comportex.core');
goog.require('org.nfrac.comportex.protocols');
org.numenta.sanity.comportex.details.to_fixed = (function org$numenta$sanity$comportex$details$to_fixed(n,digits){
return n.toFixed(digits);
});
org.numenta.sanity.comportex.details.detail_text = (function org$numenta$sanity$comportex$details$detail_text(htm,prior_htm,rgn_id,lyr_id,col){
var rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,rgn_id], null));
var lyr = cljs.core.get.cljs$core$IFn$_invoke$arity$2(rgn,lyr_id);
var depth = org.nfrac.comportex.protocols.layer_depth(lyr);
var in$ = cljs.core.cst$kw$input_DASH_value.cljs$core$IFn$_invoke$arity$1(htm);
var in_bits = cljs.core.cst$kw$in_DASH_ff_DASH_bits.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$state.cljs$core$IFn$_invoke$arity$1(lyr));
var in_sbits = cljs.core.cst$kw$in_DASH_stable_DASH_ff_DASH_bits.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$state.cljs$core$IFn$_invoke$arity$1(lyr));
return cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.str,cljs.core.interpose.cljs$core$IFn$_invoke$arity$2("\n",cljs.core.flatten(cljs.core.PersistentVector.fromArray(["__Selection__",[cljs.core.str("* timestep "),cljs.core.str(org.nfrac.comportex.protocols.timestep(rgn))].join(''),[cljs.core.str("* column "),cljs.core.str((function (){var or__6153__auto__ = col;
if(cljs.core.truth_(or__6153__auto__)){
return or__6153__auto__;
} else {
return "nil";
}
})())].join(''),"","__Input__",[cljs.core.str(in$)].join(''),[cljs.core.str("("),cljs.core.str(cljs.core.count(in_bits)),cljs.core.str(" bits, of which "),cljs.core.str(cljs.core.count(in_sbits)),cljs.core.str(" stable)")].join(''),"","__Input bits__",[cljs.core.str(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(in_bits))].join(''),"","__Active columns__",[cljs.core.str(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.protocols.active_columns(lyr)))].join(''),"","__Bursting columns__",[cljs.core.str(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.protocols.bursting_columns(lyr)))].join(''),"","__Winner cells__",[cljs.core.str(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.protocols.winner_cells(lyr)))].join(''),"","__Proximal learning__",(function (){var iter__6925__auto__ = ((function (rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69188(s__69189){
return (new cljs.core.LazySeq(null,((function (rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69189__$1 = s__69189;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__69189__$1);
if(temp__4657__auto__){
var s__69189__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__69189__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69189__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69191 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69190 = (0);
while(true){
if((i__69190 < size__6924__auto__)){
var seg_up = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69190);
cljs.core.chunk_append(b__69191,[cljs.core.str(cljs.core.cst$kw$target_DASH_id.cljs$core$IFn$_invoke$arity$1(seg_up)),cljs.core.str(" "),cljs.core.str(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(seg_up,cljs.core.cst$kw$target_DASH_id,cljs.core.array_seq([cljs.core.cst$kw$operation], 0)))].join(''));

var G__69542 = (i__69190 + (1));
i__69190 = G__69542;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69191),org$numenta$sanity$comportex$details$detail_text_$_iter__69188(cljs.core.chunk_rest(s__69189__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69191),null);
}
} else {
var seg_up = cljs.core.first(s__69189__$2);
return cljs.core.cons([cljs.core.str(cljs.core.cst$kw$target_DASH_id.cljs$core$IFn$_invoke$arity$1(seg_up)),cljs.core.str(" "),cljs.core.str(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(seg_up,cljs.core.cst$kw$target_DASH_id,cljs.core.array_seq([cljs.core.cst$kw$operation], 0)))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69188(cljs.core.rest(s__69189__$2)));
}
} else {
return null;
}
break;
}
});})(rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$target_DASH_id,cljs.core.vals(cljs.core.cst$kw$proximal.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$learning.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$learn_DASH_state.cljs$core$IFn$_invoke$arity$1(lyr))))));
})(),"","__Distal learning__",(function (){var iter__6925__auto__ = ((function (rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69194(s__69195){
return (new cljs.core.LazySeq(null,((function (rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69195__$1 = s__69195;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__69195__$1);
if(temp__4657__auto__){
var s__69195__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__69195__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69195__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69197 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69196 = (0);
while(true){
if((i__69196 < size__6924__auto__)){
var seg_up = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69196);
cljs.core.chunk_append(b__69197,[cljs.core.str(cljs.core.cst$kw$target_DASH_id.cljs$core$IFn$_invoke$arity$1(seg_up)),cljs.core.str(" "),cljs.core.str(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(seg_up,cljs.core.cst$kw$target_DASH_id,cljs.core.array_seq([cljs.core.cst$kw$operation], 0)))].join(''));

var G__69543 = (i__69196 + (1));
i__69196 = G__69543;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69197),org$numenta$sanity$comportex$details$detail_text_$_iter__69194(cljs.core.chunk_rest(s__69195__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69197),null);
}
} else {
var seg_up = cljs.core.first(s__69195__$2);
return cljs.core.cons([cljs.core.str(cljs.core.cst$kw$target_DASH_id.cljs$core$IFn$_invoke$arity$1(seg_up)),cljs.core.str(" "),cljs.core.str(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(seg_up,cljs.core.cst$kw$target_DASH_id,cljs.core.array_seq([cljs.core.cst$kw$operation], 0)))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69194(cljs.core.rest(s__69195__$2)));
}
} else {
return null;
}
break;
}
});})(rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$target_DASH_id,cljs.core.vals(cljs.core.cst$kw$distal.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$learning.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$learn_DASH_state.cljs$core$IFn$_invoke$arity$1(lyr))))));
})(),"","__Distal punishments__",(function (){var iter__6925__auto__ = ((function (rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69200(s__69201){
return (new cljs.core.LazySeq(null,((function (rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69201__$1 = s__69201;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__69201__$1);
if(temp__4657__auto__){
var s__69201__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__69201__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69201__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69203 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69202 = (0);
while(true){
if((i__69202 < size__6924__auto__)){
var seg_up = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69202);
cljs.core.chunk_append(b__69203,[cljs.core.str(cljs.core.cst$kw$target_DASH_id.cljs$core$IFn$_invoke$arity$1(seg_up))].join(''));

var G__69544 = (i__69202 + (1));
i__69202 = G__69544;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69203),org$numenta$sanity$comportex$details$detail_text_$_iter__69200(cljs.core.chunk_rest(s__69201__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69203),null);
}
} else {
var seg_up = cljs.core.first(s__69201__$2);
return cljs.core.cons([cljs.core.str(cljs.core.cst$kw$target_DASH_id.cljs$core$IFn$_invoke$arity$1(seg_up))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69200(cljs.core.rest(s__69201__$2)));
}
} else {
return null;
}
break;
}
});})(rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$target_DASH_id,cljs.core.cst$kw$distal.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$punishments.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$learn_DASH_state.cljs$core$IFn$_invoke$arity$1(lyr)))));
})(),"","__Stable cells buffer__",[cljs.core.str(cljs.core.seq(cljs.core.cst$kw$stable_DASH_cells_DASH_buffer.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$state.cljs$core$IFn$_invoke$arity$1(lyr))))].join(''),"",(cljs.core.truth_((function (){var and__6141__auto__ = col;
if(cljs.core.truth_(and__6141__auto__)){
return prior_htm;
} else {
return and__6141__auto__;
}
})())?(function (){var p_lyr = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(prior_htm,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,rgn_id,lyr_id], null));
var p_prox_sg = cljs.core.cst$kw$proximal_DASH_sg.cljs$core$IFn$_invoke$arity$1(p_lyr);
var p_distal_sg = cljs.core.cst$kw$distal_DASH_sg.cljs$core$IFn$_invoke$arity$1(p_lyr);
var d_pcon = cljs.core.cst$kw$perm_DASH_connected.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$distal.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.protocols.params(p_lyr)));
var ff_pcon = cljs.core.cst$kw$perm_DASH_connected.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$proximal.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.protocols.params(p_lyr)));
var bits = cljs.core.cst$kw$in_DASH_ff_DASH_bits.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$state.cljs$core$IFn$_invoke$arity$1(lyr));
var sig_bits = cljs.core.cst$kw$in_DASH_stable_DASH_ff_DASH_bits.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$state.cljs$core$IFn$_invoke$arity$1(lyr));
var d_bits = cljs.core.cst$kw$active_DASH_bits.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$prior_DASH_distal_DASH_state.cljs$core$IFn$_invoke$arity$1(lyr));
var d_lbits = cljs.core.cst$kw$learnable_DASH_bits.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$prior_DASH_distal_DASH_state.cljs$core$IFn$_invoke$arity$1(lyr));
return new cljs.core.PersistentVector(null, 8, 5, cljs.core.PersistentVector.EMPTY_NODE, ["__Column overlap__",[cljs.core.str(cljs.core.get.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$col_DASH_overlaps.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$state.cljs$core$IFn$_invoke$arity$1(lyr)),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [col,(0)], null)))].join(''),"","__Selected column__","__Connected ff-synapses__",(function (){var iter__6925__auto__ = ((function (p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69206(s__69207){
return (new cljs.core.LazySeq(null,((function (p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69207__$1 = s__69207;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__69207__$1);
if(temp__4657__auto__){
var s__69207__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__69207__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69207__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69209 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69208 = (0);
while(true){
if((i__69208 < size__6924__auto__)){
var vec__69242 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69208);
var si = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69242,(0),null);
var syns = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69242,(1),null);
if(cljs.core.seq(syns)){
cljs.core.chunk_append(b__69209,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [[cljs.core.str("FF segment "),cljs.core.str(si)].join(''),(function (){var iter__6925__auto__ = ((function (i__69208,s__69207__$1,vec__69242,si,syns,c__6923__auto__,size__6924__auto__,b__69209,s__69207__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69206_$_iter__69243(s__69244){
return (new cljs.core.LazySeq(null,((function (i__69208,s__69207__$1,vec__69242,si,syns,c__6923__auto__,size__6924__auto__,b__69209,s__69207__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69244__$1 = s__69244;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__69244__$1);
if(temp__4657__auto____$1){
var s__69244__$2 = temp__4657__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__69244__$2)){
var c__6923__auto____$1 = cljs.core.chunk_first(s__69244__$2);
var size__6924__auto____$1 = cljs.core.count(c__6923__auto____$1);
var b__69246 = cljs.core.chunk_buffer(size__6924__auto____$1);
if((function (){var i__69245 = (0);
while(true){
if((i__69245 < size__6924__auto____$1)){
var vec__69253 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto____$1,i__69245);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69253,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69253,(1),null);
var vec__69254 = org.nfrac.comportex.core.source_of_incoming_bit.cljs$core$IFn$_invoke$arity$4(htm,rgn_id,id,cljs.core.cst$kw$ff_DASH_deps);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69254,(0),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69254,(1),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
cljs.core.chunk_append(b__69246,[cljs.core.str("  "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= ff_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(sig_bits,id))?" S":((cljs.core.contains_QMARK_(bits,id))?" A":null)))].join(''));

var G__69545 = (i__69245 + (1));
i__69245 = G__69545;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69246),org$numenta$sanity$comportex$details$detail_text_$_iter__69206_$_iter__69243(cljs.core.chunk_rest(s__69244__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69246),null);
}
} else {
var vec__69255 = cljs.core.first(s__69244__$2);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69255,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69255,(1),null);
var vec__69256 = org.nfrac.comportex.core.source_of_incoming_bit.cljs$core$IFn$_invoke$arity$4(htm,rgn_id,id,cljs.core.cst$kw$ff_DASH_deps);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69256,(0),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69256,(1),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
return cljs.core.cons([cljs.core.str("  "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= ff_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(sig_bits,id))?" S":((cljs.core.contains_QMARK_(bits,id))?" A":null)))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69206_$_iter__69243(cljs.core.rest(s__69244__$2)));
}
} else {
return null;
}
break;
}
});})(i__69208,s__69207__$1,vec__69242,si,syns,c__6923__auto__,size__6924__auto__,b__69209,s__69207__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(i__69208,s__69207__$1,vec__69242,si,syns,c__6923__auto__,size__6924__auto__,b__69209,s__69207__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(syns));
})()], null));

var G__69546 = (i__69208 + (1));
i__69208 = G__69546;
continue;
} else {
var G__69547 = (i__69208 + (1));
i__69208 = G__69547;
continue;
}
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69209),org$numenta$sanity$comportex$details$detail_text_$_iter__69206(cljs.core.chunk_rest(s__69207__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69209),null);
}
} else {
var vec__69257 = cljs.core.first(s__69207__$2);
var si = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69257,(0),null);
var syns = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69257,(1),null);
if(cljs.core.seq(syns)){
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [[cljs.core.str("FF segment "),cljs.core.str(si)].join(''),(function (){var iter__6925__auto__ = ((function (s__69207__$1,vec__69257,si,syns,s__69207__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69206_$_iter__69258(s__69259){
return (new cljs.core.LazySeq(null,((function (s__69207__$1,vec__69257,si,syns,s__69207__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69259__$1 = s__69259;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__69259__$1);
if(temp__4657__auto____$1){
var s__69259__$2 = temp__4657__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__69259__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69259__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69261 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69260 = (0);
while(true){
if((i__69260 < size__6924__auto__)){
var vec__69268 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69260);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69268,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69268,(1),null);
var vec__69269 = org.nfrac.comportex.core.source_of_incoming_bit.cljs$core$IFn$_invoke$arity$4(htm,rgn_id,id,cljs.core.cst$kw$ff_DASH_deps);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69269,(0),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69269,(1),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
cljs.core.chunk_append(b__69261,[cljs.core.str("  "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= ff_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(sig_bits,id))?" S":((cljs.core.contains_QMARK_(bits,id))?" A":null)))].join(''));

var G__69548 = (i__69260 + (1));
i__69260 = G__69548;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69261),org$numenta$sanity$comportex$details$detail_text_$_iter__69206_$_iter__69258(cljs.core.chunk_rest(s__69259__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69261),null);
}
} else {
var vec__69270 = cljs.core.first(s__69259__$2);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69270,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69270,(1),null);
var vec__69271 = org.nfrac.comportex.core.source_of_incoming_bit.cljs$core$IFn$_invoke$arity$4(htm,rgn_id,id,cljs.core.cst$kw$ff_DASH_deps);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69271,(0),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69271,(1),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
return cljs.core.cons([cljs.core.str("  "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= ff_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(sig_bits,id))?" S":((cljs.core.contains_QMARK_(bits,id))?" A":null)))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69206_$_iter__69258(cljs.core.rest(s__69259__$2)));
}
} else {
return null;
}
break;
}
});})(s__69207__$1,vec__69257,si,syns,s__69207__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(s__69207__$1,vec__69257,si,syns,s__69207__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(syns));
})()], null),org$numenta$sanity$comportex$details$detail_text_$_iter__69206(cljs.core.rest(s__69207__$2)));
} else {
var G__69549 = cljs.core.rest(s__69207__$2);
s__69207__$1 = G__69549;
continue;
}
}
} else {
return null;
}
break;
}
});})(p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.map_indexed.cljs$core$IFn$_invoke$arity$2(cljs.core.vector,org.nfrac.comportex.protocols.cell_segments(p_prox_sg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [col,(0)], null))));
})(),"__Cells and their distal dendrite segments__",(function (){var iter__6925__auto__ = ((function (p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69272(s__69273){
return (new cljs.core.LazySeq(null,((function (p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69273__$1 = s__69273;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__69273__$1);
if(temp__4657__auto__){
var s__69273__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__69273__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69273__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69275 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69274 = (0);
while(true){
if((i__69274 < size__6924__auto__)){
var ci = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69274);
var segs = org.nfrac.comportex.protocols.cell_segments(p_distal_sg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [col,ci], null));
cljs.core.chunk_append(b__69275,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [[cljs.core.str("CELL "),cljs.core.str(ci)].join(''),[cljs.core.str(cljs.core.count(segs)),cljs.core.str(" = "),cljs.core.str(cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.count,segs))].join(''),(function (){var iter__6925__auto__ = ((function (i__69274,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410(s__69411){
return (new cljs.core.LazySeq(null,((function (i__69274,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69411__$1 = s__69411;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__69411__$1);
if(temp__4657__auto____$1){
var s__69411__$2 = temp__4657__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__69411__$2)){
var c__6923__auto____$1 = cljs.core.chunk_first(s__69411__$2);
var size__6924__auto____$1 = cljs.core.count(c__6923__auto____$1);
var b__69413 = cljs.core.chunk_buffer(size__6924__auto____$1);
if((function (){var i__69412 = (0);
while(true){
if((i__69412 < size__6924__auto____$1)){
var vec__69446 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto____$1,i__69412);
var si = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69446,(0),null);
var syns = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69446,(1),null);
cljs.core.chunk_append(b__69413,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [[cljs.core.str("  SEGMENT "),cljs.core.str(si)].join(''),(function (){var iter__6925__auto__ = ((function (i__69412,i__69274,vec__69446,si,syns,c__6923__auto____$1,size__6924__auto____$1,b__69413,s__69411__$2,temp__4657__auto____$1,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410_$_iter__69447(s__69448){
return (new cljs.core.LazySeq(null,((function (i__69412,i__69274,vec__69446,si,syns,c__6923__auto____$1,size__6924__auto____$1,b__69413,s__69411__$2,temp__4657__auto____$1,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69448__$1 = s__69448;
while(true){
var temp__4657__auto____$2 = cljs.core.seq(s__69448__$1);
if(temp__4657__auto____$2){
var s__69448__$2 = temp__4657__auto____$2;
if(cljs.core.chunked_seq_QMARK_(s__69448__$2)){
var c__6923__auto____$2 = cljs.core.chunk_first(s__69448__$2);
var size__6924__auto____$2 = cljs.core.count(c__6923__auto____$2);
var b__69450 = cljs.core.chunk_buffer(size__6924__auto____$2);
if((function (){var i__69449 = (0);
while(true){
if((i__69449 < size__6924__auto____$2)){
var vec__69457 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto____$2,i__69449);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69457,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69457,(1),null);
var vec__69458 = org.nfrac.comportex.core.source_of_distal_bit(htm,rgn_id,lyr_id,id);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69458,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69458,(1),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69458,(2),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
cljs.core.chunk_append(b__69450,[cljs.core.str("    "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= d_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(d_lbits,id))?" L":((cljs.core.contains_QMARK_(d_bits,id))?" A":null)))].join(''));

var G__69550 = (i__69449 + (1));
i__69449 = G__69550;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69450),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410_$_iter__69447(cljs.core.chunk_rest(s__69448__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69450),null);
}
} else {
var vec__69459 = cljs.core.first(s__69448__$2);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69459,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69459,(1),null);
var vec__69460 = org.nfrac.comportex.core.source_of_distal_bit(htm,rgn_id,lyr_id,id);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69460,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69460,(1),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69460,(2),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
return cljs.core.cons([cljs.core.str("    "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= d_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(d_lbits,id))?" L":((cljs.core.contains_QMARK_(d_bits,id))?" A":null)))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410_$_iter__69447(cljs.core.rest(s__69448__$2)));
}
} else {
return null;
}
break;
}
});})(i__69412,i__69274,vec__69446,si,syns,c__6923__auto____$1,size__6924__auto____$1,b__69413,s__69411__$2,temp__4657__auto____$1,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(i__69412,i__69274,vec__69446,si,syns,c__6923__auto____$1,size__6924__auto____$1,b__69413,s__69411__$2,temp__4657__auto____$1,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(syns));
})()], null));

var G__69551 = (i__69412 + (1));
i__69412 = G__69551;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69413),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410(cljs.core.chunk_rest(s__69411__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69413),null);
}
} else {
var vec__69461 = cljs.core.first(s__69411__$2);
var si = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69461,(0),null);
var syns = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69461,(1),null);
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [[cljs.core.str("  SEGMENT "),cljs.core.str(si)].join(''),(function (){var iter__6925__auto__ = ((function (i__69274,vec__69461,si,syns,s__69411__$2,temp__4657__auto____$1,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410_$_iter__69462(s__69463){
return (new cljs.core.LazySeq(null,((function (i__69274,vec__69461,si,syns,s__69411__$2,temp__4657__auto____$1,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69463__$1 = s__69463;
while(true){
var temp__4657__auto____$2 = cljs.core.seq(s__69463__$1);
if(temp__4657__auto____$2){
var s__69463__$2 = temp__4657__auto____$2;
if(cljs.core.chunked_seq_QMARK_(s__69463__$2)){
var c__6923__auto____$1 = cljs.core.chunk_first(s__69463__$2);
var size__6924__auto____$1 = cljs.core.count(c__6923__auto____$1);
var b__69465 = cljs.core.chunk_buffer(size__6924__auto____$1);
if((function (){var i__69464 = (0);
while(true){
if((i__69464 < size__6924__auto____$1)){
var vec__69472 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto____$1,i__69464);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69472,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69472,(1),null);
var vec__69473 = org.nfrac.comportex.core.source_of_distal_bit(htm,rgn_id,lyr_id,id);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69473,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69473,(1),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69473,(2),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
cljs.core.chunk_append(b__69465,[cljs.core.str("    "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= d_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(d_lbits,id))?" L":((cljs.core.contains_QMARK_(d_bits,id))?" A":null)))].join(''));

var G__69552 = (i__69464 + (1));
i__69464 = G__69552;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69465),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410_$_iter__69462(cljs.core.chunk_rest(s__69463__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69465),null);
}
} else {
var vec__69474 = cljs.core.first(s__69463__$2);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69474,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69474,(1),null);
var vec__69475 = org.nfrac.comportex.core.source_of_distal_bit(htm,rgn_id,lyr_id,id);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69475,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69475,(1),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69475,(2),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
return cljs.core.cons([cljs.core.str("    "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= d_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(d_lbits,id))?" L":((cljs.core.contains_QMARK_(d_bits,id))?" A":null)))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410_$_iter__69462(cljs.core.rest(s__69463__$2)));
}
} else {
return null;
}
break;
}
});})(i__69274,vec__69461,si,syns,s__69411__$2,temp__4657__auto____$1,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(i__69274,vec__69461,si,syns,s__69411__$2,temp__4657__auto____$1,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(syns));
})()], null),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69410(cljs.core.rest(s__69411__$2)));
}
} else {
return null;
}
break;
}
});})(i__69274,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(i__69274,segs,ci,c__6923__auto__,size__6924__auto__,b__69275,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.map_indexed.cljs$core$IFn$_invoke$arity$2(cljs.core.vector,segs));
})()], null));

var G__69553 = (i__69274 + (1));
i__69274 = G__69553;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69275),org$numenta$sanity$comportex$details$detail_text_$_iter__69272(cljs.core.chunk_rest(s__69273__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69275),null);
}
} else {
var ci = cljs.core.first(s__69273__$2);
var segs = org.nfrac.comportex.protocols.cell_segments(p_distal_sg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [col,ci], null));
return cljs.core.cons(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [[cljs.core.str("CELL "),cljs.core.str(ci)].join(''),[cljs.core.str(cljs.core.count(segs)),cljs.core.str(" = "),cljs.core.str(cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.count,segs))].join(''),(function (){var iter__6925__auto__ = ((function (segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476(s__69477){
return (new cljs.core.LazySeq(null,((function (segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69477__$1 = s__69477;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__69477__$1);
if(temp__4657__auto____$1){
var s__69477__$2 = temp__4657__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__69477__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69477__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69479 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69478 = (0);
while(true){
if((i__69478 < size__6924__auto__)){
var vec__69512 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69478);
var si = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69512,(0),null);
var syns = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69512,(1),null);
cljs.core.chunk_append(b__69479,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [[cljs.core.str("  SEGMENT "),cljs.core.str(si)].join(''),(function (){var iter__6925__auto__ = ((function (i__69478,vec__69512,si,syns,c__6923__auto__,size__6924__auto__,b__69479,s__69477__$2,temp__4657__auto____$1,segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476_$_iter__69513(s__69514){
return (new cljs.core.LazySeq(null,((function (i__69478,vec__69512,si,syns,c__6923__auto__,size__6924__auto__,b__69479,s__69477__$2,temp__4657__auto____$1,segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69514__$1 = s__69514;
while(true){
var temp__4657__auto____$2 = cljs.core.seq(s__69514__$1);
if(temp__4657__auto____$2){
var s__69514__$2 = temp__4657__auto____$2;
if(cljs.core.chunked_seq_QMARK_(s__69514__$2)){
var c__6923__auto____$1 = cljs.core.chunk_first(s__69514__$2);
var size__6924__auto____$1 = cljs.core.count(c__6923__auto____$1);
var b__69516 = cljs.core.chunk_buffer(size__6924__auto____$1);
if((function (){var i__69515 = (0);
while(true){
if((i__69515 < size__6924__auto____$1)){
var vec__69523 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto____$1,i__69515);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69523,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69523,(1),null);
var vec__69524 = org.nfrac.comportex.core.source_of_distal_bit(htm,rgn_id,lyr_id,id);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69524,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69524,(1),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69524,(2),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
cljs.core.chunk_append(b__69516,[cljs.core.str("    "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= d_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(d_lbits,id))?" L":((cljs.core.contains_QMARK_(d_bits,id))?" A":null)))].join(''));

var G__69554 = (i__69515 + (1));
i__69515 = G__69554;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69516),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476_$_iter__69513(cljs.core.chunk_rest(s__69514__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69516),null);
}
} else {
var vec__69525 = cljs.core.first(s__69514__$2);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69525,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69525,(1),null);
var vec__69526 = org.nfrac.comportex.core.source_of_distal_bit(htm,rgn_id,lyr_id,id);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69526,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69526,(1),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69526,(2),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
return cljs.core.cons([cljs.core.str("    "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= d_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(d_lbits,id))?" L":((cljs.core.contains_QMARK_(d_bits,id))?" A":null)))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476_$_iter__69513(cljs.core.rest(s__69514__$2)));
}
} else {
return null;
}
break;
}
});})(i__69478,vec__69512,si,syns,c__6923__auto__,size__6924__auto__,b__69479,s__69477__$2,temp__4657__auto____$1,segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(i__69478,vec__69512,si,syns,c__6923__auto__,size__6924__auto__,b__69479,s__69477__$2,temp__4657__auto____$1,segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(syns));
})()], null));

var G__69555 = (i__69478 + (1));
i__69478 = G__69555;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69479),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476(cljs.core.chunk_rest(s__69477__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69479),null);
}
} else {
var vec__69527 = cljs.core.first(s__69477__$2);
var si = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69527,(0),null);
var syns = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69527,(1),null);
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [[cljs.core.str("  SEGMENT "),cljs.core.str(si)].join(''),(function (){var iter__6925__auto__ = ((function (vec__69527,si,syns,s__69477__$2,temp__4657__auto____$1,segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476_$_iter__69528(s__69529){
return (new cljs.core.LazySeq(null,((function (vec__69527,si,syns,s__69477__$2,temp__4657__auto____$1,segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits){
return (function (){
var s__69529__$1 = s__69529;
while(true){
var temp__4657__auto____$2 = cljs.core.seq(s__69529__$1);
if(temp__4657__auto____$2){
var s__69529__$2 = temp__4657__auto____$2;
if(cljs.core.chunked_seq_QMARK_(s__69529__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69529__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69531 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69530 = (0);
while(true){
if((i__69530 < size__6924__auto__)){
var vec__69538 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69530);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69538,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69538,(1),null);
var vec__69539 = org.nfrac.comportex.core.source_of_distal_bit(htm,rgn_id,lyr_id,id);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69539,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69539,(1),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69539,(2),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
cljs.core.chunk_append(b__69531,[cljs.core.str("    "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= d_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(d_lbits,id))?" L":((cljs.core.contains_QMARK_(d_bits,id))?" A":null)))].join(''));

var G__69556 = (i__69530 + (1));
i__69530 = G__69556;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69531),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476_$_iter__69528(cljs.core.chunk_rest(s__69529__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69531),null);
}
} else {
var vec__69540 = cljs.core.first(s__69529__$2);
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69540,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69540,(1),null);
var vec__69541 = org.nfrac.comportex.core.source_of_distal_bit(htm,rgn_id,lyr_id,id);
var src_k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69541,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69541,(1),null);
var src_i = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69541,(2),null);
var src_rgn = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,src_k], null));
var src_id = (cljs.core.truth_(src_rgn)?org.nfrac.comportex.protocols.source_of_bit(src_rgn,src_i):src_i);
return cljs.core.cons([cljs.core.str("    "),cljs.core.str(src_k),cljs.core.str(" "),cljs.core.str(src_id),cljs.core.str((((p >= d_pcon))?" :=> ":" :.: ")),cljs.core.str(org.numenta.sanity.comportex.details.to_fixed(p,(2))),cljs.core.str(((cljs.core.contains_QMARK_(d_lbits,id))?" L":((cljs.core.contains_QMARK_(d_bits,id))?" A":null)))].join(''),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476_$_iter__69528(cljs.core.rest(s__69529__$2)));
}
} else {
return null;
}
break;
}
});})(vec__69527,si,syns,s__69477__$2,temp__4657__auto____$1,segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(vec__69527,si,syns,s__69477__$2,temp__4657__auto____$1,segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(syns));
})()], null),org$numenta$sanity$comportex$details$detail_text_$_iter__69272_$_iter__69476(cljs.core.rest(s__69477__$2)));
}
} else {
return null;
}
break;
}
});})(segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(segs,ci,s__69273__$2,temp__4657__auto__,p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.map_indexed.cljs$core$IFn$_invoke$arity$2(cljs.core.vector,segs));
})()], null),org$numenta$sanity$comportex$details$detail_text_$_iter__69272(cljs.core.rest(s__69273__$2)));
}
} else {
return null;
}
break;
}
});})(p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
,null,null));
});})(p_lyr,p_prox_sg,p_distal_sg,d_pcon,ff_pcon,bits,sig_bits,d_bits,d_lbits,rgn,lyr,depth,in$,in_bits,in_sbits))
;
return iter__6925__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.protocols.layer_depth(lyr)));
})()], null);
})():null),"","__spec__",cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.str,cljs.core.sort.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.protocols.params(rgn)))], true))));
});
