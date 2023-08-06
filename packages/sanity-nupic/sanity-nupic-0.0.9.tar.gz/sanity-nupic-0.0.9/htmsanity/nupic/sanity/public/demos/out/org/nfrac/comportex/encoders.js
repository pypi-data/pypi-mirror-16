// Compiled by ClojureScript 1.7.228 {:static-fns true, :optimize-constants true}
goog.provide('org.nfrac.comportex.encoders');
goog.require('cljs.core');
goog.require('org.nfrac.comportex.protocols');
goog.require('org.nfrac.comportex.topology');
goog.require('org.nfrac.comportex.util');
goog.require('clojure.test.check.random');
cljs.core.Keyword.prototype.org$nfrac$comportex$protocols$PSelector$ = true;

cljs.core.Keyword.prototype.org$nfrac$comportex$protocols$PSelector$extract$arity$2 = (function (this$,state){
var this$__$1 = this;
return cljs.core.get.cljs$core$IFn$_invoke$arity$2(state,this$__$1);
});

cljs.core.PersistentVector.prototype.org$nfrac$comportex$protocols$PSelector$ = true;

cljs.core.PersistentVector.prototype.org$nfrac$comportex$protocols$PSelector$extract$arity$2 = (function (this$,state){
var this$__$1 = this;
return cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(state,this$__$1);
});

/**
* @constructor
 * @implements {cljs.core.IRecord}
 * @implements {org.nfrac.comportex.protocols.PSelector}
 * @implements {cljs.core.IEquiv}
 * @implements {cljs.core.IHash}
 * @implements {cljs.core.ICollection}
 * @implements {cljs.core.ICounted}
 * @implements {cljs.core.ISeqable}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.ICloneable}
 * @implements {cljs.core.IPrintWithWriter}
 * @implements {cljs.core.IIterable}
 * @implements {cljs.core.IWithMeta}
 * @implements {cljs.core.IAssociative}
 * @implements {cljs.core.IMap}
 * @implements {cljs.core.ILookup}
*/
org.nfrac.comportex.encoders.VecSelector = (function (selectors,__meta,__extmap,__hash){
this.selectors = selectors;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70254,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70256 = (((k70254 instanceof cljs.core.Keyword))?k70254.fqn:null);
switch (G__70256) {
case "selectors":
return self__.selectors;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70254,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.VecSelector{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$selectors,self__.selectors],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70253){
var self__ = this;
var G__70253__$1 = this;
return (new cljs.core.RecordIter((0),G__70253__$1,1,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$selectors], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.VecSelector(self__.selectors,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (1 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.VecSelector.prototype.org$nfrac$comportex$protocols$PSelector$ = true;

org.nfrac.comportex.encoders.VecSelector.prototype.org$nfrac$comportex$protocols$PSelector$extract$arity$2 = (function (_,state){
var self__ = this;
var ___$1 = this;
return cljs.core.mapv.cljs$core$IFn$_invoke$arity$3(org.nfrac.comportex.protocols.extract,self__.selectors,cljs.core.repeat.cljs$core$IFn$_invoke$arity$1(state));
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$selectors,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.VecSelector(self__.selectors,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70253){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70257 = cljs.core.keyword_identical_QMARK_;
var expr__70258 = k__6775__auto__;
if(cljs.core.truth_((pred__70257.cljs$core$IFn$_invoke$arity$2 ? pred__70257.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$selectors,expr__70258) : pred__70257.call(null,cljs.core.cst$kw$selectors,expr__70258)))){
return (new org.nfrac.comportex.encoders.VecSelector(G__70253,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.VecSelector(self__.selectors,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70253),null));
}
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$selectors,self__.selectors],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70253){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.VecSelector(self__.selectors,G__70253,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.VecSelector.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.VecSelector.getBasis = (function (){
return new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$selectors], null);
});

org.nfrac.comportex.encoders.VecSelector.cljs$lang$type = true;

org.nfrac.comportex.encoders.VecSelector.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/VecSelector");
});

org.nfrac.comportex.encoders.VecSelector.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/VecSelector");
});

org.nfrac.comportex.encoders.__GT_VecSelector = (function org$nfrac$comportex$encoders$__GT_VecSelector(selectors){
return (new org.nfrac.comportex.encoders.VecSelector(selectors,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_VecSelector = (function org$nfrac$comportex$encoders$map__GT_VecSelector(G__70255){
return (new org.nfrac.comportex.encoders.VecSelector(cljs.core.cst$kw$selectors.cljs$core$IFn$_invoke$arity$1(G__70255),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(G__70255,cljs.core.cst$kw$selectors),null));
});

org.nfrac.comportex.encoders.vec_selector = (function org$nfrac$comportex$encoders$vec_selector(var_args){
var args__7218__auto__ = [];
var len__7211__auto___70262 = arguments.length;
var i__7212__auto___70263 = (0);
while(true){
if((i__7212__auto___70263 < len__7211__auto___70262)){
args__7218__auto__.push((arguments[i__7212__auto___70263]));

var G__70264 = (i__7212__auto___70263 + (1));
i__7212__auto___70263 = G__70264;
continue;
} else {
}
break;
}

var argseq__7219__auto__ = ((((0) < args__7218__auto__.length))?(new cljs.core.IndexedSeq(args__7218__auto__.slice((0)),(0))):null);
return org.nfrac.comportex.encoders.vec_selector.cljs$core$IFn$_invoke$arity$variadic(argseq__7219__auto__);
});

org.nfrac.comportex.encoders.vec_selector.cljs$core$IFn$_invoke$arity$variadic = (function (selectors){
return org.nfrac.comportex.encoders.__GT_VecSelector(selectors);
});

org.nfrac.comportex.encoders.vec_selector.cljs$lang$maxFixedArity = (0);

org.nfrac.comportex.encoders.vec_selector.cljs$lang$applyTo = (function (seq70261){
return org.nfrac.comportex.encoders.vec_selector.cljs$core$IFn$_invoke$arity$variadic(cljs.core.seq(seq70261));
});
org.nfrac.comportex.encoders.prediction_stats = (function org$nfrac$comportex$encoders$prediction_stats(x_bits,bit_votes,total_votes){
var o_votes = cljs.core.select_keys(bit_votes,x_bits);
var total_o_votes = cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core._PLUS_,cljs.core.vals(o_votes));
var o_bits = cljs.core.keys(o_votes);
return new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$bit_DASH_coverage,(cljs.core.count(o_bits) / (function (){var x__6484__auto__ = (1);
var y__6485__auto__ = cljs.core.count(x_bits);
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})()),cljs.core.cst$kw$bit_DASH_precision,(cljs.core.count(o_bits) / (function (){var x__6484__auto__ = (1);
var y__6485__auto__ = cljs.core.count(bit_votes);
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})()),cljs.core.cst$kw$votes_DASH_frac,(total_o_votes / (function (){var x__6484__auto__ = (1);
var y__6485__auto__ = total_votes;
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})()),cljs.core.cst$kw$votes_DASH_per_DASH_bit,(total_o_votes / (function (){var x__6484__auto__ = (1);
var y__6485__auto__ = cljs.core.count(x_bits);
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})())], null);
});
org.nfrac.comportex.encoders.decode_by_brute_force = (function org$nfrac$comportex$encoders$decode_by_brute_force(e,try_values,bit_votes){
var total_votes = cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core._PLUS_,cljs.core.vals(bit_votes));
if((total_votes > (0))){
return cljs.core.reverse(cljs.core.sort_by.cljs$core$IFn$_invoke$arity$2(cljs.core.juxt.cljs$core$IFn$_invoke$arity$3(cljs.core.cst$kw$votes_DASH_frac,cljs.core.cst$kw$bit_DASH_coverage,cljs.core.cst$kw$bit_DASH_precision),cljs.core.filter.cljs$core$IFn$_invoke$arity$2(cljs.core.comp.cljs$core$IFn$_invoke$arity$2(cljs.core.pos_QMARK_,cljs.core.cst$kw$votes_DASH_frac),cljs.core.map.cljs$core$IFn$_invoke$arity$2(((function (total_votes){
return (function (x){
var x_bits = org.nfrac.comportex.protocols.encode(e,x);
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(org.nfrac.comportex.encoders.prediction_stats(x_bits,bit_votes,total_votes),cljs.core.cst$kw$value,x);
});})(total_votes))
,try_values))));
} else {
return null;
}
});
org.nfrac.comportex.encoders.unaligned_bit_votes = (function org$nfrac$comportex$encoders$unaligned_bit_votes(widths,aligned){
var vec__70266 = cljs.core.juxt.cljs$core$IFn$_invoke$arity$2(cljs.core.keys,cljs.core.vals).call(null,cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.sorted_map(),aligned));
var is = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70266,(0),null);
var vs = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70266,(1),null);
var partitioned_is = org.nfrac.comportex.util.unalign_indices(widths,is);
var partitioned_vs = org.nfrac.comportex.util.splits_at(cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.count,partitioned_is),vs);
return cljs.core.map.cljs$core$IFn$_invoke$arity$3(cljs.core.zipmap,partitioned_is,partitioned_vs);
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
org.nfrac.comportex.encoders.ConcatEncoder = (function (encoders,__meta,__extmap,__hash){
this.encoders = encoders;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70270,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70272 = (((k70270 instanceof cljs.core.Keyword))?k70270.fqn:null);
switch (G__70272) {
case "encoders":
return self__.encoders;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70270,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.ConcatEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
var dim = cljs.core.apply.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.topology.combined_dimensions,cljs.core.map.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.protocols.dims_of,self__.encoders));
return org.nfrac.comportex.topology.make_topology(dim);
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.ConcatEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$encoders,self__.encoders],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70269){
var self__ = this;
var G__70269__$1 = this;
return (new cljs.core.RecordIter((0),G__70269__$1,1,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$encoders], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.ConcatEncoder(self__.encoders,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (1 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.ConcatEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.ConcatEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,xs){
var self__ = this;
var ___$1 = this;
var bit_widths = cljs.core.map.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.protocols.size_of,self__.encoders);
return org.nfrac.comportex.util.align_indices.cljs$core$IFn$_invoke$arity$2(bit_widths,cljs.core.map.cljs$core$IFn$_invoke$arity$3(org.nfrac.comportex.protocols.encode,self__.encoders,xs));
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (_,bit_votes,n_values){
var self__ = this;
var ___$1 = this;
var bit_widths = cljs.core.map.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.protocols.size_of,self__.encoders);
return cljs.core.map.cljs$core$IFn$_invoke$arity$3(((function (bit_widths,___$1){
return (function (p1__70267_SHARP_,p2__70268_SHARP_){
return org.nfrac.comportex.protocols.decode(p1__70267_SHARP_,p2__70268_SHARP_,n_values);
});})(bit_widths,___$1))
,self__.encoders,org.nfrac.comportex.encoders.unaligned_bit_votes(bit_widths,bit_votes));
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$encoders,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.ConcatEncoder(self__.encoders,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70269){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70273 = cljs.core.keyword_identical_QMARK_;
var expr__70274 = k__6775__auto__;
if(cljs.core.truth_((pred__70273.cljs$core$IFn$_invoke$arity$2 ? pred__70273.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$encoders,expr__70274) : pred__70273.call(null,cljs.core.cst$kw$encoders,expr__70274)))){
return (new org.nfrac.comportex.encoders.ConcatEncoder(G__70269,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.ConcatEncoder(self__.encoders,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70269),null));
}
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$encoders,self__.encoders],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70269){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.ConcatEncoder(self__.encoders,G__70269,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.ConcatEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.ConcatEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$encoders], null);
});

