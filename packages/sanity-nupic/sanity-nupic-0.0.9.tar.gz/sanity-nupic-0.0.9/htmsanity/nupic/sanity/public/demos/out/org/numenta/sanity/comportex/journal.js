// Compiled by ClojureScript 1.7.228 {:static-fns true, :optimize-constants true}
goog.provide('org.numenta.sanity.comportex.journal');
goog.require('cljs.core');
goog.require('clojure.set');
goog.require('org.nfrac.comportex.protocols');
goog.require('org.numenta.sanity.comportex.data');
goog.require('cljs.core.async');
goog.require('org.numenta.sanity.bridge.marshalling');
goog.require('org.numenta.sanity.comportex.details');
goog.require('org.nfrac.comportex.core');
goog.require('org.nfrac.comportex.util');
goog.require('clojure.walk');
org.numenta.sanity.comportex.journal.make_step = (function org$numenta$sanity$comportex$journal$make_step(htm,id){
var input_value = cljs.core.cst$kw$input_DASH_value.cljs$core$IFn$_invoke$arity$1(htm);
return new cljs.core.PersistentArrayMap(null, 4, ["snapshot-id",id,"timestep",org.nfrac.comportex.protocols.timestep(htm),"input-value",input_value,"sensed-values",cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,(function (){var iter__6925__auto__ = ((function (input_value){
return (function org$numenta$sanity$comportex$journal$make_step_$_iter__69569(s__69570){
return (new cljs.core.LazySeq(null,((function (input_value){
return (function (){
var s__69570__$1 = s__69570;
while(true){
var temp__4657__auto__ = cljs.core.seq(s__69570__$1);
if(temp__4657__auto__){
var s__69570__$2 = temp__4657__auto__;
if(cljs.core.chunked_seq_QMARK_(s__69570__$2)){
var c__6923__auto__ = cljs.core.chunk_first(s__69570__$2);
var size__6924__auto__ = cljs.core.count(c__6923__auto__);
var b__69572 = cljs.core.chunk_buffer(size__6924__auto__);
if((function (){var i__69571 = (0);
while(true){
if((i__69571 < size__6924__auto__)){
var sense_id = cljs.core._nth.cljs$core$IFn$_invoke$arity$2(c__6923__auto__,i__69571);
var vec__69577 = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$sensors,sense_id], null));
var selector = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69577,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69577,(1),null);
var v = org.nfrac.comportex.protocols.extract(selector,input_value);
cljs.core.chunk_append(b__69572,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [sense_id,v], null));

var G__69579 = (i__69571 + (1));
i__69571 = G__69579;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__69572),org$numenta$sanity$comportex$journal$make_step_$_iter__69569(cljs.core.chunk_rest(s__69570__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__69572),null);
}
} else {
var sense_id = cljs.core.first(s__69570__$2);
var vec__69578 = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$sensors,sense_id], null));
var selector = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69578,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69578,(1),null);
var v = org.nfrac.comportex.protocols.extract(selector,input_value);
return cljs.core.cons(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [sense_id,v], null),org$numenta$sanity$comportex$journal$make_step_$_iter__69569(cljs.core.rest(s__69570__$2)));
}
} else {
return null;
}
break;
}
});})(input_value))
,null,null));
});})(input_value))
;
return iter__6925__auto__(org.nfrac.comportex.core.sense_keys(htm));
})())], null);
});
org.numenta.sanity.comportex.journal.id_missing_response = (function org$numenta$sanity$comportex$journal$id_missing_response(id,steps_offset){
var offset = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(steps_offset) : cljs.core.deref.call(null,steps_offset));
if((offset > (0))){
if((id < offset)){
} else {
throw (new Error([cljs.core.str("Assert failed: "),cljs.core.str(cljs.core.pr_str.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([cljs.core.list(cljs.core.cst$sym$_LT_,cljs.core.cst$sym$id,cljs.core.cst$sym$offset)], 0)))].join('')));
}

cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([[cljs.core.str("Can't fetch model "),cljs.core.str(id),cljs.core.str(". We've dropped all models below id "),cljs.core.str(offset)].join('')], 0));
} else {
}

return cljs.core.PersistentArrayMap.EMPTY;
});
org.numenta.sanity.comportex.journal.command_handler = (function org$numenta$sanity$comportex$journal$command_handler(current_model,steps_offset,model_steps,steps_mult,client_infos,capture_options){
var find_model = (function org$numenta$sanity$comportex$journal$command_handler_$_find_model(id){
if(typeof id === 'number'){
var i = (id - (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(steps_offset) : cljs.core.deref.call(null,steps_offset)));
if((i < (0))){
return null;
} else {
return cljs.core.nth.cljs$core$IFn$_invoke$arity$3((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(model_steps) : cljs.core.deref.call(null,model_steps)),i,null);
}
} else {
return null;
}
});
var find_model_pair = (function org$numenta$sanity$comportex$journal$command_handler_$_find_model_pair(id){
if(typeof id === 'number'){
var i = (id - (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(steps_offset) : cljs.core.deref.call(null,steps_offset)));
if((i > (0))){
var vec__69802 = cljs.core.subvec.cljs$core$IFn$_invoke$arity$3((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(model_steps) : cljs.core.deref.call(null,model_steps)),(i - (1)),(i + (1)));
var prev_step = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69802,(0),null);
var step = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69802,(1),null);
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2((org.nfrac.comportex.protocols.timestep(prev_step) + (1)),org.nfrac.comportex.protocols.timestep(step))){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [prev_step,step], null);
} else {
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [null,step], null);
}
} else {
if((i === (0))){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [null,cljs.core.nth.cljs$core$IFn$_invoke$arity$3((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(model_steps) : cljs.core.deref.call(null,model_steps)),i,null)], null);
} else {
return null;
}
}
} else {
return null;
}
});
return (function org$numenta$sanity$comportex$journal$command_handler_$_handle_command(p__69803){
var vec__69907 = p__69803;
var vec__69908 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69907,(0),null);
var command = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69908,(0),null);
var xs = cljs.core.nthnext(vec__69908,(1));
var client_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69907,(1),null);
var client_info = (function (){var or__6153__auto__ = cljs.core.get.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(client_infos) : cljs.core.deref.call(null,client_infos)),client_id);
if(cljs.core.truth_(or__6153__auto__)){
return or__6153__auto__;
} else {
var v = (function (){var G__69909 = cljs.core.PersistentArrayMap.EMPTY;
return (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1(G__69909) : cljs.core.atom.call(null,G__69909));
})();
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(client_infos,cljs.core.assoc,client_id,v);

return v;
}
})();
var G__69910 = command;
switch (G__69910) {
case "ping":
return null;

break;
case "client-disconnect":
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq(["JOURNAL: Client disconnected."], 0));

