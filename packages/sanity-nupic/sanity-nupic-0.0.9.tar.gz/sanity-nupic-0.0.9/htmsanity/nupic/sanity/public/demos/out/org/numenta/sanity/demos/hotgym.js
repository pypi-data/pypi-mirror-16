// Compiled by ClojureScript 1.7.228 {:static-fns true, :optimize-constants true}
goog.provide('org.numenta.sanity.demos.hotgym');
goog.require('cljs.core');
goog.require('goog.dom');
goog.require('org.nfrac.comportex.cells');
goog.require('reagent.core');
goog.require('org.numenta.sanity.viz_canvas');
goog.require('org.numenta.sanity.main');
goog.require('org.nfrac.comportex.protocols');
goog.require('goog.net.XhrIo');
goog.require('org.numenta.sanity.util');
goog.require('org.numenta.sanity.comportex.data');
goog.require('org.nfrac.comportex.topology');
goog.require('cljs.core.async');
goog.require('org.numenta.sanity.bridge.marshalling');
goog.require('reagent_forms.core');
goog.require('org.nfrac.comportex.core');
goog.require('org.numenta.sanity.bridge.browser');
goog.require('org.numenta.sanity.demos.comportex_common');
goog.require('org.nfrac.comportex.util');
goog.require('org.nfrac.comportex.encoders');
goog.require('cljs.reader');
org.numenta.sanity.demos.hotgym.world_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
org.numenta.sanity.demos.hotgym.into_sim = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
org.numenta.sanity.demos.hotgym.model = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
/**
 * By example:
 *   Given 7.2, returns (7, 8, 6, 9, 5, 10, ...),
 *   Given 7.7, returns (8, 7, 9, 6, 10, 5, ...)
 */
org.numenta.sanity.demos.hotgym.middle_out_range = (function org$numenta$sanity$demos$hotgym$middle_out_range(v){
var start = cljs.core.long$(Math.round(v));
var rounded_down_QMARK_ = (v > start);
var up = cljs.core.iterate(cljs.core.inc,start);
var down = cljs.core.iterate(cljs.core.dec,start);
if(rounded_down_QMARK_){
return cljs.core.interleave.cljs$core$IFn$_invoke$arity$2(down,cljs.core.drop.cljs$core$IFn$_invoke$arity$2((1),up));
} else {
return cljs.core.interleave.cljs$core$IFn$_invoke$arity$2(up,cljs.core.drop.cljs$core$IFn$_invoke$arity$2((1),down));
}
});
org.numenta.sanity.demos.hotgym.multiples_within_radius = (function org$numenta$sanity$demos$hotgym$multiples_within_radius(center,radius,multiples_of){
var lower_bound = (center - radius);
var upper_bound = (center + radius);
return cljs.core.take_while.cljs$core$IFn$_invoke$arity$2(((function (lower_bound,upper_bound){
return (function (p1__71003_SHARP_){
return ((lower_bound <= p1__71003_SHARP_)) && ((p1__71003_SHARP_ <= upper_bound));
});})(lower_bound,upper_bound))
,cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.partial.cljs$core$IFn$_invoke$arity$2(cljs.core._STAR_,multiples_of),org.numenta.sanity.demos.hotgym.middle_out_range((center / multiples_of))));
});
/**
 * Move items from `from` to `coll` until its size reaches `max-size`
 *   or we run out of items. Specifically supports sets and maps, which don't
 *   always grow when an item is added.
 */
org.numenta.sanity.demos.hotgym.into_bounded = (function org$numenta$sanity$demos$hotgym$into_bounded(coll,max_size,from){
var coll__$1 = coll;
var from__$1 = from;
while(true){
var n_remaining = (max_size - cljs.core.count(coll__$1));
if(cljs.core.truth_((function (){var and__6141__auto__ = (n_remaining > (0));
if(and__6141__auto__){
return cljs.core.not_empty(from__$1);
} else {
return and__6141__auto__;
}
})())){
var vec__71005 = cljs.core.split_at(n_remaining,from__$1);
var taken = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71005,(0),null);
var untaken = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71005,(1),null);
var G__71006 = cljs.core.into.cljs$core$IFn$_invoke$arity$2(coll__$1,taken);
var G__71007 = untaken;
coll__$1 = G__71006;
from__$1 = G__71007;
continue;
} else {
return coll__$1;
}
break;
}
});
/**
 * Place a bit in the center.
 *   Distribute bits around the center until we've used half of the remainder.
 *   Double the density. Distribute again until we've used half of the remainder.
 *   Double the density. ...
 *   Continue until all active bits are distributed or all bits are active.
 * 
 *   Strategically choose bit positions so that the intersections between
 *   various ranges will select the same bits.
 */
org.numenta.sanity.demos.hotgym.sampled_window = (function org$numenta$sanity$demos$hotgym$sampled_window(center,n_bits,target_n_active,bit_radius){
var chosen = cljs.core.PersistentHashSet.fromArray([center], true);
var density = (((target_n_active - cljs.core.count(chosen)) / ((2) * bit_radius)) / (2));
while(true){
var remaining = (target_n_active - cljs.core.count(chosen));
var multiples_of = cljs.core.long$(((1) / density));
if(((remaining > (0))) && ((multiples_of > (0)))){
var half_remaining = cljs.core.quot(remaining,(2));
var n_take = (((cljs.core.odd_QMARK_(remaining)) || (cljs.core.odd_QMARK_(half_remaining)))?remaining:half_remaining);
var G__71009 = org.numenta.sanity.demos.hotgym.into_bounded(chosen,(n_take + cljs.core.count(chosen)),cljs.core.filter.cljs$core$IFn$_invoke$arity$2(((function (chosen,density,half_remaining,n_take,remaining,multiples_of){
return (function (p1__71008_SHARP_){
return (((0) <= p1__71008_SHARP_)) && ((p1__71008_SHARP_ <= (n_bits - (1))));
});})(chosen,density,half_remaining,n_take,remaining,multiples_of))
,org.numenta.sanity.demos.hotgym.multiples_within_radius(center,bit_radius,multiples_of)));
var G__71010 = (density * (2));
chosen = G__71009;
density = G__71010;
continue;
} else {
return chosen;
}
break;
}
});

/**
* @constructor
 * @implements {cljs.core.IRecord}
 * @implements {cljs.core.IEquiv}
 * @implements {cljs.core.IHash}
 * @implements {cljs.core.ICollection}
 * @implements {org.nfrac.comportex.protocols.PEncoder}
 * @implements {cljs.core.ICounted}
 * @implements {cljs.core.ISeqable}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.ICloneable}
 * @implements {cljs.core.IPrintWithWriter}
 * @implements {cljs.core.IIterable}
 * @implements {cljs.core.IWithMeta}
 * @implements {cljs.core.IAssociative}
 * @implements {org.nfrac.comportex.protocols.PTopological}
 * @implements {cljs.core.IMap}
 * @implements {cljs.core.ILookup}
*/
org.numenta.sanity.demos.hotgym.SamplingLinearEncoder = (function (topo,n_active,lower,upper,radius,__meta,__extmap,__hash){
this.topo = topo;
this.n_active = n_active;
this.lower = lower;
this.upper = upper;
this.radius = radius;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k71012,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__71014 = (((k71012 instanceof cljs.core.Keyword))?k71012.fqn:null);
switch (G__71014) {
case "topo":
return self__.topo;

break;
case "n-active":
return self__.n_active;

break;
case "lower":
return self__.lower;

break;
case "upper":
return self__.upper;

break;
case "radius":
return self__.radius;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k71012,else__6770__auto__);

}
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.topo;
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.numenta.sanity.demos.hotgym.SamplingLinearEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$lower,self__.lower],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$upper,self__.upper],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$radius,self__.radius],null))], null),self__.__extmap));
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IIterable$ = true;

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__71011){
var self__ = this;
var G__71011__$1 = this;
return (new cljs.core.RecordIter((0),G__71011__$1,5,new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$topo,cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$lower,cljs.core.cst$kw$upper,cljs.core.cst$kw$radius], null),cljs.core._iterator(self__.__extmap)));
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,self__.__meta,self__.__extmap,self__.__hash));
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (5 + cljs.core.count(self__.__extmap));
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
var self__ = this;
var this__6762__auto____$1 = this;
var h__6588__auto__ = self__.__hash;
if(!((h__6588__auto__ == null))){
return h__6588__auto__;
} else {
var h__6588__auto____$1 = cljs.core.hash_imap(this__6762__auto____$1);
self__.__hash = h__6588__auto____$1;

return h__6588__auto____$1;
}
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
var self__ = this;
var this__6763__auto____$1 = this;
if(cljs.core.truth_((function (){var and__6141__auto__ = other__6764__auto__;
if(cljs.core.truth_(and__6141__auto__)){
var and__6141__auto____$1 = (this__6763__auto____$1.constructor === other__6764__auto__.constructor);
if(and__6141__auto____$1){
return cljs.core.equiv_map(this__6763__auto____$1,other__6764__auto__);
} else {
return and__6141__auto____$1;
}
} else {
return and__6141__auto__;
}
})())){
return true;
} else {
return false;
}
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,x){
var self__ = this;
var ___$1 = this;
if(cljs.core.truth_(x)){
var n_bits = org.nfrac.comportex.protocols.size(self__.topo);
var domain_width = (self__.upper - self__.lower);
var center = cljs.core.long$(((((function (){var x__6491__auto__ = (function (){var x__6484__auto__ = x;
var y__6485__auto__ = self__.lower;
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})();
var y__6492__auto__ = self__.upper;
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})() - self__.lower) / domain_width) * n_bits));
var bit_radius = (self__.radius * (org.nfrac.comportex.protocols.size(self__.topo) / domain_width));
return org.numenta.sanity.demos.hotgym.sampled_window(center,n_bits,self__.n_active,bit_radius);
} else {
return cljs.core.sequence.cljs$core$IFn$_invoke$arity$1(null);
}
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (this$,bit_votes,n){
var self__ = this;
var this$__$1 = this;
var span = (self__.upper - self__.lower);
var values = cljs.core.range.cljs$core$IFn$_invoke$arity$3(self__.lower,self__.upper,(((((5) < span)) && ((span < (250))))?(1):(span / (50))));
return cljs.core.take.cljs$core$IFn$_invoke$arity$2(n,org.nfrac.comportex.encoders.decode_by_brute_force(this$__$1,values,bit_votes));
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$upper,null,cljs.core.cst$kw$topo,null,cljs.core.cst$kw$radius,null,cljs.core.cst$kw$lower,null,cljs.core.cst$kw$n_DASH_active,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__71011){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__71015 = cljs.core.keyword_identical_QMARK_;
var expr__71016 = k__6775__auto__;
if(cljs.core.truth_((pred__71015.cljs$core$IFn$_invoke$arity$2 ? pred__71015.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$topo,expr__71016) : pred__71015.call(null,cljs.core.cst$kw$topo,expr__71016)))){
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(G__71011,self__.n_active,self__.lower,self__.upper,self__.radius,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__71015.cljs$core$IFn$_invoke$arity$2 ? pred__71015.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$n_DASH_active,expr__71016) : pred__71015.call(null,cljs.core.cst$kw$n_DASH_active,expr__71016)))){
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(self__.topo,G__71011,self__.lower,self__.upper,self__.radius,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__71015.cljs$core$IFn$_invoke$arity$2 ? pred__71015.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$lower,expr__71016) : pred__71015.call(null,cljs.core.cst$kw$lower,expr__71016)))){
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(self__.topo,self__.n_active,G__71011,self__.upper,self__.radius,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__71015.cljs$core$IFn$_invoke$arity$2 ? pred__71015.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$upper,expr__71016) : pred__71015.call(null,cljs.core.cst$kw$upper,expr__71016)))){
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,G__71011,self__.radius,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__71015.cljs$core$IFn$_invoke$arity$2 ? pred__71015.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$radius,expr__71016) : pred__71015.call(null,cljs.core.cst$kw$radius,expr__71016)))){
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,G__71011,self__.__meta,self__.__extmap,null));
} else {
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__71011),null));
}
}
}
}
}
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$lower,self__.lower],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$upper,self__.upper],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$radius,self__.radius],null))], null),self__.__extmap));
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__71011){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,G__71011,self__.__extmap,self__.__hash));
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$topo,cljs.core.cst$sym$n_DASH_active,cljs.core.cst$sym$lower,cljs.core.cst$sym$upper,cljs.core.cst$sym$radius], null);
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.cljs$lang$type = true;

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.numenta.sanity.demos.hotgym/SamplingLinearEncoder");
});