org.nfrac.comportex.encoders.ConcatEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.ConcatEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/ConcatEncoder");
});

org.nfrac.comportex.encoders.ConcatEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/ConcatEncoder");
});

org.nfrac.comportex.encoders.__GT_ConcatEncoder = (function org$nfrac$comportex$encoders$__GT_ConcatEncoder(encoders){
return (new org.nfrac.comportex.encoders.ConcatEncoder(encoders,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_ConcatEncoder = (function org$nfrac$comportex$encoders$map__GT_ConcatEncoder(G__70271){
return (new org.nfrac.comportex.encoders.ConcatEncoder(cljs.core.cst$kw$encoders.cljs$core$IFn$_invoke$arity$1(G__70271),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(G__70271,cljs.core.cst$kw$encoders),null));
});

/**
 * Returns an encoder for a sequence of values, where each is encoded
 *   separately before the results are concatenated into a single
 *   sense. Each value by index is passed to the corresponding index of
 *   `encoders`.
 */
org.nfrac.comportex.encoders.encat = (function org$nfrac$comportex$encoders$encat(encoders){
return org.nfrac.comportex.encoders.__GT_ConcatEncoder(encoders);
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
org.nfrac.comportex.encoders.SplatEncoder = (function (encoder,__meta,__extmap,__hash){
this.encoder = encoder;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70278,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70280 = (((k70278 instanceof cljs.core.Keyword))?k70278.fqn:null);
switch (G__70280) {
case "encoder":
return self__.encoder;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70278,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.SplatEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return org.nfrac.comportex.protocols.topology(self__.encoder);
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.SplatEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$encoder,self__.encoder],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70277){
var self__ = this;
var G__70277__$1 = this;
return (new cljs.core.RecordIter((0),G__70277__$1,1,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$encoder], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.SplatEncoder(self__.encoder,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (1 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.SplatEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.SplatEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,xs){
var self__ = this;
var ___$1 = this;
return cljs.core.distinct.cljs$core$IFn$_invoke$arity$1(cljs.core.mapcat.cljs$core$IFn$_invoke$arity$variadic(cljs.core.partial.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.protocols.encode,self__.encoder),cljs.core.array_seq([xs], 0)));
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (_,bit_votes,n_values){
var self__ = this;
var ___$1 = this;
return org.nfrac.comportex.protocols.decode(self__.encoder,bit_votes,n_values);
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$encoder,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.SplatEncoder(self__.encoder,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70277){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70281 = cljs.core.keyword_identical_QMARK_;
var expr__70282 = k__6775__auto__;
if(cljs.core.truth_((pred__70281.cljs$core$IFn$_invoke$arity$2 ? pred__70281.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$encoder,expr__70282) : pred__70281.call(null,cljs.core.cst$kw$encoder,expr__70282)))){
return (new org.nfrac.comportex.encoders.SplatEncoder(G__70277,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.SplatEncoder(self__.encoder,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70277),null));
}
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$encoder,self__.encoder],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70277){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.SplatEncoder(self__.encoder,G__70277,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.SplatEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.SplatEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$encoder], null);
});

org.nfrac.comportex.encoders.SplatEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.SplatEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/SplatEncoder");
});

org.nfrac.comportex.encoders.SplatEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/SplatEncoder");
});

org.nfrac.comportex.encoders.__GT_SplatEncoder = (function org$nfrac$comportex$encoders$__GT_SplatEncoder(encoder){
return (new org.nfrac.comportex.encoders.SplatEncoder(encoder,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_SplatEncoder = (function org$nfrac$comportex$encoders$map__GT_SplatEncoder(G__70279){
return (new org.nfrac.comportex.encoders.SplatEncoder(cljs.core.cst$kw$encoder.cljs$core$IFn$_invoke$arity$1(G__70279),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(G__70279,cljs.core.cst$kw$encoder),null));
});

/**
 * Returns an encoder for a sequence of values. The given encoder will
 *   be applied to each value, and the resulting encodings
 *   overlaid (splatted together), taking the union of the sets of bits.
 */
org.nfrac.comportex.encoders.ensplat = (function org$nfrac$comportex$encoders$ensplat(encoder){
return org.nfrac.comportex.encoders.__GT_SplatEncoder(encoder);
});
/**
 * truncates
 */
org.nfrac.comportex.encoders.linear_bits = (function org$nfrac$comportex$encoders$linear_bits(x,lower,upper,n_bits,n_active){
var span = (upper - lower);
var x__$1 = (function (){var x__6491__auto__ = (function (){var x__6484__auto__ = x;
var y__6485__auto__ = lower;
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})();
var y__6492__auto__ = upper;
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})();
var z = ((x__$1 - lower) / span);
var i = cljs.core.long$((z * (n_bits - n_active)));
return cljs.core.range.cljs$core$IFn$_invoke$arity$2(i,(i + n_active));
});
/**
 * wraps
 */
org.nfrac.comportex.encoders.periodic_linear_bits = (function org$nfrac$comportex$encoders$periodic_linear_bits(x,lower,upper,n_bits,n_active){
var span = (upper - lower);
var z = ((x - lower) / span);
var z__$1 = cljs.core.mod(z,1.0);
var i = cljs.core.long$((z__$1 * n_bits));
var i_end = (i + n_active);
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2((((i_end > n_bits))?cljs.core.range.cljs$core$IFn$_invoke$arity$1((i_end - n_bits)):null),cljs.core.range.cljs$core$IFn$_invoke$arity$2(i,(function (){var x__6491__auto__ = i_end;
var y__6492__auto__ = n_bits;
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})()));
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
org.nfrac.comportex.encoders.LinearEncoder = (function (topo,n_active,lower,upper,periodic_QMARK_,__meta,__extmap,__hash){
this.topo = topo;
this.n_active = n_active;
this.lower = lower;
this.upper = upper;
this.periodic_QMARK_ = periodic_QMARK_;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70286,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70288 = (((k70286 instanceof cljs.core.Keyword))?k70286.fqn:null);
switch (G__70288) {
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
case "periodic?":
return self__.periodic_QMARK_;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70286,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.LinearEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.topo;
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.LinearEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$lower,self__.lower],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$upper,self__.upper],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$periodic_QMARK_,self__.periodic_QMARK_],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70285){
var self__ = this;
var G__70285__$1 = this;
return (new cljs.core.RecordIter((0),G__70285__$1,5,new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$topo,cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$lower,cljs.core.cst$kw$upper,cljs.core.cst$kw$periodic_QMARK_], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.LinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.periodic_QMARK_,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (5 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.LinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.LinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,x){
var self__ = this;
var ___$1 = this;
if(cljs.core.truth_(x)){
var n_bits = org.nfrac.comportex.protocols.size(self__.topo);
if(cljs.core.truth_(self__.periodic_QMARK_)){
return org.nfrac.comportex.encoders.periodic_linear_bits(x,self__.lower,self__.upper,n_bits,self__.n_active);
} else {
return org.nfrac.comportex.encoders.linear_bits(x,self__.lower,self__.upper,n_bits,self__.n_active);
}
} else {
return cljs.core.sequence.cljs$core$IFn$_invoke$arity$1(null);
}
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (this$,bit_votes,n){
var self__ = this;
var this$__$1 = this;
var span = (self__.upper - self__.lower);
var values = cljs.core.range.cljs$core$IFn$_invoke$arity$3(self__.lower,self__.upper,(((((5) < span)) && ((span < (250))))?(1):(span / (50))));
return cljs.core.take.cljs$core$IFn$_invoke$arity$2(n,org.nfrac.comportex.encoders.decode_by_brute_force(this$__$1,values,bit_votes));
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$upper,null,cljs.core.cst$kw$topo,null,cljs.core.cst$kw$periodic_QMARK_,null,cljs.core.cst$kw$lower,null,cljs.core.cst$kw$n_DASH_active,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.LinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.periodic_QMARK_,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70285){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70289 = cljs.core.keyword_identical_QMARK_;
var expr__70290 = k__6775__auto__;
if(cljs.core.truth_((pred__70289.cljs$core$IFn$_invoke$arity$2 ? pred__70289.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$topo,expr__70290) : pred__70289.call(null,cljs.core.cst$kw$topo,expr__70290)))){
return (new org.nfrac.comportex.encoders.LinearEncoder(G__70285,self__.n_active,self__.lower,self__.upper,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70289.cljs$core$IFn$_invoke$arity$2 ? pred__70289.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$n_DASH_active,expr__70290) : pred__70289.call(null,cljs.core.cst$kw$n_DASH_active,expr__70290)))){
return (new org.nfrac.comportex.encoders.LinearEncoder(self__.topo,G__70285,self__.lower,self__.upper,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70289.cljs$core$IFn$_invoke$arity$2 ? pred__70289.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$lower,expr__70290) : pred__70289.call(null,cljs.core.cst$kw$lower,expr__70290)))){
return (new org.nfrac.comportex.encoders.LinearEncoder(self__.topo,self__.n_active,G__70285,self__.upper,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70289.cljs$core$IFn$_invoke$arity$2 ? pred__70289.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$upper,expr__70290) : pred__70289.call(null,cljs.core.cst$kw$upper,expr__70290)))){
return (new org.nfrac.comportex.encoders.LinearEncoder(self__.topo,self__.n_active,self__.lower,G__70285,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70289.cljs$core$IFn$_invoke$arity$2 ? pred__70289.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$periodic_QMARK_,expr__70290) : pred__70289.call(null,cljs.core.cst$kw$periodic_QMARK_,expr__70290)))){
return (new org.nfrac.comportex.encoders.LinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,G__70285,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.LinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.periodic_QMARK_,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70285),null));
}
}
}
}
}
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$lower,self__.lower],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$upper,self__.upper],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$periodic_QMARK_,self__.periodic_QMARK_],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70285){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.LinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.periodic_QMARK_,G__70285,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.LinearEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.LinearEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$topo,cljs.core.cst$sym$n_DASH_active,cljs.core.cst$sym$lower,cljs.core.cst$sym$upper,cljs.core.cst$sym$periodic_QMARK_], null);
});