return cljs.core.async.untap(steps_mult,cljs.core.cst$kw$ch.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$steps_DASH_mchannel.cljs$core$IFn$_invoke$arity$1((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(client_info) : cljs.core.deref.call(null,client_info)))));

break;
case "connect":
var vec__69911 = xs;
var old_client_info = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69911,(0),null);
var map__69912 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69911,(1),null);
var map__69912__$1 = ((((!((map__69912 == null)))?((((map__69912.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69912.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69912):map__69912);
var subscriber_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69912__$1,cljs.core.cst$kw$ch);
cljs.core.add_watch(client_info,cljs.core.cst$kw$org$numenta$sanity$comportex$journal_SLASH_push_DASH_to_DASH_client,((function (vec__69911,old_client_info,map__69912,map__69912__$1,subscriber_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (_,___$1,___$2,v){
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(subscriber_c,cljs.core.update.cljs$core$IFn$_invoke$arity$3(v,cljs.core.cst$kw$steps_DASH_mchannel,((function (vec__69911,old_client_info,map__69912,map__69912__$1,subscriber_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (steps_mchannel){
return org.numenta.sanity.bridge.marshalling.channel_weak(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(steps_mchannel,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$ch,cljs.core.cst$kw$target_DASH_id], null)));
});})(vec__69911,old_client_info,map__69912,map__69912__$1,subscriber_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
));
});})(vec__69911,old_client_info,map__69912,map__69912__$1,subscriber_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
);

var temp__4657__auto__ = old_client_info;
if(cljs.core.truth_(temp__4657__auto__)){
var map__69914 = temp__4657__auto__;
var map__69914__$1 = ((((!((map__69914 == null)))?((((map__69914.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69914.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69914):map__69914);
var steps_mchannel = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69914__$1,cljs.core.cst$kw$steps_DASH_mchannel);
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq(["JOURNAL: Client reconnected."], 0));

if(cljs.core.truth_(steps_mchannel)){
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq(["JOURNAL: Client resubscribed to steps."], 0));

cljs.core.async.tap.cljs$core$IFn$_invoke$arity$2(steps_mult,cljs.core.cst$kw$ch.cljs$core$IFn$_invoke$arity$1(steps_mchannel));
} else {
}

return cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(client_info,((function (map__69914,map__69914__$1,steps_mchannel,temp__4657__auto__,vec__69911,old_client_info,map__69912,map__69912__$1,subscriber_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p1__69580_SHARP_){
var G__69916 = p1__69580_SHARP_;
if(cljs.core.truth_(steps_mchannel)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69916,cljs.core.cst$kw$steps_DASH_mchannel,steps_mchannel);
} else {
return G__69916;
}
});})(map__69914,map__69914__$1,steps_mchannel,temp__4657__auto__,vec__69911,old_client_info,map__69912,map__69912__$1,subscriber_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
);
} else {
return null;
}

break;
case "consider-future":
var vec__69917 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69917,(0),null);
var input = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69917,(1),null);
var map__69918 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69917,(2),null);
var map__69918__$1 = ((((!((map__69918 == null)))?((((map__69918.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69918.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69918):map__69918);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69918__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
return cljs.core.zipmap(org.nfrac.comportex.core.region_keys.cljs$core$IFn$_invoke$arity$1(htm),cljs.core.map.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.core.column_state_freqs,org.nfrac.comportex.core.region_seq(org.nfrac.comportex.protocols.htm_activate(org.nfrac.comportex.protocols.htm_sense(htm,input,null)))));
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "decode-predictive-columns":
var vec__69920 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69920,(0),null);
var sense_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69920,(1),null);
var n = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69920,(2),null);
var map__69921 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69920,(3),null);
var map__69921__$1 = ((((!((map__69921 == null)))?((((map__69921.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69921.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69921):map__69921);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69921__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
return org.nfrac.comportex.core.predictions.cljs$core$IFn$_invoke$arity$3(htm,sense_id,n);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-steps":
var vec__69923 = xs;
var map__69924 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69923,(0),null);
var map__69924__$1 = ((((!((map__69924 == null)))?((((map__69924.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69924.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69924):map__69924);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69924__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,cljs.core.vec(cljs.core.map.cljs$core$IFn$_invoke$arity$3(org.numenta.sanity.comportex.journal.make_step,(cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(model_steps) : cljs.core.deref.call(null,model_steps)),cljs.core.drop.cljs$core$IFn$_invoke$arity$2((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(steps_offset) : cljs.core.deref.call(null,steps_offset)),cljs.core.range.cljs$core$IFn$_invoke$arity$0()))));

break;
case "subscribe":
var vec__69926 = xs;
var steps_mchannel = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69926,(0),null);
cljs.core.async.tap.cljs$core$IFn$_invoke$arity$2(steps_mult,cljs.core.cst$kw$ch.cljs$core$IFn$_invoke$arity$1(steps_mchannel));

cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(client_info,cljs.core.assoc,cljs.core.cst$kw$steps_DASH_mchannel,steps_mchannel);

return cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq(["JOURNAL: Client subscribed to steps."], 0));

break;
case "get-network-shape":
var vec__69927 = xs;
var map__69928 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69927,(0),null);
var map__69928__$1 = ((((!((map__69928 == null)))?((((map__69928.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69928.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69928):map__69928);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69928__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,org.numenta.sanity.comportex.data.network_shape((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(current_model) : cljs.core.deref.call(null,current_model))));

break;
case "get-capture-options":
var vec__69930 = xs;
var map__69931 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69930,(0),null);
var map__69931__$1 = ((((!((map__69931 == null)))?((((map__69931.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69931.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69931):map__69931);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69931__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,clojure.walk.stringify_keys((cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(capture_options) : cljs.core.deref.call(null,capture_options))));

break;
case "set-capture-options":
var vec__69933 = xs;
var co = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69933,(0),null);
var G__69934 = capture_options;
var G__69935 = clojure.walk.keywordize_keys(co);
return (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(G__69934,G__69935) : cljs.core.reset_BANG_.call(null,G__69934,G__69935));

break;
case "get-layer-bits":
var vec__69936 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69936,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69936,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69936,(2),null);
var fetches = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69936,(3),null);
var map__69937 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69936,(4),null);
var map__69937__$1 = ((((!((map__69937 == null)))?((((map__69937.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69937.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69937):map__69937);
var cols_subset = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69937__$1,cljs.core.cst$kw$value);
var map__69938 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69936,(5),null);
var map__69938__$1 = ((((!((map__69938 == null)))?((((map__69938.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69938.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69938):map__69938);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69938__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
var lyr = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,rgn_id,lyr_id], null));
var G__69941 = cljs.core.PersistentArrayMap.EMPTY;
var G__69941__$1 = ((cljs.core.contains_QMARK_(fetches,"active-columns"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69941,"active-columns",org.nfrac.comportex.protocols.active_columns(lyr)):G__69941);
var G__69941__$2 = ((cljs.core.contains_QMARK_(fetches,"pred-columns"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69941__$1,"pred-columns",cljs.core.distinct.cljs$core$IFn$_invoke$arity$1(cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.first,org.nfrac.comportex.protocols.prior_predictive_cells(lyr)))):G__69941__$1);
var G__69941__$3 = ((cljs.core.contains_QMARK_(fetches,"overlaps-columns-alpha"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69941__$2,"overlaps-columns-alpha",org.nfrac.comportex.util.remap(((function (G__69941,G__69941__$1,G__69941__$2,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p1__69581_SHARP_){
var x__6491__auto__ = 1.0;
var y__6492__auto__ = (p1__69581_SHARP_ / (16));
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
});})(G__69941,G__69941__$1,G__69941__$2,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,cljs.core.persistent_BANG_(cljs.core.reduce_kv(((function (G__69941,G__69941__$1,G__69941__$2,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (m,p__69942,v){
var vec__69943 = p__69942;
var col = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69943,(0),null);
var _ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69943,(1),null);
var ___$1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69943,(2),null);
return cljs.core.assoc_BANG_.cljs$core$IFn$_invoke$arity$3(m,col,(function (){var x__6484__auto__ = v;
var y__6485__auto__ = cljs.core.get.cljs$core$IFn$_invoke$arity$3(m,col,(0));
return ((x__6484__auto__ > y__6485__auto__) ? x__6484__auto__ : y__6485__auto__);
})());
});})(G__69941,G__69941__$1,G__69941__$2,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,cljs.core.transient$(cljs.core.PersistentArrayMap.EMPTY),cljs.core.cst$kw$col_DASH_overlaps.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$state.cljs$core$IFn$_invoke$arity$1(lyr)))))):G__69941__$2);
var G__69941__$4 = ((cljs.core.contains_QMARK_(fetches,"boost-columns-alpha"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69941__$3,"boost-columns-alpha",(function (){var map__69944 = org.nfrac.comportex.protocols.params(lyr);
var map__69944__$1 = ((((!((map__69944 == null)))?((((map__69944.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69944.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69944):map__69944);
var max_boost = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69944__$1,cljs.core.cst$kw$max_DASH_boost);
return cljs.core.zipmap(cljs.core.range.cljs$core$IFn$_invoke$arity$0(),cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.float$,cljs.core.map.cljs$core$IFn$_invoke$arity$2(((function (map__69944,map__69944__$1,max_boost,G__69941,G__69941__$1,G__69941__$2,G__69941__$3,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p1__69582_SHARP_){
return ((p1__69582_SHARP_ - (1)) / (max_boost - (1)));
});})(map__69944,map__69944__$1,max_boost,G__69941,G__69941__$1,G__69941__$2,G__69941__$3,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,cljs.core.cst$kw$boosts.cljs$core$IFn$_invoke$arity$1(lyr))));
})()):G__69941__$3);
var G__69941__$5 = ((cljs.core.contains_QMARK_(fetches,"active-freq-columns-alpha"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69941__$4,"active-freq-columns-alpha",cljs.core.zipmap(cljs.core.range.cljs$core$IFn$_invoke$arity$0(),cljs.core.map.cljs$core$IFn$_invoke$arity$2(((function (G__69941,G__69941__$1,G__69941__$2,G__69941__$3,G__69941__$4,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p1__69583_SHARP_){
var x__6491__auto__ = 1.0;
var y__6492__auto__ = ((2) * p1__69583_SHARP_);
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
});})(G__69941,G__69941__$1,G__69941__$2,G__69941__$3,G__69941__$4,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,cljs.core.cst$kw$active_DASH_duty_DASH_cycles.cljs$core$IFn$_invoke$arity$1(lyr)))):G__69941__$4);
var G__69941__$6 = ((cljs.core.contains_QMARK_(fetches,"n-segments-columns-alpha"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69941__$5,"n-segments-columns-alpha",cljs.core.zipmap(cols_subset,cljs.core.map.cljs$core$IFn$_invoke$arity$2(((function (G__69941,G__69941__$1,G__69941__$2,G__69941__$3,G__69941__$4,G__69941__$5,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p1__69585_SHARP_){
var x__6491__auto__ = 1.0;
var y__6492__auto__ = (p1__69585_SHARP_ / 16.0);
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
});})(G__69941,G__69941__$1,G__69941__$2,G__69941__$3,G__69941__$4,G__69941__$5,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,cljs.core.map.cljs$core$IFn$_invoke$arity$2(((function (G__69941,G__69941__$1,G__69941__$2,G__69941__$3,G__69941__$4,G__69941__$5,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p1__69584_SHARP_){
return org.numenta.sanity.comportex.data.count_segs_in_column(cljs.core.cst$kw$distal_DASH_sg.cljs$core$IFn$_invoke$arity$1(lyr),org.nfrac.comportex.protocols.layer_depth(lyr),p1__69584_SHARP_);
});})(G__69941,G__69941__$1,G__69941__$2,G__69941__$3,G__69941__$4,G__69941__$5,lyr,htm,temp__4655__auto__,vec__69936,id,rgn_id,lyr_id,fetches,map__69937,map__69937__$1,cols_subset,map__69938,map__69938__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,cols_subset)))):G__69941__$5);
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69941__$6,"break?",cljs.core.empty_QMARK_(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(lyr,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$prior_DASH_distal_DASH_state,cljs.core.cst$kw$active_DASH_bits], null))));

} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-sense-bits":
var vec__69946 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69946,(0),null);
var sense_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69946,(1),null);
var fetches = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69946,(2),null);
var map__69947 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69946,(3),null);
var map__69947__$1 = ((((!((map__69947 == null)))?((((map__69947.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69947.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69947):map__69947);
var bits_subset = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69947__$1,cljs.core.cst$kw$value);
var map__69948 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69946,(4),null);
var map__69948__$1 = ((((!((map__69948 == null)))?((((map__69948.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69948.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69948):map__69948);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69948__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model_pair(id);
if(cljs.core.truth_(temp__4655__auto__)){
var vec__69951 = temp__4655__auto__;
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69951,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69951,(1),null);
var sense = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$senses,sense_id], null));
var ff_rgn_id = cljs.core.first(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$fb_DASH_deps,sense_id], null)));
var prev_ff_rgn = (((org.nfrac.comportex.protocols.size(org.nfrac.comportex.protocols.ff_topology(sense)) > (0)))?cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(prev_htm,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,ff_rgn_id], null)):null);
var G__69952 = cljs.core.PersistentArrayMap.EMPTY;
var G__69952__$1 = ((cljs.core.contains_QMARK_(fetches,"active-bits"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69952,"active-bits",cljs.core.set(org.numenta.sanity.comportex.data.active_bits(sense))):G__69952);
if(cljs.core.truth_((function (){var and__6141__auto__ = cljs.core.contains_QMARK_(fetches,"pred-bits-alpha");
if(and__6141__auto__){
return prev_ff_rgn;
} else {
return and__6141__auto__;
}
})())){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69952__$1,"pred-bits-alpha",(function (){var start = org.nfrac.comportex.core.ff_base(htm,ff_rgn_id,sense_id);
var end = (start + org.nfrac.comportex.protocols.size(org.nfrac.comportex.protocols.ff_topology(sense)));
return org.nfrac.comportex.util.remap(((function (start,end,G__69952,G__69952__$1,sense,ff_rgn_id,prev_ff_rgn,vec__69951,prev_htm,htm,temp__4655__auto__,vec__69946,id,sense_id,fetches,map__69947,map__69947__$1,bits_subset,map__69948,map__69948__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p1__69586_SHARP_){
var x__6491__auto__ = 1.0;
var y__6492__auto__ = (p1__69586_SHARP_ / (8));
return ((x__6491__auto__ < y__6492__auto__) ? x__6491__auto__ : y__6492__auto__);
});})(start,end,G__69952,G__69952__$1,sense,ff_rgn_id,prev_ff_rgn,vec__69951,prev_htm,htm,temp__4655__auto__,vec__69946,id,sense_id,fetches,map__69947,map__69947__$1,bits_subset,map__69948,map__69948__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,cljs.core.keep.cljs$core$IFn$_invoke$arity$2(((function (start,end,G__69952,G__69952__$1,sense,ff_rgn_id,prev_ff_rgn,vec__69951,prev_htm,htm,temp__4655__auto__,vec__69946,id,sense_id,fetches,map__69947,map__69947__$1,bits_subset,map__69948,map__69948__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p__69953){
var vec__69954 = p__69953;
var id__$1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69954,(0),null);
var votes = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69954,(1),null);
if(((start <= id__$1)) && ((id__$1 < end))){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(id__$1 - start),votes], null);
} else {
return null;
}
});})(start,end,G__69952,G__69952__$1,sense,ff_rgn_id,prev_ff_rgn,vec__69951,prev_htm,htm,temp__4655__auto__,vec__69946,id,sense_id,fetches,map__69947,map__69947__$1,bits_subset,map__69948,map__69948__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,org.nfrac.comportex.core.predicted_bit_votes(prev_ff_rgn))));
})());
} else {
return G__69952__$1;
}
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-proximal-synapses-by-source-bit":
var vec__69955 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69955,(0),null);
var sense_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69955,(1),null);
var bit = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69955,(2),null);
var syn_states = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69955,(3),null);
var map__69956 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69955,(4),null);
var map__69956__$1 = ((((!((map__69956 == null)))?((((map__69956.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69956.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69956):map__69956);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69956__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
return org.numenta.sanity.comportex.data.syns_from_source_bit(htm,sense_id,bit,syn_states);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-column-cells":
var vec__69958 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69958,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69958,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69958,(2),null);
var col = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69958,(3),null);
var fetches = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69958,(4),null);
var map__69959 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69958,(5),null);
var map__69959__$1 = ((((!((map__69959 == null)))?((((map__69959.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69959.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69959):map__69959);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69959__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
var lyr = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,rgn_id,lyr_id], null));
var extract_cells = ((function (lyr,htm,temp__4655__auto__,vec__69958,id,rgn_id,lyr_id,col,fetches,map__69959,map__69959__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p1__69587_SHARP_){
return cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentHashSet.EMPTY,cljs.core.keep.cljs$core$IFn$_invoke$arity$2(((function (lyr,htm,temp__4655__auto__,vec__69958,id,rgn_id,lyr_id,col,fetches,map__69959,map__69959__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id){
return (function (p__69961){
var vec__69962 = p__69961;
var column = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69962,(0),null);
var ci = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69962,(1),null);
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(col,column)){
return ci;
} else {
return null;
}
});})(lyr,htm,temp__4655__auto__,vec__69958,id,rgn_id,lyr_id,col,fetches,map__69959,map__69959__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
,p1__69587_SHARP_));
});})(lyr,htm,temp__4655__auto__,vec__69958,id,rgn_id,lyr_id,col,fetches,map__69959,map__69959__$1,response_c,G__69910,client_info,vec__69907,vec__69908,command,xs,client_id))
;
var G__69963 = cljs.core.PersistentArrayMap.EMPTY;
var G__69963__$1 = ((cljs.core.contains_QMARK_(fetches,"active-cells"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69963,"active-cells",extract_cells(org.nfrac.comportex.protocols.active_cells(lyr))):G__69963);
var G__69963__$2 = ((cljs.core.contains_QMARK_(fetches,"prior-predicted-cells"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69963__$1,"prior-predicted-cells",extract_cells(org.nfrac.comportex.protocols.prior_predictive_cells(lyr))):G__69963__$1);
if(cljs.core.contains_QMARK_(fetches,"winner-cells")){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69963__$2,"winner-cells",extract_cells(org.nfrac.comportex.protocols.winner_cells(lyr)));
} else {
return G__69963__$2;
}
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-apical-segments":
var vec__69964 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69964,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69964,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69964,(2),null);
var seg_selector = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69964,(3),null);
var map__69965 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69964,(4),null);
var map__69965__$1 = ((((!((map__69965 == null)))?((((map__69965.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69965.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69965):map__69965);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69965__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model_pair(id);
if(cljs.core.truth_(temp__4655__auto__)){
var vec__69967 = temp__4655__auto__;
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69967,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69967,(1),null);
return org.numenta.sanity.comportex.data.query_segs(htm,prev_htm,rgn_id,lyr_id,seg_selector,cljs.core.cst$kw$apical);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-distal-segments":
var vec__69968 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69968,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69968,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69968,(2),null);
var seg_selector = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69968,(3),null);
var map__69969 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69968,(4),null);
var map__69969__$1 = ((((!((map__69969 == null)))?((((map__69969.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69969.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69969):map__69969);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69969__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model_pair(id);
if(cljs.core.truth_(temp__4655__auto__)){
var vec__69971 = temp__4655__auto__;
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69971,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69971,(1),null);
return org.numenta.sanity.comportex.data.query_segs(htm,prev_htm,rgn_id,lyr_id,seg_selector,cljs.core.cst$kw$distal);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-proximal-segments":
var vec__69972 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69972,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69972,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69972,(2),null);
var seg_selector = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69972,(3),null);
var map__69973 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69972,(4),null);
var map__69973__$1 = ((((!((map__69973 == null)))?((((map__69973.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69973.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69973):map__69973);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69973__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model_pair(id);
if(cljs.core.truth_(temp__4655__auto__)){
var vec__69975 = temp__4655__auto__;
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69975,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69975,(1),null);
return org.numenta.sanity.comportex.data.query_segs(htm,prev_htm,rgn_id,lyr_id,seg_selector,cljs.core.cst$kw$proximal);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-apical-synapses":
var vec__69976 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69976,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69976,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69976,(2),null);
var seg_selector = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69976,(3),null);
var syn_states = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69976,(4),null);
var map__69977 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69976,(5),null);
var map__69977__$1 = ((((!((map__69977 == null)))?((((map__69977.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69977.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69977):map__69977);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69977__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model_pair(id);
if(cljs.core.truth_(temp__4655__auto__)){
var vec__69979 = temp__4655__auto__;
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69979,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69979,(1),null);
return org.numenta.sanity.comportex.data.query_syns(htm,prev_htm,rgn_id,lyr_id,seg_selector,syn_states,cljs.core.cst$kw$apical);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-distal-synapses":
var vec__69980 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69980,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69980,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69980,(2),null);
var seg_selector = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69980,(3),null);
var syn_states = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69980,(4),null);
var map__69981 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69980,(5),null);
var map__69981__$1 = ((((!((map__69981 == null)))?((((map__69981.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69981.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69981):map__69981);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69981__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model_pair(id);
if(cljs.core.truth_(temp__4655__auto__)){
var vec__69983 = temp__4655__auto__;
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69983,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69983,(1),null);
return org.numenta.sanity.comportex.data.query_syns(htm,prev_htm,rgn_id,lyr_id,seg_selector,syn_states,cljs.core.cst$kw$distal);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-proximal-synapses":
var vec__69984 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69984,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69984,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69984,(2),null);
var seg_selector = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69984,(3),null);
var syn_states = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69984,(4),null);
var map__69985 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69984,(5),null);
var map__69985__$1 = ((((!((map__69985 == null)))?((((map__69985.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69985.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69985):map__69985);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69985__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model_pair(id);
if(cljs.core.truth_(temp__4655__auto__)){
var vec__69987 = temp__4655__auto__;
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69987,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69987,(1),null);
return org.numenta.sanity.comportex.data.query_syns(htm,prev_htm,rgn_id,lyr_id,seg_selector,syn_states,cljs.core.cst$kw$proximal);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-details-text":
var vec__69988 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69988,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69988,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69988,(2),null);
var col = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69988,(3),null);
var map__69989 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69988,(4),null);
var map__69989__$1 = ((((!((map__69989 == null)))?((((map__69989.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69989.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69989):map__69989);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69989__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model_pair(id);
if(cljs.core.truth_(temp__4655__auto__)){
var vec__69991 = temp__4655__auto__;
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69991,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69991,(1),null);
return org.numenta.sanity.comportex.details.detail_text(htm,prev_htm,rgn_id,lyr_id,col);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-model":
var vec__69992 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69992,(0),null);
var map__69993 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69992,(1),null);
var map__69993__$1 = ((((!((map__69993 == null)))?((((map__69993.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69993.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69993):map__69993);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69993__$1,cljs.core.cst$kw$ch);
var as_str_QMARK_ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69992,(2),null);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
var G__69995 = htm;
if(cljs.core.truth_(as_str_QMARK_)){
return cljs.core.pr_str.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([G__69995], 0));
} else {
return G__69995;
}
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-layer-stats":
var vec__69996 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69996,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69996,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69996,(2),null);
var fetches = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69996,(3),null);
var map__69997 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__69996,(4),null);
var map__69997__$1 = ((((!((map__69997 == null)))?((((map__69997.cljs$lang$protocol_mask$partition0$ & (64))) || (map__69997.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__69997):map__69997);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__69997__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
var lyr = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,rgn_id,lyr_id], null));
var a_cols = org.nfrac.comportex.protocols.active_columns(lyr);
var ppc = org.nfrac.comportex.protocols.prior_predictive_cells(lyr);
var pp_cols = cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentHashSet.EMPTY,cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.first,ppc));
var ap_cols = clojure.set.intersection.cljs$core$IFn$_invoke$arity$2(pp_cols,a_cols);
var col_states = cljs.core.merge.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([cljs.core.zipmap(pp_cols,cljs.core.repeat.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$predicted)),cljs.core.zipmap(a_cols,cljs.core.repeat.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$active)),cljs.core.zipmap(ap_cols,cljs.core.repeat.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$active_DASH_predicted))], 0));
var freqs = cljs.core.frequencies(cljs.core.vals(col_states));
var G__69999 = cljs.core.PersistentArrayMap.EMPTY;
var G__69999__$1 = ((cljs.core.contains_QMARK_(fetches,"n-unpredicted-active-columns"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69999,"n-unpredicted-active-columns",cljs.core.get.cljs$core$IFn$_invoke$arity$3(freqs,cljs.core.cst$kw$active,(0))):G__69999);
var G__69999__$2 = ((cljs.core.contains_QMARK_(fetches,"n-predicted-inactive-columns"))?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69999__$1,"n-predicted-inactive-columns",cljs.core.get.cljs$core$IFn$_invoke$arity$3(freqs,cljs.core.cst$kw$predicted,(0))):G__69999__$1);
if(cljs.core.contains_QMARK_(fetches,"n-predicted-active-columns")){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__69999__$2,"n-predicted-active-columns",cljs.core.get.cljs$core$IFn$_invoke$arity$3(freqs,cljs.core.cst$kw$active_DASH_predicted,(0)));
} else {
return G__69999__$2;
}
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-cell-excitation-data":
var vec__70000 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70000,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70000,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70000,(2),null);
var sel_col = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70000,(3),null);
var map__70001 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70000,(4),null);
var map__70001__$1 = ((((!((map__70001 == null)))?((((map__70001.cljs$lang$protocol_mask$partition0$ & (64))) || (map__70001.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__70001):map__70001);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__70001__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var vec__70003 = find_model_pair(id);
var prev_htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70003,(0),null);
var htm = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70003,(1),null);
if(cljs.core.truth_(prev_htm)){
return org.numenta.sanity.comportex.data.cell_excitation_data(htm,prev_htm,rgn_id,lyr_id,sel_col);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-cells-by-state":
var vec__70004 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70004,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70004,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70004,(2),null);
var map__70005 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70004,(3),null);
var map__70005__$1 = ((((!((map__70005 == null)))?((((map__70005.cljs$lang$protocol_mask$partition0$ & (64))) || (map__70005.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__70005):map__70005);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__70005__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
var layer = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(htm,new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$regions,rgn_id,lyr_id], null));
return new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$winner_DASH_cells,org.nfrac.comportex.protocols.winner_cells(layer),cljs.core.cst$kw$active_DASH_cells,org.nfrac.comportex.protocols.active_cells(layer),cljs.core.cst$kw$pred_DASH_cells,org.nfrac.comportex.protocols.predictive_cells(layer),cljs.core.cst$kw$engaged_QMARK_,true], null);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
case "get-transitions-data":
var vec__70007 = xs;
var id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70007,(0),null);
var rgn_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70007,(1),null);
var lyr_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70007,(2),null);
var cell_sdr_fracs = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70007,(3),null);
var map__70008 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__70007,(4),null);
var map__70008__$1 = ((((!((map__70008 == null)))?((((map__70008.cljs$lang$protocol_mask$partition0$ & (64))) || (map__70008.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__70008):map__70008);
var response_c = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__70008__$1,cljs.core.cst$kw$ch);
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(response_c,(function (){var temp__4655__auto__ = find_model(id);
if(cljs.core.truth_(temp__4655__auto__)){
var htm = temp__4655__auto__;
return org.numenta.sanity.comportex.data.transitions_data(htm,rgn_id,lyr_id,cell_sdr_fracs);
} else {
return org.numenta.sanity.comportex.journal.id_missing_response(id,steps_offset);
}
})());

break;
default:
throw (new Error([cljs.core.str("No matching clause: "),cljs.core.str(command)].join('')));

}
});
});
org.numenta.sanity.comportex.journal.init = (function org$numenta$sanity$comportex$journal$init(steps_c,commands_c,current_model,n_keep){
var steps_offset = (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1((0)) : cljs.core.atom.call(null,(0)));
var model_steps = (function (){var G__70112 = cljs.core.PersistentVector.EMPTY;
return (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1(G__70112) : cljs.core.atom.call(null,G__70112));
})();
var steps_in = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var steps_mult = cljs.core.async.mult(steps_in);
var client_infos = (function (){var G__70113 = cljs.core.PersistentArrayMap.EMPTY;
return (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1(G__70113) : cljs.core.atom.call(null,G__70113));
})();
var capture_options = (function (){var G__70114 = new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$keep_DASH_steps,n_keep,cljs.core.cst$kw$ff_DASH_synapses,new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$capture_QMARK_,true,cljs.core.cst$kw$only_DASH_active_QMARK_,false,cljs.core.cst$kw$only_DASH_connected_QMARK_,false], null),cljs.core.cst$kw$distal_DASH_synapses,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$capture_QMARK_,true,cljs.core.cst$kw$only_DASH_active_QMARK_,false,cljs.core.cst$kw$only_DASH_connected_QMARK_,false,cljs.core.cst$kw$only_DASH_noteworthy_DASH_columns_QMARK_,false], null),cljs.core.cst$kw$apical_DASH_synapses,new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$capture_QMARK_,true,cljs.core.cst$kw$only_DASH_active_QMARK_,false,cljs.core.cst$kw$only_DASH_connected_QMARK_,false,cljs.core.cst$kw$only_DASH_noteworthy_DASH_columns_QMARK_,false], null)], null);
return (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1(G__70114) : cljs.core.atom.call(null,G__70114));
})();
var handle_command = org.numenta.sanity.comportex.journal.command_handler(current_model,steps_offset,model_steps,steps_mult,client_infos,capture_options);
var c__38109__auto___70213 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto___70213,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto___70213,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command){
return (function (state_70154){
var state_val_70155 = (state_70154[(1)]);
if((state_val_70155 === (7))){
var inst_70150 = (state_70154[(2)]);
var state_70154__$1 = state_70154;
var statearr_70156_70214 = state_70154__$1;
(statearr_70156_70214[(2)] = inst_70150);

(statearr_70156_70214[(1)] = (3));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (1))){
var state_70154__$1 = state_70154;
var statearr_70157_70215 = state_70154__$1;
(statearr_70157_70215[(2)] = null);

(statearr_70157_70215[(1)] = (2));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (4))){
var inst_70117 = (state_70154[(7)]);
var inst_70117__$1 = (state_70154[(2)]);
var state_70154__$1 = (function (){var statearr_70158 = state_70154;
(statearr_70158[(7)] = inst_70117__$1);

return statearr_70158;
})();
if(cljs.core.truth_(inst_70117__$1)){
var statearr_70159_70216 = state_70154__$1;
(statearr_70159_70216[(1)] = (5));

} else {
var statearr_70160_70217 = state_70154__$1;
(statearr_70160_70217[(1)] = (6));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (13))){
var inst_70117 = (state_70154[(7)]);
var inst_70122 = (state_70154[(8)]);
var inst_70135 = (state_70154[(9)]);
var inst_70142 = (state_70154[(2)]);
var inst_70143 = (cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2 ? cljs.core.reset_BANG_.cljs$core$IFn$_invoke$arity$2(model_steps,inst_70142) : cljs.core.reset_BANG_.call(null,model_steps,inst_70142));
var inst_70144 = cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(steps_offset,cljs.core._PLUS_,inst_70135);
var inst_70145 = org.numenta.sanity.comportex.journal.make_step(inst_70117,inst_70122);
var inst_70146 = cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(steps_in,inst_70145);
var state_70154__$1 = (function (){var statearr_70161 = state_70154;
(statearr_70161[(10)] = inst_70146);

(statearr_70161[(11)] = inst_70143);

(statearr_70161[(12)] = inst_70144);

return statearr_70161;
})();
var statearr_70162_70218 = state_70154__$1;
(statearr_70162_70218[(2)] = null);

(statearr_70162_70218[(1)] = (2));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (6))){
var state_70154__$1 = state_70154;
var statearr_70163_70219 = state_70154__$1;
(statearr_70163_70219[(2)] = null);

(statearr_70163_70219[(1)] = (7));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (3))){
var inst_70152 = (state_70154[(2)]);
var state_70154__$1 = state_70154;
return cljs.core.async.impl.ioc_helpers.return_chan(state_70154__$1,inst_70152);
} else {
if((state_val_70155 === (12))){
var inst_70124 = (state_70154[(13)]);
var state_70154__$1 = state_70154;
var statearr_70164_70220 = state_70154__$1;
(statearr_70164_70220[(2)] = inst_70124);

(statearr_70164_70220[(1)] = (13));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (2))){
var state_70154__$1 = state_70154;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_70154__$1,(4),steps_c);
} else {
if((state_val_70155 === (11))){
var inst_70124 = (state_70154[(13)]);
var inst_70135 = (state_70154[(9)]);
var inst_70139 = cljs.core.subvec.cljs$core$IFn$_invoke$arity$2(inst_70124,inst_70135);
var state_70154__$1 = state_70154;
var statearr_70165_70221 = state_70154__$1;
(statearr_70165_70221[(2)] = inst_70139);

(statearr_70165_70221[(1)] = (13));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (9))){
var state_70154__$1 = state_70154;
var statearr_70166_70222 = state_70154__$1;
(statearr_70166_70222[(2)] = (0));

(statearr_70166_70222[(1)] = (10));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (5))){
var inst_70126 = (state_70154[(14)]);
var inst_70117 = (state_70154[(7)]);
var inst_70119 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(steps_offset) : cljs.core.deref.call(null,steps_offset));
var inst_70120 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(model_steps) : cljs.core.deref.call(null,model_steps));
var inst_70121 = cljs.core.count(inst_70120);
var inst_70122 = (inst_70119 + inst_70121);
var inst_70123 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(model_steps) : cljs.core.deref.call(null,model_steps));
var inst_70124 = cljs.core.conj.cljs$core$IFn$_invoke$arity$2(inst_70123,inst_70117);
var inst_70125 = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(capture_options) : cljs.core.deref.call(null,capture_options));
var inst_70126__$1 = cljs.core.cst$kw$keep_DASH_steps.cljs$core$IFn$_invoke$arity$1(inst_70125);
var inst_70127 = (inst_70126__$1 < (0));
var inst_70128 = cljs.core.not(inst_70127);
var state_70154__$1 = (function (){var statearr_70167 = state_70154;
(statearr_70167[(14)] = inst_70126__$1);

(statearr_70167[(13)] = inst_70124);

(statearr_70167[(8)] = inst_70122);

return statearr_70167;
})();
if(inst_70128){
var statearr_70168_70223 = state_70154__$1;
(statearr_70168_70223[(1)] = (8));

} else {
var statearr_70169_70224 = state_70154__$1;
(statearr_70169_70224[(1)] = (9));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (10))){
var inst_70135 = (state_70154[(9)]);
var inst_70135__$1 = (state_70154[(2)]);
var inst_70137 = (inst_70135__$1 > (0));
var state_70154__$1 = (function (){var statearr_70170 = state_70154;
(statearr_70170[(9)] = inst_70135__$1);

return statearr_70170;
})();
if(cljs.core.truth_(inst_70137)){
var statearr_70171_70225 = state_70154__$1;
(statearr_70171_70225[(1)] = (11));

} else {
var statearr_70172_70226 = state_70154__$1;
(statearr_70172_70226[(1)] = (12));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_70155 === (8))){
var inst_70126 = (state_70154[(14)]);
var inst_70124 = (state_70154[(13)]);
var inst_70130 = cljs.core.count(inst_70124);
var inst_70131 = (inst_70130 - inst_70126);
var inst_70132 = (((0) > inst_70131) ? (0) : inst_70131);
var state_70154__$1 = state_70154;
var statearr_70173_70227 = state_70154__$1;
(statearr_70173_70227[(2)] = inst_70132);

(statearr_70173_70227[(1)] = (10));


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
});})(c__38109__auto___70213,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command))
;
return ((function (switch__37995__auto__,c__38109__auto___70213,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command){
return (function() {
var org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__ = null;
var org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____0 = (function (){
var statearr_70177 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_70177[(0)] = org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__);

(statearr_70177[(1)] = (1));

return statearr_70177;
});
var org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____1 = (function (state_70154){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_70154);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e70178){if((e70178 instanceof Object)){
var ex__37999__auto__ = e70178;
var statearr_70179_70228 = state_70154;
(statearr_70179_70228[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_70154);

return cljs.core.cst$kw$recur;
} else {
throw e70178;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__70229 = state_70154;
state_70154 = G__70229;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__ = function(state_70154){
switch(arguments.length){
case 0:
return org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____1.call(this,state_70154);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____0;
org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____1;
return org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto___70213,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command))
})();
var state__38111__auto__ = (function (){var statearr_70180 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_70180[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto___70213);

return statearr_70180;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto___70213,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command))
);


var c__38109__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__38109__auto__,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command){
return (function (){
var f__38110__auto__ = (function (){var switch__37995__auto__ = ((function (c__38109__auto__,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command){
return (function (state_70196){
var state_val_70197 = (state_70196[(1)]);
if((state_val_70197 === (1))){
var state_70196__$1 = state_70196;
var statearr_70198_70230 = state_70196__$1;
(statearr_70198_70230[(2)] = null);

(statearr_70198_70230[(1)] = (2));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70197 === (2))){
var state_70196__$1 = state_70196;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_70196__$1,(4),commands_c);
} else {
if((state_val_70197 === (3))){
var inst_70194 = (state_70196[(2)]);
var state_70196__$1 = state_70196;
return cljs.core.async.impl.ioc_helpers.return_chan(state_70196__$1,inst_70194);
} else {
if((state_val_70197 === (4))){
var inst_70183 = (state_70196[(7)]);
var inst_70183__$1 = (state_70196[(2)]);
var inst_70184 = (inst_70183__$1 == null);
var inst_70185 = cljs.core.not(inst_70184);
var state_70196__$1 = (function (){var statearr_70199 = state_70196;
(statearr_70199[(7)] = inst_70183__$1);

return statearr_70199;
})();
if(inst_70185){
var statearr_70200_70231 = state_70196__$1;
(statearr_70200_70231[(1)] = (5));

} else {
var statearr_70201_70232 = state_70196__$1;
(statearr_70201_70232[(1)] = (6));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_70197 === (5))){
var inst_70183 = (state_70196[(7)]);
var inst_70187 = (handle_command.cljs$core$IFn$_invoke$arity$1 ? handle_command.cljs$core$IFn$_invoke$arity$1(inst_70183) : handle_command.call(null,inst_70183));
var state_70196__$1 = (function (){var statearr_70202 = state_70196;
(statearr_70202[(8)] = inst_70187);

return statearr_70202;
})();
var statearr_70203_70233 = state_70196__$1;
(statearr_70203_70233[(2)] = null);

(statearr_70203_70233[(1)] = (2));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70197 === (6))){
var inst_70190 = cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq(["CLOSING JOURNAL"], 0));
var state_70196__$1 = state_70196;
var statearr_70204_70234 = state_70196__$1;
(statearr_70204_70234[(2)] = inst_70190);

(statearr_70204_70234[(1)] = (7));


return cljs.core.cst$kw$recur;
} else {
if((state_val_70197 === (7))){
var inst_70192 = (state_70196[(2)]);
var state_70196__$1 = state_70196;
var statearr_70205_70235 = state_70196__$1;
(statearr_70205_70235[(2)] = inst_70192);

(statearr_70205_70235[(1)] = (3));


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
});})(c__38109__auto__,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command))
;
return ((function (switch__37995__auto__,c__38109__auto__,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command){
return (function() {
var org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__ = null;
var org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____0 = (function (){
var statearr_70209 = [null,null,null,null,null,null,null,null,null];
(statearr_70209[(0)] = org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__);

(statearr_70209[(1)] = (1));

return statearr_70209;
});
var org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____1 = (function (state_70196){
while(true){
var ret_value__37997__auto__ = (function (){try{while(true){
var result__37998__auto__ = switch__37995__auto__(state_70196);
if(cljs.core.keyword_identical_QMARK_(result__37998__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__37998__auto__;
}
break;
}
}catch (e70210){if((e70210 instanceof Object)){
var ex__37999__auto__ = e70210;
var statearr_70211_70236 = state_70196;
(statearr_70211_70236[(5)] = ex__37999__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_70196);

return cljs.core.cst$kw$recur;
} else {
throw e70210;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__37997__auto__,cljs.core.cst$kw$recur)){
var G__70237 = state_70196;
state_70196 = G__70237;
continue;
} else {
return ret_value__37997__auto__;
}
break;
}
});
org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__ = function(state_70196){
switch(arguments.length){
case 0:
return org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____0.call(this);
case 1:
return org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____1.call(this,state_70196);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$0 = org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____0;
org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__.cljs$core$IFn$_invoke$arity$1 = org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto____1;
return org$numenta$sanity$comportex$journal$init_$_state_machine__37996__auto__;
})()
;})(switch__37995__auto__,c__38109__auto__,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command))
})();
var state__38111__auto__ = (function (){var statearr_70212 = (f__38110__auto__.cljs$core$IFn$_invoke$arity$0 ? f__38110__auto__.cljs$core$IFn$_invoke$arity$0() : f__38110__auto__.call(null));
(statearr_70212[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__38109__auto__);

return statearr_70212;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38111__auto__);
});})(c__38109__auto__,steps_offset,model_steps,steps_in,steps_mult,client_infos,capture_options,handle_command))
);

return c__38109__auto__;
});