org.numenta.sanity.demos.hotgym.SamplingLinearEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.numenta.sanity.demos.hotgym/SamplingLinearEncoder");
});

org.numenta.sanity.demos.hotgym.__GT_SamplingLinearEncoder = (function org$numenta$sanity$demos$hotgym$__GT_SamplingLinearEncoder(topo,n_active,lower,upper,radius){
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(topo,n_active,lower,upper,radius,null,null,null));
});

org.numenta.sanity.demos.hotgym.map__GT_SamplingLinearEncoder = (function org$numenta$sanity$demos$hotgym$map__GT_SamplingLinearEncoder(G__71013){
return (new org.numenta.sanity.demos.hotgym.SamplingLinearEncoder(cljs.core.cst$kw$topo.cljs$core$IFn$_invoke$arity$1(G__71013),cljs.core.cst$kw$n_DASH_active.cljs$core$IFn$_invoke$arity$1(G__71013),cljs.core.cst$kw$lower.cljs$core$IFn$_invoke$arity$1(G__71013),cljs.core.cst$kw$upper.cljs$core$IFn$_invoke$arity$1(G__71013),cljs.core.cst$kw$radius.cljs$core$IFn$_invoke$arity$1(G__71013),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__71013,cljs.core.cst$kw$topo,cljs.core.array_seq([cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$lower,cljs.core.cst$kw$upper,cljs.core.cst$kw$radius], 0)),null));
});

/**
 * A linear encoder that samples the surrounding radius, rather than
 *   activating all of it. Sampling density decreases as distance increases.
 * 
 *   * `dimensions` is the size of the encoder in bits along one or more
 *  dimensions, a vector e.g. [500].
 * 
 *   * `n-active` is the number of bits to be active.
 * 
 *   * `[lower upper]` gives the numeric range to cover. The input number
 *  will be clamped to this range.
 * 
 *   * `radius` describes the range to sample.
 * 
 *   Recommendations:
 * 
 *   * `lower` and `upper` should be `radius` below and above the actual
 *  lower and upper bounds. Otherwise the radius will extend off the
 *  number line, creating representations that behave a bit differently
 *  from the rest.
 */
org.numenta.sanity.demos.hotgym.sampling_linear_encoder = (function org$numenta$sanity$demos$hotgym$sampling_linear_encoder(dimensions,n_active,p__71019,radius){
var vec__71021 = p__71019;
var lower = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71021,(0),null);
var upper = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71021,(1),null);
var topo = org.nfrac.comportex.topology.make_topology(dimensions);
return org.numenta.sanity.demos.hotgym.map__GT_SamplingLinearEncoder(new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$topo,topo,cljs.core.cst$kw$n_DASH_active,n_active,cljs.core.cst$kw$lower,lower,cljs.core.cst$kw$upper,upper,cljs.core.cst$kw$radius,radius], null));
});
org.numenta.sanity.demos.hotgym.anomaly_score = (function org$numenta$sanity$demos$hotgym$anomaly_score(p__71022){
var map__71025 = p__71022;
var map__71025__$1 = ((((!((map__71025 == null)))?((((map__71025.cljs$lang$protocol_mask$partition0$ & (64))) || (map__71025.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__71025):map__71025);
var active = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71025__$1,cljs.core.cst$kw$active);
var active_predicted = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71025__$1,cljs.core.cst$kw$active_DASH_predicted);
var total = (active + active_predicted);
if((total > (0))){
return (active / total);
} else {
return (1);
}
});
org.numenta.sanity.demos.hotgym.consider_consumption_BANG_ = (function org$numenta$sanity$demos$hotgym$consider_consumption_BANG_(step__GT_scores,step,consumption){
var candidate = new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$consumption,consumption], null);
var out_c = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var snapshot_id = cljs.core.cst$kw$snapshot_DASH_id.cljs$core$IFn$_invoke$arity$1(step);
cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.main.into_journal,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, ["consider-future",snapshot_id,candidate,org.numenta.sanity.bridge.marshalling.channel.cljs$core$IFn$_invoke$arity$2(out_c,true)], null));

var c__38109__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto__,candidate,out_c,snapshot_id){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto__,candidate,out_c,snapshot_id){
return (function (state_71065){
var state_val_71066 = (state_71065[(1)]);
if((state_val_71066 === (1))){
var state_71065__$1 = state_71065;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_71065__$1,(2),out_c);
} else {
if((state_val_71066 === (2))){
var inst_71054 = (state_71065[(2)]);
var inst_71055 = cljs.core.seq(inst_71054);
var inst_71056 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_71055,(0),null);
var inst_71057 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_71056,(0),null);
var inst_71058 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_71056,(1),null);
var inst_71059 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_71060 = [step,consumption];
var inst_71061 = (new cljs.core.PersistentVector(null,2,(5),inst_71059,inst_71060,null));
var inst_71062 = org.numenta.sanity.demos.hotgym.anomaly_score(inst_71058);
var inst_71063 = cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(step__GT_scores,cljs.core.assoc_in,inst_71061,inst_71062);
var state_71065__$1 = (function (){var statearr_71067 = state_71065;
(statearr_71067[(7)] = inst_71057);

return statearr_71067;
})();
return cljs.core.async.impl.ioc_helpers.return_chan(state_71065__$1,inst_71063);
} else {
return null;
}
}
});})(c__38109__auto__,candidate,out_c,snapshot_id))
;
return ((function (switch__37995__auto__,c__38109__auto__,candidate,out_c,snapshot_id){
return (function() {
var org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto____0 = (function (){
var statearr_71071 = [null,null,null,null,null,null,null,null];
(statearr_71071[(0)] = org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto__);

(statearr_71071[(1)] = (1));

return statearr_71071;
});
var org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto____1 = (function (state_71065){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_71065);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e71072){if((e71072 instanceof Object)){
var ex__37999__auto__ = e71072;
var statearr_71073_71075 = state_71065;
(statearr_71073_71075[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_71065);

return cljs.core.cst$kw$recur;
} else {
throw e71072;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__71076 = state_71065;
state_71065 = G__71076;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto__ = function(state_71065){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto____1.call(this,state_71065);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto____0;
org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$hotgym$consider_consumption_BANG__$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto__,candidate,out_c,snapshot_id))
})();
var state__38111__auto__ = (function (){var statearr_71074 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_71074[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto__);

return statearr_71074;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto__,candidate,out_c,snapshot_id))
);

return c__38109__auto__;
});
org.numenta.sanity.demos.hotgym.try_boundaries_QMARK_ = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(true);
org.numenta.sanity.demos.hotgym.try_last_value_QMARK_ = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(true);
org.numenta.sanity.demos.hotgym.n_predictions = reagent.core.atom.cljs$core$IFn$_invoke$arity$1((3));
org.numenta.sanity.demos.hotgym.unit_width = (8);
org.numenta.sanity.demos.hotgym.cx = (org.numenta.sanity.demos.hotgym.unit_width / (2));
org.numenta.sanity.demos.hotgym.max_r = org.numenta.sanity.demos.hotgym.cx;
org.numenta.sanity.demos.hotgym.actual_svg = (function org$numenta$sanity$demos$hotgym$actual_svg(step,top,unit_height){
var actual_consumption = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(step,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$input_DASH_value,cljs.core.cst$kw$consumption], null));
var y_actual = ((top - actual_consumption) * unit_height);
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$rect,new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$x,(0),cljs.core.cst$kw$y,(y_actual - 1.5),cljs.core.cst$kw$width,org.numenta.sanity.demos.hotgym.unit_width,cljs.core.cst$kw$height,(3),cljs.core.cst$kw$fill,"black"], null)], null);
});
org.numenta.sanity.demos.hotgym.prediction_svg = (function org$numenta$sanity$demos$hotgym$prediction_svg(y_scores){
var min_score = cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.min,cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.second,y_scores));
var candidates = cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.first,cljs.core.filter.cljs$core$IFn$_invoke$arity$2(((function (min_score){
return (function (p__71081){
var vec__71082 = p__71081;
var consumption = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71082,(0),null);
var score = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71082,(1),null);
return cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(score,min_score);
});})(min_score))
,y_scores));
var vec__71080 = cljs.core.nth.cljs$core$IFn$_invoke$arity$2(candidates,cljs.core.quot(cljs.core.count(candidates),(2)));
var y = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71080,(0),null);
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$rect,new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$x,(0),cljs.core.cst$kw$y,(y - (1)),cljs.core.cst$kw$width,org.numenta.sanity.demos.hotgym.unit_width,cljs.core.cst$kw$height,(2),cljs.core.cst$kw$fill,"#78B4FB"], null)], null);
});
org.numenta.sanity.demos.hotgym.anomaly_gradient_svg = (function org$numenta$sanity$demos$hotgym$anomaly_gradient_svg(y_scores){
return cljs.core.into.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g], null),(function (){var iter__6925__auto__ = (function org$numenta$sanity$demos$hotgym$anomaly_gradient_svg_$_iter__71101(s__71102){
return (new cljs.core.LazySeq(null,(function (){
var s__71102__$1 = s__71102;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__71102__$1);
if(temp__4657__auto__){
var s__71102__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__71102__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__71102__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__71104 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__71103 = (0);
while(true){
if((i__71103 < size__6924__auto__)){
var vec__71113 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__71103);
var vec__71114 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71113,(0),null);
var y1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71114,(0),null);
var score1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71114,(1),null);
var vec__71115 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71113,(1),null);
var y2 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71115,(0),null);
var score2 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71115,(1),null);
var grad_id = [cljs.core.str(cljs.core.random_uuid())].join('');
cljs.core.chunk_append(b__71104,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$defs,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$linearGradient,new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$id,grad_id,cljs.core.cst$kw$x1,(0),cljs.core.cst$kw$y1,(0),cljs.core.cst$kw$x2,(0),cljs.core.cst$kw$y2,(1)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$stop,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$offset,"0%",cljs.core.cst$kw$stop_DASH_color,"red",cljs.core.cst$kw$stop_DASH_opacity,score1], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$stop,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$offset,"100%",cljs.core.cst$kw$stop_DASH_color,"red",cljs.core.cst$kw$stop_DASH_opacity,score2], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$rect,new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$x,(org.numenta.sanity.demos.hotgym.cx - org.numenta.sanity.demos.hotgym.max_r),cljs.core.cst$kw$y,y1,cljs.core.cst$kw$width,((2) * org.numenta.sanity.demos.hotgym.max_r),cljs.core.cst$kw$height,(y2 - y1),cljs.core.cst$kw$fill,[cljs.core.str("url(#"),cljs.core.str(grad_id),cljs.core.str(")")].join('')], null)], null)], null));

