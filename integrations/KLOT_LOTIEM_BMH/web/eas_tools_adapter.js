export const EAS_EVENT_CODES={"Severe Thunderstorm Warning":"SVR","Tornado Warning":"TOR","Flash Flood Warning":"FFW","Special Weather Statement":"SPW","Extreme Wind Warning":"EWW"};
export const PRODUCT_ENTRIES=["@AUTO_ID","@ACTIVE_ALERTS","@SEVERE_DYNAMIC","@PRODUCT:VPZZFP","@PRODUCT:HWOLOT","@PRODUCT:HWOIWX","@AUTO_SEVERE_ID","@NEW_CON_ALERTS","@CAN_EXP_ALERTS"];
export function buildPreview({event="SVR",locations="ILC-,INC-",message="This is a test."}={}){return {simulation:true,event,locations,message,generated_at:new Date().toISOString()};}