org.nfrac.comportex.encoders.LinearEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.LinearEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/LinearEncoder");
});

org.nfrac.comportex.encoders.LinearEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/LinearEncoder");
});

org.nfrac.comportex.encoders.__GT_LinearEncoder = (function org$nfrac$comportex$encoders$__GT_LinearEncoder(topo,n_active,lower,upper,periodic_QMARK_){
return (new org.nfrac.comportex.encoders.LinearEncoder(topo,n_active,lower,upper,periodic_QMARK_,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_LinearEncoder = (function org$nfrac$comportex$encoders$map__GT_LinearEncoder(G__70287){
return (new org.nfrac.comportex.encoders.LinearEncoder(cljs.core.cst$kw$topo.cljs$core$IFn$_invoke$arity$1(G__70287),cljs.core.cst$kw$n_DASH_active.cljs$core$IFn$_invoke$arity$1(G__70287),cljs.core.cst$kw$lower.cljs$core$IFn$_invoke$arity$1(G__70287),cljs.core.cst$kw$upper.cljs$core$IFn$_invoke$arity$1(G__70287),cljs.core.cst$kw$periodic_QMARK_.cljs$core$IFn$_invoke$arity$1(G__70287),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__70287,cljs.core.cst$kw$topo,cljs.core.array_seq([cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$lower,cljs.core.cst$kw$upper,cljs.core.cst$kw$periodic_QMARK_], 0)),null));
});

/**
 * Returns a simple encoder for a single number. It encodes a number
 *   by its position on a continuous scale within a numeric range.
 * 
 *   * `dimensions` is the size of the encoder in bits along one or more
 *  dimensions, a vector e.g. [500].
 * 
 *   * `n-active` is the number of bits to be active.
 * 
 *   * `[lower upper]` gives the numeric range to cover. The input number
 *  will be clamped to this range.
 */
org.nfrac.comportex.encoders.linear_encoder = (function org$nfrac$comportex$encoders$linear_encoder(var_args){
var args70293 = [];
var len__7211__auto___70300 = arguments.length;
var i__7212__auto___70301 = (0);
while(true){
if((i__7212__auto___70301 < len__7211__auto___70300)){
args70293.push((arguments[i__7212__auto___70301]));

var G__70302 = (i__7212__auto___70301 + (1));
i__7212__auto___70301 = G__70302;
continue;
} else {
}
break;
}

var G__70295 = args70293.length;
switch (G__70295) {
case 3:
return org.nfrac.comportex.encoders.linear_encoder.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
case 4:
return org.nfrac.comportex.encoders.linear_encoder.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
default:
throw (new Error([cljs.core.str("Invalid arity: "),cljs.core.str(args70293.length)].join('')));

}
});

org.nfrac.comportex.encoders.linear_encoder.cljs$core$IFn$_invoke$arity$3 = (function (dimensions,n_active,p__70296){
var vec__70297 = p__70296;
var lower = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70297,(0),null);
var upper = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70297,(1),null);
return org.nfrac.comportex.encoders.linear_encoder.cljs$core$IFn$_invoke$arity$4(dimensions,n_active,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [lower,upper], null),false);
});

org.nfrac.comportex.encoders.linear_encoder.cljs$core$IFn$_invoke$arity$4 = (function (dimensions,n_active,p__70298,periodic_QMARK_){
var vec__70299 = p__70298;
var lower = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70299,(0),null);
var upper = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70299,(1),null);
var topo = org.nfrac.comportex.topology.make_topology(dimensions);
return org.nfrac.comportex.encoders.map__GT_LinearEncoder(new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$topo,topo,cljs.core.cst$kw$n_DASH_active,n_active,cljs.core.cst$kw$lower,lower,cljs.core.cst$kw$upper,upper,cljs.core.cst$kw$periodic_QMARK_,periodic_QMARK_], null));
});

org.nfrac.comportex.encoders.linear_encoder.cljs$lang$maxFixedArity = 4;

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
org.nfrac.comportex.encoders.CategoryEncoder = (function (topo,value__GT_index,__meta,__extmap,__hash){
this.topo = topo;
this.value__GT_index = value__GT_index;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70305,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70307 = (((k70305 instanceof cljs.core.Keyword))?k70305.fqn:null);
switch (G__70307) {
case "topo":
return self__.topo;

break;
case "value->index":
return self__.value__GT_index;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70305,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.CategoryEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.topo;
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.CategoryEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$value_DASH__GT_index,self__.value__GT_index],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70304){
var self__ = this;
var G__70304__$1 = this;
return (new cljs.core.RecordIter((0),G__70304__$1,2,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$topo,cljs.core.cst$kw$value_DASH__GT_index], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.CategoryEncoder(self__.topo,self__.value__GT_index,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (2 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.CategoryEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.CategoryEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,x){
var self__ = this;
var ___$1 = this;
var temp__4655__auto__ = (self__.value__GT_index.cljs$core$IFn$_invoke$arity$1 ? self__.value__GT_index.cljs$core$IFn$_invoke$arity$1(x) : self__.value__GT_index.call(null,x));
if(cljs.core.truth_(temp__4655__auto__)){
var idx = temp__4655__auto__;
var n_bits = org.nfrac.comportex.protocols.size(self__.topo);
var n_active = cljs.core.quot(n_bits,cljs.core.count(self__.value__GT_index));
var i = (idx * n_active);
return cljs.core.range.cljs$core$IFn$_invoke$arity$2(i,(i + n_active));
} else {
return cljs.core.sequence.cljs$core$IFn$_invoke$arity$1(null);
}
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (this$,bit_votes,n){
var self__ = this;
var this$__$1 = this;
return cljs.core.take.cljs$core$IFn$_invoke$arity$2(n,org.nfrac.comportex.encoders.decode_by_brute_force(this$__$1,cljs.core.keys(self__.value__GT_index),bit_votes));
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$topo,null,cljs.core.cst$kw$value_DASH__GT_index,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.CategoryEncoder(self__.topo,self__.value__GT_index,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70304){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70308 = cljs.core.keyword_identical_QMARK_;
var expr__70309 = k__6775__auto__;
if(cljs.core.truth_((pred__70308.cljs$core$IFn$_invoke$arity$2 ? pred__70308.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$topo,expr__70309) : pred__70308.call(null,cljs.core.cst$kw$topo,expr__70309)))){
return (new org.nfrac.comportex.encoders.CategoryEncoder(G__70304,self__.value__GT_index,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70308.cljs$core$IFn$_invoke$arity$2 ? pred__70308.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$value_DASH__GT_index,expr__70309) : pred__70308.call(null,cljs.core.cst$kw$value_DASH__GT_index,expr__70309)))){
return (new org.nfrac.comportex.encoders.CategoryEncoder(self__.topo,G__70304,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.CategoryEncoder(self__.topo,self__.value__GT_index,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70304),null));
}
}
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$value_DASH__GT_index,self__.value__GT_index],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70304){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.CategoryEncoder(self__.topo,self__.value__GT_index,G__70304,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.CategoryEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.CategoryEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$topo,cljs.core.cst$sym$value_DASH__GT_index], null);
});

org.nfrac.comportex.encoders.CategoryEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.CategoryEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/CategoryEncoder");
});

org.nfrac.comportex.encoders.CategoryEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/CategoryEncoder");
});

org.nfrac.comportex.encoders.__GT_CategoryEncoder = (function org$nfrac$comportex$encoders$__GT_CategoryEncoder(topo,value__GT_index){
return (new org.nfrac.comportex.encoders.CategoryEncoder(topo,value__GT_index,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_CategoryEncoder = (function org$nfrac$comportex$encoders$map__GT_CategoryEncoder(G__70306){
return (new org.nfrac.comportex.encoders.CategoryEncoder(cljs.core.cst$kw$topo.cljs$core$IFn$_invoke$arity$1(G__70306),cljs.core.cst$kw$value_DASH__GT_index.cljs$core$IFn$_invoke$arity$1(G__70306),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__70306,cljs.core.cst$kw$topo,cljs.core.array_seq([cljs.core.cst$kw$value_DASH__GT_index], 0)),null));
});

org.nfrac.comportex.encoders.category_encoder = (function org$nfrac$comportex$encoders$category_encoder(dimensions,values){
var topo = org.nfrac.comportex.topology.make_topology(dimensions);
return org.nfrac.comportex.encoders.map__GT_CategoryEncoder(new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$topo,topo,cljs.core.cst$kw$value_DASH__GT_index,cljs.core.zipmap(values,cljs.core.range.cljs$core$IFn$_invoke$arity$0())], null));
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
org.nfrac.comportex.encoders.NoEncoder = (function (topo,__meta,__extmap,__hash){
this.topo = topo;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70313,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70315 = (((k70313 instanceof cljs.core.Keyword))?k70313.fqn:null);
switch (G__70315) {
case "topo":
return self__.topo;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70313,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.NoEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.NoEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.topo;
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.NoEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70312){
var self__ = this;
var G__70312__$1 = this;
return (new cljs.core.RecordIter((0),G__70312__$1,1,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$topo], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.NoEncoder(self__.topo,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (1 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.NoEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.NoEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,x){
var self__ = this;
var ___$1 = this;
return x;
});

org.nfrac.comportex.encoders.NoEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (this$,bit_votes,n){
var self__ = this;
var this$__$1 = this;
return new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.keys(bit_votes)], null);
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$topo,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.NoEncoder(self__.topo,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70312){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70316 = cljs.core.keyword_identical_QMARK_;
var expr__70317 = k__6775__auto__;
if(cljs.core.truth_((pred__70316.cljs$core$IFn$_invoke$arity$2 ? pred__70316.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$topo,expr__70317) : pred__70316.call(null,cljs.core.cst$kw$topo,expr__70317)))){
return (new org.nfrac.comportex.encoders.NoEncoder(G__70312,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.NoEncoder(self__.topo,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70312),null));
}
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70312){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.NoEncoder(self__.topo,G__70312,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.NoEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.NoEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$topo], null);
});

org.nfrac.comportex.encoders.NoEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.NoEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/NoEncoder");
});

org.nfrac.comportex.encoders.NoEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/NoEncoder");
});