var G__71119 = (i__71103 + (1));
i__71103 = G__71119;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__71104),org$numenta$sanity$demos$hotgym$anomaly_gradient_svg_$_iter__71101(cljs.core.chunk_rest(s__71102__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__71104),null);
}
} else {
var vec__71116 = cljs.core.first(s__71102__$2);
var vec__71117 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71116,(0),null);
var y1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71117,(0),null);
var score1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71117,(1),null);
var vec__71118 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71116,(1),null);
var y2 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71118,(0),null);
var score2 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71118,(1),null);
var grad_id = [cljs.core.str(cljs.core.random_uuid())].join('');
return cljs.core.cons(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$defs,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$linearGradient,new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$id,grad_id,cljs.core.cst$kw$x1,(0),cljs.core.cst$kw$y1,(0),cljs.core.cst$kw$x2,(0),cljs.core.cst$kw$y2,(1)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$stop,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$offset,"0%",cljs.core.cst$kw$stop_DASH_color,"red",cljs.core.cst$kw$stop_DASH_opacity,score1], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$stop,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$offset,"100%",cljs.core.cst$kw$stop_DASH_color,"red",cljs.core.cst$kw$stop_DASH_opacity,score2], null)], null)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$rect,new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$x,(org.numenta.sanity.demos.hotgym.cx - org.numenta.sanity.demos.hotgym.max_r),cljs.core.cst$kw$y,y1,cljs.core.cst$kw$width,((2) * org.numenta.sanity.demos.hotgym.max_r),cljs.core.cst$kw$height,(y2 - y1),cljs.core.cst$kw$fill,[cljs.core.str("url(#"),cljs.core.str(grad_id),cljs.core.str(")")].join('')], null)], null)], null),org$numenta$sanity$demos$hotgym$anomaly_gradient_svg_$_iter__71101(cljs.core.rest(s__71102__$2)));
}
} else {
return null;
}
break;
}
}),null,null));
});
return iter__6925__auto__(cljs.core.partition.cljs$core$IFn$_invoke$arity$3((2),(1),cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.first,y_scores)));
})());
});
org.numenta.sanity.demos.hotgym.anomaly_samples_svg = (function org$numenta$sanity$demos$hotgym$anomaly_samples_svg(ys){
return cljs.core.into.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g], null),(function (){var iter__6925__auto__ = (function org$numenta$sanity$demos$hotgym$anomaly_samples_svg_$_iter__71126(s__71127){
return (new cljs.core.LazySeq(null,(function (){
var s__71127__$1 = s__71127;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__71127__$1);
if(temp__4657__auto__){
var s__71127__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__71127__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__71127__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__71129 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__71128 = (0);
while(true){
if((i__71128 < size__6924__auto__)){
var y = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__71128);
cljs.core.chunk_append(b__71129,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$circle,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$fill,"brown",cljs.core.cst$kw$cx,org.numenta.sanity.demos.hotgym.cx,cljs.core.cst$kw$cy,y,cljs.core.cst$kw$r,1.5], null)], null));

var G__71132 = (i__71128 + (1));
i__71128 = G__71132;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__71129),org$numenta$sanity$demos$hotgym$anomaly_samples_svg_$_iter__71126(cljs.core.chunk_rest(s__71127__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__71129),null);
}
} else {
var y = cljs.core.first(s__71127__$2);
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$circle,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$fill,"brown",cljs.core.cst$kw$cx,org.numenta.sanity.demos.hotgym.cx,cljs.core.cst$kw$cy,y,cljs.core.cst$kw$r,1.5], null)], null),org$numenta$sanity$demos$hotgym$anomaly_samples_svg_$_iter__71126(cljs.core.rest(s__71127__$2)));
}
} else {
return null;
}
break;
}
}),null,null));
});
return iter__6925__auto__(ys);
})());
});
org.numenta.sanity.demos.hotgym.consumption_axis_svg = (function org$numenta$sanity$demos$hotgym$consumption_axis_svg(h,bottom,top){
var label_every = (10);
return cljs.core.into.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g], null),(function (){var iter__6925__auto__ = ((function (label_every){
return (function org$numenta$sanity$demos$hotgym$consumption_axis_svg_$_iter__71139(s__71140){
return (new cljs.core.LazySeq(null,((function (label_every){
return (function (){
var s__71140__$1 = s__71140;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__71140__$1);
if(temp__4657__auto__){
var s__71140__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__71140__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__71140__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__71142 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__71141 = (0);
while(true){
if((i__71141 < size__6924__auto__)){
var i = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__71141);
cljs.core.chunk_append(b__71142,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$text,new cljs.core.PersistentArrayMap(null, 8, [cljs.core.cst$kw$x,(-5),cljs.core.cst$kw$y,(h * ((1) - ((i - bottom) / (top - bottom)))),cljs.core.cst$kw$dy,"0.35em",cljs.core.cst$kw$font_DASH_family,"sans-serif",cljs.core.cst$kw$font_DASH_size,"9px",cljs.core.cst$kw$fill,"rgb(104, 104, 104)",cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$font_DASH_weight,"bold"], null),cljs.core.cst$kw$text_DASH_anchor,"end"], null),[cljs.core.str(i)].join('')], null));

var G__71145 = (i__71141 + (1));
i__71141 = G__71145;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__71142),org$numenta$sanity$demos$hotgym$consumption_axis_svg_$_iter__71139(cljs.core.chunk_rest(s__71140__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__71142),null);
}
} else {
var i = cljs.core.first(s__71140__$2);
return cljs.core.cons(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$text,new cljs.core.PersistentArrayMap(null, 8, [cljs.core.cst$kw$x,(-5),cljs.core.cst$kw$y,(h * ((1) - ((i - bottom) / (top - bottom)))),cljs.core.cst$kw$dy,"0.35em",cljs.core.cst$kw$font_DASH_family,"sans-serif",cljs.core.cst$kw$font_DASH_size,"9px",cljs.core.cst$kw$fill,"rgb(104, 104, 104)",cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$font_DASH_weight,"bold"], null),cljs.core.cst$kw$text_DASH_anchor,"end"], null),[cljs.core.str(i)].join('')], null),org$numenta$sanity$demos$hotgym$consumption_axis_svg_$_iter__71139(cljs.core.rest(s__71140__$2)));
}
} else {
return null;
}
break;
}
});})(label_every))
,null,null));
});})(label_every))
;
return iter__6925__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$3(bottom,top,label_every));
})());
});
org.numenta.sanity.demos.hotgym.extend_past_px = (30);
org.numenta.sanity.demos.hotgym.horizontal_label = (function org$numenta$sanity$demos$hotgym$horizontal_label(x,y,w,transition_QMARK_,contents_above,contents_below){
return cljs.core.into.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$position,"relative"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 8, [cljs.core.cst$kw$position,"absolute",cljs.core.cst$kw$left,x,cljs.core.cst$kw$top,(y - 0.5),cljs.core.cst$kw$width,((w - x) + org.numenta.sanity.demos.hotgym.extend_past_px),cljs.core.cst$kw$transition_DASH_property,(cljs.core.truth_(transition_QMARK_)?"top":"none"),cljs.core.cst$kw$transition_DASH_duration,"0.15s",cljs.core.cst$kw$height,(1),cljs.core.cst$kw$background_DASH_color,"black"], null)], null)], null)], null),(function (){var iter__6925__auto__ = (function org$numenta$sanity$demos$hotgym$horizontal_label_$_iter__71156(s__71157){
return (new cljs.core.LazySeq(null,(function (){
var s__71157__$1 = s__71157;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__71157__$1);
if(temp__4657__auto__){
var s__71157__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__71157__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__71157__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__71159 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__71158 = (0);
while(true){
if((i__71158 < size__6924__auto__)){
var vec__71164 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__71158);
var contents = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71164,(0),null);
var top = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71164,(1),null);
if(cljs.core.truth_(contents)){
cljs.core.chunk_append(b__71159,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 8, [cljs.core.cst$kw$position,"absolute",cljs.core.cst$kw$top,y,cljs.core.cst$kw$transition_DASH_property,(cljs.core.truth_(transition_QMARK_)?"top":"none"),cljs.core.cst$kw$transition_DASH_duration,"0.15s",cljs.core.cst$kw$left,w,cljs.core.cst$kw$font_DASH_family,"sans-serif",cljs.core.cst$kw$font_DASH_size,"9px",cljs.core.cst$kw$font_DASH_weight,"bold"], null)], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$position,"absolute",cljs.core.cst$kw$top,top,cljs.core.cst$kw$transition_DASH_property,"top",cljs.core.cst$kw$transition_DASH_duration,"0.15s",cljs.core.cst$kw$left,(4)], null)], null),contents], null)], null));

var G__71166 = (i__71158 + (1));
i__71158 = G__71166;
continue;
} else {
var G__71167 = (i__71158 + (1));
i__71158 = G__71167;
continue;
}
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__71159),org$numenta$sanity$demos$hotgym$horizontal_label_$_iter__71156(cljs.core.chunk_rest(s__71157__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__71159),null);
}
} else {
var vec__71165 = cljs.core.first(s__71157__$2);
var contents = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71165,(0),null);
var top = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71165,(1),null);
if(cljs.core.truth_(contents)){
return cljs.core.cons(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 8, [cljs.core.cst$kw$position,"absolute",cljs.core.cst$kw$top,y,cljs.core.cst$kw$transition_DASH_property,(cljs.core.truth_(transition_QMARK_)?"top":"none"),cljs.core.cst$kw$transition_DASH_duration,"0.15s",cljs.core.cst$kw$left,w,cljs.core.cst$kw$font_DASH_family,"sans-serif",cljs.core.cst$kw$font_DASH_size,"9px",cljs.core.cst$kw$font_DASH_weight,"bold"], null)], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$position,"absolute",cljs.core.cst$kw$top,top,cljs.core.cst$kw$transition_DASH_property,"top",cljs.core.cst$kw$transition_DASH_duration,"0.15s",cljs.core.cst$kw$left,(4)], null)], null),contents], null)], null),org$numenta$sanity$demos$hotgym$horizontal_label_$_iter__71156(cljs.core.rest(s__71157__$2)));
} else {
var G__71168 = cljs.core.rest(s__71157__$2);
s__71157__$1 = G__71168;
continue;
}
}
} else {
return null;
}
break;
}
}),null,null));
});
return iter__6925__auto__(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [contents_above,"-2.7em"], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [contents_below,"0.2em"], null)], null));
})());
});
org.numenta.sanity.demos.hotgym.y__GT_consumption = (function org$numenta$sanity$demos$hotgym$y__GT_consumption(y,h,top,bottom){
return ((((1) - (y / h)) * (top - bottom)) + bottom);
});
org.numenta.sanity.demos.hotgym.consumption__GT_y = (function org$numenta$sanity$demos$hotgym$consumption__GT_y(consumption,top,unit_height){
return ((top - consumption) * unit_height);
});
org.numenta.sanity.demos.hotgym.anomaly_radar_pane = (function org$numenta$sanity$demos$hotgym$anomaly_radar_pane(){
var step__GT_scores = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(cljs.core.PersistentArrayMap.EMPTY);
var hover_i = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
var hover_y = reagent.core.atom.cljs$core$IFn$_invoke$arity$1(null);
cljs.core.add_watch(org.numenta.sanity.main.steps,cljs.core.cst$kw$org$numenta$sanity$demos$hotgym_SLASH_fetch_DASH_anomaly_DASH_radar,((function (step__GT_scores,hover_i,hover_y){
return (function (_,___$1,___$2,steps_v){
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(step__GT_scores,cljs.core.select_keys,steps_v);

var seq__71383 = cljs.core.seq(cljs.core.remove.cljs$core$IFn$_invoke$arity$2(cljs.core.partial.cljs$core$IFn$_invoke$arity$2(cljs.core.contains_QMARK_,(cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(step__GT_scores) : cljs.core.deref.call(null,step__GT_scores))),steps_v));
var chunk__71385 = null;
var count__71386 = (0);
var i__71387 = (0);
while(true){
if((i__71387 < count__71386)){
var step = chunk__71385.cljs$core$IIndexed$_nth$arity$2(null,i__71387);
var out_c_71597 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var snapshot_id_71598 = cljs.core.cst$kw$snapshot_DASH_id.cljs$core$IFn$_invoke$arity$1(step);
cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.main.into_journal,new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, ["decode-predictive-columns",snapshot_id_71598,cljs.core.cst$kw$power_DASH_consumption,(cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.hotgym.n_predictions) : cljs.core.deref.call(null,org.numenta.sanity.demos.hotgym.n_predictions)),org.numenta.sanity.bridge.marshalling.channel.cljs$core$IFn$_invoke$arity$2(out_c_71597,true)], null));

if(cljs.core.truth_((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.hotgym.try_boundaries_QMARK_) : cljs.core.deref.call(null,org.numenta.sanity.demos.hotgym.try_boundaries_QMARK_)))){
org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,(-10));

org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,(110));
} else {
}

if(cljs.core.truth_((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.hotgym.try_last_value_QMARK_) : cljs.core.deref.call(null,org.numenta.sanity.demos.hotgym.try_last_value_QMARK_)))){
org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(step,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$input_DASH_value,cljs.core.cst$kw$consumption], null)));
} else {
}