org.nfrac.comportex.encoders.__GT_NoEncoder = (function org$nfrac$comportex$encoders$__GT_NoEncoder(topo){
return (new org.nfrac.comportex.encoders.NoEncoder(topo,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_NoEncoder = (function org$nfrac$comportex$encoders$map__GT_NoEncoder(G__70314){
return (new org.nfrac.comportex.encoders.NoEncoder(cljs.core.cst$kw$topo.cljs$core$IFn$_invoke$arity$1(G__70314),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(G__70314,cljs.core.cst$kw$topo),null));
});

org.nfrac.comportex.encoders.no_encoder = (function org$nfrac$comportex$encoders$no_encoder(dimensions){
var topo = org.nfrac.comportex.topology.make_topology(dimensions);
return org.nfrac.comportex.encoders.map__GT_NoEncoder(new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$topo,topo], null));
});
org.nfrac.comportex.encoders.unique_sdr = (function org$nfrac$comportex$encoders$unique_sdr(x,n_bits,n_active){
var rngs = clojure.test.check.random.split_n(clojure.test.check.random.make_random.cljs$core$IFn$_invoke$arity$1(cljs.core.hash(x)),cljs.core.long$((n_active * 1.25)));
return cljs.core.into.cljs$core$IFn$_invoke$arity$3(cljs.core.List.EMPTY,cljs.core.comp.cljs$core$IFn$_invoke$arity$3(cljs.core.map.cljs$core$IFn$_invoke$arity$1(((function (rngs){
return (function (p1__70320_SHARP_){
return org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$2(p1__70320_SHARP_,n_bits);
});})(rngs))
),cljs.core.distinct.cljs$core$IFn$_invoke$arity$0(),cljs.core.take.cljs$core$IFn$_invoke$arity$1(n_active)),rngs);
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
org.nfrac.comportex.encoders.UniqueEncoder = (function (topo,n_active,cache,__meta,__extmap,__hash){
this.topo = topo;
this.n_active = n_active;
this.cache = cache;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70322,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70324 = (((k70322 instanceof cljs.core.Keyword))?k70322.fqn:null);
switch (G__70324) {
case "topo":
return self__.topo;

break;
case "n-active":
return self__.n_active;

break;
case "cache":
return self__.cache;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70322,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.UniqueEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.topo;
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.UniqueEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$cache,self__.cache],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70321){
var self__ = this;
var G__70321__$1 = this;
return (new cljs.core.RecordIter((0),G__70321__$1,3,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$topo,cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$cache], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.UniqueEncoder(self__.topo,self__.n_active,self__.cache,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (3 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.UniqueEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.UniqueEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,x){
var self__ = this;
var ___$1 = this;
if((x == null)){
return cljs.core.sequence.cljs$core$IFn$_invoke$arity$1(null);
} else {
var or__6153__auto__ = cljs.core.get.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(self__.cache) : cljs.core.deref.call(null,self__.cache)),x);
if(cljs.core.truth_(or__6153__auto__)){
return or__6153__auto__;
} else {
var sdr = org.nfrac.comportex.encoders.unique_sdr(x,org.nfrac.comportex.protocols.size(self__.topo),self__.n_active);
return cljs.core.get.cljs$core$IFn$_invoke$arity$2(cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(self__.cache,cljs.core.assoc,x,sdr),x);
}
}
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (this$,bit_votes,n){
var self__ = this;
var this$__$1 = this;
return cljs.core.take.cljs$core$IFn$_invoke$arity$2(n,org.nfrac.comportex.encoders.decode_by_brute_force(this$__$1,cljs.core.keys((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(self__.cache) : cljs.core.deref.call(null,self__.cache))),bit_votes));
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$topo,null,cljs.core.cst$kw$cache,null,cljs.core.cst$kw$n_DASH_active,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.UniqueEncoder(self__.topo,self__.n_active,self__.cache,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70321){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70325 = cljs.core.keyword_identical_QMARK_;
var expr__70326 = k__6775__auto__;
if(cljs.core.truth_((pred__70325.cljs$core$IFn$_invoke$arity$2 ? pred__70325.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$topo,expr__70326) : pred__70325.call(null,cljs.core.cst$kw$topo,expr__70326)))){
return (new org.nfrac.comportex.encoders.UniqueEncoder(G__70321,self__.n_active,self__.cache,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70325.cljs$core$IFn$_invoke$arity$2 ? pred__70325.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$n_DASH_active,expr__70326) : pred__70325.call(null,cljs.core.cst$kw$n_DASH_active,expr__70326)))){
return (new org.nfrac.comportex.encoders.UniqueEncoder(self__.topo,G__70321,self__.cache,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70325.cljs$core$IFn$_invoke$arity$2 ? pred__70325.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$cache,expr__70326) : pred__70325.call(null,cljs.core.cst$kw$cache,expr__70326)))){
return (new org.nfrac.comportex.encoders.UniqueEncoder(self__.topo,self__.n_active,G__70321,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.UniqueEncoder(self__.topo,self__.n_active,self__.cache,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70321),null));
}
}
}
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$cache,self__.cache],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70321){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.UniqueEncoder(self__.topo,self__.n_active,self__.cache,G__70321,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.UniqueEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.UniqueEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$topo,cljs.core.cst$sym$n_DASH_active,cljs.core.cst$sym$cache], null);
});

org.nfrac.comportex.encoders.UniqueEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.UniqueEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/UniqueEncoder");
});

org.nfrac.comportex.encoders.UniqueEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/UniqueEncoder");
});