var c__38109__auto___71599 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (seq__71383,chunk__71385,count__71386,i__71387,c__38109__auto___71599,out_c_71597,snapshot_id_71598,step,step__GT_scores,hover_i,hover_y){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (seq__71383,chunk__71385,count__71386,i__71387,c__38109__auto___71599,out_c_71597,snapshot_id_71598,step,step__GT_scores,hover_i,hover_y){
return (function (state_71433){
var state_val_71434 = (state_71433[(1)]);
if((state_val_71434 === (7))){
var inst_71429 = (state_71433[(2)]);
var state_71433__$1 = state_71433;
var statearr_71435_71600 = state_71433__$1;
(statearr_71435_71600[(2)] = inst_71429);

(statearr_71435_71600[(1)] = (4));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (1))){
var state_71433__$1 = state_71433;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_71433__$1,(2),out_c_71597);
} else {
if((state_val_71434 === (4))){
var inst_71431 = (state_71433[(2)]);
var state_71433__$1 = state_71433;
return cljs.core.async.impl.ioc_helpers.return_chan(state_71433__$1,inst_71431);
} else {
if((state_val_71434 === (13))){
var inst_71424 = (state_71433[(2)]);
var state_71433__$1 = state_71433;
var statearr_71436_71601 = state_71433__$1;
(statearr_71436_71601[(2)] = inst_71424);

(statearr_71436_71601[(1)] = (10));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (6))){
var inst_71397 = (state_71433[(7)]);
var inst_71410 = (state_71433[(8)]);
var inst_71410__$1 = cljs.core.seq(inst_71397);
var state_71433__$1 = (function (){var statearr_71437 = state_71433;
(statearr_71437[(8)] = inst_71410__$1);

return statearr_71437;
})();
if(inst_71410__$1){
var statearr_71438_71602 = state_71433__$1;
(statearr_71438_71602[(1)] = (8));

} else {
var statearr_71439_71603 = state_71433__$1;
(statearr_71439_71603[(1)] = (9));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (3))){
var inst_71400 = (state_71433[(9)]);
var inst_71399 = (state_71433[(10)]);
var inst_71402 = (inst_71400 < inst_71399);
var inst_71403 = inst_71402;
var state_71433__$1 = state_71433;
if(cljs.core.truth_(inst_71403)){
var statearr_71440_71604 = state_71433__$1;
(statearr_71440_71604[(1)] = (5));

} else {
var statearr_71441_71605 = state_71433__$1;
(statearr_71441_71605[(1)] = (6));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (12))){
var inst_71410 = (state_71433[(8)]);
var inst_71419 = cljs.core.first(inst_71410);
var inst_71420 = org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,inst_71419);
var inst_71421 = cljs.core.next(inst_71410);
var inst_71397 = inst_71421;
var inst_71398 = null;
var inst_71399 = (0);
var inst_71400 = (0);
var state_71433__$1 = (function (){var statearr_71442 = state_71433;
(statearr_71442[(7)] = inst_71397);

(statearr_71442[(9)] = inst_71400);

(statearr_71442[(11)] = inst_71420);

(statearr_71442[(12)] = inst_71398);

(statearr_71442[(10)] = inst_71399);

return statearr_71442;
})();
var statearr_71443_71606 = state_71433__$1;
(statearr_71443_71606[(2)] = null);

(statearr_71443_71606[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (2))){
var inst_71394 = (state_71433[(2)]);
var inst_71395 = cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$value,inst_71394);
var inst_71396 = cljs.core.seq(inst_71395);
var inst_71397 = inst_71396;
var inst_71398 = null;
var inst_71399 = (0);
var inst_71400 = (0);
var state_71433__$1 = (function (){var statearr_71444 = state_71433;
(statearr_71444[(7)] = inst_71397);

(statearr_71444[(9)] = inst_71400);

(statearr_71444[(12)] = inst_71398);

(statearr_71444[(10)] = inst_71399);

return statearr_71444;
})();
var statearr_71445_71607 = state_71433__$1;
(statearr_71445_71607[(2)] = null);

(statearr_71445_71607[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (11))){
var inst_71410 = (state_71433[(8)]);
var inst_71414 = cljs.core.chunk_first(inst_71410);
var inst_71415 = cljs.core.chunk_rest(inst_71410);
var inst_71416 = cljs.core.count(inst_71414);
var inst_71397 = inst_71415;
var inst_71398 = inst_71414;
var inst_71399 = inst_71416;
var inst_71400 = (0);
var state_71433__$1 = (function (){var statearr_71449 = state_71433;
(statearr_71449[(7)] = inst_71397);

(statearr_71449[(9)] = inst_71400);

(statearr_71449[(12)] = inst_71398);

(statearr_71449[(10)] = inst_71399);

return statearr_71449;
})();
var statearr_71450_71608 = state_71433__$1;
(statearr_71450_71608[(2)] = null);

(statearr_71450_71608[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (9))){
var state_71433__$1 = state_71433;
var statearr_71451_71609 = state_71433__$1;
(statearr_71451_71609[(2)] = null);

(statearr_71451_71609[(1)] = (10));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (5))){
var inst_71397 = (state_71433[(7)]);
var inst_71400 = (state_71433[(9)]);
var inst_71398 = (state_71433[(12)]);
var inst_71399 = (state_71433[(10)]);
var inst_71405 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(inst_71398,inst_71400);
var inst_71406 = org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,inst_71405);
var inst_71407 = (inst_71400 + (1));
var tmp71446 = inst_71397;
var tmp71447 = inst_71398;
var tmp71448 = inst_71399;
var inst_71397__$1 = tmp71446;
var inst_71398__$1 = tmp71447;
var inst_71399__$1 = tmp71448;
var inst_71400__$1 = inst_71407;
var state_71433__$1 = (function (){var statearr_71452 = state_71433;
(statearr_71452[(13)] = inst_71406);

(statearr_71452[(7)] = inst_71397__$1);

(statearr_71452[(9)] = inst_71400__$1);

(statearr_71452[(12)] = inst_71398__$1);

(statearr_71452[(10)] = inst_71399__$1);

return statearr_71452;
})();
var statearr_71453_71610 = state_71433__$1;
(statearr_71453_71610[(2)] = null);

(statearr_71453_71610[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (10))){
var inst_71427 = (state_71433[(2)]);
var state_71433__$1 = state_71433;
var statearr_71454_71611 = state_71433__$1;
(statearr_71454_71611[(2)] = inst_71427);

(statearr_71454_71611[(1)] = (7));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71434 === (8))){
var inst_71410 = (state_71433[(8)]);
var inst_71412 = cljs.core.chunked_seq_QMARK_(inst_71410);
var state_71433__$1 = state_71433;
if(inst_71412){
var statearr_71455_71612 = state_71433__$1;
(statearr_71455_71612[(1)] = (11));

} else {
var statearr_71456_71613 = state_71433__$1;
(statearr_71456_71613[(1)] = (12));

}

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
}
}
}
});})(seq__71383,chunk__71385,count__71386,i__71387,c__38109__auto___71599,out_c_71597,snapshot_id_71598,step,step__GT_scores,hover_i,hover_y))
;
return ((function (seq__71383,chunk__71385,count__71386,i__71387,switch__37995__auto__,c__38109__auto___71599,out_c_71597,snapshot_id_71598,step,step__GT_scores,hover_i,hover_y){
return (function() {
var org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____0 = (function (){
var statearr_71460 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_71460[(0)] = org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__);

(statearr_71460[(1)] = (1));

return statearr_71460;
});
var org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____1 = (function (state_71433){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_71433);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e71461){if((e71461 instanceof Object)){
var ex__37999__auto__ = e71461;
var statearr_71462_71614 = state_71433;
(statearr_71462_71614[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_71433);

return cljs.core.cst$kw$recur;
} else {
throw e71461;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__71615 = state_71433;
state_71433 = G__71615;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__ = function(state_71433){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____1.call(this,state_71433);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____0;
org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__;
})()
;})(seq__71383,chunk__71385,count__71386,i__71387,switch__37995__auto__,c__38109__auto___71599,out_c_71597,snapshot_id_71598,step,step__GT_scores,hover_i,hover_y))
})();
var state__38111__auto__ = (function (){var statearr_71463 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_71463[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto___71599);

return statearr_71463;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(seq__71383,chunk__71385,count__71386,i__71387,c__38109__auto___71599,out_c_71597,snapshot_id_71598,step,step__GT_scores,hover_i,hover_y))
);


var G__71616 = seq__71383;
var G__71617 = chunk__71385;
var G__71618 = count__71386;
var G__71619 = (i__71387 + (1));
seq__71383 = G__71616;
chunk__71385 = G__71617;
count__71386 = G__71618;
i__71387 = G__71619;
continue;
} else {
var temp__4657__auto__ = cljs.core.seq(seq__71383);
if(temp__4657__auto__){
var seq__71383__$1 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__71383__$1)){
var c__6956__auto__ = cljs.core.chunk_first(seq__71383__$1);
var G__71620 = cljs.core.chunk_rest(seq__71383__$1);
var G__71621 = c__6956__auto__;
var G__71622 = cljs.core.count(c__6956__auto__);
var G__71623 = (0);
seq__71383 = G__71620;
chunk__71385 = G__71621;
count__71386 = G__71622;
i__71387 = G__71623;
continue;
} else {
var step = cljs.core.first(seq__71383__$1);
var out_c_71624 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var snapshot_id_71625 = cljs.core.cst$kw$snapshot_DASH_id.cljs$core$IFn$_invoke$arity$1(step);
cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(org.numenta.sanity.main.into_journal,new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, ["decode-predictive-columns",snapshot_id_71625,cljs.core.cst$kw$power_DASH_consumption,(cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.hotgym.n_predictions) : cljs.core.deref.call(null,org.numenta.sanity.demos.hotgym.n_predictions)),org.numenta.sanity.bridge.marshalling.channel.cljs$core$IFn$_invoke$arity$2(out_c_71624,true)], null));

if(cljs.core.truth_((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.hotgym.try_boundaries_QMARK_) : cljs.core.deref.call(null,org.numenta.sanity.demos.hotgym.try_boundaries_QMARK_)))){
org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,(-10));

org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,(110));
} else {
}

if(cljs.core.truth_((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.hotgym.try_last_value_QMARK_) : cljs.core.deref.call(null,org.numenta.sanity.demos.hotgym.try_last_value_QMARK_)))){
org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(step,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$input_DASH_value,cljs.core.cst$kw$consumption], null)));
} else {
}

var c__38109__auto___71626 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (seq__71383,chunk__71385,count__71386,i__71387,c__38109__auto___71626,out_c_71624,snapshot_id_71625,step,seq__71383__$1,temp__4657__auto__,step__GT_scores,hover_i,hover_y){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (seq__71383,chunk__71385,count__71386,i__71387,c__38109__auto___71626,out_c_71624,snapshot_id_71625,step,seq__71383__$1,temp__4657__auto__,step__GT_scores,hover_i,hover_y){
return (function (state_71508){
var state_val_71509 = (state_71508[(1)]);
if((state_val_71509 === (7))){
var inst_71504 = (state_71508[(2)]);
var state_71508__$1 = state_71508;
var statearr_71510_71627 = state_71508__$1;
(statearr_71510_71627[(2)] = inst_71504);

(statearr_71510_71627[(1)] = (4));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (1))){
var state_71508__$1 = state_71508;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_71508__$1,(2),out_c_71624);
} else {
if((state_val_71509 === (4))){
var inst_71506 = (state_71508[(2)]);
var state_71508__$1 = state_71508;
return cljs.core.async.impl.ioc_helpers.return_chan(state_71508__$1,inst_71506);
} else {
if((state_val_71509 === (13))){
var inst_71499 = (state_71508[(2)]);
var state_71508__$1 = state_71508;
var statearr_71511_71628 = state_71508__$1;
(statearr_71511_71628[(2)] = inst_71499);

(statearr_71511_71628[(1)] = (10));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (6))){
var inst_71485 = (state_71508[(7)]);
var inst_71472 = (state_71508[(8)]);
var inst_71485__$1 = cljs.core.seq(inst_71472);
var state_71508__$1 = (function (){var statearr_71512 = state_71508;
(statearr_71512[(7)] = inst_71485__$1);

return statearr_71512;
})();
if(inst_71485__$1){
var statearr_71513_71629 = state_71508__$1;
(statearr_71513_71629[(1)] = (8));

} else {
var statearr_71514_71630 = state_71508__$1;
(statearr_71514_71630[(1)] = (9));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (3))){
var inst_71474 = (state_71508[(9)]);
var inst_71475 = (state_71508[(10)]);
var inst_71477 = (inst_71475 < inst_71474);
var inst_71478 = inst_71477;
var state_71508__$1 = state_71508;
if(cljs.core.truth_(inst_71478)){
var statearr_71515_71631 = state_71508__$1;
(statearr_71515_71631[(1)] = (5));

} else {
var statearr_71516_71632 = state_71508__$1;
(statearr_71516_71632[(1)] = (6));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (12))){
var inst_71485 = (state_71508[(7)]);
var inst_71494 = cljs.core.first(inst_71485);
var inst_71495 = org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,inst_71494);
var inst_71496 = cljs.core.next(inst_71485);
var inst_71472 = inst_71496;
var inst_71473 = null;
var inst_71474 = (0);
var inst_71475 = (0);
var state_71508__$1 = (function (){var statearr_71517 = state_71508;
(statearr_71517[(11)] = inst_71473);

(statearr_71517[(9)] = inst_71474);

(statearr_71517[(8)] = inst_71472);

(statearr_71517[(10)] = inst_71475);

(statearr_71517[(12)] = inst_71495);

return statearr_71517;
})();
var statearr_71518_71633 = state_71508__$1;
(statearr_71518_71633[(2)] = null);

(statearr_71518_71633[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (2))){
var inst_71469 = (state_71508[(2)]);
var inst_71470 = cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$value,inst_71469);
var inst_71471 = cljs.core.seq(inst_71470);
var inst_71472 = inst_71471;
var inst_71473 = null;
var inst_71474 = (0);
var inst_71475 = (0);
var state_71508__$1 = (function (){var statearr_71519 = state_71508;
(statearr_71519[(11)] = inst_71473);

(statearr_71519[(9)] = inst_71474);

(statearr_71519[(8)] = inst_71472);

(statearr_71519[(10)] = inst_71475);

return statearr_71519;
})();
var statearr_71520_71634 = state_71508__$1;
(statearr_71520_71634[(2)] = null);

(statearr_71520_71634[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (11))){
var inst_71485 = (state_71508[(7)]);
var inst_71489 = cljs.core.chunk_first(inst_71485);
var inst_71490 = cljs.core.chunk_rest(inst_71485);
var inst_71491 = cljs.core.count(inst_71489);
var inst_71472 = inst_71490;
var inst_71473 = inst_71489;
var inst_71474 = inst_71491;
var inst_71475 = (0);
var state_71508__$1 = (function (){var statearr_71524 = state_71508;
(statearr_71524[(11)] = inst_71473);

(statearr_71524[(9)] = inst_71474);

(statearr_71524[(8)] = inst_71472);

(statearr_71524[(10)] = inst_71475);

return statearr_71524;
})();
var statearr_71525_71635 = state_71508__$1;
(statearr_71525_71635[(2)] = null);

(statearr_71525_71635[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (9))){
var state_71508__$1 = state_71508;
var statearr_71526_71636 = state_71508__$1;
(statearr_71526_71636[(2)] = null);

(statearr_71526_71636[(1)] = (10));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (5))){
var inst_71473 = (state_71508[(11)]);
var inst_71474 = (state_71508[(9)]);
var inst_71472 = (state_71508[(8)]);
var inst_71475 = (state_71508[(10)]);
var inst_71480 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(inst_71473,inst_71475);
var inst_71481 = org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,step,inst_71480);
var inst_71482 = (inst_71475 + (1));
var tmp71521 = inst_71473;
var tmp71522 = inst_71474;
var tmp71523 = inst_71472;
var inst_71472__$1 = tmp71523;
var inst_71473__$1 = tmp71521;
var inst_71474__$1 = tmp71522;
var inst_71475__$1 = inst_71482;
var state_71508__$1 = (function (){var statearr_71527 = state_71508;
(statearr_71527[(11)] = inst_71473__$1);

(statearr_71527[(13)] = inst_71481);

(statearr_71527[(9)] = inst_71474__$1);

(statearr_71527[(8)] = inst_71472__$1);

(statearr_71527[(10)] = inst_71475__$1);

return statearr_71527;
})();
var statearr_71528_71637 = state_71508__$1;
(statearr_71528_71637[(2)] = null);

(statearr_71528_71637[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (10))){
var inst_71502 = (state_71508[(2)]);
var state_71508__$1 = state_71508;
var statearr_71529_71638 = state_71508__$1;
(statearr_71529_71638[(2)] = inst_71502);

(statearr_71529_71638[(1)] = (7));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71509 === (8))){
var inst_71485 = (state_71508[(7)]);
var inst_71487 = cljs.core.chunked_seq_QMARK_(inst_71485);
var state_71508__$1 = state_71508;
if(inst_71487){
var statearr_71530_71639 = state_71508__$1;
(statearr_71530_71639[(1)] = (11));

} else {
var statearr_71531_71640 = state_71508__$1;
(statearr_71531_71640[(1)] = (12));

}

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
}
}
}
});})(seq__71383,chunk__71385,count__71386,i__71387,c__38109__auto___71626,out_c_71624,snapshot_id_71625,step,seq__71383__$1,temp__4657__auto__,step__GT_scores,hover_i,hover_y))
;
return ((function (seq__71383,chunk__71385,count__71386,i__71387,switch__37995__auto__,c__38109__auto___71626,out_c_71624,snapshot_id_71625,step,seq__71383__$1,temp__4657__auto__,step__GT_scores,hover_i,hover_y){
return (function() {
var org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__ = null;
var org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____0 = (function (){
var statearr_71535 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_71535[(0)] = org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__);

(statearr_71535[(1)] = (1));

return statearr_71535;
});
var org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____1 = (function (state_71508){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_71508);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e71536){if((e71536 instanceof Object)){
var ex__37999__auto__ = e71536;
var statearr_71537_71641 = state_71508;
(statearr_71537_71641[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_71508);

return cljs.core.cst$kw$recur;
} else {
throw e71536;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__71642 = state_71508;
state_71508 = G__71642;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__ = function(state_71508){
switch(arguments.length){
case 0:
return org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____1.call(this,state_71508);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____0;
org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto____1;
return org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_state_machine__37996__auto__;
})()
;})(seq__71383,chunk__71385,count__71386,i__71387,switch__37995__auto__,c__38109__auto___71626,out_c_71624,snapshot_id_71625,step,seq__71383__$1,temp__4657__auto__,step__GT_scores,hover_i,hover_y))
})();
var state__38111__auto__ = (function (){var statearr_71538 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_71538[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto___71626);

return statearr_71538;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(seq__71383,chunk__71385,count__71386,i__71387,c__38109__auto___71626,out_c_71624,snapshot_id_71625,step,seq__71383__$1,temp__4657__auto__,step__GT_scores,hover_i,hover_y))
);


var G__71643 = cljs.core.next(seq__71383__$1);
var G__71644 = null;
var G__71645 = (0);
var G__71646 = (0);
seq__71383 = G__71643;
chunk__71385 = G__71644;
count__71386 = G__71645;
i__71387 = G__71646;
continue;
}
} else {
return null;
}
}
break;
}
});})(step__GT_scores,hover_i,hover_y))
);

return ((function (step__GT_scores,hover_i,hover_y){
return (function (){
var h = (400);
var draw_steps = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.viz_options) : cljs.core.deref.call(null,org.numenta.sanity.main.viz_options)),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$drawing,cljs.core.cst$kw$draw_DASH_steps], null));
var w = (org.numenta.sanity.demos.hotgym.unit_width * draw_steps);
var h_pad_top = (15);
var h_pad_bottom = (8);
var w_pad_left = (20);
var w_pad_right = (42);
var top = (110);
var bottom = (-10);
var unit_height = (h / (top - bottom));
var label_every = (10);
var center_dt = cljs.core.cst$kw$dt.cljs$core$IFn$_invoke$arity$1(cljs.core.peek((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.selection) : cljs.core.deref.call(null,org.numenta.sanity.main.selection))));
var dt0 = (function (){var x__6484__auto__ = (-1);
var y__6485__auto__ = (center_dt - cljs.core.quot(draw_steps,(2)));
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})();
var center_i = (center_dt - dt0);
var draw_dts = cljs.core.range.cljs$core$IFn$_invoke$arity$2(dt0,(function (){var x__6491__auto__ = (dt0 + draw_steps);
var y__6492__auto__ = cljs.core.count((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps)));
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})());
return new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$position,"relative",cljs.core.cst$kw$width,((w_pad_left + w) + w_pad_right)], null)], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 6, [cljs.core.cst$kw$position,"absolute",cljs.core.cst$kw$top,(0),cljs.core.cst$kw$left,(0),cljs.core.cst$kw$font_DASH_family,"sans-serif",cljs.core.cst$kw$font_DASH_size,"9px",cljs.core.cst$kw$font_DASH_weight,"bold"], null)], null),"power-consumption"], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$svg,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$height,((h + h_pad_top) + h_pad_bottom),cljs.core.cst$kw$width,((w + w_pad_left) + w_pad_right)], null),new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$transform,[cljs.core.str("translate("),cljs.core.str(w_pad_left),cljs.core.str(","),cljs.core.str(h_pad_top),cljs.core.str(")")].join('')], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.consumption_axis_svg,h,bottom,top], null),cljs.core.into.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g], null),(function (){var iter__6925__auto__ = ((function (h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539(s__71540){
return (new cljs.core.LazySeq(null,((function (h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (){
var s__71540__$1 = s__71540;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__71540__$1);
if(temp__4657__auto__){
var s__71540__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__71540__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__71540__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__71542 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__71541 = (0);
while(true){
if((i__71541 < size__6924__auto__)){
var i = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__71541);
var dt = cljs.core.nth.cljs$core$IFn$_invoke$arity$2(draw_dts,i);
var from_step = cljs.core.nth.cljs$core$IFn$_invoke$arity$3((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps)),(dt + (1)),null);
var y_scores = (cljs.core.truth_(from_step)?(function (){var iter__6925__auto__ = ((function (i__71541,dt,from_step,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539_$_iter__71567(s__71568){
return (new cljs.core.LazySeq(null,((function (i__71541,dt,from_step,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (){
var s__71568__$1 = s__71568;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__71568__$1);
if(temp__4657__auto____$1){
var s__71568__$2 = temp__4657__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__71568__$2)){
var c__6923__auto____$1 = cljs.core.chunk_first(s__71568__$2);
var size__6924__auto____$1 = cljs.core.count(c__6923__auto____$1);
var b__71570 = cljs.core.chunk_buffer(size__6924__auto____$1);
if((function (){var i__71569 = (0);
while(true){
if((i__71569 < size__6924__auto____$1)){
var vec__71575 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto____$1,i__71569);
var consumption = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71575,(0),null);
var score = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71575,(1),null);
cljs.core.chunk_append(b__71570,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.consumption__GT_y(consumption,top,unit_height),score], null));

var G__71647 = (i__71569 + (1));
i__71569 = G__71647;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__71570),org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539_$_iter__71567(cljs.core.chunk_rest(s__71568__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__71570),null);
}
} else {
var vec__71576 = cljs.core.first(s__71568__$2);
var consumption = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71576,(0),null);
var score = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71576,(1),null);
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.consumption__GT_y(consumption,top,unit_height),score], null),org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539_$_iter__71567(cljs.core.rest(s__71568__$2)));
}
} else {
return null;
}
break;
}
});})(i__71541,dt,from_step,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
,null,null));
});})(i__71541,dt,from_step,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
;
return iter__6925__auto__(cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.first,cljs.core.get.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(step__GT_scores) : cljs.core.deref.call(null,step__GT_scores)),from_step)));
})():null);
cljs.core.chunk_append(b__71542,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$transform,[cljs.core.str("translate("),cljs.core.str((org.numenta.sanity.demos.hotgym.unit_width * ((draw_steps - (1)) - i))),cljs.core.str(",0)")].join('')], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$rect,(function (){var G__71577 = new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$x,(0),cljs.core.cst$kw$y,(0),cljs.core.cst$kw$width,org.numenta.sanity.demos.hotgym.unit_width,cljs.core.cst$kw$height,h,cljs.core.cst$kw$fill,"white"], null);
if(cljs.core.truth_(from_step)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$variadic(G__71577,cljs.core.cst$kw$on_DASH_click,((function (i__71541,G__71577,dt,from_step,y_scores,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (e){
var y = (e.clientY - e.target.getBoundingClientRect().top);
return org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,from_step,org.numenta.sanity.demos.hotgym.y__GT_consumption(y,h,top,bottom));
});})(i__71541,G__71577,dt,from_step,y_scores,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
,cljs.core.array_seq([cljs.core.cst$kw$on_DASH_mouse_DASH_move,((function (i__71541,G__71577,dt,from_step,y_scores,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (e){
var y = (e.clientY - e.target.getBoundingClientRect().top);
(cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(hover_i,i) : cljs.core.reset_BANG_.call(null,hover_i,i));

return (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(hover_y,y) : cljs.core.reset_BANG_.call(null,hover_y,y));
});})(i__71541,G__71577,dt,from_step,y_scores,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
,cljs.core.cst$kw$on_DASH_mouse_DASH_leave,((function (i__71541,G__71577,dt,from_step,y_scores,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (e){
(cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(hover_i,null) : cljs.core.reset_BANG_.call(null,hover_i,null));

return (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(hover_y,null) : cljs.core.reset_BANG_.call(null,hover_y,null));
});})(i__71541,G__71577,dt,from_step,y_scores,i,c__6923__auto__,size__6924__auto__,b__71542,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
], 0));
} else {
return G__71577;
}
})()], null),new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$pointer_DASH_events,"none"], null)], null),(cljs.core.truth_(cljs.core.not_empty(y_scores))?new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.anomaly_gradient_svg,y_scores], null):null),(cljs.core.truth_(cljs.core.not_empty(y_scores))?new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.anomaly_samples_svg,cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.first,y_scores)], null):null),(((((0) <= dt)) && ((dt < cljs.core.count((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps))))))?new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.actual_svg,cljs.core.nth.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps)),dt),top,unit_height], null):null),(cljs.core.truth_(cljs.core.not_empty(y_scores))?new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.prediction_svg,y_scores], null):null)], null)], null));