org.nfrac.comportex.encoders.__GT_UniqueEncoder = (function org$nfrac$comportex$encoders$__GT_UniqueEncoder(topo,n_active,cache){
return (new org.nfrac.comportex.encoders.UniqueEncoder(topo,n_active,cache,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_UniqueEncoder = (function org$nfrac$comportex$encoders$map__GT_UniqueEncoder(G__70323){
return (new org.nfrac.comportex.encoders.UniqueEncoder(cljs.core.cst$kw$topo.cljs$core$IFn$_invoke$arity$1(G__70323),cljs.core.cst$kw$n_DASH_active.cljs$core$IFn$_invoke$arity$1(G__70323),cljs.core.cst$kw$cache.cljs$core$IFn$_invoke$arity$1(G__70323),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__70323,cljs.core.cst$kw$topo,cljs.core.array_seq([cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$cache], 0)),null));
});

/**
 * This encoder generates a unique bit set for each distinct value,
 *   based on its hash. `dimensions` is given as a vector.
 */
org.nfrac.comportex.encoders.unique_encoder = (function org$nfrac$comportex$encoders$unique_encoder(dimensions,n_active){
var topo = org.nfrac.comportex.topology.make_topology(dimensions);
return org.nfrac.comportex.encoders.map__GT_UniqueEncoder(new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$topo,topo,cljs.core.cst$kw$n_DASH_active,n_active,cljs.core.cst$kw$cache,(function (){var G__70330 = cljs.core.PersistentArrayMap.EMPTY;
return (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1(G__70330) : cljs.core.atom.call(null,G__70330));
})()], null));
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
org.nfrac.comportex.encoders.Linear2DEncoder = (function (topo,n_active,x_max,y_max,__meta,__extmap,__hash){
this.topo = topo;
this.n_active = n_active;
this.x_max = x_max;
this.y_max = y_max;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70332,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70334 = (((k70332 instanceof cljs.core.Keyword))?k70332.fqn:null);
switch (G__70334) {
case "topo":
return self__.topo;

break;
case "n-active":
return self__.n_active;

break;
case "x-max":
return self__.x_max;

break;
case "y-max":
return self__.y_max;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70332,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.topo;
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.Linear2DEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$x_DASH_max,self__.x_max],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$y_DASH_max,self__.y_max],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70331){
var self__ = this;
var G__70331__$1 = this;
return (new cljs.core.RecordIter((0),G__70331__$1,4,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$topo,cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$x_DASH_max,cljs.core.cst$kw$y_DASH_max], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.Linear2DEncoder(self__.topo,self__.n_active,self__.x_max,self__.y_max,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (4 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,p__70335){
var self__ = this;
var vec__70336 = p__70335;
var x = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70336,(0),null);
var y = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70336,(1),null);
var ___$1 = this;
if(cljs.core.truth_(x)){
var vec__70337 = org.nfrac.comportex.protocols.dimensions(self__.topo);
var w = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70337,(0),null);
var h = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70337,(1),null);
var x__$1 = (function (){var x__6491__auto__ = (function (){var x__6484__auto__ = x;
var y__6485__auto__ = (0);
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})();
var y__6492__auto__ = self__.x_max;
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})();
var y__$1 = (function (){var x__6491__auto__ = (function (){var x__6484__auto__ = y;
var y__6485__auto__ = (0);
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})();
var y__6492__auto__ = self__.y_max;
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})();
var xz = (x__$1 / self__.x_max);
var yz = (y__$1 / self__.y_max);
var xi = cljs.core.long$((xz * w));
var yi = cljs.core.long$((yz * h));
var coord = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [xi,yi], null);
var idx = org.nfrac.comportex.protocols.index_of_coordinates(self__.topo,coord);
return cljs.core.take.cljs$core$IFn$_invoke$arity$2(self__.n_active,cljs.core.mapcat.cljs$core$IFn$_invoke$arity$variadic(((function (vec__70337,w,h,x__$1,y__$1,xz,yz,xi,yi,coord,idx,___$1,vec__70336,x,y){
return (function (radius){
return org.nfrac.comportex.protocols.neighbours_indices.cljs$core$IFn$_invoke$arity$4(self__.topo,idx,radius,(radius - (1)));
});})(vec__70337,w,h,x__$1,y__$1,xz,yz,xi,yi,coord,idx,___$1,vec__70336,x,y))
,cljs.core.array_seq([cljs.core.range.cljs$core$IFn$_invoke$arity$1((10))], 0)));
} else {
return cljs.core.sequence.cljs$core$IFn$_invoke$arity$1(null);
}
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (this$,bit_votes,n){
var self__ = this;
var this$__$1 = this;
var values = (function (){var iter__6925__auto__ = ((function (this$__$1){
return (function org$nfrac$comportex$encoders$iter__70338(s__70339){
return (new cljs.core.LazySeq(null,((function (this$__$1){
return (function (){
var s__70339__$1 = s__70339;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__70339__$1);
if(temp__4657__auto__){
var xs__5205__auto__ = temp__4657__auto__;
var x = cljs.core.first(xs__5205__auto__);
var iterys__6921__auto__ = ((function (s__70339__$1,x,xs__5205__auto__,temp__4657__auto__,this$__$1){
return (function org$nfrac$comportex$encoders$iter__70338_$_iter__70340(s__70341){
return (new cljs.core.LazySeq(null,((function (s__70339__$1,x,xs__5205__auto__,temp__4657__auto__,this$__$1){
return (function (){
var s__70341__$1 = s__70341;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__70341__$1);
if(temp__4657__auto____$1){
var s__70341__$2 = temp__4657__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__70341__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__70341__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__70343 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__70342 = (0);
while(true){
if((i__70342 < size__6924__auto__)){
var y = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__70342);
cljs.core.chunk_append(b__70343,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x,y], null));

var G__70353 = (i__70342 + (1));
i__70342 = G__70353;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__70343),org$nfrac$comportex$encoders$iter__70338_$_iter__70340(cljs.core.chunk_rest(s__70341__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__70343),null);
}
} else {
var y = cljs.core.first(s__70341__$2);
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x,y], null),org$nfrac$comportex$encoders$iter__70338_$_iter__70340(cljs.core.rest(s__70341__$2)));
}
} else {
return null;
}
break;
}
});})(s__70339__$1,x,xs__5205__auto__,temp__4657__auto__,this$__$1))
,null,null));
});})(s__70339__$1,x,xs__5205__auto__,temp__4657__auto__,this$__$1))
;
var fs__6922__auto__ = cljs.core.seq(iterys__6921__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$1(self__.y_max)));
if(fs__6922__auto__){
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2(fs__6922__auto__,org$nfrac$comportex$encoders$iter__70338(cljs.core.rest(s__70339__$1)));
} else {
var G__70354 = cljs.core.rest(s__70339__$1);
s__70339__$1 = G__70354;
continue;
}
} else {
return null;
}
break;
}
});})(this$__$1))
,null,null));
});})(this$__$1))
;
return iter__6925__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$1(self__.x_max));
})();
return cljs.core.take.cljs$core$IFn$_invoke$arity$2(n,org.nfrac.comportex.encoders.decode_by_brute_force(this$__$1,values,bit_votes));
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$topo,null,cljs.core.cst$kw$x_DASH_max,null,cljs.core.cst$kw$n_DASH_active,null,cljs.core.cst$kw$y_DASH_max,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.Linear2DEncoder(self__.topo,self__.n_active,self__.x_max,self__.y_max,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70331){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70349 = cljs.core.keyword_identical_QMARK_;
var expr__70350 = k__6775__auto__;
if(cljs.core.truth_((pred__70349.cljs$core$IFn$_invoke$arity$2 ? pred__70349.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$topo,expr__70350) : pred__70349.call(null,cljs.core.cst$kw$topo,expr__70350)))){
return (new org.nfrac.comportex.encoders.Linear2DEncoder(G__70331,self__.n_active,self__.x_max,self__.y_max,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70349.cljs$core$IFn$_invoke$arity$2 ? pred__70349.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$n_DASH_active,expr__70350) : pred__70349.call(null,cljs.core.cst$kw$n_DASH_active,expr__70350)))){
return (new org.nfrac.comportex.encoders.Linear2DEncoder(self__.topo,G__70331,self__.x_max,self__.y_max,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70349.cljs$core$IFn$_invoke$arity$2 ? pred__70349.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$x_DASH_max,expr__70350) : pred__70349.call(null,cljs.core.cst$kw$x_DASH_max,expr__70350)))){
return (new org.nfrac.comportex.encoders.Linear2DEncoder(self__.topo,self__.n_active,G__70331,self__.y_max,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70349.cljs$core$IFn$_invoke$arity$2 ? pred__70349.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$y_DASH_max,expr__70350) : pred__70349.call(null,cljs.core.cst$kw$y_DASH_max,expr__70350)))){
return (new org.nfrac.comportex.encoders.Linear2DEncoder(self__.topo,self__.n_active,self__.x_max,G__70331,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.Linear2DEncoder(self__.topo,self__.n_active,self__.x_max,self__.y_max,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70331),null));
}
}
}
}
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$x_DASH_max,self__.x_max],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$y_DASH_max,self__.y_max],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70331){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.Linear2DEncoder(self__.topo,self__.n_active,self__.x_max,self__.y_max,G__70331,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.Linear2DEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.Linear2DEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$topo,cljs.core.cst$sym$n_DASH_active,cljs.core.cst$sym$x_DASH_max,cljs.core.cst$sym$y_DASH_max], null);
});

org.nfrac.comportex.encoders.Linear2DEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.Linear2DEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/Linear2DEncoder");
});

org.nfrac.comportex.encoders.Linear2DEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/Linear2DEncoder");
});

org.nfrac.comportex.encoders.__GT_Linear2DEncoder = (function org$nfrac$comportex$encoders$__GT_Linear2DEncoder(topo,n_active,x_max,y_max){
return (new org.nfrac.comportex.encoders.Linear2DEncoder(topo,n_active,x_max,y_max,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_Linear2DEncoder = (function org$nfrac$comportex$encoders$map__GT_Linear2DEncoder(G__70333){
return (new org.nfrac.comportex.encoders.Linear2DEncoder(cljs.core.cst$kw$topo.cljs$core$IFn$_invoke$arity$1(G__70333),cljs.core.cst$kw$n_DASH_active.cljs$core$IFn$_invoke$arity$1(G__70333),cljs.core.cst$kw$x_DASH_max.cljs$core$IFn$_invoke$arity$1(G__70333),cljs.core.cst$kw$y_DASH_max.cljs$core$IFn$_invoke$arity$1(G__70333),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__70333,cljs.core.cst$kw$topo,cljs.core.array_seq([cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$x_DASH_max,cljs.core.cst$kw$y_DASH_max], 0)),null));
});

/**
 * Returns a simple encoder for a tuple of two numbers representing a
 *   position in rectangular bounds. The encoder maps input spatial
 *   positions to boxes of active bits in corresponding spatial positions
 *   of the encoded sense. So input positions close in both coordinates
 *   will have overlapping bit sets.
 * 
 *   * `dimensions` - of the encoded bits, given as a vector [nx ny].
 * 
 *   * `n-active` is the number of bits to be active.
 * 
 *   * `[x-max y-max]` gives the numeric range of input space to
 *   cover. The numbers will be clamped to this range, and below by
 *   zero.
 */
org.nfrac.comportex.encoders.linear_2d_encoder = (function org$nfrac$comportex$encoders$linear_2d_encoder(dimensions,n_active,p__70355){
var vec__70357 = p__70355;
var x_max = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70357,(0),null);
var y_max = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70357,(1),null);
var topo = org.nfrac.comportex.topology.make_topology(dimensions);
return org.nfrac.comportex.encoders.map__GT_Linear2DEncoder(new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$topo,topo,cljs.core.cst$kw$n_DASH_active,n_active,cljs.core.cst$kw$x_DASH_max,x_max,cljs.core.cst$kw$y_DASH_max,y_max], null));
});
org.nfrac.comportex.encoders.coordinate_neighbours = (function org$nfrac$comportex$encoders$coordinate_neighbours(coord,radii){
var G__70401 = cljs.core.count(coord);
switch (G__70401) {
case (1):
var vec__70402 = coord;
var cx = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70402,(0),null);
var vec__70403 = radii;
var rx = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70403,(0),null);
var iter__6925__auto__ = ((function (vec__70402,cx,vec__70403,rx,G__70401){
return (function org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70404(s__70405){
return (new cljs.core.LazySeq(null,((function (vec__70402,cx,vec__70403,rx,G__70401){
return (function (){
var s__70405__$1 = s__70405;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__70405__$1);
if(temp__4657__auto__){
var s__70405__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__70405__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__70405__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__70407 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__70406 = (0);
while(true){
if((i__70406 < size__6924__auto__)){
var x = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__70406);
cljs.core.chunk_append(b__70407,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [x], null));

var G__70445 = (i__70406 + (1));
i__70406 = G__70445;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__70407),org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70404(cljs.core.chunk_rest(s__70405__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__70407),null);
}
} else {
var x = cljs.core.first(s__70405__$2);
return cljs.core.cons(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [x], null),org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70404(cljs.core.rest(s__70405__$2)));
}
} else {
return null;
}
break;
}
});})(vec__70402,cx,vec__70403,rx,G__70401))
,null,null));
});})(vec__70402,cx,vec__70403,rx,G__70401))
;
return iter__6925__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$2((cx - rx),((cx + rx) + (1))));