var G__71648 = (i__71541 + (1));
i__71541 = G__71648;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__71542),org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539(cljs.core.chunk_rest(s__71540__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__71542),null);
}
} else {
var i = cljs.core.first(s__71540__$2);
var dt = cljs.core.nth.cljs$core$IFn$_invoke$arity$2(draw_dts,i);
var from_step = cljs.core.nth.cljs$core$IFn$_invoke$arity$3((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps)),(dt + (1)),null);
var y_scores = (cljs.core.truth_(from_step)?(function (){var iter__6925__auto__ = ((function (dt,from_step,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539_$_iter__71578(s__71579){
return (new cljs.core.LazySeq(null,((function (dt,from_step,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (){
var s__71579__$1 = s__71579;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__71579__$1);
if(temp__4657__auto____$1){
var s__71579__$2 = temp__4657__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__71579__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__71579__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__71581 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__71580 = (0);
while(true){
if((i__71580 < size__6924__auto__)){
var vec__71586 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__71580);
var consumption = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71586,(0),null);
var score = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71586,(1),null);
cljs.core.chunk_append(b__71581,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.consumption__GT_y(consumption,top,unit_height),score], null));

var G__71649 = (i__71580 + (1));
i__71580 = G__71649;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__71581),org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539_$_iter__71578(cljs.core.chunk_rest(s__71579__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__71581),null);
}
} else {
var vec__71587 = cljs.core.first(s__71579__$2);
var consumption = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71587,(0),null);
var score = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71587,(1),null);
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.consumption__GT_y(consumption,top,unit_height),score], null),org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539_$_iter__71578(cljs.core.rest(s__71579__$2)));
}
} else {
return null;
}
break;
}
});})(dt,from_step,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
,null,null));
});})(dt,from_step,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
;
return iter__6925__auto__(cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.first,cljs.core.get.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(step__GT_scores) : cljs.core.deref.call(null,step__GT_scores)),from_step)));
})():null);
return cljs.core.cons(new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$transform,[cljs.core.str("translate("),cljs.core.str((org.numenta.sanity.demos.hotgym.unit_width * ((draw_steps - (1)) - i))),cljs.core.str(",0)")].join('')], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$rect,(function (){var G__71588 = new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$x,(0),cljs.core.cst$kw$y,(0),cljs.core.cst$kw$width,org.numenta.sanity.demos.hotgym.unit_width,cljs.core.cst$kw$height,h,cljs.core.cst$kw$fill,"white"], null);
if(cljs.core.truth_(from_step)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$variadic(G__71588,cljs.core.cst$kw$on_DASH_click,((function (G__71588,dt,from_step,y_scores,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (e){
var y = (e.clientY - e.target.getBoundingClientRect().top);
return org.numenta.sanity.demos.hotgym.consider_consumption_BANG_(step__GT_scores,from_step,org.numenta.sanity.demos.hotgym.y__GT_consumption(y,h,top,bottom));
});})(G__71588,dt,from_step,y_scores,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
,cljs.core.array_seq([cljs.core.cst$kw$on_DASH_mouse_DASH_move,((function (G__71588,dt,from_step,y_scores,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (e){
var y = (e.clientY - e.target.getBoundingClientRect().top);
(cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(hover_i,i) : cljs.core.reset_BANG_.call(null,hover_i,i));

return (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(hover_y,y) : cljs.core.reset_BANG_.call(null,hover_y,y));
});})(G__71588,dt,from_step,y_scores,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
,cljs.core.cst$kw$on_DASH_mouse_DASH_leave,((function (G__71588,dt,from_step,y_scores,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (e){
(cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(hover_i,null) : cljs.core.reset_BANG_.call(null,hover_i,null));

return (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(hover_y,null) : cljs.core.reset_BANG_.call(null,hover_y,null));
});})(G__71588,dt,from_step,y_scores,i,s__71540__$2,temp__4657__auto__,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
], 0));
} else {
return G__71588;
}
})()], null),new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$pointer_DASH_events,"none"], null)], null),(cljs.core.truth_(cljs.core.not_empty(y_scores))?new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.anomaly_gradient_svg,y_scores], null):null),(cljs.core.truth_(cljs.core.not_empty(y_scores))?new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.anomaly_samples_svg,cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.first,y_scores)], null):null),(((((0) <= dt)) && ((dt < cljs.core.count((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps))))))?new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.actual_svg,cljs.core.nth.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps)),dt),top,unit_height], null):null),(cljs.core.truth_(cljs.core.not_empty(y_scores))?new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.prediction_svg,y_scores], null):null)], null)], null),org$numenta$sanity$demos$hotgym$anomaly_radar_pane_$_iter__71539(cljs.core.rest(s__71540__$2)));
}
} else {
return null;
}
break;
}
});})(h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
,null,null));
});})(h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
;
return iter__6925__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$1(cljs.core.count(draw_dts)));
})()),(function (){var x = (org.numenta.sanity.demos.hotgym.unit_width * ((draw_steps - (1)) - center_i));
var points = [cljs.core.str(x),cljs.core.str(","),cljs.core.str((0)),cljs.core.str(" "),cljs.core.str(x),cljs.core.str(","),cljs.core.str((-1)),cljs.core.str(" "),cljs.core.str((x + org.numenta.sanity.demos.hotgym.unit_width)),cljs.core.str(","),cljs.core.str((-1)),cljs.core.str(" "),cljs.core.str((x + org.numenta.sanity.demos.hotgym.unit_width)),cljs.core.str(","),cljs.core.str((0))].join('');
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,(function (){var points__$1 = [cljs.core.str(x),cljs.core.str(","),cljs.core.str((0)),cljs.core.str(" "),cljs.core.str(x),cljs.core.str(","),cljs.core.str((-1)),cljs.core.str(" "),cljs.core.str((x + org.numenta.sanity.demos.hotgym.unit_width)),cljs.core.str(","),cljs.core.str((-1)),cljs.core.str(" "),cljs.core.str((x + org.numenta.sanity.demos.hotgym.unit_width)),cljs.core.str(","),cljs.core.str((0))].join('');
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$polyline,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$stroke,cljs.core.cst$kw$highlight.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.viz_canvas.state_colors),cljs.core.cst$kw$stroke_DASH_width,(3),cljs.core.cst$kw$fill,"none",cljs.core.cst$kw$points,points__$1], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$polyline,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$stroke,"black",cljs.core.cst$kw$stroke_DASH_width,0.75,cljs.core.cst$kw$fill,"none",cljs.core.cst$kw$points,points__$1], null)], null)], null);
})(),(function (){var points__$1 = [cljs.core.str(x),cljs.core.str(","),cljs.core.str(h),cljs.core.str(" "),cljs.core.str(x),cljs.core.str(","),cljs.core.str((h + (6))),cljs.core.str(" "),cljs.core.str((x + org.numenta.sanity.demos.hotgym.unit_width)),cljs.core.str(","),cljs.core.str((h + (6))),cljs.core.str(" "),cljs.core.str((x + org.numenta.sanity.demos.hotgym.unit_width)),cljs.core.str(","),cljs.core.str(h)].join('');
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$g,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$polyline,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$stroke,cljs.core.cst$kw$highlight.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.viz_canvas.state_colors),cljs.core.cst$kw$stroke_DASH_width,(3),cljs.core.cst$kw$fill,"none",cljs.core.cst$kw$points,points__$1], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$polyline,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$stroke,"black",cljs.core.cst$kw$stroke_DASH_width,0.75,cljs.core.cst$kw$fill,"none",cljs.core.cst$kw$points,points__$1], null)], null)], null);
})()], null);
})()], null)], null),(cljs.core.truth_((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(hover_y) : cljs.core.deref.call(null,hover_y)))?(function (){var i = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(hover_i) : cljs.core.deref.call(null,hover_i));
var dt = cljs.core.nth.cljs$core$IFn$_invoke$arity$2(draw_dts,i);
var from_step = cljs.core.nth.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps)),(dt + (1)));
var y = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(hover_y) : cljs.core.deref.call(null,hover_y));
var consumption = org.numenta.sanity.demos.hotgym.y__GT_consumption(y,h,top,bottom);
var vec__71589 = cljs.core.first(cljs.core.filter.cljs$core$IFn$_invoke$arity$2(((function (i,dt,from_step,y,consumption,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y){
return (function (p__71592){
var vec__71593 = p__71592;
var vec__71594 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71593,(0),null);
var c1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71594,(0),null);
var s1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71594,(1),null);
var vec__71595 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71593,(1),null);
var c2 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71595,(0),null);
var s2 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71595,(1),null);
return ((c1 <= consumption)) && ((consumption <= c2));
});})(i,dt,from_step,y,consumption,h,draw_steps,w,h_pad_top,h_pad_bottom,w_pad_left,w_pad_right,top,bottom,unit_height,label_every,center_dt,dt0,center_i,draw_dts,step__GT_scores,hover_i,hover_y))
,cljs.core.partition.cljs$core$IFn$_invoke$arity$3((2),(1),cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.first,cljs.core.get.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(step__GT_scores) : cljs.core.deref.call(null,step__GT_scores)),from_step)))));
var vec__71590 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71589,(0),null);
var lower_consumption = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71590,(0),null);
var lower_score = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71590,(1),null);
var vec__71591 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71589,(1),null);
var upper_consumption = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71591,(0),null);
var upper_score = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71591,(1),null);
var lower_y = org.numenta.sanity.demos.hotgym.consumption__GT_y(lower_consumption,top,unit_height);
var upper_y = org.numenta.sanity.demos.hotgym.consumption__GT_y(upper_consumption,top,unit_height);
var dt_left = (w_pad_left + (org.numenta.sanity.demos.hotgym.unit_width * (((draw_steps - (1)) - i) + 0.5)));
return new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$position,"absolute",cljs.core.cst$kw$left,(0),cljs.core.cst$kw$top,h_pad_top,cljs.core.cst$kw$pointer_DASH_events,"none"], null)], null),new cljs.core.PersistentVector(null, 7, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.horizontal_label,dt_left,lower_y,(w + w_pad_left),true,null,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,[cljs.core.str(lower_consumption.toFixed((1))),cljs.core.str("kW")].join(''),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$br], null),[cljs.core.str(lower_score.toFixed((3)))].join('')], null)], null),(function (){var contents = new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,[cljs.core.str(consumption.toFixed((1))),cljs.core.str("kW")].join(''),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$br], null),"click"], null);
var vec__71596 = ((((y - upper_y) > (30)))?new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [contents,null], null):((((lower_y - y) > (30)))?new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [null,contents], null):new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [null,null], null)
));
var above = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71596,(0),null);
var below = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71596,(1),null);
return new cljs.core.PersistentVector(null, 7, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.horizontal_label,dt_left,y,(w + w_pad_left),false,above,below], null);
})(),new cljs.core.PersistentVector(null, 7, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.horizontal_label,dt_left,upper_y,(w + w_pad_left),true,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,[cljs.core.str(upper_consumption.toFixed((1))),cljs.core.str("kW")].join(''),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$br], null),[cljs.core.str(upper_score.toFixed((3)))].join('')], null),null], null)], null);
})():null)], null);
});
;})(step__GT_scores,hover_i,hover_y))
});
org.numenta.sanity.demos.hotgym.world_pane = (function org$numenta$sanity$demos$hotgym$world_pane(){
if(cljs.core.truth_(cljs.core.not_empty((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.steps) : cljs.core.deref.call(null,org.numenta.sanity.main.steps))))){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$margin_DASH_top,(10)], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.anomaly_radar_pane], null)], null)], null),cljs.core.into.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$margin_DASH_top,(30)], null)], null),(function (){var iter__6925__auto__ = (function org$numenta$sanity$demos$hotgym$world_pane_$_iter__71660(s__71661){
return (new cljs.core.LazySeq(null,(function (){
var s__71661__$1 = s__71661;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__71661__$1);
if(temp__4657__auto__){
var s__71661__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__71661__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__71661__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__71663 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__71662 = (0);
while(true){
if((i__71662 < size__6924__auto__)){
var vec__71668 = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__71662);
var sense_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71668,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71668,(1),null);
cljs.core.chunk_append(b__71663,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$margin_DASH_bottom,(20)], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$span,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$font_DASH_family,"sans-serif",cljs.core.cst$kw$font_DASH_size,"9px",cljs.core.cst$kw$font_DASH_weight,"bold"], null)], null),cljs.core.name(sense_id)], null),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$br], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$strong,[cljs.core.str(v)].join('')], null)], null)], null));

var G__71670 = (i__71662 + (1));
i__71662 = G__71670;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__71663),org$numenta$sanity$demos$hotgym$world_pane_$_iter__71660(cljs.core.chunk_rest(s__71661__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__71663),null);
}
} else {
var vec__71669 = cljs.core.first(s__71661__$2);
var sense_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71669,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71669,(1),null);
return cljs.core.cons(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$margin_DASH_bottom,(20)], null)], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$span,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$style,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$font_DASH_family,"sans-serif",cljs.core.cst$kw$font_DASH_size,"9px",cljs.core.cst$kw$font_DASH_weight,"bold"], null)], null),cljs.core.name(sense_id)], null),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$br], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$strong,[cljs.core.str(v)].join('')], null)], null)], null),org$numenta$sanity$demos$hotgym$world_pane_$_iter__71660(cljs.core.rest(s__71661__$2)));
}
} else {
return null;
}
break;
}
}),null,null));
});
return iter__6925__auto__(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$sensed_DASH_values.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.main.selected_step.cljs$core$IFn$_invoke$arity$0()),cljs.core.cst$kw$power_DASH_consumption));
})())], null);
} else {
return null;
}
});
org.numenta.sanity.demos.hotgym.set_model_BANG_ = (function org$numenta$sanity$demos$hotgym$set_model_BANG_(){
return org.numenta.sanity.helpers.with_ui_loading_message((function (){
var init_QMARK_ = ((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.hotgym.model) : cljs.core.deref.call(null,org.numenta.sanity.demos.hotgym.model)) == null);
var G__71679_71687 = org.numenta.sanity.demos.hotgym.model;
var G__71680_71688 = org.nfrac.comportex.core.region_network(new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$rgn_DASH_0,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$power_DASH_consumption,cljs.core.cst$kw$is_DASH_weekend_QMARK_,cljs.core.cst$kw$hour_DASH_of_DASH_day], null)], null),cljs.core.constantly(org.nfrac.comportex.core.sensory_region),new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$rgn_DASH_0,cljs.core.assoc.cljs$core$IFn$_invoke$arity$variadic(org.nfrac.comportex.cells.better_parameter_defaults,cljs.core.cst$kw$depth,(1),cljs.core.array_seq([cljs.core.cst$kw$max_DASH_segments,(128),cljs.core.cst$kw$distal_DASH_perm_DASH_connected,0.2,cljs.core.cst$kw$distal_DASH_perm_DASH_init,0.2], 0))], null),new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$power_DASH_consumption,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$consumption,org.numenta.sanity.demos.hotgym.sampling_linear_encoder(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [((1024) + (256))], null),(17),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [-12.8,112.8], null),12.8)], null)], null),new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$is_DASH_weekend_QMARK_,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$is_DASH_weekend_QMARK_,org.nfrac.comportex.encoders.category_encoder(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(10)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [true,false], null))], null),cljs.core.cst$kw$hour_DASH_of_DASH_day,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$hour_DASH_of_DASH_day,org.nfrac.comportex.encoders.category_encoder(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [((40) * (24))], null),cljs.core.range.cljs$core$IFn$_invoke$arity$1((24)))], null)], null));
(cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(G__71679_71687,G__71680_71688) : cljs.core.reset_BANG_.call(null,G__71679_71687,G__71680_71688));

if(init_QMARK_){
var G__71682_71689 = "../data/hotgym.consumption_weekend_hour.edn";
var G__71683_71690 = ((function (G__71682_71689,init_QMARK_){
return (function (e){
if(cljs.core.truth_(e.target.isSuccess())){
var response = e.target.getResponseText();
var inputs = cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.partial.cljs$core$IFn$_invoke$arity$2(cljs.core.zipmap,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$consumption,cljs.core.cst$kw$is_DASH_weekend_QMARK_,cljs.core.cst$kw$hour_DASH_of_DASH_day], null)),cljs.reader.read_string(response));
return cljs.core.async.onto_chan.cljs$core$IFn$_invoke$arity$3(org.numenta.sanity.demos.hotgym.world_c,inputs,false);
} else {
var G__71684 = [cljs.core.str("Request to "),cljs.core.str(e.target.getLastUri()),cljs.core.str(" failed. "),cljs.core.str(e.target.getStatus()),cljs.core.str(" - "),cljs.core.str(e.target.getStatusText())].join('');
return log.error(G__71684);
}
});})(G__71682_71689,init_QMARK_))
;
goog.net.XhrIo.send(G__71682_71689,G__71683_71690);

return org.numenta.sanity.bridge.browser.init.cljs$core$IFn$_invoke$arity$4(org.numenta.sanity.demos.hotgym.model,org.numenta.sanity.demos.hotgym.world_c,org.numenta.sanity.main.into_journal,org.numenta.sanity.demos.hotgym.into_sim);
} else {
var G__71685 = org.numenta.sanity.main.network_shape;
var G__71686 = org.numenta.sanity.util.translate_network_shape(org.numenta.sanity.comportex.data.network_shape((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(org.numenta.sanity.demos.hotgym.model) : cljs.core.deref.call(null,org.numenta.sanity.demos.hotgym.model))));
return (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(G__71685,G__71686) : cljs.core.reset_BANG_.call(null,G__71685,G__71686));
}
}));
});
org.numenta.sanity.demos.hotgym.model_tab = (function org$numenta$sanity$demos$hotgym$model_tab(){
return new cljs.core.PersistentVector(null, 7, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$div,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Numenta's \"hotgym\" dataset."], null),new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Uses the solution from:",new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$br], null),new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$a,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$href,"http://mrcslws.com/gorilla/?path=hotgym.clj"], null),"Predicting power consumptions with HTM"], null)], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"This demo highlights the Anomaly Radar display on the left. The anomaly\n   scores for possible next inputs are sampled, and the sample points are shown\n   as dots. The prediction is a blue dash, and the actual value is a black\n   dash. The red->white scale represents the anomaly score. The anomaly score is\n   correct wherever there's a dot, and it's estimated elsewhere."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"Inspect the numbers by hovering your mouse over the Anomaly Radar. Click\n   to add your own samples. You might want to pause the simulation first."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"This demo chooses samples by decoding the predictive columns, as\n   explained in the essay above."], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$p,"It's fun to click the black dashes and see if it changes the\n   prediction. When this happens, it shows that the HTM actually predicted\n   something better than we thought, we just didn't sample the right points. You\n   could expand on this demo to try different strategies for choosing a clever\n   set of samples, finding the right balance between results and code\n   performance."], null)], null);
});
org.numenta.sanity.demos.hotgym.init = (function org$numenta$sanity$demos$hotgym$init(){
reagent.core.render.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.main.sanity_app,"Comportex",new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.model_tab], null),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.numenta.sanity.demos.hotgym.world_pane], null),org.numenta.sanity.demos.comportex_common.all_features,org.numenta.sanity.demos.hotgym.into_sim], null),goog.dom.getElement("sanity-app"));

return org.numenta.sanity.demos.hotgym.set_model_BANG_();
});
goog.exportSymbol('org.numenta.sanity.demos.hotgym.init', org.numenta.sanity.demos.hotgym.init);