break;
case (2):
var vec__70410 = coord;
var cx = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70410,(0),null);
var cy = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70410,(1),null);
var vec__70411 = radii;
var rx = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70411,(0),null);
var ry = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70411,(1),null);
var iter__6925__auto__ = ((function (vec__70410,cx,cy,vec__70411,rx,ry,G__70401){
return (function org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70412(s__70413){
return (new cljs.core.LazySeq(null,((function (vec__70410,cx,cy,vec__70411,rx,ry,G__70401){
return (function (){
var s__70413__$1 = s__70413;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__70413__$1);
if(temp__4657__auto__){
var xs__5205__auto__ = temp__4657__auto__;
var x = cljs.core.first(xs__5205__auto__);
var iterys__6921__auto__ = ((function (s__70413__$1,x,xs__5205__auto__,temp__4657__auto__,vec__70410,cx,cy,vec__70411,rx,ry,G__70401){
return (function org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70412_$_iter__70414(s__70415){
return (new cljs.core.LazySeq(null,((function (s__70413__$1,x,xs__5205__auto__,temp__4657__auto__,vec__70410,cx,cy,vec__70411,rx,ry,G__70401){
return (function (){
var s__70415__$1 = s__70415;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__70415__$1);
if(temp__4657__auto____$1){
var s__70415__$2 = temp__4657__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__70415__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__70415__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__70417 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__70416 = (0);
while(true){
if((i__70416 < size__6924__auto__)){
var y = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__70416);
cljs.core.chunk_append(b__70417,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x,y], null));

var G__70446 = (i__70416 + (1));
i__70416 = G__70446;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__70417),org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70412_$_iter__70414(cljs.core.chunk_rest(s__70415__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__70417),null);
}
} else {
var y = cljs.core.first(s__70415__$2);
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [x,y], null),org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70412_$_iter__70414(cljs.core.rest(s__70415__$2)));
}
} else {
return null;
}
break;
}
});})(s__70413__$1,x,xs__5205__auto__,temp__4657__auto__,vec__70410,cx,cy,vec__70411,rx,ry,G__70401))
,null,null));
});})(s__70413__$1,x,xs__5205__auto__,temp__4657__auto__,vec__70410,cx,cy,vec__70411,rx,ry,G__70401))
;
var fs__6922__auto__ = cljs.core.seq(iterys__6921__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$2((cy - ry),((cy + ry) + (1)))));
if(fs__6922__auto__){
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2(fs__6922__auto__,org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70412(cljs.core.rest(s__70413__$1)));
} else {
var G__70447 = cljs.core.rest(s__70413__$1);
s__70413__$1 = G__70447;
continue;
}
} else {
return null;
}
break;
}
});})(vec__70410,cx,cy,vec__70411,rx,ry,G__70401))
,null,null));
});})(vec__70410,cx,cy,vec__70411,rx,ry,G__70401))
;
return iter__6925__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$2((cx - rx),((cx + rx) + (1))));

break;
case (3):
var vec__70423 = coord;
var cx = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70423,(0),null);
var cy = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70423,(1),null);
var cz = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70423,(2),null);
var vec__70424 = radii;
var rx = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70424,(0),null);
var ry = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70424,(1),null);
var rz = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70424,(2),null);
var iter__6925__auto__ = ((function (vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401){
return (function org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70425(s__70426){
return (new cljs.core.LazySeq(null,((function (vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401){
return (function (){
var s__70426__$1 = s__70426;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__70426__$1);
if(temp__4657__auto__){
var xs__5205__auto__ = temp__4657__auto__;
var x = cljs.core.first(xs__5205__auto__);
var iterys__6921__auto__ = ((function (s__70426__$1,x,xs__5205__auto__,temp__4657__auto__,vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401){
return (function org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70425_$_iter__70427(s__70428){
return (new cljs.core.LazySeq(null,((function (s__70426__$1,x,xs__5205__auto__,temp__4657__auto__,vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401){
return (function (){
var s__70428__$1 = s__70428;
while(true){
var temp__4657__auto____$1 = cljs.core.seq(s__70428__$1);
if(temp__4657__auto____$1){
var xs__5205__auto____$1 = temp__4657__auto____$1;
var y = cljs.core.first(xs__5205__auto____$1);
var iterys__6921__auto__ = ((function (s__70428__$1,s__70426__$1,y,xs__5205__auto____$1,temp__4657__auto____$1,x,xs__5205__auto__,temp__4657__auto__,vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401){
return (function org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70425_$_iter__70427_$_iter__70429(s__70430){
return (new cljs.core.LazySeq(null,((function (s__70428__$1,s__70426__$1,y,xs__5205__auto____$1,temp__4657__auto____$1,x,xs__5205__auto__,temp__4657__auto__,vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401){
return (function (){
var s__70430__$1 = s__70430;
while(true){
var temp__4657__auto____$2 = cljs.core.seq(s__70430__$1);
if(temp__4657__auto____$2){
var s__70430__$2 = temp__4657__auto____$2;
if(cljs.core.chunked_seq_QMARK_(s__70430__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__70430__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__70432 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__70431 = (0);
while(true){
if((i__70431 < size__6924__auto__)){
var z = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__70431);
cljs.core.chunk_append(b__70432,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [x,y,z], null));

var G__70448 = (i__70431 + (1));
i__70431 = G__70448;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__70432),org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70425_$_iter__70427_$_iter__70429(cljs.core.chunk_rest(s__70430__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__70432),null);
}
} else {
var z = cljs.core.first(s__70430__$2);
return cljs.core.cons(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [x,y,z], null),org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70425_$_iter__70427_$_iter__70429(cljs.core.rest(s__70430__$2)));
}
} else {
return null;
}
break;
}
});})(s__70428__$1,s__70426__$1,y,xs__5205__auto____$1,temp__4657__auto____$1,x,xs__5205__auto__,temp__4657__auto__,vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401))
,null,null));
});})(s__70428__$1,s__70426__$1,y,xs__5205__auto____$1,temp__4657__auto____$1,x,xs__5205__auto__,temp__4657__auto__,vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401))
;
var fs__6922__auto__ = cljs.core.seq(iterys__6921__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$2((cz - rz),((cz + rz) + (1)))));
if(fs__6922__auto__){
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2(fs__6922__auto__,org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70425_$_iter__70427(cljs.core.rest(s__70428__$1)));
} else {
var G__70449 = cljs.core.rest(s__70428__$1);
s__70428__$1 = G__70449;
continue;
}
} else {
return null;
}
break;
}
});})(s__70426__$1,x,xs__5205__auto__,temp__4657__auto__,vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401))
,null,null));
});})(s__70426__$1,x,xs__5205__auto__,temp__4657__auto__,vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401))
;
var fs__6922__auto__ = cljs.core.seq(iterys__6921__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$2((cy - ry),((cy + ry) + (1)))));
if(fs__6922__auto__){
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2(fs__6922__auto__,org$nfrac$comportex$encoders$coordinate_neighbours_$_iter__70425(cljs.core.rest(s__70426__$1)));
} else {
var G__70450 = cljs.core.rest(s__70426__$1);
s__70426__$1 = G__70450;
continue;
}
} else {
return null;
}
break;
}
});})(vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401))
,null,null));
});})(vec__70423,cx,cy,cz,vec__70424,rx,ry,rz,G__70401))
;
return iter__6925__auto__(cljs.core.range.cljs$core$IFn$_invoke$arity$2((cx - rx),((cx + rx) + (1))));

break;
default:
throw (new Error([cljs.core.str("No matching clause: "),cljs.core.str(cljs.core.count(coord))].join('')));

}
});
org.nfrac.comportex.encoders.coordinate_order = (function org$nfrac$comportex$encoders$coordinate_order(coord){
return clojure.test.check.random.rand_double(clojure.test.check.random.make_random.cljs$core$IFn$_invoke$arity$1(cljs.core.hash([cljs.core.str(coord)].join(''))));
});
org.nfrac.comportex.encoders.coordinate_bit = (function org$nfrac$comportex$encoders$coordinate_bit(size,coord){
return org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$2(cljs.core.second(clojure.test.check.random.split(clojure.test.check.random.make_random.cljs$core$IFn$_invoke$arity$1(cljs.core.hash([cljs.core.str(coord)].join(''))))),size);
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
org.nfrac.comportex.encoders.CoordinateEncoder = (function (topo,n_active,scale_factors,radii,__meta,__extmap,__hash){
this.topo = topo;
this.n_active = n_active;
this.scale_factors = scale_factors;
this.radii = radii;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70452,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70454 = (((k70452 instanceof cljs.core.Keyword))?k70452.fqn:null);
switch (G__70454) {
case "topo":
return self__.topo;

break;
case "n-active":
return self__.n_active;

break;
case "scale-factors":
return self__.scale_factors;

break;
case "radii":
return self__.radii;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70452,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.topo;
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.CoordinateEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$scale_DASH_factors,self__.scale_factors],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$radii,self__.radii],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70451){
var self__ = this;
var G__70451__$1 = this;
return (new cljs.core.RecordIter((0),G__70451__$1,4,new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$topo,cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$scale_DASH_factors,cljs.core.cst$kw$radii], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.CoordinateEncoder(self__.topo,self__.n_active,self__.scale_factors,self__.radii,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (4 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,coord){
var self__ = this;
var ___$1 = this;
if(cljs.core.truth_(cljs.core.first(coord))){
var int_coord = cljs.core.map.cljs$core$IFn$_invoke$arity$3(cljs.core.comp.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.util.round,cljs.core._STAR_),coord,self__.scale_factors);
var neighs = org.nfrac.comportex.encoders.coordinate_neighbours(int_coord,self__.radii);
return cljs.core.distinct.cljs$core$IFn$_invoke$arity$1(cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.partial.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.encoders.coordinate_bit,org.nfrac.comportex.protocols.size(self__.topo)),org.nfrac.comportex.util.top_n_keys_by_value(self__.n_active,cljs.core.zipmap(neighs,cljs.core.map.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.encoders.coordinate_order,neighs)))));
} else {
return null;
}
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$radii,null,cljs.core.cst$kw$topo,null,cljs.core.cst$kw$n_DASH_active,null,cljs.core.cst$kw$scale_DASH_factors,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.CoordinateEncoder(self__.topo,self__.n_active,self__.scale_factors,self__.radii,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70451){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70455 = cljs.core.keyword_identical_QMARK_;
var expr__70456 = k__6775__auto__;
if(cljs.core.truth_((pred__70455.cljs$core$IFn$_invoke$arity$2 ? pred__70455.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$topo,expr__70456) : pred__70455.call(null,cljs.core.cst$kw$topo,expr__70456)))){
return (new org.nfrac.comportex.encoders.CoordinateEncoder(G__70451,self__.n_active,self__.scale_factors,self__.radii,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70455.cljs$core$IFn$_invoke$arity$2 ? pred__70455.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$n_DASH_active,expr__70456) : pred__70455.call(null,cljs.core.cst$kw$n_DASH_active,expr__70456)))){
return (new org.nfrac.comportex.encoders.CoordinateEncoder(self__.topo,G__70451,self__.scale_factors,self__.radii,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70455.cljs$core$IFn$_invoke$arity$2 ? pred__70455.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$scale_DASH_factors,expr__70456) : pred__70455.call(null,cljs.core.cst$kw$scale_DASH_factors,expr__70456)))){
return (new org.nfrac.comportex.encoders.CoordinateEncoder(self__.topo,self__.n_active,G__70451,self__.radii,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70455.cljs$core$IFn$_invoke$arity$2 ? pred__70455.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$radii,expr__70456) : pred__70455.call(null,cljs.core.cst$kw$radii,expr__70456)))){
return (new org.nfrac.comportex.encoders.CoordinateEncoder(self__.topo,self__.n_active,self__.scale_factors,G__70451,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.CoordinateEncoder(self__.topo,self__.n_active,self__.scale_factors,self__.radii,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70451),null));
}
}
}
}
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$scale_DASH_factors,self__.scale_factors],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$radii,self__.radii],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70451){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.CoordinateEncoder(self__.topo,self__.n_active,self__.scale_factors,self__.radii,G__70451,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.CoordinateEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.CoordinateEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 4, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$topo,cljs.core.cst$sym$n_DASH_active,cljs.core.cst$sym$scale_DASH_factors,cljs.core.cst$sym$radii], null);
});

org.nfrac.comportex.encoders.CoordinateEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.CoordinateEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/CoordinateEncoder");
});

org.nfrac.comportex.encoders.CoordinateEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/CoordinateEncoder");
});

org.nfrac.comportex.encoders.__GT_CoordinateEncoder = (function org$nfrac$comportex$encoders$__GT_CoordinateEncoder(topo,n_active,scale_factors,radii){
return (new org.nfrac.comportex.encoders.CoordinateEncoder(topo,n_active,scale_factors,radii,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_CoordinateEncoder = (function org$nfrac$comportex$encoders$map__GT_CoordinateEncoder(G__70453){
return (new org.nfrac.comportex.encoders.CoordinateEncoder(cljs.core.cst$kw$topo.cljs$core$IFn$_invoke$arity$1(G__70453),cljs.core.cst$kw$n_DASH_active.cljs$core$IFn$_invoke$arity$1(G__70453),cljs.core.cst$kw$scale_DASH_factors.cljs$core$IFn$_invoke$arity$1(G__70453),cljs.core.cst$kw$radii.cljs$core$IFn$_invoke$arity$1(G__70453),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__70453,cljs.core.cst$kw$topo,cljs.core.array_seq([cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$scale_DASH_factors,cljs.core.cst$kw$radii], 0)),null));
});

/**
 * Coordinate encoder for integer coordinates, unbounded, with one,
 *   two or three dimensions. Expects a coordinate, i.e. a sequence of
 *   numbers with 1, 2 or 3 elements. These raw values will be multiplied
 *   by corresponding `scale-factors` to obtain integer grid
 *   coordinates. Each dimension has an associated radius within which
 *   there is some similarity in encoded SDRs.
 */
org.nfrac.comportex.encoders.coordinate_encoder = (function org$nfrac$comportex$encoders$coordinate_encoder(dimensions,n_active,scale_factors,radii){
var topo = org.nfrac.comportex.topology.make_topology(dimensions);
return org.nfrac.comportex.encoders.map__GT_CoordinateEncoder(new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$topo,topo,cljs.core.cst$kw$n_DASH_active,n_active,cljs.core.cst$kw$scale_DASH_factors,scale_factors,cljs.core.cst$kw$radii,radii], null));
});
/**
 * By example:
 *   Given 7.2, returns (7, 8, 6, 9, 5, 10, ...),
 *   Given 7.7, returns (8, 7, 9, 6, 10, 5, ...)
 */
org.nfrac.comportex.encoders.middle_out_range = (function org$nfrac$comportex$encoders$middle_out_range(v){
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
org.nfrac.comportex.encoders.multiples_within_radius = (function org$nfrac$comportex$encoders$multiples_within_radius(center,radius,multiples_of){
var lower_bound = (center - radius);
var upper_bound = (center + radius);
return cljs.core.take_while.cljs$core$IFn$_invoke$arity$2(((function (lower_bound,upper_bound){
return (function (p1__70459_SHARP_){
return ((lower_bound <= p1__70459_SHARP_)) && ((p1__70459_SHARP_ <= upper_bound));
});})(lower_bound,upper_bound))
,cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.partial.cljs$core$IFn$_invoke$arity$2(cljs.core._STAR_,multiples_of),org.nfrac.comportex.encoders.middle_out_range((center / multiples_of))));
});
org.nfrac.comportex.encoders.handle_multiples_at_edges = (function org$nfrac$comportex$encoders$handle_multiples_at_edges(periodic_QMARK_,n_bits,multiples_of,coll){
if(cljs.core.not(periodic_QMARK_)){
return cljs.core.filter.cljs$core$IFn$_invoke$arity$2((function (p1__70460_SHARP_){
return (((0) <= p1__70460_SHARP_)) && ((p1__70460_SHARP_ <= (n_bits - (1))));
}),coll);
} else {
var m_wrap = ((cljs.core.quot((n_bits - (1)),multiples_of) + (1)) * multiples_of);
return cljs.core.map.cljs$core$IFn$_invoke$arity$2(((function (m_wrap){
return (function (p1__70461_SHARP_){
return cljs.core.mod(p1__70461_SHARP_,m_wrap);
});})(m_wrap))
,coll);
}
});
/**
 * Move items from `from` to `coll` until its size reaches `max-size`
 *   or we run out of items. Specifically supports sets and maps, which don't
 *   always grow when an item is added.
 */
org.nfrac.comportex.encoders.into_bounded = (function org$nfrac$comportex$encoders$into_bounded(coll,max_size,from){
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
var vec__70463 = cljs.core.split_at(n_remaining,from__$1);
var taken = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70463,(0),null);
var untaken = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70463,(1),null);
var G__70464 = cljs.core.into.cljs$core$IFn$_invoke$arity$2(coll__$1,taken);
var G__70465 = untaken;
coll__$1 = G__70464;
from__$1 = G__70465;
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
org.nfrac.comportex.encoders.sampled_window = (function org$nfrac$comportex$encoders$sampled_window(center,n_bits,target_n_active,bit_radius,periodic_QMARK_){
var chosen = cljs.core.PersistentHashSet.fromArray([center], true);
var density = (((target_n_active - cljs.core.count(chosen)) / ((2) * bit_radius)) / (2));
while(true){
var remaining = (target_n_active - cljs.core.count(chosen));
var multiples_of = cljs.core.long$(((1) / density));
if(((remaining > (0))) && ((multiples_of > (0)))){
var half_remaining = cljs.core.quot(remaining,(2));
var n_take = ((((1) === remaining))?remaining:half_remaining);
var G__70466 = org.nfrac.comportex.encoders.into_bounded(chosen,(n_take + cljs.core.count(chosen)),org.nfrac.comportex.encoders.handle_multiples_at_edges(periodic_QMARK_,n_bits,multiples_of,org.nfrac.comportex.encoders.multiples_within_radius(center,bit_radius,multiples_of)));
var G__70467 = (density * (2));
chosen = G__70466;
density = G__70467;
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
org.nfrac.comportex.encoders.SamplingLinearEncoder = (function (topo,n_active,lower,upper,radius,periodic_QMARK_,__meta,__extmap,__hash){
this.topo = topo;
this.n_active = n_active;
this.lower = lower;
this.upper = upper;
this.radius = radius;
this.periodic_QMARK_ = periodic_QMARK_;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2229667594;
this.cljs$lang$protocol_mask$partition1$ = 8192;
})
org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__6767__auto__,k__6768__auto__){
var self__ = this;
var this__6767__auto____$1 = this;
return cljs.core._lookup.cljs$core$IFn$_invoke$arity$3(this__6767__auto____$1,k__6768__auto__,null);
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__6769__auto__,k70469,else__6770__auto__){
var self__ = this;
var this__6769__auto____$1 = this;
var G__70471 = (((k70469 instanceof cljs.core.Keyword))?k70469.fqn:null);
switch (G__70471) {
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
case "periodic?":
return self__.periodic_QMARK_;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k70469,else__6770__auto__);

}
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PTopological$ = true;

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PTopological$topology$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.topo;
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__6781__auto__,writer__6782__auto__,opts__6783__auto__){
var self__ = this;
var this__6781__auto____$1 = this;
var pr_pair__6784__auto__ = ((function (this__6781__auto____$1){
return (function (keyval__6785__auto__){
return cljs.core.pr_sequential_writer(writer__6782__auto__,cljs.core.pr_writer,""," ","",opts__6783__auto__,keyval__6785__auto__);
});})(this__6781__auto____$1))
;
return cljs.core.pr_sequential_writer(writer__6782__auto__,pr_pair__6784__auto__,"#org.nfrac.comportex.encoders.SamplingLinearEncoder{",", ","}",opts__6783__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$lower,self__.lower],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$upper,self__.upper],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$radius,self__.radius],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$periodic_QMARK_,self__.periodic_QMARK_],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IIterable$ = true;

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__70468){
var self__ = this;
var G__70468__$1 = this;
return (new cljs.core.RecordIter((0),G__70468__$1,6,new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$topo,cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$lower,cljs.core.cst$kw$upper,cljs.core.cst$kw$radius,cljs.core.cst$kw$periodic_QMARK_], null),cljs.core._iterator(self__.__extmap)));
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__6765__auto__){
var self__ = this;
var this__6765__auto____$1 = this;
return self__.__meta;
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__6761__auto__){
var self__ = this;
var this__6761__auto____$1 = this;
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,self__.periodic_QMARK_,self__.__meta,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__6771__auto__){
var self__ = this;
var this__6771__auto____$1 = this;
return (6 + cljs.core.count(self__.__extmap));
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__6762__auto__){
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

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this__6763__auto__,other__6764__auto__){
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

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$ = true;

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$encode$arity$2 = (function (_,x){
var self__ = this;
var ___$1 = this;
if(cljs.core.truth_(x)){
var n_bits = org.nfrac.comportex.protocols.size(self__.topo);
var domain_width = (self__.upper - self__.lower);
var z = ((x - self__.lower) / domain_width);
var center = (cljs.core.truth_(self__.periodic_QMARK_)?cljs.core.long$((cljs.core.mod(z,1.0) * (n_bits - (1)))):cljs.core.long$(((function (){var x__6491__auto__ = (function (){var x__6484__auto__ = z;
var y__6485__auto__ = 0.0;
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})();
var y__6492__auto__ = 1.0;
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
})() * (n_bits - (1)))));
var bit_radius = (self__.radius * (org.nfrac.comportex.protocols.size(self__.topo) / domain_width));
return org.nfrac.comportex.encoders.sampled_window(center,n_bits,self__.n_active,bit_radius,self__.periodic_QMARK_);
} else {
return cljs.core.sequence.cljs$core$IFn$_invoke$arity$1(null);
}
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.org$nfrac$comportex$protocols$PEncoder$decode$arity$3 = (function (this$,bit_votes,n){
var self__ = this;
var this$__$1 = this;
var span = (self__.upper - self__.lower);
var values = cljs.core.range.cljs$core$IFn$_invoke$arity$3(self__.lower,self__.upper,(((((5) < span)) && ((span < (250))))?(1):(span / (50))));
return cljs.core.take.cljs$core$IFn$_invoke$arity$2(n,org.nfrac.comportex.encoders.decode_by_brute_force(this$__$1,values,bit_votes));
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__6776__auto__,k__6777__auto__){
var self__ = this;
var this__6776__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 6, [cljs.core.cst$kw$upper,null,cljs.core.cst$kw$topo,null,cljs.core.cst$kw$radius,null,cljs.core.cst$kw$periodic_QMARK_,null,cljs.core.cst$kw$lower,null,cljs.core.cst$kw$n_DASH_active,null], null), null),k__6777__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core.with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__6776__auto____$1),self__.__meta),k__6777__auto__);
} else {
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,self__.periodic_QMARK_,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__6777__auto__)),null));
}
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__6774__auto__,k__6775__auto__,G__70468){
var self__ = this;
var this__6774__auto____$1 = this;
var pred__70472 = cljs.core.keyword_identical_QMARK_;
var expr__70473 = k__6775__auto__;
if(cljs.core.truth_((pred__70472.cljs$core$IFn$_invoke$arity$2 ? pred__70472.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$topo,expr__70473) : pred__70472.call(null,cljs.core.cst$kw$topo,expr__70473)))){
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(G__70468,self__.n_active,self__.lower,self__.upper,self__.radius,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70472.cljs$core$IFn$_invoke$arity$2 ? pred__70472.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$n_DASH_active,expr__70473) : pred__70472.call(null,cljs.core.cst$kw$n_DASH_active,expr__70473)))){
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,G__70468,self__.lower,self__.upper,self__.radius,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70472.cljs$core$IFn$_invoke$arity$2 ? pred__70472.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$lower,expr__70473) : pred__70472.call(null,cljs.core.cst$kw$lower,expr__70473)))){
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,self__.n_active,G__70468,self__.upper,self__.radius,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70472.cljs$core$IFn$_invoke$arity$2 ? pred__70472.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$upper,expr__70473) : pred__70472.call(null,cljs.core.cst$kw$upper,expr__70473)))){
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,G__70468,self__.radius,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70472.cljs$core$IFn$_invoke$arity$2 ? pred__70472.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$radius,expr__70473) : pred__70472.call(null,cljs.core.cst$kw$radius,expr__70473)))){
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,G__70468,self__.periodic_QMARK_,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__70472.cljs$core$IFn$_invoke$arity$2 ? pred__70472.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$periodic_QMARK_,expr__70473) : pred__70472.call(null,cljs.core.cst$kw$periodic_QMARK_,expr__70473)))){
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,G__70468,self__.__meta,self__.__extmap,null));
} else {
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,self__.periodic_QMARK_,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__6775__auto__,G__70468),null));
}
}
}
}
}
}
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__6779__auto__){
var self__ = this;
var this__6779__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$topo,self__.topo],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$n_DASH_active,self__.n_active],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$lower,self__.lower],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$upper,self__.upper],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$radius,self__.radius],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[cljs.core.cst$kw$periodic_QMARK_,self__.periodic_QMARK_],null))], null),self__.__extmap));
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__6766__auto__,G__70468){
var self__ = this;
var this__6766__auto____$1 = this;
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(self__.topo,self__.n_active,self__.lower,self__.upper,self__.radius,self__.periodic_QMARK_,G__70468,self__.__extmap,self__.__hash));
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__6772__auto__,entry__6773__auto__){
var self__ = this;
var this__6772__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__6773__auto__)){
return cljs.core._assoc(this__6772__auto____$1,cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(0)),cljs.core._nth.cljs$core$IFn$_invoke$arity$2(entry__6773__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__6772__auto____$1,entry__6773__auto__);
}
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.getBasis = (function (){
return new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$topo,cljs.core.cst$sym$n_DASH_active,cljs.core.cst$sym$lower,cljs.core.cst$sym$upper,cljs.core.cst$sym$radius,cljs.core.cst$sym$periodic_QMARK_], null);
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.cljs$lang$type = true;

org.nfrac.comportex.encoders.SamplingLinearEncoder.cljs$lang$ctorPrSeq = (function (this__6801__auto__){
return cljs.core._conj(cljs.core.List.EMPTY,"org.nfrac.comportex.encoders/SamplingLinearEncoder");
});

org.nfrac.comportex.encoders.SamplingLinearEncoder.cljs$lang$ctorPrWriter = (function (this__6801__auto__,writer__6802__auto__){
return cljs.core._write(writer__6802__auto__,"org.nfrac.comportex.encoders/SamplingLinearEncoder");
});

org.nfrac.comportex.encoders.__GT_SamplingLinearEncoder = (function org$nfrac$comportex$encoders$__GT_SamplingLinearEncoder(topo,n_active,lower,upper,radius,periodic_QMARK_){
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(topo,n_active,lower,upper,radius,periodic_QMARK_,null,null,null));
});

org.nfrac.comportex.encoders.map__GT_SamplingLinearEncoder = (function org$nfrac$comportex$encoders$map__GT_SamplingLinearEncoder(G__70470){
return (new org.nfrac.comportex.encoders.SamplingLinearEncoder(cljs.core.cst$kw$topo.cljs$core$IFn$_invoke$arity$1(G__70470),cljs.core.cst$kw$n_DASH_active.cljs$core$IFn$_invoke$arity$1(G__70470),cljs.core.cst$kw$lower.cljs$core$IFn$_invoke$arity$1(G__70470),cljs.core.cst$kw$upper.cljs$core$IFn$_invoke$arity$1(G__70470),cljs.core.cst$kw$radius.cljs$core$IFn$_invoke$arity$1(G__70470),cljs.core.cst$kw$periodic_QMARK_.cljs$core$IFn$_invoke$arity$1(G__70470),null,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__70470,cljs.core.cst$kw$topo,cljs.core.array_seq([cljs.core.cst$kw$n_DASH_active,cljs.core.cst$kw$lower,cljs.core.cst$kw$upper,cljs.core.cst$kw$radius,cljs.core.cst$kw$periodic_QMARK_], 0)),null));
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
org.nfrac.comportex.encoders.sampling_linear_encoder = (function org$nfrac$comportex$encoders$sampling_linear_encoder(var_args){
var args70476 = [];
var len__7211__auto___70483 = arguments.length;
var i__7212__auto___70484 = (0);
while(true){
if((i__7212__auto___70484 < len__7211__auto___70483)){
args70476.push((arguments[i__7212__auto___70484]));

var G__70485 = (i__7212__auto___70484 + (1));
i__7212__auto___70484 = G__70485;
continue;
} else {
}
break;
}

var G__70478 = args70476.length;
switch (G__70478) {
case 4:
return org.nfrac.comportex.encoders.sampling_linear_encoder.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
case 5:
return org.nfrac.comportex.encoders.sampling_linear_encoder.cljs$core$IFn$_invoke$arity$5((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]),(arguments[(4)]));

break;
default:
throw (new Error([cljs.core.str("Invalid arity: "),cljs.core.str(args70476.length)].join('')));

}
});

org.nfrac.comportex.encoders.sampling_linear_encoder.cljs$core$IFn$_invoke$arity$4 = (function (dimensions,n_active,p__70479,radius){
var vec__70480 = p__70479;
var lower = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70480,(0),null);
var upper = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70480,(1),null);
return org.nfrac.comportex.encoders.sampling_linear_encoder.cljs$core$IFn$_invoke$arity$5(dimensions,n_active,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [lower,upper], null),radius,false);
});

org.nfrac.comportex.encoders.sampling_linear_encoder.cljs$core$IFn$_invoke$arity$5 = (function (dimensions,n_active,p__70481,radius,periodic_QMARK_){
var vec__70482 = p__70481;
var lower = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70482,(0),null);
var upper = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70482,(1),null);
var topo = org.nfrac.comportex.topology.make_topology(dimensions);
return org.nfrac.comportex.encoders.map__GT_SamplingLinearEncoder(new cljs.core.PersistentArrayMap(null, 6, [cljs.core.cst$kw$topo,topo,cljs.core.cst$kw$n_DASH_active,n_active,cljs.core.cst$kw$lower,lower,cljs.core.cst$kw$upper,upper,cljs.core.cst$kw$radius,radius,cljs.core.cst$kw$periodic_QMARK_,periodic_QMARK_], null));
});

org.nfrac.comportex.encoders.sampling_linear_encoder.cljs$lang$maxFixedArity = 5;
org.nfrac.comportex.encoders.sensor_cat = (function org$nfrac$comportex$encoders$sensor_cat(var_args){
var args__7218__auto__ = [];
var len__7211__auto___70488 = arguments.length;
var i__7212__auto___70489 = (0);
while(true){
if((i__7212__auto___70489 < len__7211__auto___70488)){
args__7218__auto__.push((arguments[i__7212__auto___70489]));

var G__70490 = (i__7212__auto___70489 + (1));
i__7212__auto___70489 = G__70490;
continue;
} else {
}
break;
}

var argseq__7219__auto__ = ((((0) < args__7218__auto__.length))?(new cljs.core.IndexedSeq(args__7218__auto__.slice((0)),(0))):null);
return org.nfrac.comportex.encoders.sensor_cat.cljs$core$IFn$_invoke$arity$variadic(argseq__7219__auto__);
});

org.nfrac.comportex.encoders.sensor_cat.cljs$core$IFn$_invoke$arity$variadic = (function (sensors){
var selectors = cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.first,sensors);
var encoders = cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.second,sensors);
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.apply.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.encoders.vec_selector,selectors),org.nfrac.comportex.encoders.encat(encoders)], null);
});

org.nfrac.comportex.encoders.sensor_cat.cljs$lang$maxFixedArity = (0);

org.nfrac.comportex.encoders.sensor_cat.cljs$lang$applyTo = (function (seq70487){
return org.nfrac.comportex.encoders.sensor_cat.cljs$core$IFn$_invoke$arity$variadic(cljs.core.seq(seq70487));
});
