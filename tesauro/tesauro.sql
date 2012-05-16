--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

--
-- Data for Name: tesauro; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY tesauro (id, parent_id, name, descripcion, notas) FROM stdin;
9	113	001	Fecha exacta	
12	10	001005	Violaciones al derecho a la vida	
13	10	001010	Violaciones al derecho a la integridad personal	
14	10	001015	Violaciones al derecho a la libertad y seguridad personales	
15	51	001	Derechos civiles y políticos	
18	17	003025	Derechos de las personas privadas de la libertad	
19	15	001005	Derecho a la vida	
20	15	001010	Derecho a la integridad personal	
26	14	001015015	Encarcelamiento arbitrario	
27	13	001010010	Intimidación	
40	1	T63	Estados de Mexico	
48	1	T10	Ocupación	
49	1	T39	Sexo	
51	1	T03	Derecho afectado	
57	56	002	Documento oficial	
58	56	006	Documento de organización internacional	
75	1	T21	Tipos de Relaciones	
80	75	002	Relaciones de afiliación	
88	53	010	Abuso sexual de menores	
91	53	480	Prostitución forzada	
95	93	018002	Queja o petición ante OPDH	
96	93	018004	Queja o petición ante OIG	
98	94	020002	Denuncia penal	
99	94	020004	Queja administrativa	
111	49	001	Hombre	
112	49	002	Mujer	
115	113	003	Se desconoce el día	
118	117	001	Activo	
120	117	003	Inactivo	
123	1	T42	Confiabilidad	
124	1	T09	Escolaridad	
129	1	T12	Religion	
131	1	T08	Estado civil	
135	1	T04	Tipo de acto o VDH	
139	15	001030	Derecho a la seguridad jurídica	
141	53	490	Prostitución y pornografía infantil	
142	1	T17	Tipo de lugar	
143	142	006	Institución penitenciaria	
150	53	520	Radio	
151	53	530	Radios comunitarias	
156	53	550	Reformas legislativas	
158	53	620	Televisión	
163	160	001001	Directamente llevó a cabo el acto	
164	160	001002	Dio órdenes que tuvieron como consecuencia el acto	
166	165	005	Entidades estatales	
167	165	010	Entidades no estatales	
168	166	005005	Poder ejecutivo	
169	166	005010	Poder legislativo	
170	168	005005010	Poder ejecutivo estatal	
171	168	005005005	Poder ejecutivo federal	
196	53	120	Desastres naturales	
201	53	180	Empresas privadas transnacionales	
211	53	260	Institutos estatales de acceso a la información	
212	53	240	Instituto Federal Electoral - IFE	
213	53	270	Justicia	
219	53	220	Impunidad	
221	53	290	Maquiladoras	
226	53	310	Medios de comunicación impresos	
230	53	250	Institutos electorales estatales	
238	53	400	Partidos políticos	
242	53	360	Mujeres	
243	53	350	Movimientos sociales	
245	53	440	Política exterior	
246	53	450	Políticas públicas	
251	53	390	Participación ciudadana	
252	53	510	Pueblos indígenas	
256	53	560	Represión	
258	53	580	Seguridad pública	
261	53	590	Sindicatos	
262	53	570	Salud	
263	53	140	Educación	
264	53	600	Soberanía alimentaria	
266	53	470	Privatización	
269	53	660	Tratados de libre comercio	
270	53	670	VIH/SIDA	
271	53	690	Violencia familiar	
5429	54	001	Características personales	
5431	54	002	Afiliación	
8014	40	023	Quintana Roo	
8015	40	004	Campeche	
8016	40	010	Durango	
8017	40	011	Guanajuato	
8018	40	012	Guerrero	
8019	40	013	Hidalgo	
8020	40	014	Jalisco	
8021	40	015	México	
8022	40	016	Michoacán	
8024	40	018	Nayarit	
8025	40	019	Nuevo León	
8026	40	030	Veracruz	
8027	40	031	Yucatán	
8028	40	032	Zacatecas	
8029	40	003	Baja California Sur	
8031	40	001	Aguascalientes	
8032	40	026	Sonora	
8033	40	021	Puebla	
8034	40	020	Oaxaca	
8035	40	005	Coahuila	
8036	40	022	Querétaro	
8038	40	009	Distrito Federal	
8039	40	008	Chihuahua	
8040	40	029	Tlaxcala	
8042	40	025	Sinaloa	
8044	40	024	San Luis Potosí	
8046	40	027	Tabasco	
8049	40	007	Chiapas	
8051	40	006	Colima	
8052	8020	014001	Acatic	
8054	8020	014003	Ahualulco de Mercado	
8055	8020	014004	Amacueca	
8056	8020	014005	Amatitán	
8057	8020	014006	Ameca	
209	53	210	Iglesias	Comprende iglesias de cualquier credo
232	53	370	Narcotráfico	Asigna también el tema de "Delincuencia organizada" que se encuentra en esta misma lista.
208	53	420	Personas con discapacidad	Comprende cualquier tipo de discapacidad física o mental
247	53	500	Proyectos económicos	Incluye megaproyectos.
272	53	680	Violencia contra las mujeres	Incluye violencia física y psicológica.
8058	8020	014007	San Juanito de Escobedo	
8059	8020	014008	Arandas	
8060	8020	014009	El Arenal	
8061	8020	014010	Atemajac de Brizuela	
8062	8020	014011	Atengo	
8063	8020	014012	Atenguillo	
8064	8020	014013	Atotonilco el Alto	
8065	8020	014014	Atoyac	
8067	8020	014016	Ayotlán	
8068	8020	014017	Ayutla	
8069	8020	014018	La Barca	
8070	8020	014019	Bolaños	
8071	8020	014020	Cabo Corrientes	
8072	8020	014021	Casimiro Castillo	
8073	8020	014022	Cihuatlán	
8074	8020	014023	Zapotlán el Grande	
8075	8020	014024	Cocula	
8076	8020	014025	Colotlán	
8078	8020	014027	Cuautitlán de García Barragán	
8079	8020	014028	Cuautla	
8080	8020	014029	Cuquío	
8081	8020	014030	Chapala	
8082	8020	014031	Chimaltitán	
8083	8020	014032	Chiquilistlán	
8084	8020	014033	Degollado	
8085	8020	014034	Ejutla	
8086	8020	014035	Encarnación de Díaz	
8087	8020	014036	Etzatlán	
8088	8020	014037	El Grullo	
8089	8020	014038	Guachinango	
8090	8020	014039	Guadalajara	
8091	8020	014040	Hostotipaquillo	
8094	8020	014043	La Huerta	
8095	8020	014044	Ixtlahuacán de los Membrillos	
8096	8020	014045	Ixtlahuacán del Río	
8097	8020	014046	Jalostotitlán	
8098	8020	014047	Jamay	
8100	8020	014049	Jilotlán de los Dolores	
8101	8020	014050	Jocotepec	
8102	8020	014051	Juanacatlán	
8103	8020	014052	Juchitlán	
8104	8020	014053	Lagos de Moreno	
8105	8020	014054	El Limón	
8106	8020	014055	Magdalena	
8107	8020	014056	Santa María del Oro	
8109	8020	014058	Mascota	
8110	8020	014059	Mazamitla	
8111	8020	014060	Mexticacán	
8112	8020	014061	Mezquitic	
8113	8020	014062	Mixtlán	
8114	8020	014063	Ocotlán	
8115	8020	014064	Ojuelos de Jalisco	
8116	8020	014065	Pihuamo	
8117	8020	014066	Poncitlán	
8118	8020	014067	Puerto Vallarta	
8119	8020	014068	Villa Purificación	
8120	8020	014069	Quitupan	
8122	8020	014071	San Cristóbal de la Barranca	
8123	8020	014072	San Diego de Alejandría	
8124	8020	014073	San Juan de los Lagos	
8125	8020	014074	San Julián	
8126	8020	014075	San Marcos	
8127	8020	014076	San Martín de Bolaños	
8128	8020	014077	San Martín Hidalgo	
8129	8020	014078	San Miguel el Alto	
8130	8020	014079	Gómez Farías	
8132	8020	014081	Santa María de los Ángeles	
8133	8020	014082	Sayula	
8134	8020	014083	Tala	
8135	8020	014084	Talpa de Allende	
8136	8020	014085	Tamazula de Gordiano	
8137	8020	014086	Tapalpa	
8138	8020	014087	Tecalitlán	
8139	8020	014088	Tecolotlán	
8140	8020	014089	Techaluta de Montenegro	
8141	8020	014090	Tenamaxtlán	
8142	8020	014091	Teocaltiche	
8143	8020	014092	Teocuitatlán de Corona	
8144	8020	014093	Tepatitlán de Morelos	
8145	8020	014094	Tequila	
8146	8020	014095	Teuchitlán	
8149	8020	014098	Tlaquepaque	
8150	8020	014099	Tolimán	
8151	8020	014100	Tomatlán	
8152	8020	014101	Tonalá	
8153	8020	014102	Tonaya	
8154	8020	014103	Tonila	
8155	8020	014104	Totatiche	
8156	8020	014105	Tototlán	
8157	8020	014106	Tuxcacuesco	
8158	8020	014107	Tuxcueca	
8159	8020	014108	Tuxpan	
8161	8020	014110	Unión de Tula	
8162	8020	014111	Valle de Guadalupe	
8163	8020	014112	Valle de Juárez	
8164	8020	014113	San Gabriel	
8165	8020	014114	Villa Corona	
8166	8020	014115	Villa Guerrero	
8167	8020	014116	Villa Hidalgo	
8168	8020	014117	Cañadas de Obregón	
8170	8020	014119	Zacoalco de Torres	
8171	8020	014120	Zapopan	
8172	8020	014121	Zapotiltic	
8173	8020	014122	Zapotitlán de Vadillo	
8174	8020	014123	Zapotlán del Rey	
8175	8020	014124	Zapotlanejo	
8176	8020	014125	San Ignacio Cerro Gordo	
8178	8033	021001	Acajete	
8179	8033	021002	Acateno	
8180	8033	021003	Acatlán	
8181	8033	021004	Acatzingo	
8184	8033	021007	Ahuatlán	
8185	8033	021008	Ahuazotepec	
8186	8033	021009	Ahuehuetitla	
8187	8033	021010	Ajalpan	
8188	8033	021011	Albino Zertuche	
8189	8033	021012	Aljojuca	
8190	8033	021013	Altepexi	
8191	8033	021014	Amixtlán	
8192	8033	021015	Amozoc	
8194	8033	021017	Atempan	
8195	8033	021018	Atexcal	
8196	8033	021019	Atlixco	
8197	8033	021020	Atoyatempan	
8198	8033	021021	Atzala	
8199	8033	021022	Atzitzihuacán	
8200	8033	021023	Atzitzintla	
8201	8033	021024	Axutla	
8202	8033	021025	Ayotoxco de Guerrero	
8203	8033	021026	Calpan	
8204	8033	021027	Caltepec	
8148	8020	014097	Tlajomulco de Zúñiga	
8092	8020	014041	Huejúcar	
8206	8033	021029	Caxhuacan	
8207	8033	021030	Coatepec	
8208	8033	021031	Coatzingo	
8209	8033	021032	Cohetzala	
8210	8033	021033	Cohuecan	
8211	8033	021034	Coronango	
8212	8033	021035	Coxcatlán	
8213	8033	021036	Coyomeapan	
8215	8033	021038	Cuapiaxtla de Madero	
8216	8033	021039	Cuautempan	
8217	8033	021040	Cuautinchán	
8218	8033	021041	Cuautlancingo	
8219	8033	021042	Cuayuca de Andrade	
8220	8033	021043	Cuetzalan del Progreso	
8221	8033	021044	Cuyoaco	
8222	8033	021045	Chalchicomula de Sesma	
8223	8033	021046	Chapulco	
8224	8033	021047	Chiautla	
8226	8033	021049	Chiconcuautla	
8227	8033	021050	Chichiquila	
8228	8033	021051	Chietla	
8229	8033	021052	Chigmecatitlán	
8230	8033	021053	Chignahuapan	
8231	8033	021054	Chignautla	
8232	8033	021055	Chila	
8233	8033	021056	Chila de la Sal	
8234	8033	021057	Honey	
8235	8033	021058	Chilchotla	
8236	8033	021059	Chinantla	
8237	8033	021060	Domingo Arenas	
8238	8033	021061	Eloxochitlán	
8239	8033	021062	Epatlán	
8241	8033	021064	Francisco Z. Mena	
8242	8033	021065	General Felipe Ángeles	
8243	8033	021066	Guadalupe	
8244	8033	021067	Guadalupe Victoria	
8245	8033	021068	Hermenegildo Galeana	
8246	8033	021069	Huaquechula	
8247	8033	021070	Huatlatlauca	
8248	8033	021071	Huauchinango	
8249	8033	021072	Huehuetla	
8250	8033	021073	Huehuetlán el Chico	
8251	8033	021074	Huejotzingo	
8252	8033	021075	Hueyapan	
8254	8033	021077	Hueytlalpan	
8255	8033	021078	Huitzilan de Serdán	
8256	8033	021079	Huitziltepec	
8257	8033	021080	Atlequizayan	
8258	8033	021081	Ixcamilpa de Guerrero	
8259	8033	021082	Ixcaquixtla	
8260	8033	021083	Ixtacamaxtitlán	
8261	8033	021084	Ixtepec	
8263	8033	021086	Jalpan	
8264	8033	021087	Jolalpan	
8265	8033	021088	Jonotla	
8266	8033	021089	Jopala	
8267	8033	021090	Juan C. Bonilla	
8268	8033	021091	Juan Galindo	
8269	8033	021092	Juan N. Méndez	
8270	8033	021093	Lafragua	
8271	8033	021094	Libres	
8272	8033	021095	La Magdalena Tlatlauquitepec	
8273	8033	021096	Mazapiltepec de Juárez	
8274	8033	021097	Mixtla	
8275	8033	021098	Molcaxac	
8277	8033	021100	Naupan	
8278	8033	021101	Nauzontla	
8279	8033	021102	Nealtican	
8280	8033	021103	Nicolás Bravo	
8281	8033	021104	Nopalucan	
8282	8033	021105	Ocotepec	
8283	8033	021106	Ocoyucan	
8284	8033	021107	Olintla	
8285	8033	021108	Oriental	
8287	8033	021110	Palmar de Bravo	
8288	8033	021111	Pantepec	
8289	8033	021112	Petlalcingo	
8290	8033	021113	Piaxtla	
8291	8033	021114	Puebla	
8292	8033	021115	Quecholac	
8293	8033	021116	Quimixtlán	
8294	8033	021117	Rafael Lara Grajales	
8296	8033	021119	San Andrés Cholula	
8297	8033	021120	San Antonio Cañada	
8298	8033	021121	San Diego la Mesa Tochimiltzingo	
8299	8033	021122	San Felipe Teotlalcingo	
8300	8033	021123	San Felipe Tepatlán	
8301	8033	021124	San Gabriel Chilac	
8302	8033	021125	San Gregorio Atzompa	
8303	8033	021126	San Jerónimo Tecuanipan	
8304	8033	021127	San Jerónimo Xayacatlán	
8305	8033	021128	San José Chiapa	
8307	8033	021130	San Juan Atenco	
8308	8033	021131	San Juan Atzompa	
8309	8033	021132	San Martín Texmelucan	
8310	8033	021133	San Martín Totoltepec	
8311	8033	021134	San Matías Tlalancaleca	
8312	8033	021135	San Miguel Ixitlán	
8313	8033	021136	San Miguel Xoxtla	
8314	8033	021137	San Nicolás Buenos Aires	
8315	8033	021138	San Nicolás de los Ranchos	
8316	8033	021139	San Pablo Anicano	
8317	8033	021140	San Pedro Cholula	
8319	8033	021142	San Salvador el Seco	
8320	8033	021143	San Salvador el Verde	
8321	8033	021144	San Salvador Huixcolotla	
8323	8033	021146	Santa Catarina Tlaltempan	
8324	8033	021147	Santa Inés Ahuatempan	
8325	8033	021148	Santa Isabel Cholula	
8326	8033	021149	Santiago Miahuatlán	
8327	8033	021150	Huehuetlán el Grande	
8328	8033	021151	Santo Tomás Hueyotlipan	
8329	8033	021152	Soltepec	
8330	8033	021153	Tecali de Herrera	
8331	8033	021154	Tecamachalco	
8332	8033	021155	Tecomatlán	
8333	8033	021156	Tehuacán	
8334	8033	021157	Tehuitzingo	
8335	8033	021158	Tenampulco	
8336	8033	021159	Teopantlán	
8337	8033	021160	Teotlalco	
8339	8033	021162	Tepango de Rodríguez	
8340	8033	021163	Tepatlaxco de Hidalgo	
8341	8033	021164	Tepeaca	
8342	8033	021165	Tepemaxalco	
8343	8033	021166	Tepeojuma	
8344	8033	021167	Tepetzintla	
8345	8033	021168	Tepexco	
8346	8033	021169	Tepexi de Rodríguez	
8347	8033	021170	Tepeyahualco	
8348	8033	021171	Tepeyahualco de Cuauhtémoc	
8349	8033	021172	Tetela de Ocampo	
8350	8033	021173	Teteles de Avila Castillo	
8351	8033	021174	Teziutlán	
8352	8033	021175	Tianguismanalco	
8353	8033	021176	Tilapa	
8355	8033	021178	Tlacuilotepec	
8356	8033	021179	Tlachichuca	
8357	8033	021180	Tlahuapan	
8358	8033	021181	Tlaltenango	
8359	8033	021182	Tlanepantla	
8360	8033	021183	Tlaola	
8361	8033	021184	Tlapacoya	
8362	8033	021185	Tlapanalá	
8363	8033	021186	Tlatlauquitepec	
8364	8033	021187	Tlaxco	
8365	8033	021188	Tochimilco	
8366	8033	021189	Tochtepec	
8367	8033	021190	Totoltepec de Guerrero	
8368	8033	021191	Tulcingo	
8369	8033	021192	Tuzamapan de Galeana	
8370	8033	021193	Tzicatlacoyan	
8372	8033	021195	Vicente Guerrero	
8373	8033	021196	Xayacatlán de Bravo	
8374	8033	021197	Xicotepec	
8375	8033	021198	Xicotlán	
8376	8033	021199	Xiutetelco	
8377	8033	021200	Xochiapulco	
8378	8033	021201	Xochiltepec	
8379	8033	021202	Xochitlán de Vicente Suárez	
8380	8033	021203	Xochitlán Todos Santos	
8381	8033	021204	Yaonáhuac	
8382	8033	021205	Yehualtepec	
8383	8033	021206	Zacapala	
8384	8033	021207	Zacapoaxtla	
8386	8033	021209	Zapotitlán	
8387	8033	021210	Zapotitlán de Méndez	
8388	8033	021211	Zaragoza	
8389	8033	021212	Zautla	
8390	8033	021213	Zihuateutla	
8391	8033	021214	Zinacatepec	
8392	8033	021215	Zongozotla	
8393	8033	021216	Zoquiapan	
8394	8033	021217	Zoquitlán	
8396	8023	017001	Amacuzac	
8398	8023	017003	Axochiapan	
8399	8023	017004	Ayala	
8400	8023	017005	Coatlán del Río	
8401	8023	017006	Cuautla	
8402	8023	017007	Cuernavaca	
8403	8023	017008	Emiliano Zapata	
8404	8023	017009	Huitzilac	
8405	8023	017010	Jantetelco	
8406	8023	017011	Jiutepec	
8407	8023	017012	Jojutla	
8408	8023	017013	Jonacatepec	
8409	8023	017014	Mazatepec	
8411	8023	017016	Ocuituco	
8412	8023	017017	Puente de Ixtla	
8413	8023	017018	Temixco	
8414	8023	017019	Tepalcingo	
8415	8023	017020	Tepoztlán	
8416	8023	017021	Tetecala	
8417	8023	017022	Tetela del Volcán	
8418	8023	017023	Tlalnepantla	
8419	8023	017024	Tlaltizapán	
8420	8023	017025	Tlaquiltenango	
8422	8023	017027	Totolapan	
8423	8023	017028	Xochitepec	
8424	8023	017029	Yautepec	
8425	8023	017030	Yecapixtla	
8426	8023	017031	Zacatepec	
8427	8023	017032	Zacualpan	
8428	8023	017033	Temoac	
8429	8027	031001	Abalá	
8430	8027	031002	Acanceh	
8431	8027	031003	Akil	
8432	8027	031004	Baca	
8433	8027	031005	Bokobá	
8435	8027	031007	Cacalchén	
8436	8027	031008	Calotmul	
8437	8027	031009	Cansahcab	
8438	8027	031010	Cantamayec	
8440	8027	031012	Cenotillo	
8441	8027	031013	Conkal	
8442	8027	031014	Cuncunul	
8443	8027	031015	Cuzamá	
8445	8027	031017	Chankom	
8446	8027	031018	Chapab	
8447	8027	031019	Chemax	
8448	8027	031020	Chicxulub Pueblo	
8449	8027	031021	Chichimilá	
8450	8027	031022	Chikindzonot	
8451	8027	031023	Chocholá	
8452	8027	031024	Chumayel	
8453	8027	031025	Dzán	
8454	8027	031026	Dzemul	
8456	8027	031028	Dzilam de Bravo	
8458	8027	031030	Dzitás	
8459	8027	031031	Dzoncauich	
8460	8027	031032	Espita	
8461	8027	031033	Halachó	
8462	8027	031034	Hocabá	
8465	8027	031037	Huhí	
8466	8027	031038	Hunucmá	
8467	8027	031039	Ixil	
8468	8027	031040	Izamal	
8470	8027	031042	Kantunil	
8471	8027	031043	Kaua	
8472	8027	031044	Kinchil	
8473	8027	031045	Kopomá	
8474	8027	031046	Mama	
8475	8027	031047	Maní	
8477	8027	031049	Mayapán	
8479	8027	031051	Mocochá	
8480	8027	031052	Motul	
8481	8027	031053	Muna	
8482	8027	031054	Muxupip	
8483	8027	031055	Opichén	
8484	8027	031056	Oxkutzcab	
8485	8027	031057	Panabá	
8486	8027	031058	Peto	
8488	8027	031060	Quintana Roo	
8489	8027	031061	Río Lagartos	
8490	8027	031062	Sacalum	
8491	8027	031063	Samahil	
8492	8027	031064	Sanahcat	
8493	8027	031065	San Felipe	
8494	8027	031066	Santa Elena	
8495	8027	031067	Seyé	
8497	8027	031069	Sotuta	
8498	8027	031070	Sucilá	
8499	8027	031071	Sudzal	
8500	8027	031072	Suma	
8502	8027	031074	Tahmek	
8463	8027	031035	Hoctún	
8464	8027	031036	Homún	
8476	8027	031048	Maxcanú	
8501	8027	031073	Tahdziú	
8503	8027	031075	Teabo	
8504	8027	031076	Tecoh	
8505	8027	031077	Tekal de Venegas	
8506	8027	031078	Tekantó	
8508	8027	031080	Tekit	
8509	8027	031081	Tekom	
8510	8027	031082	Telchac Pueblo	
8511	8027	031083	Telchac Puerto	
8512	8027	031084	Temax	
8513	8027	031085	Temozón	
8514	8027	031086	Tepakán	
8515	8027	031087	Tetiz	
8517	8027	031089	Ticul	
8518	8027	031090	Timucuy	
8519	8027	031091	Tinum	
8520	8027	031092	Tixcacalcupul	
8521	8027	031093	Tixkokob	
8522	8027	031094	Tixmehuac	
8523	8027	031095	Tixpéhual	
8524	8027	031096	Tizimín	
8526	8027	031098	Tzucacab	
8527	8027	031099	Uayma	
8529	8027	031101	Umán	
8530	8027	031102	Valladolid	
8531	8027	031103	Xocchel	
8532	8027	031104	Yaxcabá	
8534	8027	031106	Yobaín	
8535	8049	007001	Acacoyagua	
8536	8049	007002	Acala	
8537	8049	007003	Acapetahua	
8538	8049	007004	Altamirano	
8539	8049	007005	Amatán	
8540	8049	007006	Amatenango de la Frontera	
8541	8049	007007	Amatenango del Valle	
8543	8049	007009	Arriaga	
8545	8049	007011	Bella Vista	
8546	8049	007012	Berriozábal	
8547	8049	007013	Bochil	
8548	8049	007014	El Bosque	
8549	8049	007015	Cacahoatán	
8550	8049	007016	Catazajá	
8551	8049	007017	Cintalapa	
8552	8049	007018	Coapilla	
8553	8049	007019	Comitán de Domínguez	
8554	8049	007020	La Concordia	
8555	8049	007021	Copainalá	
8556	8049	007022	Chalchihuitán	
8557	8049	007023	Chamula	
8558	8049	007024	Chanal	
8559	8049	007025	Chapultenango	
8561	8049	007027	Chiapa de Corzo	
8562	8049	007028	Chiapilla	
8563	8049	007029	Chicoasén	
8564	8049	007030	Chicomuselo	
8565	8049	007031	Chilón	
8566	8049	007032	Escuintla	
8567	8049	007033	Francisco León	
8568	8049	007034	Frontera Comalapa	
8569	8049	007035	Frontera Hidalgo	
8570	8049	007036	La Grandeza	
8571	8049	007037	Huehuetán	
8572	8049	007038	Huixtán	
8574	8049	007040	Huixtla	
8575	8049	007041	La Independencia	
8576	8049	007042	Ixhuatán	
8577	8049	007043	Ixtacomitán	
8578	8049	007044	Ixtapa	
8579	8049	007045	Ixtapangajoya	
8580	8049	007046	Jiquipilas	
8581	8049	007047	Jitotol	
8582	8049	007048	Juárez	
8583	8049	007049	Larráinzar	
8585	8049	007051	Mapastepec	
8586	8049	007052	Las Margaritas	
8587	8049	007053	Mazapa de Madero	
8588	8049	007054	Mazatán	
8589	8049	007055	Metapa	
8590	8049	007056	Mitontic	
8591	8049	007057	Motozintla	
8592	8049	007058	Nicolás Ruíz	
8594	8049	007060	Ocotepec	
8595	8049	007061	Ocozocoautla de Espinosa	
8596	8049	007062	Ostuacán	
8597	8049	007063	Osumacinta	
8598	8049	007064	Oxchuc	
8599	8049	007065	Palenque	
8603	8049	007069	Pijijiapan	
8604	8049	007070	El Porvenir	
8605	8049	007071	Villa Comaltitlán	
8606	8049	007072	Pueblo Nuevo Solistahuacán	
8607	8049	007073	Rayón	
8608	8049	007074	Reforma	
8609	8049	007075	Las Rosas	
8610	8049	007076	Sabanilla	
8611	8049	007077	Salto de Agua	
8612	8049	007078	San Cristóbal de las Casas	
8613	8049	007079	San Fernando	
8614	8049	007080	Siltepec	
8616	8049	007082	Sitalá	
8617	8049	007083	Socoltenango	
8618	8049	007084	Solosuchiapa	
8619	8049	007085	Soyaló	
8620	8049	007086	Suchiapa	
8621	8049	007087	Suchiate	
8622	8049	007088	Sunuapa	
8623	8049	007089	Tapachula	
8624	8049	007090	Tapalapa	
8626	8049	007092	Tecpatán	
8627	8049	007093	Tenejapa	
8628	8049	007094	Teopisca	
8629	8049	007096	Tila	
8630	8049	007097	Tonalá	
8631	8049	007098	Totolapa	
8633	8049	007100	Tumbalá	
8634	8049	007101	Tuxtla Gutiérrez	
8635	8049	007102	Tuxtla Chico	
8636	8049	007103	Tuzantán	
8637	8049	007104	Tzimol	
8638	8049	007105	Unión Juárez	
8639	8049	007106	Venustiano Carranza	
8640	8049	007107	Villa Corzo	
8641	8049	007108	Villaflores	
8642	8049	007109	Yajalón	
8644	8049	007111	Zinacantán	
8645	8049	007112	San Juan Cancuc	
8646	8049	007113	Aldama	
8647	8049	007114	Benemérito de las Américas	
8648	8049	007115	Maravilla Tenejapa	
8649	8049	007116	Marqués de Comillas	
8650	8049	007117	Montecristo de Guerrero	
8651	8049	007118	San Andrés Duraznal	
8652	8049	007119	Santiago el Pinar	
8653	8032	026001	Aconchi	
8654	8032	026002	Agua Prieta	
8655	8032	026003	Alamos	
8542	8049	007008	Angel Albino Corzo	
8656	8032	026004	Altar	
8658	8032	026006	Arizpe	
8659	8032	026007	Atil	
8660	8032	026008	Bacadéhuachi	
8661	8032	026009	Bacanora	
8662	8032	026010	Bacerac	
8663	8032	026011	Bacoachi	
8664	8032	026012	Bácum	
8665	8032	026013	Banámichi	
8667	8032	026015	Bavispe	
8668	8032	026016	Benjamín Hill	
8669	8032	026017	Caborca	
8670	8032	026018	Cajeme	
8671	8032	026019	Cananea	
8672	8032	026020	Carbó	
8673	8032	026021	La Colorada	
8674	8032	026022	Cucurpe	
8675	8032	026023	Cumpas	
8676	8032	026024	Divisaderos	
8677	8032	026025	Empalme	
8678	8032	026026	Etchojoa	
8680	8032	026028	Granados	
8681	8032	026029	Guaymas	
8682	8032	026030	Hermosillo	
8683	8032	026031	Huachinera	
8684	8032	026032	Huásabas	
8685	8032	026033	Huatabampo	
8686	8032	026034	Huépac	
8687	8032	026035	Imuris	
8688	8032	026036	Magdalena	
8689	8032	026037	Mazatán	
8691	8032	026039	Naco	
8692	8032	026040	Nácori Chico	
8693	8032	026041	Nacozari de García	
8694	8032	026042	Navojoa	
8695	8032	026043	Nogales	
8696	8032	026044	Onavas	
8697	8032	026045	Opodepe	
8698	8032	026046	Oquitoa	
8699	8032	026047	Pitiquito	
8700	8032	026048	Puerto Peñasco	
8701	8032	026049	Quiriego	
8702	8032	026050	Rayón	
8703	8032	026051	Rosario	
8706	8032	026054	San Javier	
8707	8032	026055	San Luis Río Colorado	
8708	8032	026056	San Miguel de Horcasitas	
8709	8032	026057	San Pedro de la Cueva	
8710	8032	026058	Santa Ana	
8711	8032	026059	Santa Cruz	
8712	8032	026060	Sáric	
8713	8032	026061	Soyopa	
8714	8032	026062	Suaqui Grande	
8715	8032	026063	Tepache	
8717	8032	026065	Tubutama	
8718	8032	026066	Ures	
8719	8032	026067	Villa Hidalgo	
8720	8032	026068	Villa Pesqueira	
8721	8032	026069	Yécora	
8722	8032	026070	General Plutarco Elías Calles	
8723	8032	026071	Benito Juárez	
8724	8032	026072	San Ignacio Río Muerto	
8727	8028	032001	Apozol	
8728	8028	032002	Apulco	
8729	8028	032003	Atolinga	
8731	8028	032005	Calera	
8732	8028	032006	Cañitas de Felipe Pescador	
8733	8028	032007	Concepción del Oro	
8734	8028	032008	Cuauhtémoc	
8735	8028	032009	Chalchihuites	
8736	8028	032010	Fresnillo	
8737	8028	032011	Trinidad García de la Cadena	
8738	8028	032012	Genaro Codina	
8739	8028	032013	General Enrique Estrada	
8741	8028	032015	El Plateado de Joaquín Amaro	
8742	8028	032016	General Pánfilo Natera	
8744	8028	032018	Huanusco	
8745	8028	032019	Jalpa	
8746	8028	032020	Jerez	
8747	8028	032021	Jiménez del Teul	
8748	8028	032022	Juan Aldama	
8749	8028	032023	Juchipila	
8750	8028	032024	Loreto	
8752	8028	032026	Mazapil	
8753	8028	032027	Melchor Ocampo	
8754	8028	032028	Mezquital del Oro	
8755	8028	032029	Miguel Auza	
8756	8028	032030	Momax	
8757	8028	032031	Monte Escobedo	
8758	8028	032032	Morelos	
8759	8028	032033	Moyahua de Estrada	
8760	8028	032034	Nochistlán de Mejía	
8761	8028	032035	Noria de Ángeles	
8762	8028	032036	Ojocaliente	
8763	8028	032037	Pánuco	
8764	8028	032038	Pinos	
8765	8028	032039	Río Grande	
8767	8028	032041	El Salvador	
8768	8028	032042	Sombrerete	
8769	8028	032043	Susticacán	
8770	8028	032044	Tabasco	
8771	8028	032045	Tepechitlán	
8772	8028	032046	Tepetongo	
8774	8028	032048	Tlaltenango de Sánchez Román	
8775	8028	032049	Valparaíso	
8776	8028	032050	Vetagrande	
8777	8028	032051	Villa de Cos	
8778	8028	032052	Villa García	
8780	8028	032054	Villa Hidalgo	
8781	8028	032055	Villanueva	
8782	8028	032056	Zacatecas	
8783	8028	032057	Trancoso	
8784	8028	032058	Santa María de la Paz	
8785	8038	009002	Azcapotzalco	
8786	8038	009003	Coyoacán	
8787	8038	009004	Cuajimalpa de Morelos	
8788	8038	009005	Gustavo A. Madero	
8789	8038	009006	Iztacalco	
8790	8038	009007	Iztapalapa	
8791	8038	009008	La Magdalena Contreras	
8792	8038	009009	Milpa Alta	
8793	8038	009010	Álvaro Obregón	
8795	8038	009012	Tlalpan	
8796	8038	009013	Xochimilco	
8797	8038	009014	Benito Juárez	
8798	8038	009015	Cuauhtémoc	
8799	8038	009016	Miguel Hidalgo	
8800	8038	009017	Venustiano Carranza	
8801	8019	013001	Acatlán	
8802	8019	013002	Acaxochitlán	
8803	8019	013003	Actopan	
8805	8019	013005	Ajacuba	
8806	8019	013006	Alfajayucan	
8807	8019	013007	Almoloya	
8808	8019	013008	Apan	
8773	8028	032047	Teúl de González Ortega	
8809	8019	013009	El Arenal	
8810	8019	013010	Atitalaquia	
8811	8019	013011	Atlapexco	
8812	8019	013012	Atotonilco el Grande	
8813	8019	013013	Atotonilco de Tula	
8814	8019	013014	Calnali	
8815	8019	013015	Cardonal	
8817	8019	013017	Chapantongo	
8818	8019	013018	Chapulhuacán	
8819	8019	013019	Chilcuautla	
8820	8019	013020	Eloxochitlán	
8821	8019	013021	Emiliano Zapata	
8822	8019	013022	Epazoyucan	
8823	8019	013023	Francisco I. Madero	
8824	8019	013024	Huasca de Ocampo	
8825	8019	013025	Huautla	
8826	8019	013026	Huazalingo	
8827	8019	013027	Huehuetla	
8828	8019	013028	Huejutla de Reyes	
8829	8019	013029	Huichapan	
8830	8019	013030	Ixmiquilpan	
8832	8019	013032	Jaltocán	
8833	8019	013033	Juárez Hidalgo	
8834	8019	013034	Lolotla	
8835	8019	013035	Metepec	
8836	8019	013036	San Agustín Metzquititlán	
8837	8019	013037	Metztitlán	
8838	8019	013038	Mineral del Chico	
8839	8019	013039	Mineral del Monte	
8840	8019	013040	La Misión	
8841	8019	013041	Mixquiahuala de Juárez	
8842	8019	013042	Molango de Escamilla	
8843	8019	013043	Nicolás Flores	
8844	8019	013044	Nopala de Villagrán	
8845	8019	013045	Omitlán de Juárez	
8846	8019	013046	San Felipe Orizatlán	
8847	8019	013047	Pacula	
8848	8019	013048	Pachuca de Soto	
8849	8019	013049	Pisaflores	
8851	8019	013051	Mineral de la Reforma	
8852	8019	013052	San Agustín Tlaxiaca	
8853	8019	013053	San Bartolo Tutotepec	
8854	8019	013054	San Salvador	
8855	8019	013055	Santiago de Anaya	
8856	8019	013056	Santiago Tulantepec de Lugo Guerrero	
8857	8019	013057	Singuilucan	
8858	8019	013058	Tasquillo	
8859	8019	013059	Tecozautla	
8860	8019	013060	Tenango de Doria	
8861	8019	013061	Tepeapulco	
8862	8019	013062	Tepehuacán de Guerrero	
8864	8019	013064	Tepetitlán	
8865	8019	013065	Tetepango	
8866	8019	013066	Villa de Tezontepec	
8867	8019	013067	Tezontepec de Aldama	
8868	8019	013068	Tianguistengo	
8869	8019	013069	Tizayuca	
8870	8019	013070	Tlahuelilpan	
8871	8019	013071	Tlahuiltepa	
8872	8019	013072	Tlanalapa	
8873	8019	013073	Tlanchinol	
8874	8019	013074	Tlaxcoapan	
8875	8019	013075	Tolcayuca	
8877	8019	013077	Tulancingo de Bravo	
8878	8019	013078	Xochiatipan	
8879	8019	013079	Xochicoatlán	
8880	8019	013080	Yahualica	
8881	8019	013081	Zacualtipán de Ángeles	
8882	8019	013082	Zapotlán de Juárez	
8883	8019	013083	Zempoala	
8885	8041	028001	Abasolo	
8886	8041	028002	Aldama	
8887	8041	028003	Altamira	
8888	8041	028004	Antiguo Morelos	
8889	8041	028005	Burgos	
8890	8041	028006	Bustamante	
8891	8041	028007	Camargo	
8892	8041	028008	Casas	
8893	8041	028009	Ciudad Madero	
8895	8041	028011	Gómez Farías	
8896	8041	028012	González	
8897	8041	028013	Güémez	
8898	8041	028014	Guerrero	
8899	8041	028015	Gustavo Díaz Ordaz	
8900	8041	028016	Hidalgo	
8901	8041	028017	Jaumave	
8902	8041	028018	Jiménez	
8904	8041	028020	Mainero	
8905	8041	028021	El Mante	
8906	8041	028022	Matamoros	
8907	8041	028023	Méndez	
8908	8041	028024	Mier	
8909	8041	028025	Miguel Alemán	
8910	8041	028026	Miquihuana	
8911	8041	028027	Nuevo Laredo	
8913	8041	028029	Ocampo	
8914	8041	028030	Padilla	
8915	8041	028031	Palmillas	
8916	8041	028032	Reynosa	
8917	8041	028033	Río Bravo	
8918	8041	028034	San Carlos	
8919	8041	028035	San Fernando	
8920	8041	028036	San Nicolás	
8921	8041	028037	Soto la Marina	
8922	8041	028038	Tampico	
8923	8041	028039	Tula	
8924	8041	028040	Valle Hermoso	
8925	8041	028041	Victoria	
8927	8041	028043	Xicoténcatl	
8928	8022	016001	Acuitzio	
8929	8022	016002	Aguililla	
8930	8022	016003	Álvaro Obregón	
8931	8022	016004	Angamacutiro	
8932	8022	016005	Angangueo	
8933	8022	016006	Apatzingán	
8934	8022	016007	Aporo	
8935	8022	016008	Aquila	
8936	8022	016009	Ario	
8937	8022	016010	Arteaga	
8939	8022	016012	Buenavista	
8940	8022	016013	Carácuaro	
8941	8022	016014	Coahuayana	
8942	8022	016015	Coalcomán de Vázquez Pallares	
8943	8022	016016	Coeneo	
8944	8022	016017	Contepec	
8945	8022	016018	Copándaro	
8946	8022	016019	Cotija	
8947	8022	016020	Cuitzeo	
8948	8022	016021	Charapan	
8950	8022	016023	Chavinda	
8951	8022	016024	Cherán	
8952	8022	016025	Chilchota	
8953	8022	016026	Chinicuila	
8954	8022	016027	Chucándiro	
8955	8022	016028	Churintzio	
8956	8022	016029	Churumuco	
8957	8022	016030	Ecuandureo	
8959	8022	016032	Erongarícuaro	
8960	8022	016033	Gabriel Zamora	
8961	8022	016034	Hidalgo	
8962	8022	016035	La Huacana	
8963	8022	016036	Huandacareo	
8964	8022	016037	Huaniqueo	
8965	8022	016038	Huetamo	
8966	8022	016039	Huiramba	
8967	8022	016040	Indaparapeo	
8968	8022	016041	Irimbo	
8969	8022	016042	Ixtlán	
8970	8022	016043	Jacona	
8972	8022	016045	Jiquilpan	
8973	8022	016046	Juárez	
8974	8022	016047	Jungapeo	
8975	8022	016048	Lagunillas	
8976	8022	016049	Madero	
8977	8022	016050	Maravatío	
8978	8022	016051	Marcos Castellanos	
8979	8022	016052	Lázaro Cárdenas	
8980	8022	016053	Morelia	
8981	8022	016054	Morelos	
8984	8022	016057	Nocupétaro	
8985	8022	016058	Nuevo Parangaricutiro	
8986	8022	016059	Nuevo Urecho	
8987	8022	016060	Numarán	
8988	8022	016061	Ocampo	
8989	8022	016062	Pajacuarán	
8990	8022	016063	Panindícuaro	
8991	8022	016064	Parácuaro	
8992	8022	016065	Paracho	
8993	8022	016066	Pátzcuaro	
8994	8022	016067	Penjamillo	
8996	8022	016069	La Piedad	
8997	8022	016070	Purépero	
8998	8022	016071	Puruándiro	
8999	8022	016072	Queréndaro	
9000	8022	016073	Quiroga	
9001	8022	016074	Cojumatlán de Régules	
9002	8022	016075	Los Reyes	
9003	8022	016076	Sahuayo	
9004	8022	016077	San Lucas	
9005	8022	016078	Santa Ana Maya	
9007	8022	016080	Senguio	
9008	8022	016081	Susupuato	
9009	8022	016082	Tacámbaro	
9010	8022	016083	Tancítaro	
9011	8022	016084	Tangamandapio	
9012	8022	016085	Tangancícuaro	
9013	8022	016086	Tanhuato	
9014	8022	016087	Taretan	
9015	8022	016088	Tarímbaro	
9016	8022	016089	Tepalcatepec	
9017	8022	016090	Tingambato	
9019	8022	016092	Tiquicheo de Nicolás Romero	
9020	8022	016093	Tlalpujahua	
9021	8022	016094	Tlazazalca	
9022	8022	016095	Tocumbo	
9023	8022	016096	Tumbiscatío	
9024	8022	016097	Turicato	
9025	8022	016098	Tuxpan	
9026	8022	016099	Tuzantla	
9027	8022	016100	Tzintzuntzan	
9028	8022	016101	Tzitzio	
9029	8022	016102	Uruapan	
9031	8022	016104	Villamar	
9032	8022	016105	Vista Hermosa	
9033	8022	016106	Yurécuaro	
9034	8022	016107	Zacapu	
9035	8022	016108	Zamora	
9036	8022	016109	Zináparo	
9037	8022	016110	Zinapécuaro	
9038	8022	016111	Ziracuaretiro	
9039	8022	016112	Zitácuaro	
9040	8022	016113	José Sixto Verduzco	
9041	8015	004001	Calkiní	
9043	8015	004003	Carmen	
9044	8015	004004	Champotón	
9045	8015	004005	Hecelchakán	
9046	8015	004006	Hopelchén	
9047	8015	004007	Palizada	
9048	8015	004008	Tenabo	
9049	8015	004009	Escárcega	
9050	8015	004010	Calakmul	
9052	8018	012001	Acapulco de Juárez	
9053	8018	012002	Ahuacuotzingo	
9054	8018	012003	Ajuchitlán del Progreso	
9055	8018	012004	Alcozauca de Guerrero	
9056	8018	012005	Alpoyeca	
9057	8018	012006	Apaxtla	
9058	8018	012007	Arcelia	
9060	8018	012009	Atlamajalcingo del Monte	
9061	8018	012010	Atlixtac	
9062	8018	012011	Atoyac de Álvarez	
9063	8018	012012	Ayutla de los Libres	
9065	8018	012014	Benito Juárez	
9066	8018	012015	Buenavista de Cuéllar	
9067	8018	012016	Coahuayutla de José María Izazaga	
9068	8018	012017	Cocula	
9069	8018	012018	Copala	
9070	8018	012019	Copalillo	
9071	8018	012020	Copanatoyac	
9073	8018	012022	Coyuca de Catalán	
9074	8018	012023	Cuajinicuilapa	
9075	8018	012024	Cualác	
9076	8018	012025	Cuautepec	
9077	8018	012026	Cuetzala del Progreso	
9078	8018	012027	Cutzamala de Pinzón	
9079	8018	012028	Chilapa de Álvarez	
9080	8018	012029	Chilpancingo de los Bravo	
9081	8018	012030	Florencio Villarreal	
9082	8018	012031	General Canuto A. Neri	
9083	8018	012032	General Heliodoro Castillo	
9084	8018	012033	Huamuxtitlán	
9085	8018	012034	Huitzuco de los Figueroa	
9087	8018	012036	Igualapa	
9088	8018	012037	Ixcateopan de Cuauhtémoc	
9090	8018	012039	Juan R. Escudero	
9091	8018	012040	Leonardo Bravo	
9092	8018	012041	Malinaltepec	
9093	8018	012042	Mártir de Cuilapan	
9094	8018	012043	Metlatónoc	
9095	8018	012044	Mochitlán	
9096	8018	012045	Olinalá	
9097	8018	012046	Ometepec	
9099	8018	012048	Petatlán	
9100	8018	012049	Pilcaya	
9101	8018	012050	Pungarabato	
9102	8018	012051	Quechultenango	
9103	8018	012052	San Luis Acatlán	
8982	8022	016055	Múgica	
9089	8018	012038	Zihuatanejo de Azueta	
9104	8018	012053	San Marcos	
9105	8018	012054	San Miguel Totolapan	
9106	8018	012055	Taxco de Alarcón	
9107	8018	012056	Tecoanapa	
9108	8018	012057	Técpan de Galeana	
9109	8018	012058	Teloloapan	
9110	8018	012059	Tepecoacuilco de Trujano	
9111	8018	012060	Tetipac	
9112	8018	012061	Tixtla de Guerrero	
9113	8018	012062	Tlacoachistlahuaca	
9114	8018	012063	Tlacoapa	
9116	8018	012065	Tlalixtaquilla de Maldonado	
9117	8018	012066	Tlapa de Comonfort	
9118	8018	012067	Tlapehuala	
9119	8018	012068	La Unión de Isidoro Montes de Oca	
9120	8018	012069	Xalpatláhuac	
9121	8018	012070	Xochihuehuetlán	
9122	8018	012071	Xochistlahuaca	
9123	8018	012072	Zapotitlán Tablas	
9124	8018	012073	Zirándaro	
9125	8018	012074	Zitlala	
9126	8018	012075	Eduardo Neri	
9127	8018	012076	Acatepec	
9129	8018	012078	Cochoapa el Grande	
9130	8018	012079	José Joaquin de Herrera	
9131	8018	012080	Juchitán	
9132	8018	012081	Iliatenco	
9133	8044	024001	Ahualulco	
9134	8044	024002	Alaquines	
9135	8044	024003	Aquismón	
9137	8044	024005	Cárdenas	
9138	8044	024006	Catorce	
9139	8044	024007	Cedral	
9140	8044	024008	Cerritos	
9141	8044	024009	Cerro de San Pedro	
9142	8044	024010	Ciudad del Maíz	
9143	8044	024011	Ciudad Fernández	
9144	8044	024012	Tancanhuitz	
9145	8044	024013	Ciudad Valles	
9146	8044	024014	Coxcatlán	
9147	8044	024015	Charcas	
9148	8044	024016	Ebano	
9149	8044	024017	Guadalcázar	
9150	8044	024018	Huehuetlán	
9152	8044	024020	Matehuala	
9153	8044	024021	Mexquitic de Carmona	
9154	8044	024022	Moctezuma	
9155	8044	024023	Rayón	
9156	8044	024024	Rioverde	
9157	8044	024025	Salinas	
9158	8044	024026	San Antonio	
9159	8044	024027	San Ciro de Acosta	
9160	8044	024028	San Luis Potosí	
9162	8044	024030	San Nicolás Tolentino	
9163	8044	024031	Santa Catarina	
9164	8044	024032	Santa María del Río	
9165	8044	024033	Santo Domingo	
9166	8044	024034	San Vicente Tancuayalab	
9167	8044	024035	Soledad de Graciano Sánchez	
9168	8044	024036	Tamasopo	
9169	8044	024037	Tamazunchale	
9170	8044	024038	Tampacán	
9171	8044	024039	Tampamolón Corona	
9172	8044	024040	Tamuín	
9173	8044	024041	Tanlajás	
9174	8044	024042	Tanquián de Escobedo	
9175	8044	024043	Tierra Nueva	
9176	8044	024044	Vanegas	
9177	8044	024045	Venado	
9179	8044	024047	Villa de Guadalupe	
9180	8044	024048	Villa de la Paz	
9181	8044	024049	Villa de Ramos	
9182	8044	024050	Villa de Reyes	
9183	8044	024051	Villa Hidalgo	
9184	8044	024052	Villa Juárez	
9185	8044	024053	Axtla de Terrazas	
9186	8044	024054	Xilitla	
9187	8044	024055	Zaragoza	
9188	8044	024056	Villa de Arista	
9189	8044	024057	Matlapa	
9190	8044	024058	El Naranjo	
9191	8039	008001	Ahumada	
9192	8039	008002	Aldama	
9193	8039	008003	Allende	
9195	8039	008005	Ascensión	
9196	8039	008006	Bachíniva	
9197	8039	008007	Balleza	
9198	8039	008008	Batopilas	
9199	8039	008009	Bocoyna	
9200	8039	008010	Buenaventura	
9201	8039	008011	Camargo	
9202	8039	008012	Carichí	
9203	8039	008013	Casas Grandes	
9204	8039	008014	Coronado	
9206	8039	008016	La Cruz	
9207	8039	008017	Cuauhtémoc	
9208	8039	008018	Cusihuiriachi	
9209	8039	008019	Chihuahua	
9210	8039	008020	Chínipas	
9211	8039	008021	Delicias	
9213	8039	008023	Galeana	
9214	8039	008024	Santa Isabel	
9215	8039	008025	Gómez Farías	
9216	8039	008026	Gran Morelos	
9217	8039	008027	Guachochi	
9218	8039	008028	Guadalupe	
9219	8039	008029	Guadalupe y Calvo	
9220	8039	008030	Guazapares	
9221	8039	008031	Guerrero	
9222	8039	008032	Hidalgo del Parral	
9223	8039	008033	Huejotitán	
9224	8039	008034	Ignacio Zaragoza	
9225	8039	008035	Janos	
9226	8039	008036	Jiménez	
9227	8039	008037	Juárez	
9228	8039	008038	Julimes	
9230	8039	008040	Madera	
9231	8039	008041	Maguarichi	
9232	8039	008042	Manuel Benavides	
9233	8039	008043	Matachí	
9234	8039	008044	Matamoros	
9235	8039	008045	Meoqui	
9236	8039	008046	Morelos	
9237	8039	008047	Moris	
9239	8039	008049	Nonoava	
9240	8039	008050	Nuevo Casas Grandes	
9241	8039	008051	Ocampo	
9242	8039	008052	Ojinaga	
9243	8039	008053	Praxedis G. Guerrero	
9244	8039	008054	Riva Palacio	
9245	8039	008055	Rosales	
9246	8039	008056	Rosario	
9247	8039	008057	San Francisco de Borja	
9249	8039	008059	San Francisco del Oro	
9250	8039	008060	Santa Bárbara	
9251	8039	008061	Satevó	
9252	8039	008062	Saucillo	
9253	8039	008063	Temósachic	
9254	8039	008064	El Tule	
9255	8039	008065	Urique	
9256	8039	008066	Uruachi	
9257	8039	008067	Valle de Zaragoza	
9259	8036	022001	Amealco de Bonfil	
9260	8036	022002	Pinal de Amoles	
9261	8036	022003	Arroyo Seco	
9262	8036	022004	Cadereyta de Montes	
9263	8036	022005	Colón	
9264	8036	022006	Corregidora	
9265	8036	022007	Ezequiel Montes	
9266	8036	022008	Huimilpan	
9268	8036	022010	Landa de Matamoros	
9269	8036	022011	El Marqués	
9270	8036	022012	Pedro Escobedo	
9271	8036	022013	Peñamiller	
9272	8036	022014	Querétaro	
9273	8036	022015	San Joaquín	
9274	8036	022016	San Juan del Río	
9275	8036	022017	Tequisquiapan	
9276	8036	022018	Tolimán	
9277	8016	010001	Canatlán	
9278	8016	010002	Canelas	
9280	8016	010004	Cuencamé	
9281	8016	010005	Durango	
9282	8016	010006	General Simón Bolívar	
9283	8016	010007	Gómez Palacio	
9284	8016	010008	Guadalupe Victoria	
9285	8016	010009	Guanaceví	
9286	8016	010010	Hidalgo	
9287	8016	010011	Indé	
9288	8016	010012	Lerdo	
9289	8016	010013	Mapimí	
9291	8016	010015	Nazas	
9293	8016	010017	Ocampo	
9294	8016	010018	El Oro	
9295	8016	010019	Otáez	
9296	8016	010020	Pánuco de Coronado	
9297	8016	010021	Peñón Blanco	
9298	8016	010022	Poanas	
9299	8016	010023	Pueblo Nuevo	
9300	8016	010024	Rodeo	
9301	8016	010025	San Bernardo	
9302	8016	010026	San Dimas	
9303	8016	010027	San Juan de Guadalupe	
9305	8016	010029	San Luis del Cordero	
9306	8016	010030	San Pedro del Gallo	
9307	8016	010031	Santa Clara	
9308	8016	010032	Santiago Papasquiaro	
9310	8016	010034	Tamazula	
9311	8016	010035	Tepehuanes	
9312	8016	010036	Tlahualilo	
9313	8016	010037	Topia	
9314	8016	010038	Vicente Guerrero	
9315	8016	010039	Nuevo Ideal	
9318	8029	003003	La Paz	
9319	8029	003008	Los Cabos	
9320	8029	003009	Loreto	
9321	8017	011001	Abasolo	
9322	8017	011002	Acámbaro	
9323	8017	011003	San Miguel de Allende	
9324	8017	011004	Apaseo el Alto	
9325	8017	011005	Apaseo el Grande	
9326	8017	011006	Atarjea	
9327	8017	011007	Celaya	
9328	8017	011008	Manuel Doblado	
9329	8017	011009	Comonfort	
9330	8017	011010	Coroneo	
9331	8017	011011	Cortazar	
9332	8017	011012	Cuerámaro	
9333	8017	011013	Doctor Mora	
9335	8017	011015	Guanajuato	
9336	8017	011016	Huanímaro	
9337	8017	011017	Irapuato	
9338	8017	011018	Jaral del Progreso	
9339	8017	011019	Jerécuaro	
9340	8017	011020	León	
9341	8017	011021	Moroleón	
9342	8017	011022	Ocampo	
9343	8017	011023	Pénjamo	
9344	8017	011024	Pueblo Nuevo	
9345	8017	011025	Purísima del Rincón	
9346	8017	011026	Romita	
9347	8017	011027	Salamanca	
9348	8017	011028	Salvatierra	
9349	8017	011029	San Diego de la Unión	
9350	8017	011030	San Felipe	
9351	8017	011031	San Francisco del Rincón	
9352	8017	011032	San José Iturbide	
9353	8017	011033	San Luis de la Paz	
9354	8017	011034	Santa Catarina	
9355	8017	011035	Santa Cruz de Juventino Rosas	
9356	8017	011036	Santiago Maravatío	
9357	8017	011037	Silao	
9358	8017	011038	Tarandacuao	
9359	8017	011039	Tarimoro	
9361	8017	011041	Uriangato	
9362	8017	011042	Valle de Santiago	
9363	8017	011043	Victoria	
9364	8017	011044	Villagrán	
9366	8017	011046	Yuriria	
9367	8021	015001	Acambay	
9368	8021	015002	Acolman	
9369	8021	015003	Aculco	
9370	8021	015004	Almoloya de Alquisiras	
9372	8021	015006	Almoloya del Río	
9373	8021	015007	Amanalco	
9374	8021	015008	Amatepec	
9375	8021	015009	Amecameca	
9376	8021	015010	Apaxco	
9377	8021	015011	Atenco	
9378	8021	015012	Atizapán	
9379	8021	015013	Atizapán de Zaragoza	
9380	8021	015014	Atlacomulco	
9381	8021	015015	Atlautla	
9382	8021	015016	Axapusco	
9384	8021	015018	Calimaya	
9385	8021	015019	Capulhuac	
9386	8021	015020	Coacalco de Berriozábal	
9387	8021	015021	Coatepec Harinas	
9388	8021	015022	Cocotitlán	
9390	8021	015024	Cuautitlán	
9391	8021	015025	Chalco	
9392	8021	015026	Chapa de Mota	
9393	8021	015027	Chapultepec	
9394	8021	015028	Chiautla	
9395	8021	015029	Chicoloapan	
9396	8021	015030	Chiconcuac	
9397	8021	015031	Chimalhuacán	
9398	8021	015032	Donato Guerra	
9399	8021	015033	Ecatepec de Morelos	
9365	8017	011045	Xichú	
9400	8021	015034	Ecatzingo	
9401	8021	015035	Huehuetoca	
9403	8021	015037	Huixquilucan	
9404	8021	015038	Isidro Fabela	
9405	8021	015039	Ixtapaluca	
9406	8021	015040	Ixtapan de la Sal	
9407	8021	015041	Ixtapan del Oro	
9408	8021	015042	Ixtlahuaca	
9409	8021	015043	Xalatlaco	
9410	8021	015044	Jaltenco	
9411	8021	015045	Jilotepec	
9412	8021	015046	Jilotzingo	
9413	8021	015047	Jiquipilco	
9414	8021	015048	Jocotitlán	
9416	8021	015050	Juchitepec	
9417	8021	015051	Lerma	
9418	8021	015052	Malinalco	
9419	8021	015053	Melchor Ocampo	
9420	8021	015054	Metepec	
9421	8021	015055	Mexicaltzingo	
9422	8021	015056	Morelos	
9423	8021	015057	Naucalpan de Juárez	
9424	8021	015058	Nezahualcóyotl	
9425	8021	015059	Nextlalpan	
9426	8021	015060	Nicolás Romero	
9427	8021	015061	Nopaltepec	
9429	8021	015063	Ocuilan	
9430	8021	015064	El Oro	
9431	8021	015065	Otumba	
9432	8021	015066	Otzoloapan	
9433	8021	015067	Otzolotepec	
9434	8021	015068	Ozumba	
9435	8021	015069	Papalotla	
9436	8021	015070	La Paz	
9437	8021	015071	Polotitlán	
9438	8021	015072	Rayón	
9440	8021	015074	San Felipe del Progreso	
9441	8021	015075	San Martín de las Pirámides	
9442	8021	015076	San Mateo Atenco	
9443	8021	015077	San Simón de Guerrero	
9444	8021	015078	Santo Tomás	
9445	8021	015079	Soyaniquilpan de Juárez	
9446	8021	015080	Sultepec	
9447	8021	015081	Tecámac	
9448	8021	015082	Tejupilco	
9450	8021	015084	Temascalapa	
9451	8021	015085	Temascalcingo	
9452	8021	015086	Temascaltepec	
9453	8021	015087	Temoaya	
9454	8021	015088	Tenancingo	
9455	8021	015089	Tenango del Aire	
9456	8021	015090	Tenango del Valle	
9457	8021	015091	Teoloyucán	
9458	8021	015092	Teotihuacán	
9459	8021	015093	Tepetlaoxtoc	
9460	8021	015094	Tepetlixpa	
9461	8021	015095	Tepotzotlán	
9463	8021	015097	Texcaltitlán	
9464	8021	015098	Texcalyacac	
9465	8021	015099	Texcoco	
9466	8021	015100	Tezoyuca	
9467	8021	015101	Tianguistenco	
9468	8021	015102	Timilpan	
9469	8021	015103	Tlalmanalco	
9470	8021	015104	Tlalnepantla de Baz	
9471	8021	015105	Tlatlaya	
9472	8021	015106	Toluca	
9474	8021	015108	Tultepec	
9475	8021	015109	Tultitlán	
9476	8021	015110	Valle de Bravo	
9477	8021	015111	Villa de Allende	
9479	8021	015113	Villa Guerrero	
9480	8021	015114	Villa Victoria	
9481	8021	015115	Xonacatlán	
9482	8021	015116	Zacazonapan	
9483	8021	015117	Zacualpan	
9484	8021	015118	Zinacantepec	
9485	8021	015119	Zumpahuacán	
9486	8021	015120	Zumpango	
9487	8021	015121	Cuautitlán Izcalli	
9488	8021	015122	Valle de Chalco Solidaridad	
9489	8021	015123	Luvianos	
9490	8021	015124	San José del Rincón	
9491	8021	015125	Tonanitla	
9492	8046	027001	Balancán	
9494	8046	027003	Centla	
9495	8046	027004	Centro	
9496	8046	027005	Comalcalco	
9497	8046	027006	Cunduacán	
9498	8046	027007	Emiliano Zapata	
9499	8046	027008	Huimanguillo	
9500	8046	027009	Jalapa	
9501	8046	027010	Jalpa de Méndez	
9502	8046	027011	Jonuta	
9503	8046	027012	Macuspana	
9504	8046	027013	Nacajuca	
9506	8046	027015	Tacotalpa	
9507	8046	027016	Teapa	
9508	8046	027017	Tenosique	
9509	8030	002001	Ensenada	
9510	8030	002002	Mexicali	
9511	8030	002003	Tecate	
9512	8030	002004	Tijuana	
9514	8042	025001	Ahome	
9515	8042	025002	Angostura	
9516	8042	025003	Badiraguato	
9517	8042	025004	Concordia	
9518	8042	025005	Cosalá	
9519	8042	025006	Culiacán	
9520	8042	025007	Choix	
9521	8042	025008	Elota	
9522	8042	025009	Escuinapa	
9523	8042	025010	El Fuerte	
9524	8042	025011	Guasave	
9525	8042	025012	Mazatlán	
9526	8042	025013	Mocorito	
9527	8042	025014	Rosario	
9529	8042	025016	San Ignacio	
9530	8042	025017	Sinaloa	
9531	8042	025018	Navolato	
9532	8034	020001	Abejones	
9533	8034	020002	Acatlán de Pérez Figueroa	
9534	8034	020003	Asunción Cacalotepec	
9535	8034	020004	Asunción Cuyotepeji	
9536	8034	020005	Asunción Ixtaltepec	
9537	8034	020006	Asunción Nochixtlán	
9538	8034	020007	Asunción Ocotlán	
9540	8034	020009	Ayotzintepec	
9541	8034	020010	El Barrio de la Soledad	
9542	8034	020011	Calihualá	
9543	8034	020012	Candelaria Loxicha	
9544	8034	020013	Ciénega de Zimatlán	
9545	8034	020014	Ciudad Ixtepec	
9546	8034	020015	Coatecas Altas	
9547	8034	020016	Coicoyán de las Flores	
9548	8034	020017	La Compañía	
9549	8034	020018	Concepción Buenavista	
9550	8034	020019	Concepción Pápalo	
9551	8034	020020	Constancia del Rosario	
9552	8034	020021	Cosolapa	
9553	8034	020022	Cosoltepec	
9555	8034	020024	Cuyamecalco Villa de Zaragoza	
9556	8034	020025	Chahuites	
9557	8034	020026	Chalcatongo de Hidalgo	
9558	8034	020027	Chiquihuitlán de Benito Juárez	
9559	8034	020028	Heroica Ciudad de Ejutla de Crespo	
9560	8034	020029	Eloxochitlán de Flores Magón	
9561	8034	020030	El Espinal	
9562	8034	020031	Tamazulápam del Espíritu Santo	
9564	8034	020033	Guadalupe Etla	
9565	8034	020034	Guadalupe de Ramírez	
9566	8034	020035	Guelatao de Juárez	
9567	8034	020036	Guevea de Humboldt	
9568	8034	020037	Mesones Hidalgo	
9569	8034	020038	Villa Hidalgo	
9571	8034	020040	Huautepec	
9572	8034	020041	Huautla de Jiménez	
9573	8034	020042	Ixtlán de Juárez	
9575	8034	020044	Loma Bonita	
9576	8034	020045	Magdalena Apasco	
9577	8034	020046	Magdalena Jaltepec	
9578	8034	020047	Santa Magdalena Jicotlán	
9579	8034	020048	Magdalena Mixtepec	
9580	8034	020049	Magdalena Ocotlán	
9581	8034	020050	Magdalena Peñasco	
9582	8034	020051	Magdalena Teitipac	
9583	8034	020052	Magdalena Tequisistlán	
9584	8034	020053	Magdalena Tlacotepec	
9585	8034	020054	Magdalena Zahuatlán	
9586	8034	020055	Mariscala de Juárez	
9587	8034	020056	Mártires de Tacubaya	
9589	8034	020058	Mazatlán Villa de Flores	
9590	8034	020059	Miahuatlán de Porfirio Díaz	
9591	8034	020060	Mixistlán de la Reforma	
9592	8034	020061	Monjas	
9593	8034	020062	Natividad	
9594	8034	020063	Nazareno Etla	
9595	8034	020064	Nejapa de Madero	
9596	8034	020065	Ixpantepec Nieves	
9597	8034	020066	Santiago Niltepec	
9598	8034	020067	Oaxaca de Juárez	
9599	8034	020068	Ocotlán de Morelos	
9600	8034	020069	La Pe	
9601	8034	020070	Pinotepa de Don Luis	
9602	8034	020071	Pluma Hidalgo	
9604	8034	020073	Putla Villa de Guerrero	
9605	8034	020074	Santa Catarina Quioquitani	
9606	8034	020075	Reforma de Pineda	
9607	8034	020076	La Reforma	
9608	8034	020077	Reyes Etla	
9609	8034	020078	Rojas de Cuauhtémoc	
9610	8034	020079	Salina Cruz	
9611	8034	020080	San Agustín Amatengo	
9612	8034	020081	San Agustín Atenango	
9613	8034	020082	San Agustín Chayuco	
9614	8034	020083	San Agustín de las Juntas	
9615	8034	020084	San Agustín Etla	
9616	8034	020085	San Agustín Loxicha	
9617	8034	020086	San Agustín Tlacotepec	
9618	8034	020087	San Agustín Yatareni	
9620	8034	020089	San Andrés Dinicuiti	
9621	8034	020090	San Andrés Huaxpaltepec	
9622	8034	020091	San Andrés Huayápam	
9623	8034	020092	San Andrés Ixtlahuaca	
9624	8034	020093	San Andrés Lagunas	
9625	8034	020094	San Andrés Nuxiño	
9626	8034	020095	San Andrés Paxtlán	
9627	8034	020096	San Andrés Sinaxtla	
9628	8034	020097	San Andrés Solaga	
9629	8034	020098	San Andrés Teotilálpam	
9630	8034	020099	San Andrés Tepetlapa	
9631	8034	020100	San Andrés Yaá	
9633	8034	020102	San Andrés Zautla	
9634	8034	020103	San Antonino Castillo Velasco	
9635	8034	020104	San Antonino el Alto	
9636	8034	020105	San Antonino Monte Verde	
9637	8034	020106	San Antonio Acutla	
9638	8034	020107	San Antonio de la Cal	
9639	8034	020108	San Antonio Huitepec	
9640	8034	020109	San Antonio Nanahuatípam	
9641	8034	020110	San Antonio Sinicahua	
9642	8034	020111	San Antonio Tepetlapa	
9643	8034	020112	San Baltazar Chichicápam	
9644	8034	020113	San Baltazar Loxicha	
9646	8034	020115	San Bartolo Coyotepec	
9647	8034	020116	San Bartolomé Ayautla	
9648	8034	020117	San Bartolomé Loxicha	
9649	8034	020118	San Bartolomé Quialana	
9650	8034	020119	San Bartolomé Yucuañe	
9651	8034	020120	San Bartolomé Zoogocho	
9652	8034	020121	San Bartolo Soyaltepec	
9653	8034	020122	San Bartolo Yautepec	
9654	8034	020123	San Bernardo Mixtepec	
9655	8034	020124	San Blas Atempa	
9656	8034	020125	San Carlos Yautepec	
9657	8034	020126	San Cristóbal Amatlán	
9658	8034	020127	San Cristóbal Amoltepec	
9659	8034	020128	San Cristóbal Lachirioag	
9660	8034	020129	San Cristóbal Suchixtlahuaca	
9661	8034	020130	San Dionisio del Mar	
9662	8034	020131	San Dionisio Ocotepec	
9663	8034	020132	San Dionisio Ocotlán	
9665	8034	020134	San Felipe Jalapa de Díaz	
9666	8034	020135	San Felipe Tejalápam	
9667	8034	020136	San Felipe Usila	
9668	8034	020137	San Francisco Cahuacuá	
9669	8034	020138	San Francisco Cajonos	
9670	8034	020139	San Francisco Chapulapa	
9672	8034	020141	San Francisco del Mar	
9673	8034	020142	San Francisco Huehuetlán	
9674	8034	020143	San Francisco Ixhuatán	
9675	8034	020144	San Francisco Jaltepetongo	
9574	8034	020043	Heroica Ciudad de Juchitán de Zaragoza	
9676	8034	020145	San Francisco Lachigoló	
9678	8034	020147	San Francisco Nuxaño	
9679	8034	020148	San Francisco Ozolotepec	
9680	8034	020149	San Francisco Sola	
9681	8034	020150	San Francisco Telixtlahuaca	
9682	8034	020151	San Francisco Teopan	
9684	8034	020153	San Gabriel Mixtepec	
9685	8034	020154	San Ildefonso Amatlán	
9686	8034	020155	San Ildefonso Sola	
9687	8034	020156	San Ildefonso Villa Alta	
9688	8034	020157	San Jacinto Amilpas	
9689	8034	020158	San Jacinto Tlacotepec	
9690	8034	020159	San Jerónimo Coatlán	
9692	8034	020161	San Jerónimo Sosola	
9693	8034	020162	San Jerónimo Taviche	
9694	8034	020163	San Jerónimo Tecóatl	
9695	8034	020164	San Jorge Nuchita	
9696	8034	020165	San José Ayuquila	
9697	8034	020166	San José Chiltepec	
9698	8034	020167	San José del Peñasco	
9699	8034	020168	San José Estancia Grande	
9700	8034	020169	San José Independencia	
9701	8034	020170	San José Lachiguiri	
9702	8034	020171	San José Tenango	
9703	8034	020172	San Juan Achiutla	
9704	8034	020173	San Juan Atepec	
9705	8034	020174	Ánimas Trujano	
9706	8034	020175	San Juan Bautista Atatlahuca	
9707	8034	020176	San Juan Bautista Coixtlahuaca	
9709	8034	020178	San Juan Bautista Guelache	
9710	8034	020179	San Juan Bautista Jayacatlán	
9711	8034	020180	San Juan Bautista Lo de Soto	
9712	8034	020181	San Juan Bautista Suchitepec	
9713	8034	020182	San Juan Bautista Tlacoatzintepec	
9714	8034	020183	San Juan Bautista Tlachichilco	
9715	8034	020184	San Juan Bautista Tuxtepec	
9716	8034	020185	San Juan Cacahuatepec	
9717	8034	020186	San Juan Cieneguilla	
9718	8034	020187	San Juan Coatzóspam	
9719	8034	020188	San Juan Colorado	
9720	8034	020189	San Juan Comaltepec	
9721	8034	020190	San Juan Cotzocón	
9723	8034	020192	San Juan Chilateca	
9724	8034	020193	San Juan del Estado	
9725	8034	020194	San Juan del Río	
9726	8034	020195	San Juan Diuxi	
9728	8034	020197	San Juan Guelavía	
9729	8034	020198	San Juan Guichicovi	
9730	8034	020199	San Juan Ihualtepec	
9731	8034	020200	San Juan Juquila Mixes	
9732	8034	020201	San Juan Juquila Vijanos	
9733	8034	020202	San Juan Lachao	
9734	8034	020203	San Juan Lachigalla	
9735	8034	020204	San Juan Lajarcia	
9736	8034	020205	San Juan Lalana	
9737	8034	020206	San Juan de los Cués	
9738	8034	020207	San Juan Mazatlán	
9739	8034	020208	San Juan Mixtepec -Dto. 08 -	
9740	8034	020209	San Juan Mixtepec -Dto. 26 -	
9742	8034	020211	San Juan Ozolotepec	
9743	8034	020212	San Juan Petlapa	
9745	8034	020214	San Juan Quiotepec	
9746	8034	020215	San Juan Sayultepec	
9747	8034	020216	San Juan Tabaá	
9748	8034	020217	San Juan Tamazola	
9749	8034	020218	San Juan Teita	
9750	8034	020219	San Juan Teitipac	
9751	8034	020220	San Juan Tepeuxila	
9752	8034	020221	San Juan Teposcolula	
9753	8034	020222	San Juan Yaeé	
9754	8034	020223	San Juan Yatzona	
9755	8034	020224	San Juan Yucuita	
9756	8034	020225	San Lorenzo	
9758	8034	020227	San Lorenzo Cacaotepec	
9759	8034	020228	San Lorenzo Cuaunecuiltitla	
9760	8034	020229	San Lorenzo Texmelécan	
9761	8034	020230	San Lorenzo Victoria	
9762	8034	020231	San Lucas Camotlán	
9763	8034	020232	San Lucas Ojitlán	
9764	8034	020233	San Lucas Quiaviní	
9765	8034	020234	San Lucas Zoquiápam	
9766	8034	020235	San Luis Amatlán	
9767	8034	020236	San Marcial Ozolotepec	
9768	8034	020237	San Marcos Arteaga	
9769	8034	020238	San Martín de los Cansecos	
9771	8034	020240	San Martín Itunyoso	
9773	8034	020242	San Martín Peras	
9774	8034	020243	San Martín Tilcajete	
9775	8034	020244	San Martín Toxpalan	
9776	8034	020245	San Martín Zacatepec	
9777	8034	020246	San Mateo Cajonos	
9778	8034	020247	Capulálpam de Méndez	
9779	8034	020248	San Mateo del Mar	
9780	8034	020249	San Mateo Yoloxochitlán	
9781	8034	020250	San Mateo Etlatongo	
9782	8034	020251	San Mateo Nejápam	
9783	8034	020252	San Mateo Peñasco	
9784	8034	020253	San Mateo Piñas	
9786	8034	020255	San Mateo Sindihui	
9789	8034	020258	San Miguel Achiutla	
9790	8034	020259	San Miguel Ahuehuetitlán	
9791	8034	020260	San Miguel Aloápam	
9792	8034	020261	San Miguel Amatitlán	
9793	8034	020262	San Miguel Amatlán	
9794	8034	020263	San Miguel Coatlán	
9795	8034	020264	San Miguel Chicahua	
9796	8034	020265	San Miguel Chimalapa	
9797	8034	020266	San Miguel del Puerto	
9798	8034	020267	San Miguel del Río	
9799	8034	020268	San Miguel Ejutla	
9800	8034	020269	San Miguel el Grande	
9801	8034	020270	San Miguel Huautla	
9804	8034	020273	San Miguel Peras	
9805	8034	020274	San Miguel Piedras	
9806	8034	020275	San Miguel Quetzaltepec	
9741	8034	020210	San Juan Ñumí	
9770	8034	020239	San Martín Huamelúlpam	
9807	8034	020276	San Miguel Santa Flor	
9808	8034	020277	Villa Sola de Vega	
9809	8034	020278	San Miguel Soyaltepec	
9810	8034	020279	San Miguel Suchixtepec	
9811	8034	020280	Villa Talea de Castro	
9812	8034	020281	San Miguel Tecomatlán	
9813	8034	020282	San Miguel Tenango	
9814	8034	020283	San Miguel Tequixtepec	
9815	8034	020284	San Miguel Tilquiápam	
9816	8034	020285	San Miguel Tlacamama	
9817	8034	020286	San Miguel Tlacotepec	
9819	8034	020288	San Miguel Yotao	
9820	8034	020289	San Nicolás	
9821	8034	020290	San Nicolás Hidalgo	
9822	8034	020291	San Pablo Coatlán	
9823	8034	020292	San Pablo Cuatro Venados	
9824	8034	020293	San Pablo Etla	
9825	8034	020294	San Pablo Huitzo	
9826	8034	020295	San Pablo Huixtepec	
9828	8034	020297	San Pablo Tijaltepec	
9829	8034	020298	San Pablo Villa de Mitla	
9830	8034	020299	San Pablo Yaganiza	
9831	8034	020300	San Pedro Amuzgos	
9832	8034	020301	San Pedro Apóstol	
9833	8034	020302	San Pedro Atoyac	
9834	8034	020303	San Pedro Cajonos	
9835	8034	020304	San Pedro Coxcaltepec Cántaros	
9836	8034	020305	San Pedro Comitancillo	
9837	8034	020306	San Pedro el Alto	
9838	8034	020307	San Pedro Huamelula	
9839	8034	020308	San Pedro Huilotepec	
9840	8034	020309	San Pedro Ixcatlán	
9841	8034	020310	San Pedro Ixtlahuaca	
9843	8034	020312	San Pedro Jicayán	
9844	8034	020313	San Pedro Jocotipac	
9845	8034	020314	San Pedro Juchatengo	
9846	8034	020315	San Pedro Mártir	
9847	8034	020316	San Pedro Mártir Quiechapa	
9848	8034	020317	San Pedro Mártir Yucuxaco	
9849	8034	020318	San Pedro Mixtepec -Dto. 22 -	
9850	8034	020319	San Pedro Mixtepec -Dto. 26 -	
9851	8034	020320	San Pedro Molinos	
9852	8034	020321	San Pedro Nopala	
9853	8034	020322	San Pedro Ocopetatillo	
9854	8034	020323	San Pedro Ocotepec	
9855	8034	020324	San Pedro Pochutla	
9856	8034	020325	San Pedro Quiatoni	
9858	8034	020327	San Pedro Tapanatepec	
9859	8034	020328	San Pedro Taviche	
9860	8034	020329	San Pedro Teozacoalco	
9861	8034	020330	San Pedro Teutila	
9862	8034	020331	San Pedro Tidaá	
9863	8034	020332	San Pedro Topiltepec	
9865	8034	020334	Villa de Tututepec de Melchor Ocampo	
9866	8034	020335	San Pedro Yaneri	
9867	8034	020336	San Pedro Yólox	
9869	8034	020338	Villa de Etla	
9870	8034	020339	San Pedro y San Pablo Teposcolula	
9871	8034	020340	San Pedro y San Pablo Tequixtepec	
9872	8034	020341	San Pedro Yucunama	
9873	8034	020342	San Raymundo Jalpan	
9874	8034	020343	San Sebastián Abasolo	
9875	8034	020344	San Sebastián Coatlán	
9876	8034	020345	San Sebastián Ixcapa	
9877	8034	020346	San Sebastián Nicananduta	
9878	8034	020347	San Sebastián Río Hondo	
9879	8034	020348	San Sebastián Tecomaxtlahuaca	
9880	8034	020349	San Sebastián Teitipac	
9881	8034	020350	San Sebastián Tutla	
9882	8034	020351	San Simón Almolongas	
9883	8034	020352	San Simón Zahuatlán	
9884	8034	020353	Santa Ana	
9885	8034	020354	Santa Ana Ateixtlahuaca	
9886	8034	020355	Santa Ana Cuauhtémoc	
9888	8034	020357	Santa Ana Tavela	
9889	8034	020358	Santa Ana Tlapacoyan	
9890	8034	020359	Santa Ana Yareni	
9891	8034	020360	Santa Ana Zegache	
9892	8034	020361	Santa Catalina Quierí	
9893	8034	020362	Santa Catarina Cuixtla	
9894	8034	020363	Santa Catarina Ixtepeji	
9895	8034	020364	Santa Catarina Juquila	
9896	8034	020365	Santa Catarina Lachatao	
9897	8034	020366	Santa Catarina Loxicha	
9899	8034	020368	Santa Catarina Minas	
9900	8034	020369	Santa Catarina Quiané	
9901	8034	020370	Santa Catarina Tayata	
9902	8034	020371	Santa Catarina Ticuá	
9904	8034	020373	Santa Catarina Zapoquila	
9905	8034	020374	Santa Cruz Acatepec	
9906	8034	020375	Santa Cruz Amilpas	
9907	8034	020376	Santa Cruz de Bravo	
9908	8034	020377	Santa Cruz Itundujia	
9909	8034	020378	Santa Cruz Mixtepec	
9910	8034	020379	Santa Cruz Nundaco	
9911	8034	020380	Santa Cruz Papalutla	
9912	8034	020381	Santa Cruz Tacache de Mina	
9913	8034	020382	Santa Cruz Tacahua	
9914	8034	020383	Santa Cruz Tayata	
9916	8034	020385	Santa Cruz Xoxocotlán	
9917	8034	020386	Santa Cruz Zenzontepec	
9918	8034	020387	Santa Gertrudis	
9919	8034	020388	Santa Inés del Monte	
9920	8034	020389	Santa Inés Yatzeche	
9921	8034	020390	Santa Lucía del Camino	
9923	8034	020392	Santa Lucía Monteverde	
9924	8034	020393	Santa Lucía Ocotlán	
9925	8034	020394	Santa María Alotepec	
9926	8034	020395	Santa María Apazco	
9928	8034	020397	Heroica Ciudad de Tlaxiaco	
9929	8034	020398	Ayoquezco de Aldama	
9930	8034	020399	Santa María Atzompa	
9931	8034	020400	Santa María Camotlán	
9932	8034	020401	Santa María Colotepec	
9933	8034	020402	Santa María Cortijo	
9934	8034	020403	Santa María Coyotepec	
9864	8034	020333	San Pedro Totolápam	
9935	8034	020404	Santa María Chachoápam	
9936	8034	020405	Villa de Chilapa de Díaz	
9937	8034	020406	Santa María Chilchotla	
9938	8034	020407	Santa María Chimalapa	
9939	8034	020408	Santa María del Rosario	
9940	8034	020409	Santa María del Tule	
9941	8034	020410	Santa María Ecatepec	
9942	8034	020411	Santa María Guelacé	
9943	8034	020412	Santa María Guienagati	
9945	8034	020414	Santa María Huazolotitlán	
9946	8034	020415	Santa María Ipalapa	
9947	8034	020416	Santa María Ixcatlán	
9948	8034	020417	Santa María Jacatepec	
9949	8034	020418	Santa María Jalapa del Marqués	
9950	8034	020419	Santa María Jaltianguis	
9951	8034	020420	Santa María Lachixío	
9952	8034	020421	Santa María Mixtequilla	
9953	8034	020422	Santa María Nativitas	
9954	8034	020423	Santa María Nduayaco	
9956	8034	020425	Santa María Pápalo	
9957	8034	020426	Santa María Peñoles	
9958	8034	020427	Santa María Petapa	
9959	8034	020428	Santa María Quiegolani	
9960	8034	020429	Santa María Sola	
9961	8034	020430	Santa María Tataltepec	
9962	8034	020431	Santa María Tecomavaca	
9963	8034	020432	Santa María Temaxcalapa	
9964	8034	020433	Santa María Temaxcaltepec	
9965	8034	020434	Santa María Teopoxco	
9966	8034	020435	Santa María Tepantlali	
9967	8034	020436	Santa María Texcatitlán	
9969	8034	020438	Santa María Tlalixtac	
9970	8034	020439	Santa María Tonameca	
9971	8034	020440	Santa María Totolapilla	
9972	8034	020441	Santa María Xadani	
9973	8034	020442	Santa María Yalina	
9974	8034	020443	Santa María Yavesía	
9975	8034	020444	Santa María Yolotepec	
9977	8034	020446	Santa María Yucuhiti	
9978	8034	020447	Santa María Zacatepec	
9979	8034	020448	Santa María Zaniza	
9980	8034	020449	Santa María Zoquitlán	
9981	8034	020450	Santiago Amoltepec	
9982	8034	020451	Santiago Apoala	
9983	8034	020452	Santiago Apóstol	
9984	8034	020453	Santiago Astata	
9985	8034	020454	Santiago Atitlán	
9986	8034	020455	Santiago Ayuquililla	
9989	8034	020458	Santiago Comaltepec	
9990	8034	020459	Santiago Chazumba	
9991	8034	020460	Santiago Choápam	
9992	8034	020461	Santiago del Río	
9993	8034	020462	Santiago Huajolotitlán	
9994	8034	020463	Santiago Huauclilla	
9995	8034	020464	Santiago Ihuitlán Plumas	
9996	8034	020465	Santiago Ixcuintepec	
9997	8034	020466	Santiago Ixtayutla	
9998	8034	020467	Santiago Jamiltepec	
9999	8034	020468	Santiago Jocotepec	
10000	8034	020469	Santiago Juxtlahuaca	
10001	8034	020470	Santiago Lachiguiri	
10002	8034	020471	Santiago Lalopa	
10003	8034	020472	Santiago Laollaga	
10004	8034	020473	Santiago Laxopa	
10005	8034	020474	Santiago Llano Grande	
10006	8034	020475	Santiago Matatlán	
10007	8034	020476	Santiago Miltepec	
10008	8034	020477	Santiago Minas	
10009	8034	020478	Santiago Nacaltepec	
10010	8034	020479	Santiago Nejapilla	
10011	8034	020480	Santiago Nundiche	
10012	8034	020481	Santiago Nuyoó	
10013	8034	020482	Santiago Pinotepa Nacional	
10014	8034	020483	Santiago Suchilquitongo	
10015	8034	020484	Santiago Tamazola	
10016	8034	020485	Santiago Tapextla	
10018	8034	020487	Santiago Tenango	
10020	8034	020489	Santiago Tetepec	
10021	8034	020490	Santiago Texcalcingo	
10022	8034	020491	Santiago Textitlán	
10023	8034	020492	Santiago Tilantongo	
10024	8034	020493	Santiago Tillo	
10025	8034	020494	Santiago Tlazoyaltepec	
10026	8034	020495	Santiago Xanica	
10027	8034	020496	Santiago Xiacuí	
10028	8034	020497	Santiago Yaitepec	
10029	8034	020498	Santiago Yaveo	
10033	8034	020502	Santiago Zacatepec	
10034	8034	020503	Santiago Zoochila	
10035	8034	020504	Nuevo Zoquiápam	
10036	8034	020505	Santo Domingo Ingenio	
10037	8034	020506	Santo Domingo Albarradas	
10038	8034	020507	Santo Domingo Armenta	
10039	8034	020508	Santo Domingo Chihuitán	
10040	8034	020509	Santo Domingo de Morelos	
10041	8034	020510	Santo Domingo Ixcatlán	
10044	8034	020513	Santo Domingo Petapa	
10045	8034	020514	Santo Domingo Roayaga	
10046	8034	020515	Santo Domingo Tehuantepec	
10047	8034	020516	Santo Domingo Teojomulco	
10048	8034	020517	Santo Domingo Tepuxtepec	
10049	8034	020518	Santo Domingo Tlatayápam	
10050	8034	020519	Santo Domingo Tomaltepec	
10051	8034	020520	Santo Domingo Tonalá	
10053	8034	020522	Santo Domingo Xagacía	
10054	8034	020523	Santo Domingo Yanhuitlán	
10055	8034	020524	Santo Domingo Yodohino	
10056	8034	020525	Santo Domingo Zanatepec	
10057	8034	020526	Santos Reyes Nopala	
10058	8034	020527	Santos Reyes Pápalo	
10059	8034	020528	Santos Reyes Tepejillo	
10062	8034	020531	Santo Tomás Mazaltepec	
10063	8034	020532	Santo Tomás Ocotepec	
10064	8034	020533	Santo Tomás Tamazulapan	
10065	8034	020534	San Vicente Coatlán	
10066	8034	020535	San Vicente Lachixío	
10017	8034	020486	Villa Tejúpam de la Unión	
10068	8034	020537	Silacayoápam	
10069	8034	020538	Sitio de Xitlapehua	
10070	8034	020539	Soledad Etla	
10071	8034	020540	Villa de Tamazulápam del Progreso	
10072	8034	020541	Tanetze de Zaragoza	
10073	8034	020542	Taniche	
10074	8034	020543	Tataltepec de Valdés	
10075	8034	020544	Teococuilco de Marcos Pérez	
10076	8034	020545	Teotitlán de Flores Magón	
10077	8034	020546	Teotitlán del Valle	
10078	8034	020547	Teotongo	
10079	8034	020548	Tepelmeme Villa de Morelos	
10080	8034	020549	Tezoatlán de Segura y Luna	
10081	8034	020550	San Jerónimo Tlacochahuaya	
10082	8034	020551	Tlacolula de Matamoros	
10083	8034	020552	Tlacotepec Plumas	
10084	8034	020553	Tlalixtac de Cabrera	
10085	8034	020554	Totontepec Villa de Morelos	
10086	8034	020555	Trinidad Zaachila	
10087	8034	020556	La Trinidad Vista Hermosa	
10088	8034	020557	Unión Hidalgo	
10089	8034	020558	Valerio Trujano	
10090	8034	020559	San Juan Bautista Valle Nacional	
10091	8034	020560	Villa Díaz Ordaz	
10092	8034	020561	Yaxe	
10093	8034	020562	Magdalena Yodocono de Porfirio Díaz	
10094	8034	020563	Yogana	
10095	8034	020564	Yutanduchi de Guerrero	
10096	8034	020565	Villa de Zaachila	
10097	8034	020566	Zapotitlán del Río	
10098	8034	020567	Zapotitlán Lagunas	
10100	8034	020569	Santa Inés de Zaragoza	
10101	8034	020570	Zimatlán de Álvarez	
10102	8024	018001	Acaponeta	
10103	8024	018002	Ahuacatlán	
10104	8024	018003	Amatlán de Cañas	
10105	8024	018004	Compostela	
10106	8024	018005	Huajicori	
10107	8024	018006	Ixtlán del Río	
10108	8024	018007	Jala	
10109	8024	018008	Xalisco	
10110	8024	018009	Del Nayar	
10111	8024	018010	Rosamorada	
10112	8024	018011	Ruíz	
10113	8024	018012	San Blas	
10115	8024	018014	Santa María del Oro	
10116	8024	018015	Santiago Ixcuintla	
10117	8024	018016	Tecuala	
10118	8024	018017	Tepic	
10119	8024	018018	Tuxpan	
10120	8024	018019	La Yesca	
10121	8024	018020	Bahía de Banderas	
10122	8025	019001	Abasolo	
10123	8025	019002	Agualeguas	
10124	8025	019003	Los Aldamas	
10125	8025	019004	Allende	
10126	8025	019005	Anáhuac	
10127	8025	019006	Apodaca	
10129	8025	019008	Bustamante	
10130	8025	019009	Cadereyta Jiménez	
10131	8025	019010	Carmen	
10132	8025	019011	Cerralvo	
10133	8025	019012	Ciénega de Flores	
10134	8025	019013	China	
10135	8025	019014	Dr. Arroyo	
10137	8025	019016	Dr. González	
10138	8025	019017	Galeana	
10139	8025	019018	García	
10141	8025	019020	Gral. Bravo	
10142	8025	019021	Gral. Escobedo	
10143	8025	019022	Gral. Terán	
10145	8025	019024	Gral. Zaragoza	
10146	8025	019025	Gral. Zuazua	
10147	8025	019026	Guadalupe	
10148	8025	019027	Los Herreras	
10149	8025	019028	Higueras	
10150	8025	019029	Hualahuises	
10151	8025	019030	Iturbide	
10152	8025	019031	Juárez	
10153	8025	019032	Lampazos de Naranjo	
10154	8025	019033	Linares	
10155	8025	019034	Marín	
10156	8025	019035	Melchor Ocampo	
10157	8025	019036	Mier y Noriega	
10158	8025	019037	Mina	
10159	8025	019038	Montemorelos	
10160	8025	019039	Monterrey	
10161	8025	019040	Parás	
10162	8025	019041	Pesquería	
10163	8025	019042	Los Ramones	
10164	8025	019043	Rayones	
10165	8025	019044	Sabinas Hidalgo	
10167	8025	019046	San Nicolás de los Garza	
10168	8025	019047	Hidalgo	
10169	8025	019048	Santa Catarina	
10170	8025	019049	Santiago	
10171	8025	019050	Vallecillo	
10174	8035	005001	Abasolo	
10175	8035	005002	Acuña	
10176	8035	005003	Allende	
10177	8035	005004	Arteaga	
10178	8035	005005	Candela	
10179	8035	005006	Castaños	
10181	8035	005008	Escobedo	
10182	8035	005009	Francisco I. Madero	
10183	8035	005010	Frontera	
10184	8035	005011	General Cepeda	
10185	8035	005012	Guerrero	
10186	8035	005013	Hidalgo	
10187	8035	005014	Jiménez	
10188	8035	005015	Juárez	
10190	8035	005017	Matamoros	
10191	8035	005018	Monclova	
10192	8035	005019	Morelos	
10194	8035	005021	Nadadores	
10195	8035	005022	Nava	
10196	8035	005023	Ocampo	
10197	8035	005024	Parras	
10199	8035	005026	Progreso	
10200	8035	005027	Ramos Arizpe	
10201	8035	005028	Sabinas	
10202	8035	005029	Sacramento	
10203	8035	005030	Saltillo	
10204	8035	005031	San Buenaventura	
10206	8035	005033	San Pedro	
10207	8035	005034	Sierra Mojada	
10208	8035	005035	Torreón	
10209	8035	005036	Viesca	
10210	8035	005037	Villa Unión	
10211	8035	005038	Zaragoza	
10213	8014	023001	Cozumel	
10136	8025	019015	Dr. Coss	
10067	8034	020536	San Vicente Nuñú	
10214	8014	023002	Felipe Carrillo Puerto	
10215	8014	023003	Isla Mujeres	
10216	8014	023004	Othón P. Blanco	
10218	8014	023006	José María Morelos	
10219	8014	023007	Lázaro Cárdenas	
10220	8014	023008	Solidaridad	
10221	8040	029001	Amaxac de Guerrero	
10222	8040	029002	Apetatitlán de Antonio Carvajal	
10223	8040	029003	Atlangatepec	
10225	8040	029005	Apizaco	
10226	8040	029006	Calpulalpan	
10227	8040	029007	El Carmen Tequexquitla	
10228	8040	029008	Cuapiaxtla	
10229	8040	029009	Cuaxomulco	
10231	8040	029011	Muñoz de Domingo Arenas	
10232	8040	029012	Españita	
10233	8040	029013	Huamantla	
10234	8040	029014	Hueyotlipan	
10235	8040	029015	Ixtacuixtla de Mariano Matamoros	
10236	8040	029016	Ixtenco	
10238	8040	029018	Contla de Juan Cuamatzi	
10239	8040	029019	Tepetitla de Lardizábal	
10240	8040	029020	Sanctórum de Lázaro Cárdenas	
10241	8040	029021	Nanacamilpa de Mariano Arista	
10242	8040	029022	Acuamanala de Miguel Hidalgo	
10243	8040	029023	Natívitas	
10244	8040	029024	Panotla	
10245	8040	029025	San Pablo del Monte	
10246	8040	029026	Santa Cruz Tlaxcala	
10247	8040	029027	Tenancingo	
10248	8040	029028	Teolocholco	
10249	8040	029029	Tepeyanco	
10250	8040	029030	Terrenate	
10251	8040	029031	Tetla de la Solidaridad	
10252	8040	029032	Tetlatlahuca	
10253	8040	029033	Tlaxcala	
10254	8040	029034	Tlaxco	
10255	8040	029035	Tocatlán	
10256	8040	029036	Totolac	
10258	8040	029038	Tzompantepec	
10259	8040	029039	Xaloztoc	
10260	8040	029040	Xaltocan	
10261	8040	029041	Papalotla de Xicohténcatl	
10262	8040	029042	Xicohtzinco	
10264	8040	029044	Zacatelco	
10265	8040	029045	Benito Juárez	
10266	8040	029046	Emiliano Zapata	
10267	8040	029047	Lázaro Cárdenas	
10268	8040	029048	La Magdalena Tlaltelulco	
10271	8040	029051	San Jerónimo Zacualpan	
10272	8040	029052	San José Teacalco	
10273	8040	029053	San Juan Huactzinco	
10274	8040	029054	San Lorenzo Axocomanitla	
10275	8040	029055	San Lucas Tecopilco	
10276	8040	029056	Santa Ana Nopalucan	
10277	8040	029057	Santa Apolonia Teacalco	
10278	8040	029058	Santa Catarina Ayometla	
10279	8040	029059	Santa Cruz Quilehtla	
10280	8040	029060	Santa Isabel Xiloxoxtla	
10281	8031	001001	Aguascalientes	
10282	8031	001002	Asientos	
10283	8031	001003	Calvillo	
10284	8031	001004	Cosío	
10287	8031	001007	Rincón de Romos	
10288	8031	001008	San José de Gracia	
10289	8031	001009	Tepezalá	
10290	8031	001010	El Llano	
10291	8031	001011	San Francisco de los Romo	
10292	8026	030001	Acajete	
10293	8026	030002	Acatlán	
10294	8026	030003	Acayucan	
10295	8026	030004	Actopan	
10296	8026	030005	Acula	
10298	8026	030007	Camarón de Tejeda	
10299	8026	030008	Alpatláhuac	
10300	8026	030009	Alto Lucero de Gutiérrez Barrios	
10301	8026	030010	Altotonga	
10302	8026	030011	Alvarado	
10303	8026	030012	Amatitlán	
10304	8026	030013	Naranjos Amatlán	
10305	8026	030014	Amatlán de los Reyes	
10306	8026	030015	Angel R. Cabada	
10307	8026	030016	La Antigua	
10309	8026	030018	Aquila	
10310	8026	030019	Astacinga	
10311	8026	030020	Atlahuilco	
10312	8026	030021	Atoyac	
10313	8026	030022	Atzacan	
10314	8026	030023	Atzalan	
10316	8026	030025	Ayahualulco	
10317	8026	030026	Banderilla	
10318	8026	030027	Benito Juárez	
10319	8026	030028	Boca del Río	
10320	8026	030029	Calcahualco	
10321	8026	030030	Camerino Z. Mendoza	
10322	8026	030031	Carrillo Puerto	
10323	8026	030032	Catemaco	
10324	8026	030033	Cazones de Herrera	
10325	8026	030034	Cerro Azul	
10326	8026	030035	Citlaltépetl	
10327	8026	030036	Coacoatzintla	
10329	8026	030038	Coatepec	
10330	8026	030039	Coatzacoalcos	
10331	8026	030040	Coatzintla	
10332	8026	030041	Coetzala	
10333	8026	030042	Colipa	
10334	8026	030043	Comapa	
10335	8026	030044	Córdoba	
10337	8026	030046	Cosautlán de Carvajal	
10338	8026	030047	Coscomatepec	
10339	8026	030048	Cosoleacaque	
10340	8026	030049	Cotaxtla	
10341	8026	030050	Coxquihui	
10342	8026	030051	Coyutla	
10343	8026	030052	Cuichapa	
10344	8026	030053	Cuitláhuac	
10345	8026	030054	Chacaltianguis	
10346	8026	030055	Chalma	
10347	8026	030056	Chiconamel	
10348	8026	030057	Chiconquiaco	
10349	8026	030058	Chicontepec	
10351	8026	030060	Chinampa de Gorostiza	
10352	8026	030061	Las Choapas	
10353	8026	030062	Chocamán	
10354	8026	030063	Chontla	
10355	8026	030064	Chumatlán	
10224	8040	029004	Atltzayanca	
10263	8040	029043	Yauhquemehcan	
10269	8040	029049	San Damián Texóloc	
10356	8026	030065	Emiliano Zapata	
10357	8026	030066	Espinal	
10358	8026	030067	Filomeno Mata	
10359	8026	030068	Fortín	
10360	8026	030069	Gutiérrez Zamora	
10361	8026	030070	Hidalgotitlán	
10362	8026	030071	Huatusco	
10364	8026	030073	Hueyapan de Ocampo	
10365	8026	030074	Huiloapan de Cuauhtémoc	
10366	8026	030075	Ignacio de la Llave	
10367	8026	030076	Ilamatlán	
10368	8026	030077	Isla	
10369	8026	030078	Ixcatepec	
10370	8026	030079	Ixhuacán de los Reyes	
10371	8026	030080	Ixhuatlán del Café	
10372	8026	030081	Ixhuatlancillo	
10373	8026	030082	Ixhuatlán del Sureste	
10375	8026	030084	Ixmatlahuacan	
10376	8026	030085	Ixtaczoquitlán	
10377	8026	030086	Jalacingo	
10378	8026	030087	Xalapa	
10379	8026	030088	Jalcomulco	
10380	8026	030089	Jáltipan	
10381	8026	030090	Jamapa	
10383	8026	030092	Xico	
10384	8026	030093	Jilotepec	
10385	8026	030094	Juan Rodríguez Clara	
10386	8026	030095	Juchique de Ferrer	
10388	8026	030097	Lerdo de Tejada	
10389	8026	030098	Magdalena	
10390	8026	030099	Maltrata	
10392	8026	030101	Mariano Escobedo	
10393	8026	030102	Martínez de la Torre	
10394	8026	030103	Mecatlán	
10395	8026	030104	Mecayapan	
10396	8026	030105	Medellín	
10397	8026	030106	Miahuatlán	
10398	8026	030107	Las Minas	
10399	8026	030108	Minatitlán	
10400	8026	030109	Misantla	
10401	8026	030110	Mixtla de Altamirano	
10402	8026	030111	Moloacán	
10403	8026	030112	Naolinco	
10405	8026	030114	Nautla	
10406	8026	030115	Nogales	
10407	8026	030116	Oluta	
10408	8026	030117	Omealca	
10409	8026	030118	Orizaba	
10410	8026	030119	Otatitlán	
10411	8026	030120	Oteapan	
10412	8026	030121	Ozuluama de Mascareñas	
10413	8026	030122	Pajapan	
10414	8026	030123	Pánuco	
10416	8026	030125	Paso del Macho	
10417	8026	030126	Paso de Ovejas	
10418	8026	030127	La Perla	
10419	8026	030128	Perote	
10420	8026	030129	Platón Sánchez	
10421	8026	030130	Playa Vicente	
10423	8026	030132	Las Vigas de Ramírez	
10424	8026	030133	Pueblo Viejo	
10425	8026	030134	Puente Nacional	
10426	8026	030135	Rafael Delgado	
10427	8026	030136	Rafael Lucio	
10428	8026	030137	Los Reyes	
10429	8026	030138	Río Blanco	
10430	8026	030139	Saltabarranca	
10431	8026	030140	San Andrés Tenejapan	
10432	8026	030141	San Andrés Tuxtla	
10433	8026	030142	San Juan Evangelista	
10434	8026	030143	Santiago Tuxtla	
10435	8026	030144	Sayula de Alemán	
10436	8026	030145	Soconusco	
10437	8026	030146	Sochiapa	
10438	8026	030147	Soledad Atzompa	
10440	8026	030149	Soteapan	
10441	8026	030150	Tamalín	
10442	8026	030151	Tamiahua	
10443	8026	030152	Tampico Alto	
10444	8026	030153	Tancoco	
10445	8026	030154	Tantima	
10447	8026	030156	Tatatila	
10449	8026	030158	Tecolutla	
10450	8026	030159	Tehuipango	
10452	8026	030161	Tempoal	
10453	8026	030162	Tenampa	
10454	8026	030163	Tenochtitlán	
10455	8026	030164	Teocelo	
10456	8026	030165	Tepatlaxco	
10457	8026	030166	Tepetlán	
10458	8026	030167	Tepetzintla	
10459	8026	030168	Tequila	
10460	8026	030169	José Azueta	
10461	8026	030170	Texcatepec	
10462	8026	030171	Texhuacán	
10464	8026	030173	Tezonapa	
10465	8026	030174	Tierra Blanca	
10466	8026	030175	Tihuatlán	
10467	8026	030176	Tlacojalpan	
10468	8026	030177	Tlacolulan	
10469	8026	030178	Tlacotalpan	
10470	8026	030179	Tlacotepec de Mejía	
10471	8026	030180	Tlachichilco	
10472	8026	030181	Tlalixcoyan	
10473	8026	030182	Tlalnelhuayocan	
10474	8026	030183	Tlapacoyan	
10475	8026	030184	Tlaquilpa	
10477	8026	030186	Tomatlán	
10478	8026	030187	Tonayán	
10479	8026	030188	Totutla	
10480	8026	030189	Tuxpan	
10481	8026	030190	Tuxtilla	
10482	8026	030191	Ursulo Galván	
10484	8026	030193	Veracruz	
10485	8026	030194	Villa Aldama	
10486	8026	030195	Xoxocotla	
10487	8026	030196	Yanga	
10488	8026	030197	Yecuatla	
10489	8026	030198	Zacualpan	
10490	8026	030199	Zaragoza	
10491	8026	030200	Zentla	
10492	8026	030201	Zongolica	
10494	8026	030203	Zozocolco de Hidalgo	
10495	8026	030204	Agua Dulce	
10496	8026	030205	El Higo	
10497	8026	030206	Nanchital de Lázaro Cárdenas del Río	
10498	8026	030207	Tres Valles	
10499	8026	030208	Carlos A. Carrillo	
10500	8026	030209	Tatahuicapan de Juárez	
10501	8026	030210	Uxpanapa	
10502	8026	030211	San Rafael	
10503	8026	030212	Santiago Sochiapan	
10387	8026	030096	Landero y Coss	
10451	8026	030160	Álamo Temapache	
10505	8051	006001	Armería	
10506	8051	006002	Colima	
10507	8051	006003	Comala	
10508	8051	006004	Coquimatlán	
10509	8051	006005	Cuauhtémoc	
10510	8051	006006	Ixtlahuacán	
10511	8051	006007	Manzanillo	
10513	8051	006009	Tecomán	
10514	8051	006010	Villa de Álvarez	
11000	121	002000000	América	
11001	11000	002002017	Belice	
11032	15	001035	Derecho a la verdad	
11033	15	001040	Derecho de petición	
9006	8022	016079	Salvador Escalante	
11038	15	001065	Derecho a la libertad de expresión e información	
11039	15	001070	Derecho de réplica	
11040	15	001075	Derecho al acceso a la información pública y a la información personal	
11041	15	001080	Derecho a la libertad de asociación	
11042	11041	001080005	Derecho a formar asociaciones	
11043	11041	001080010	Derecho de afiliarse a asociaciones	
11044	15	001085	Derecho a la libertad de reunión	
11045	15	001090	Derecho a beneficiarse del progreso científico y sus aplicaciones	
11046	15	001095	Derecho a fundar una familia	
11047	15	001100	Derecho a la libertad de conciencia y religión	
11048	15	001105	Derecho a la libertad de tránsito	
11049	15	001110	Derecho a la nacionalidad	
11050	15	001115	Derecho de asilo	
11051	15	001120	Derecho de residencia	
11052	15	001125	Derecho a salir del país	
11053	15	001130	Derecho a la no discriminación	
11055	15	001140	Derecho a votar	
11056	15	001145	Derecho a postularse a cargos electivos	
11057	15	001150	Derecho a formar partidos políticos	
11058	15	001155	Derecho a militar en partidos políticos	
11059	15	001160	Derecho al acceso a la función pública	
11060	15	001165	Derecho a elecciones libres y democráticas	
11061	16	002005	Derecho a la educación	
11062	16	002010	Derecho a la salud	
11063	11062	002010005	Derecho a la salud sexual y reproductiva	
11065	11063	002010005010	Derecho a no ser objeto de aborto forzado	
11066	11063	002010005015	Derecho a la interrupción del embarazo en casos permitidos por la ley	
11067	11063	002010005020	Derecho a planificar libremente los hijos que se desea tener	
11068	11063	002010005025	Derecho a los servicios de salud sexual y reproductiva	
11069	16	002015	Derecho al trabajo	
11070	16	002020	Derecho a la alimentación adecuada	
11071	16	002025	Derecho a la vivienda adecuada	
11072	16	002030	Derecho a un medio ambiente sano	
11073	16	002035	Derecho a las prestaciones de seguridad social	
11074	16	002040	Derecho al acceso a los servicios públicos	
11075	16	002045	Derecho a la cultura	
11076	11075	002045005	Derecho a la protección de los intereses morales y materiales	
11077	11075	002045010	Derecho a la preservación de la cultura	
11082	11080	003005010	Derecho de las mujeres a la protección por embarazo	
11083	11080	003005015	Derecho de las mujeres a no ser objeto de violencia económica por su género	
11084	11080	003005020	Derecho de las mujeres a no ser objeto de violencia física por su género	
11085	11080	003005025	Derecho de las mujeres a no ser objeto de violencia psicológica por su género	
11086	11080	003005030	Derecho de las mujeres trabajadoras a la protección	
11095	17	003015	Derechos de las y los migrantes	
11096	11095	003015005	Derecho de las y los migrantes a la identidad cultural	
11098	11095	003015010	Derecho de las y los migrantes a la unidad familiar y a la reunificación familiar	
11101	17	003020	Derechos de los y las trabajadore(a)s	
11102	11101	003020030	Derecho de los y las trabajadore(a)s a la sindicación	
11103	11101	003020035	Derecho de los y las trabajadore(a)s a la democracia sindical	
11104	11101	003020040	Derecho de los y las trabajadore(a)s a la huelga	
11107	18	003025005	Derecho de las personas privadas de la libertad a instalaciones adecuadas	
11108	18	003025010	Derecho de las personas privadas de la libertad a trato digno y humano	
11109	18	003025015	Derecho de las personas privadas de la libertad a información sobre los reglamentos	
11110	18	003025020	Derecho de las personas privadas de la libertad a presentar quejas	
11111	18	003025025	Derecho de las personas privadas de la libertad a servicios médicos	
11113	11112	003030005	Derecho de las personas LGBT a no ser objeto de violencia por su orientación sexual	
11114	17	003035	Derechos de las niñas y los niños	
11115	11114	003035005	Derecho de las niñas y los niños a expresarse y ser escuchada(o)	
11116	11114	003035010	Derecho de las niñas y los niños a jugar y descansar	
11117	11114	003035015	Derecho de las niñas y los niños a la protección	
11118	11114	003035020	Derecho de las niñas y los niños a no trabajar	
11119	17	003040	Derechos de las personas con discapacidad	
11120	11119	003040005	Derecho de las personas con discapacidad a beneficios sociales	
11125	11124	003045005	Derecho de las personas adultas mayores a la protección	
11126	17	003050	Derechos de las y los extranjero(a)s	
11127	11126	003050005	Derecho de las y los extranjero(a)s a audiencia en casos de expulsión	
11129	17	003055	Derechos de las personas desplazadas	
11130	11129	003055035	Derecho de las personas desplazadas a indemnización por desplazamiento	
11131	11129	003055250	Derechos de las personas desplazadas en términos de políticas públicas	
11132	11129	003055005	Derecho a la prevención y protección contra el desplazamiento 	
11154	12	001005010	Ejecución	
11157	12	001005025	Muerte bajo custodia	
11159	12	001005035	Muerte resultado de negligencia	
11161	11160	001005040005	Muerte resultado de la aplicación de la tortura	
11162	11160	001005040010	Muerte resultado del uso desproporcionado o indebido de la fuerza pública	
11165	12	001005055	Muerte violenta	
11166	13	001010005	Agresiones físicas	
9018	8022	016091	Tingüindín	
11169	27	001010010005	Amenazas	Excepto "amenazas de muerte", si es el caso usa el término incluido en esta lista.
11079	16	002055	Derecho a la propiedad	Usar para todo tipo de propiedad privada: bienes inmuebles, pertenencias personales, dinero, etc. Para "propiedad intelectual" usar el "Derecho a la cultura" [o el nivel inmediatamente inferior]
11170	27	001010010010	Amenazas de muerte	
11171	27	001010010015	Vigilancia	
11172	27	001010010020	Hostigamiento	
11174	13	001010020	Intento de violación sexual	
11175	13	001010025	Hostigamiento sexual	
11176	13	001010030	Agresión sexual	
11178	13	001010040	Tortura	
11179	13	001010045	Tratos crueles, inhumanos o degradantes	
11184	10	001020	Violaciones al derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11223	10	001030	Violaciones al derecho a la seguridad jurídica	
11224	10	001035	Violaciones al derecho a la verdad	
11225	10	001040	Violaciones al derecho de petición	
11227	10	001050	Violaciones al derecho al respeto a la honra y reputación	
11228	11129	003055010	Derecho de las personas desplazadas a la protección contra la destrucción, apropiación, ocupación o uso arbitrario e ilegal de sus bienes que hayan abandonado 	
11229	11129	003055015	Derecho de las personas desplazadas a la reunificación familiar 	
11230	11129	003055020	Derecho de las personas desplazadas a participar en la planificación y gestión de su reasentamiento 	
11231	11129	003055025	Derecho de las personas desplazadas a recibir asistencia a su regreso, reasentamiento y reintegración 	
11232	11129	003055030	Derecho de las personas desplazadas a recibir protección y asistencia humanitaria 	
11237	11236	001060005	Violación a la correspondencia	
11239	10	001065	Violaciones al derecho a la libertad de expresión e información	
11240	11239	001065005	Censura	
11242	10	001070	Violaciones al derecho de réplica	
11243	10	001075	Violaciones al derecho al acceso a la información pública y a la información personal	
11246	10	001080	Violaciones al derecho a la libertad de asociación	
11247	11246	001080005	Violaciones al derecho a formar asociaciones	
11248	11246	001080010	Violaciones al derecho de afiliarse a asociaciones	
11249	10	001085	Violaciones al derecho a la libertad de reunión	
11250	10	001090	Violaciones al derecho a beneficiarse del progreso científico y sus aplicaciones	
11251	10	001095	Violaciones al derecho a fundar una familia	
11252	10	001100	Violaciones al derecho a la libertad de conciencia y religión	
11253	10	001105	Violaciones al derecho a la libertad de tránsito	
11254	10	001110	Violaciones al derecho a la nacionalidad	
11255	10	001115	Violaciones al derecho de asilo	
11256	10	001120	Violaciones al derecho de residencia	
11257	10	001125	Violaciones al derecho a salir del país	
11258	10	001130	Discriminación	
11260	10	001140	Violaciones al derecho a votar	
11261	10	001145	Violaciones al derecho a postularse a cargos electivos	
11262	10	001150	Violaciones al derecho a formar partidos políticos	
11263	10	001155	Violaciones al derecho a militar en partidos políticos	
11264	10	001160	Violaciones al derecho al acceso a la función pública	
11265	10	001165	Violaciones al derecho a elecciones libres y democráticas	
11266	135	002	Violaciones a los derechos económicos, sociales, culturales y ambientales	
11267	11266	002005	Violaciones al derecho a la educación	
11268	11266	002010	Violaciones al derecho a la salud	
11269	11268	002010005	Violaciones al derecho a la salud sexual y reproductiva	
11270	11269	002010005005	Violaciones al derecho a no ser objeto de esterilización sin consentimiento informado	
11271	11269	002010005010	Violaciones al derecho a no ser objeto de aborto forzado	
11272	11269	002010005015	Violaciones al derecho a la interrupción del embarazo en casos permitidos por la ley	
11273	11269	002010005020	Violaciones al derecho a planificar libremente los hijos que se desea tener	
11274	11269	002010005025	Violaciones al derecho a los servicios de salud sexual y reproductiva	
11275	11266	002015	Violaciones al derecho al trabajo	
11276	11266	002020	Violaciones al derecho a la alimentación adecuada	
11277	11266	002025	Violaciones al derecho a la vivienda adecuada	
11278	11266	002030	Violaciones al derecho a un medio ambiente sano	
11279	11266	002035	Violaciones al derecho a las prestaciones de seguridad social	
11280	11266	002040	Violaciones al derecho al acceso a los servicios públicos	
11281	11266	002045	Violaciones al derecho a la cultura	
11283	11281	002045010	Violaciones al derecho a la preservación de la cultura	
11287	11286	003005	Violaciones a los derechos de las mujeres	
11288	11287	003005005	Violaciones al derecho de las mujeres a gozar de permiso por maternidad	
11289	11287	003005010	Violaciones al derecho de las mujeres a la protección por embarazo	
11290	11287	003005015	Violaciones al derecho de las mujeres a no ser objeto de violencia económica por su género	
11291	11287	003005020	Violaciones al derecho de las mujeres a no ser objeto de violencia física por su género	
11292	11287	003005025	Violaciones al derecho de las mujeres a no ser objeto de violencia psicológica por su género	
11293	11287	003005030	Violaciones al derecho de las mujeres trabajadoras a la protección	
11285	11266	002055	Violaciones al derecho a la propiedad	Usar para todo tipo de propiedad privada: bienes inmuebles, pertenencias personales, dinero, etc., Para "propiedad intelectual" usar el "Derecho a la cultura" [o el nivel inmediatamente inferior]
11185	11184	001020005	Esclavitud	Es el estado o condición de un individuo sobre el cual se ejercitan los derechos de propiedad o algunos de ellos. Art. 1, Convención sobre Esclavitud. Ver también: Subcomisión de Derechos Humanos, Estudio actualizado sobre la aplicación y el seguimiento de las convenciones sobre la esclavitud, E/CN.4/Sub.2/2000/3, par 19.
11244	11243	001075005	Retención de información	Obstrucción al acceso del solicitante a la información requerida de forma arbitraria o injustificada por parte de un fucionario, servidor público o cualquier persona responsable de otorgar la información requerida.
11302	11286	003015	Violaciones a los derechos de las y los migrantes	
11303	11302	003015005	Violaciones al derecho de las y los migrantes a la identidad cultural	
11305	11302	003015010	Violaciones al derecho de las y los migrantes a la unidad familiar y a la reunificación familiar	
11307	11302	003015250	Violaciones a los derechos de las y los migrantes en términos de políticas públicas	
11308	11286	003020	Violaciones a los derechos de los y las trabajadore(a)s	
11313	11286	003025	Violaciones a los derechos de las personas privadas de la libertad	
11315	11313	003025005	Violaciones al derecho de las personas privadas de la libertad a instalaciones adecuadas	
11316	11313	003025010	Violaciones al derecho de las personas privadas de la libertad a trato digno y humano	
11317	11313	003025015	Violaciones al derecho de las personas privadas de la libertad a información sobre los reglamentos	
11318	11313	003025020	Violaciones al derecho de las personas privadas de la libertad a presentar quejas	
11319	11313	003025025	Violaciones al derecho de las personas privadas de la libertad a servicios médicos	
11321	11320	003030005	Violaciones al derecho de las personas LGBT a no ser objeto de violencia por su orientación sexual	
11322	11286	003035	Violaciones a los derechos de las niñas y los niños	
11324	11322	003035010	Violaciones al derecho de las niñas y los niños a jugar y descansar	
11325	11322	003035015	Violaciones al derecho de las niñas y los niños a la protección	
11326	11322	003035020	Violaciones al derecho de las niñas y los niños a no trabajar	
11327	11286	003040	Violaciones a los derechos de las personas con discapacidad	
11328	11327	003040005	Violaciones al derecho de las personas con discapacidad a beneficios sociales	
11329	11327	003040010	Violaciones al derecho de las personas con discapacidad a la asistencia	
11331	11327	003040020	Violaciones al derecho de las personas con discapacidad al empleo adecuado	
11332	11286	003045	Violaciones a los derechos de las personas adultas mayores	
11333	11332	003045005	Violaciones al derecho de las personas adultas mayores a la protección	
11334	11286	003050	Violaciones a los derechos de las y los extranjero(a)s	
11335	11334	003050005	Violaciones al derecho de las y los extranjero(a)s a audiencia en casos de expulsión	
11337	11286	003055	Violaciones a los derechos de las personas desplazadas	
11338	11337	003055035	Violaciones al derecho de las personas desplazadas a la indemnización por desplazamiento	
11339	11337	003055250	Violaciones a los derechos de las personas desplazadas en términos de políticas públicas	
11340	11337	003055005	Violaciones al derecho a la prevención y protección contra el desplazamiento 	
11343	11337	003055015	Violaciones al derecho de las personas desplazadas a la reunificación familiar	
11344	11337	003055020	Violaciones al derecho de las personas desplazadas a participar en la planificación y gestión de su reasentamiento	
11345	11337	003055025	Violaciones al derecho de las personas desplazadas a recibir asistencia a su regreso, reasentamiento y reintegración	
11346	11337	003055030	Violaciones al derecho de las personas desplazadas a recibir protección y asistencia humanitaria	
11347	171	005005005005	Presidencia de la República	
11348	171	005005005010	Secretaría de Estado	
11350	171	005005005020	Programa federal	
11351	171	005005005025	Fuerzas armadas	
11352	11351	005005005025005	Ejército mexicano	
11354	170	005005010005	Gubernatura estatal	
11355	170	005005010010	Secretaría estatal	
11357	170	005005010020	Programa estatal	
11359	168	005005015	Poder ejecutivo municipal	
11360	11359	005005015005	Presidencia municipal	
11361	11359	005005015010	Cabildo municipal	
11363	11359	005005015020	Programa municipal	
11364	11359	005005015025	Fuerzas municipales de seguridad pública	
11365	168	005005020	Autoridades comunitarias	
11366	11365	005005020005	Autoridad comunitaria	
11367	11365	005005020010	Consejo/asamblea comunitaria	
11368	11365	005005020015	Institución comunitaria	
11369	11365	005005020020	Programa comunitario	
11370	11365	005005020025	Fuerzas comunitarias de seguridad pública	
11373	11371	005010005010	Senado de la República	
11374	11371	005010005015	Cámara de diputados federal	
11377	169	005010010	Poder legislativo estatal	
11378	11377	005010010005	Congreso estatal	
11379	11377	005010010010	Comisión legislativa estatal	
11380	11377	005010010015	Fracción parlamentaria estatal	
11381	166	005015	Poder judicial	
11382	11381	005015005	Poder judicial federal	
11385	11382	005015005015	Juzgado federal	
11386	11382	005015005020	Judicatura federal	
11387	11381	005015010	Poder judicial estatal	
11388	11387	005015010015	Juzgado estatal	
11394	11389	005020025	Organismos de recursos naturales y medio ambiente federales	
11397	167	010005	Empresa privada	
11398	167	010010	Institución financiera	
11401	11397	010005015	Empresa privada local	
11407	167	010020	Institución religiosa	
11410	167	010035	Grupo de delincuencia organizada	
11414	11410	010035020	Banda de secuestradores	
11416	167	010045	Persona que abusa de su poder	
11417	11416	010045005	Persona que abusa de su poder dentro de la familia	
11418	11416	010045010	Persona que abusa de su poder dentro de la escuela	
11419	11416	010045015	Persona que abusa de su poder dentro del trabajo	
11420	11416	010045020	Persona que abusa de su poder dentro de la comunidad	
11424	171	005005005045	Institución federal del sistema penitenciario	
11425	171	005005005050	Agencia federal de inteligencia 	
11428	170	005005010040	Institución estatal del sistema penitenciario	
11429	170	005005010045	Agencia estatal de inteligencia 	
11430	11359	005005015035	Institución municipal del sistema carcelario	
11431	11387	005015010005	Tribunal estatal superior	
11434	11417	010045005010	Padre, madre, tutor(a)	
11435	11418	010045010005	Administrador(a) escolar	
11436	11418	010045010010	Profesor(a)	
11437	11419	010045015005	Patrón(a)	
11438	11419	010045015010	Jefe(a), supervisor(a)	
11441	165	015	Entidades internacionales	
11442	11441	015005	Organismos internacionales privados	
11486	1	T14	Idioma	
11468	127	055	Tarahumara	Usado por: Raramuri, Rarámuris
11490	1	T07	Tipo de persona colectiva	
11583	11000	002002025	Costa Rica	
11584	11000	002002030	El Salvador	
11585	11000	002002036	Guatemala	
11586	11000	002002039	Honduras	
11588	11000	002002046	Panamá	
11592	11000	002001026	Cuba	
11593	11000	002001028	República Dominicana	
11594	11000	002001038	Haití	
11595	11000	002001040	Jamaica	
11596	11000	002001049	Puerto Rico	
11597	11000	002003013	Argentina	
11598	11000	002003019	Bolivia	
11599	11000	002003020	Brasil	
11600	11000	002003023	Chile	
11601	11000	002003024	Colombia	
11602	11000	002003029	Ecuador	
11603	11000	002003047	Paraguay	
11604	11000	002003048	Perú	
11605	11000	002003059	Uruguay	
11607	11000	002004021	Canadá	
11608	11000	002004057	Estados Unidos	
11610	11000	002002042	México	
11611	11609	005001012	Australia	
11612	11609	003001019	China	
11614	11609	003001031	Corea, República Democrática Popular de	
11615	11609	003001032	Corea, República de	
11617	11609	003002023	India	
11618	11609	003002030	Kazajstán	
11619	11609	003002034	Kirguistán	
11620	11609	003002052	Tayikistán	
11621	11609	003002055	Turkmenistán	
11622	11609	003002057	Uzbekistán	
11623	11609	003005013	Azerbaiyán	
11624	11609	003005021	Georgia	
11625	11609	003005026	Iraq	
11627	121	004000000	Europa	
11628	11627	004001014	Belarús	
11629	11627	004001017	Bulgaria	
11630	11627	004001020	República Checa	
11631	11627	004001032	Hungría	
11632	11627	004001043	Moldova, República de	
11633	11627	004001047	Polonia	
11634	11627	004001049	Rumania	
11635	11627	004001052	Eslovaquia	
11636	11627	004001058	Ucrania	
11637	11627	004002039	Lituania	
11638	11627	004002056	Suecia	
11639	11627	004002059	Reino Unido	
11641	11627	004003031	Santa Sede	
11642	11627	004003036	Italia	
11643	11627	004003041	Macedonia, Antigua República Yugoslava de	
11644	11627	004003048	Portugal	
11645	11627	004003053	Eslovenia	
11646	11627	004003054	España	
11648	11627	004003065	Montenegro, República de (a partir de junio 2006)	
11649	11627	004003080	Kosovo	
11650	11627	004004015	Bélgica	
11651	11627	004004026	Francia	
11652	11627	004004028	Alemania	
11653	11627	004004045	Países Bajos	
11654	11627	004004057	Suiza	
11655	50	001	Edad exacta	
11656	50	002	Edad aproximada	
11670	1	T40	Tipo de dirección	
11671	11670	001	Dirección de casa	
11672	11670	002	Dirección del trabajo	
11676	11351	005005005025010	Fuerza aérea	
11677	11351	005005005025015	Armada	
11681	11426	005005010030010	Institución estatal de investigación pericial	
11683	11365	005005020030	Institución comunitaria encargada de la administración de justicia	
11684	11365	005005020035	Institución comunitaria del sistema de sanciones	
11685	11387	005015010020	Judicatura estatal	
11690	11686	005025020	Organismos de recursos naturales y medio ambiente estatales	
11691	11686	005025025	Organismos de producción y servicios públicos estatales	
11693	11420	010045020010	Líder en la comunidad	
11728	1	T46	Estatus intervención y expediente	
11729	1	T62	Legislación nacional	
11730	1	T06	Instrumentos internacionales	
11731	19	001005250	Derecho a la vida en términos de políticas públicas	
11732	19	001005255	Derecho a la vida en términos de legislación	
11733	19	001005260	Derecho a la vida en términos de resoluciones judiciales	
11734	20	001010250	Derecho a la integridad personal en términos de políticas públicas	
11735	20	001010255	Derecho a la integridad personal en términos de legislación	
11737	21	001015250	Derecho a la libertad y seguridad personales en términos de políticas públicas	
11738	21	001015255	Derecho a la libertad y seguridad personales en términos de legislación	
11739	21	001015260	Derecho a la libertad y seguridad personales en términos de resoluciones judiciales	
11740	134	001020250	Derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de políticas públicas	
11741	134	001020255	Derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de legislación	
11742	134	001020260	Derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de resoluciones judiciales	
11743	11159	001005035005	Muerte resultado de negligencia médica	
11744	12	001005250	Violaciones al derecho a la vida en términos de políticas públicas	
11745	11744	001005250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la vida	
11705	154	185	Reubicado(a)	
11746	11744	001005250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la vida	
11747	11744	001005250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la vida	
11748	11744	001005250020	Caso específico de no realización del derecho a la vida en términos de políticas públicas	
11749	12	001005255	Violaciones al derecho a la vida en términos de legislación	
11750	11749	001005255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la vida	
11751	11749	001005255010	Adopción de legislación regresiva en la protección, respeto y garantía del derecho a la vida	
11752	11749	001005255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la vida	
11753	11749	001005255020	Caso específico de no realización del derecho a la vida en términos de legislación	
11754	12	001005260	Violaciones al derecho a la vida en términos de resoluciones judiciales	
11756	11754	001005260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la vida	
11757	11754	001005260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la vida	
11758	11754	001005260020	Caso específico de no realización del derecho a la vida en términos de resoluciones judiciales	
11760	11759	001010250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la integridad personal	
11761	11759	001010250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la integridad personal	
11762	11759	001010250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la integridad personal	
11763	11759	001010250020	Caso específico de no realización del derecho a la integridad personal en términos de políticas públicas	
11764	13	001010255	Violaciones al derecho a la integridad personal en términos de legislación	
11765	11764	001010255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la integridad personal	
11766	11764	001010255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la integridad personal	
11767	11764	001010255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la integridad personal	
11768	11764	001010255020	Caso específico de no realización del derecho a la integridad personal en términos de legislación	
11769	13	001010260	Violaciones al derecho a la integridad personal en términos de resoluciones judiciales	
11770	11769	001010260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la integridad personal	
11772	11769	001010260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la integridad personal	
11773	11769	001010260020	Caso específico de no realización del derecho a la integridad personal en términos de resoluciones judiciales	
11775	14	001015045	Redada	
11776	14	001015250	Violaciones al derecho a la libertad y seguridad personales en términos de políticas públicas	
11777	11776	001015250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la libertad y seguridad personales	
11778	11776	001015250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la libertad y seguridad personales	
11779	11776	001015250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la libertad y seguridad personales	
11780	11776	001015250020	Caso específico de no realización del derecho a la libertad y seguridad personales en términos de políticas públicas	
11781	14	001015255	Violaciones al derecho a la libertad y seguridad personales en términos de legislación	
11782	11781	001015255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la libertad y seguridad personales 	
11783	11781	001015255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la libertad y seguridad personales	
11784	11781	001015255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la libertad y seguridad personales	
11787	11786	001015260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad y seguridad personales	
11788	11786	001015260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la libertad y seguridad personales	
11789	11786	001015260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad y seguridad personales	
11790	11786	001015260020	Caso específico de no realización del derecho a la libertad y seguridad personales en términos de resoluciones judiciales	
11791	11184	001020250	Violaciones al derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de políticas públicas	
11792	11791	001020250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11793	11791	001020250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11794	11791	001020250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11795	11791	001020250020	Caso específico de no realización del derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de políticas públicas	
11796	11184	001020255	Violaciones al derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de legislación	
11797	11796	001020255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11798	11796	001020255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11799	11796	001020255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11800	11796	001020255020	Caso específico de no realización del derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de legislación	
11801	11184	001020260	Violaciones al derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de resoluciones judiciales	
11802	11801	001020260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11803	11801	001020260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11804	11801	001020260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
11806	138	001025005	Derecho a un tribunal competente	
11808	138	001025015	Derecho a un juicio público	
11809	138	001025020	Derecho a un juicio expedito	
11810	138	001025025	Igualdad entre las partes (Principio de)	
11811	138	001025030	Derecho a hallarse presente en el proceso	
11812	138	001025035	Derecho de apelación	
11813	138	001025040	Derecho a presentar pruebas	
11817	11816	001025055005	Derecho a  ser informado(a) de las razones de la detención	
11818	11816	001025055010	Derecho a ser informado(a) de los cargos en su contra	
11821	11816	001025055025	Derecho a impugnar la legalidad de la detención	
11822	11816	001025055030	Derecho a reparación por la detención arbitraria o ilegal	
11823	11816	001025055035	Derecho a la presunción de inocencia	
11826	11816	001025055050	Derecho a tener acceso a asistencia letrada durante el interrogatorio	
11828	11816	001025055055	Derecho al defensor(a) de su elección	
11829	11816	001025055060	Derecho a un defensor(a) de oficio	
11830	11816	001025055065	Derecho a comunicarse con su defensor(a)	
11831	11816	001025055070	Derecho a una defensa eficaz	
11832	11816	001025055075	Derecho a defenderse personalmente	
11833	11816	001025055080	Derecho a disponer del tiempo y los medios adecuados para su defensa	
11835	11816	001025055090	Derecho a no ser juzgado(a) dos veces por el mismo delito	
11836	11816	001025055095	Derecho a la no aplicación retroactiva de la ley en su perjuicio	
11837	11816	001025055100	Derecho de indemnización por error judicial	
11838	11816	001025055105	Derecho de separación entre  procesado(a)s y sentenciado(a)s	
11840	11839	001025060005	Derecho a una reparación adecuada, efectiva y rápida del daño sufrido	
11841	11839	001025060010	Derecho a la consideración y atención especiales durante los procedimientos que evite la revictimización	
11842	11839	001025060015	Derecho al acceso a la información pertinente sobre las violaciones o delitos y mecanismos de reparación	
11843	11839	001025060020	Derecho a la protección contra actos de intimidación y represalia, para sí y su familia antes, durante y después de los procedimientos	
11844	11839	001025060025	Derecho a la asistencia apropiada para acceder a la justicia	
11846	11839	001025060035	Derecho a ser informado(a) sobre el desarrollo del proceso penal	
11847	11839	001025060040	Derecho a la coadyuvancia	
11848	11839	001025060045	Derecho a la atención médica y sicológica de urgencia	
11849	138	001025250	Derecho al acceso a la justicia en términos de políticas públicas	
11850	138	001025255	Derecho al acceso a la justicia en términos de legislación	
11851	138	001025260	Derecho al acceso a la justicia en términos de resoluciones judiciales	
11852	11191	001025005	Violaciones al derecho a un tribunal competente	
11853	11191	001025010	Violaciones al derecho a un tribunal independiente e imparcial	
11854	11191	001025015	Violaciones al derecho a un juicio público	
11855	11191	001025020	Violaciones al derecho a un juicio expedito	
11856	11191	001025025	Violaciones a la igualdad entre las partes (Principio de)	
11857	11191	001025030	Violaciones al derecho a hallarse presente en el proceso	
11858	11191	001025035	Violaciones al derecho de apelación	
11859	11191	001025040	Violaciones al derecho a presentar pruebas	
11863	11862	001025055005	Violaciones al derecho a  ser informado(a) de las razones de la detención	
11864	11862	001025055010	Violaciones al derecho a ser informado(a) de los cargos en su contra	
11867	11862	001025055025	Violaciones al derecho a impugnar la legalidad de la detención	
11868	11862	001025055030	Violaciones al derecho a reparación por la detención arbitraria o ilegal	
11869	11862	001025055035	Violaciones al derecho a la presunción de inocencia	
11870	11862	001025055040	Violaciones al derecho a la libertad bajo fianza	
11871	11862	001025055045	Violaciones al derecho a no declarar en su contra	
11873	11862	001025055055	Violaciones al derecho al defensor(a) de su elección	
11874	11862	001025055060	Violaciones al derecho a un defensor(a) de oficio	
11875	11862	001025055065	Violaciones al derecho a comunicarse con su defensor(a)	
11876	11862	001025055070	Violaciones al derecho a una defensa eficaz	
11877	11862	001025055075	Violaciones al derecho a defenderse personalmente	
11878	11862	001025055080	Violaciones al derecho a disponer del tiempo y los medios adecuados para su defensa	
11880	11862	001025055090	Violaciones al derecho a no ser juzgado(a) dos veces por el mismo delito	
11881	11862	001025055095	Violaciones al derecho a la no aplicación retroactiva de la ley en su perjuicio	
11882	11862	001025055100	Violaciones al derecho de indemnización por error judicial	
11883	11862	001025055105	Violaciones al derecho de separación entre  procesado(a)s y sentenciado(a)s	
11885	11884	001025060005	Violaciones al derecho a una reparación adecuada, efectiva y rápida del daño sufrido	
11886	11884	001025060010	Violaciones al derecho a la consideración y atención especiales durante los procedimientos que evite la revictimización	
11887	11884	001025060015	Violaciones al derecho al acceso a la información pertinente sobre las violaciones o delitos y mecanismos de reparación	
11889	11884	001025060025	Violaciones al derecho a la asistencia apropiada para acceder a la justicia	
11891	11884	001025060035	Violaciones al derecho a ser informado(a) sobre el desarrollo del proceso penal	
11892	11884	001025060040	Violaciones al derecho a la coadyuvancia	
11860	11191	001025045	Violaciones al derecho a un(a) fiscal imparcial y objetivo(a)	
11894	11191	001025250	Violaciones al derecho al acceso a la justicia en términos de políticas públicas	
11896	11894	001025250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho al acceso a la justicia	
11897	11894	001025250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho al acceso a la justicia	
11898	11894	001025250020	Caso específico de no realización del derecho a un debido proceso en términos de políticas públicas al acceso a la justicia	
11899	11191	001025255	Violaciones al derecho al acceso a la justicia en términos de legislación	
11900	11899	001025255005	Falta de adopción de legislación que respete, proteja y garantice el derecho al acceso a la justicia	
11901	11899	001025255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho al acceso a la justicia	
11902	11899	001025255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho al acceso a la justicia	
11903	11899	001025255020	Caso específico de no realización del derecho al acceso a la justicia en términos de legislación	
11904	11191	001025260	Violaciones al derecho al acceso a la justicia en términos de resoluciones judiciales	
11905	11904	001025260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a la justicia	
11906	11904	001025260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho al acceso a la justicia	
11907	11904	001025260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a la justicia	
11908	11904	001025260020	Caso específico de no realización del derecho al acceso a la justicia en términos de resoluciones judiciales	
11909	139	001030250	Derecho a la seguridad jurídica en términos de políticas públicas	
11911	139	001030255	Derecho a la seguridad jurídica en términos de legislación	
11912	139	001030260	Derecho a la seguridad jurídica en términos de resoluciones judiciales	
11913	11032	001035250	Derecho a la verdad en términos de políticas públicas	
11914	11032	001035255	Derecho a la verdad en términos de legislación	
11915	11032	001035260	Derecho a la verdad en términos de resoluciones judiciales	
11916	11033	001040250	Derecho de petición en términos de políticas públicas	
11917	11033	001040255	Derecho de petición en términos de legislación	
11918	11033	001040260	Derecho de petición en términos de resoluciones judiciales	
11922	11035	001050250	Derecho al respeto de la honra y reputación en términos de políticas públicas	
11923	11035	001050255	Derecho al respeto de la honra y reputación en términos de legislación	
11924	11035	001050260	Derecho al respeto de la honra y reputación en términos de resoluciones judiciales	
11925	11036	001055250	Derecho a la inviolabilidad de domicilio en términos de políticas públicas	
11926	11036	001055255	Derecho a la inviolabilidad de domicilio en términos de legislación	
11927	11036	001055260	Derecho a la inviolabilidad de domicilio en términos de resoluciones judiciales	
11928	11037	001060250	Derecho a la inviolabilidad de las comunicaciones en términos de políticas públicas	
11929	11037	001060255	Derecho a la inviolabilidad de las comunicaciones en términos de legislación	
11930	11037	001060260	Derecho a la inviolabilidad de las comunicaciones en términos de resoluciones judiciales	
11931	11038	001065250	Derecho a la libertad de expresión e información en términos de políticas públicas	
11932	11038	001065255	Derecho a la libertad de expresión e información en términos de legislación	
11933	11038	001065260	Derecho a la libertad de expresión e información en términos de resoluciones judiciales	
11934	11039	001070250	Derecho de réplica en términos de políticas públicas	
11935	11039	001070255	Derecho de réplica en términos de legislación	
11936	11039	001070260	Derecho de réplica en términos de resoluciones judiciales	
11938	11040	001075255	Derecho al acceso a la información pública y a la información personal en términos de legislación	
11939	11040	001075260	Derecho al acceso a la información pública y a la información personal en términos de resoluciones judiciales	
11940	11041	001080250	Derecho a la libertad de asociación en términos de políticas públicas	
11941	11041	001080255	Derecho a la libertad de asociación en términos de legislación	
11942	11041	001080260	Derecho a la libertad de asociación en términos de resoluciones judiciales	
11943	11044	001085250	Derecho a la libertad de reunión en términos de políticas públicas	
11944	11044	001085255	Derecho a la libertad de reunión en términos de legislación	
11945	11044	001085260	Derecho a la libertad de reunión en términos de resoluciones judiciales	
11946	11045	001090250	Derecho a beneficiarse del progreso científico y sus aplicaciones en términos de políticas públicas	
11947	11045	001090255	Derecho a beneficiarse del progreso científico y sus aplicaciones en términos de legislación	
11948	11045	001090260	Derecho a beneficiarse del progreso científico y sus aplicaciones en términos de resoluciones judiciales	
11949	11223	001030250	Violaciones al derecho a la seguridad jurídica en términos de políticas públicas	
11950	11223	001030255	Violaciones al derecho a la seguridad jurídica en términos de legislación	
11951	11223	001030260	Violaciones al derecho a la seguridad jurídica en términos de resoluciones judiciales	
11952	11949	001030250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la seguridad jurídica	
11954	11949	001030250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la seguridad jurídica	
11955	11949	001030250020	Caso específico de no realización del derecho a la seguridad jurídica en términos de políticas públicas	
13690	13689	008002	Cinta de video o película académico	
11921	11034	001045260	Derecho a la vida privada en términos de resoluciones judiciales	
11920	11034	001045255	Derecho a la vida privada en términos de legislación	
11956	11950	001030255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la seguridad jurídica	
11957	11950	001030255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la seguridad jurídica	
11958	11950	001030255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la seguridad jurídica	
11959	11950	001030255020	Caso específico de no realización del derecho a la seguridad jurídica en términos de legislación	
11960	11951	001030260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la seguridad jurídica	
11961	11951	001030260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la seguridad jurídica	
11962	11951	001030260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la seguridad jurídica	
11963	11951	001030260020	Caso específico de no realización del derecho a la seguridad jurídica en términos de resoluciones judiciales	
11964	11224	001035250	Violaciones al derecho a la verdad en términos de políticas públicas	
11965	11964	001035250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la verdad	
11966	11964	001035250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la verdad	
11967	11964	001035250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la verdad	
11968	11964	001035250020	Caso específico de no realización del derecho a la verdad en términos de políticas públicas	
11969	11224	001035255	Violaciones al derecho a la verdad en términos de legislación	
11970	11969	001035255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la verdad	
11972	11969	001035255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la verdad	
11973	11969	001035255020	Caso específico de no realización del derecho a la verdad en términos de legislación	
11974	11224	001035260	Violaciones al derecho a la verdad en términos de resoluciones judiciales	
11975	11974	001035260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la verdad	
11976	11974	001035260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la verdad	
11977	11974	001035260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la verdad	
11978	11974	001035260020	Caso específico de no realización del derecho a la verdad en términos de resoluciones judiciales	
11979	11225	001040250	Violaciones al derecho de petición en términos de políticas públicas	
11980	11979	001040250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de petición	
11981	11979	001040250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de petición	
11982	11979	001040250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de petición	
11983	11979	001040250020	Caso específico de no realización del derecho de petición en términos de políticas públicas	
11984	11225	001040255	Violaciones al derecho de petición en términos de legislación	
11985	11984	001040255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de petición	
11986	11984	001040255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de petición	
11987	11984	001040255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho de petición	
11988	11984	001040255020	Caso específico de no realización del derecho de petición en términos de legislación	
11989	11225	001040260	Violaciones al derecho de petición en términos de resoluciones judiciales	
11990	11989	001040260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de petición	
11991	11989	001040260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de petición	
11992	11989	001040260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de petición	
11993	11989	001040260020	Caso específico de no realización del derecho de petición en términos de resoluciones judiciales	
12009	11227	001050250	Violaciones al derecho al respeto de la honra y reputación en términos de políticas públicas	
12010	12009	001050250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho al respeto de la honra y reputación	
12058	12054	001065250020	Caso específico de no realización del derecho a la libertad de expresión e información en términos de políticas públicas	
12001	11999	001045255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la vida privada	
12003	11999	001045255020	Caso específico de no realización del derecho a la vida privada en términos de legislación	
12000	11999	001045255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la vida privada	
12008	12004	001045260020	Caso específico de no realización del derecho a la vida privada en términos de resoluciones judiciales	
11995	11994	001045250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la vida privada	
11996	11994	001045250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la vida privada	
12004	11226	001045260	Violaciones al derecho a la vida privada en términos de resoluciones judiciales	
12007	12004	001045260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la vida privada	
11997	11994	001045250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la vida privada	
11999	11226	001045255	Violaciones al derecho a la vida privada en términos de legislación	
11994	11226	001045250	Violaciones al derecho a la vida privada en términos de políticas públicas	
12011	12009	001050250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho al respeto de la honra y reputación	
12012	12009	001050250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho al respeto de la honra y reputación	
12013	12009	001050250020	Caso específico de no realización del derecho al respeto de la honra y reputación en términos de políticas públicas	
12014	11227	001050255	Violaciones al derecho al respeto de la honra y reputación en términos de legislación	
12015	12014	001050255005	Falta de adopción de legislación que respete, proteja y garantice el derecho al respeto de la honra y reputación	
12016	12014	001050255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho al respeto de la honra y reputación	
12017	12014	001050255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho al respeto de la honra y reputación	
12018	12014	001050255020	Caso específico de no realización del derecho al respeto de la honra y reputación en términos de legislación	
12019	11227	001050260	Violaciones al derecho al respeto de la honra y reputación en términos de resoluciones judiciales	
12020	12019	001050260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho al respeto de la honra y reputación	
12021	12019	001050260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho al respeto de la honra y reputación	
12022	12019	001050260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho al respeto de la honra y reputación	
12023	12019	001050260020	Caso específico de no realización del derecho al respeto de la honra y reputación en términos de resoluciones judiciales	
12024	11233	001055250	Violaciones al derecho a la inviolabilidad de domicilio en términos de políticas públicas	
12025	12024	001055250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la inviolabilidad de domicilio	
12026	12024	001055250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la inviolabilidad de domicilio	
12027	12024	001055250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la inviolabilidad de domicilio	
12028	12024	001055250020	Caso específico de no realización del derecho a la inviolabilidad de domicilio en términos de políticas públicas	
12029	11233	001055255	Violaciones al derecho a la inviolabilidad de domicilio en términos de legislación	
12030	12029	001055255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la inviolabilidad de domicilio	
12031	12029	001055255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la inviolabilidad de domicilio	
12032	12029	001055255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la inviolabilidad de domicilio	
12033	12029	001055255020	Caso específico de no realización del derecho  en términos de legislación a la inviolabilidad de domicilio	
12034	11233	001055260	Violaciones al derecho a la inviolabilidad de domicilio en términos de resoluciones judiciales	
12036	12034	001055260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la inviolabilidad de domicilio	
12037	12034	001055260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la inviolabilidad de domicilio	
12038	12034	001055260020	Caso específico de no realización del derecho a la inviolabilidad de domicilio en términos de resoluciones judiciales	
12039	11236	001060250	Violaciones al derecho a la inviolabilidad de las comunicaciones en términos de políticas públicas	
12040	12039	001060250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la inviolabilidad de las comunicaciones	
12041	12039	001060250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la inviolabilidad de las comunicaciones	
12042	12039	001060250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la inviolabilidad de las comunicaciones	
12043	12039	001060250020	Caso específico de no realización del derecho a la inviolabilidad de las comunicaciones en términos de políticas públicas	
12044	11236	001060255	Violaciones al derecho a la inviolabilidad de las comunicaciones en términos de legislación	
12045	12044	001060255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la inviolabilidad de las comunicaciones	
12046	12044	001060255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la inviolabilidad de las comunicaciones	
12047	12044	001060255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la inviolabilidad de las comunicaciones	
12048	12044	001060255020	Caso específico de no realización del derecho a la inviolabilidad de las comunicaciones en términos de legislación	
12049	11236	001060260	Violaciones al derecho a la inviolabilidad de las comunicaciones en términos de resoluciones judiciales	
12050	12049	001060260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la inviolabilidad de las comunicaciones	
12051	12049	001060260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la inviolabilidad de las comunicaciones	
12053	12049	001060260020	Caso específico de no realización del derecho a la inviolabilidad de las comunicaciones en términos de resoluciones judiciales	
12054	11239	001065250	Violaciones al derecho a la libertad de expresión e información en términos de políticas públicas	
12055	12054	001065250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de expresión e información	
12056	12054	001065250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la libertad de expresión e información	
12057	12054	001065250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de expresión e información	
12059	11239	001065255	Violaciones al derecho a la libertad de expresión e información en términos de legislación	
12060	12059	001065255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la libertad de expresión e información	
12061	12059	001065255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la libertad de expresión e información	
12062	12059	001065255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la libertad de expresión e información	
12063	12059	001065255020	Caso específico de no realización del derecho a la libertad de expresión e información en términos de legislación	
12064	11239	001065260	Violaciones al derecho a la libertad de expresión e información en términos de resoluciones judiciales	
12065	12064	001065260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de expresión e información	
12066	12064	001065260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la libertad de expresión e información	
12067	12064	001065260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de expresión e información	
12068	12064	001065260020	Caso específico de no realización del derecho a la libertad de expresión e información en términos de resoluciones judiciales	
12069	11242	001070250	Violaciones al derecho de réplica en términos de políticas públicas	
12070	12069	001070250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de réplica	
12071	12069	001070250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de réplica	
12072	12069	001070250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de réplica	
12073	12069	001070250020	Caso específico de no realización del derecho de réplica en términos de políticas públicas	
12074	11242	001070255	Violaciones al derecho de réplica en términos de legislación	
12075	12074	001070255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de réplica	
12076	12074	001070255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de réplica	
12077	12074	001070255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho de réplica	
12078	12074	001070255020	Caso específico de no realización del derecho de réplica en términos de legislación	
12079	11242	001070260	Violaciones al derecho de réplica en términos de resoluciones judiciales	
12080	12079	001070260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de réplica	
12081	12079	001070260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de réplica	
12082	12079	001070260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de réplica	
12083	12079	001070260020	Caso específico de no realización del derecho de réplica en términos de resoluciones judiciales	
12085	12084	001075250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho al acceso a la información pública y a la información personal	
12086	12084	001075250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho al acceso a la información pública y a la información personal	
12087	12084	001075250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho al acceso a la información pública y a la información personal	
12088	12084	001075250020	Caso específico de no realización del derecho al acceso a la información pública y a la información personal en términos de políticas públicas	
12089	11243	001075255	Violaciones al derecho al acceso a la información pública y a la información personal en términos de legislación	
12090	12089	001075255005	Falta de adopción de legislación que respete, proteja y garantice el derecho al acceso a la información pública y a la información personal	
12091	12089	001075255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho al acceso a la información pública y a la información personal	
12092	12089	001075255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho al acceso a la información pública y a la información personal	
12093	12089	001075255020	Caso específico de no realización del derecho al acceso a la información pública y a la información personal en términos de legislación	
12094	11243	001075260	Violaciones al derecho al acceso a la información pública y a la información personal en términos de resoluciones judiciales	
12095	12094	001075260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a la información pública y a la información personal	
12096	12094	001075260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho al acceso a la información pública y a la información personal	
12098	12094	001075260020	Caso específico de no realización del derecho al acceso a la información pública y a la información personal en términos de resoluciones judiciales	
12099	11246	001080250	Violaciones al derecho a la libertad de asociación en términos de políticas públicas	
12100	12099	001080250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de asociación	
12101	12099	001080250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la libertad de asociación	
12102	12099	001080250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de asociación	
12103	12099	001080250020	Caso específico de no realización del derecho a la libertad de asociación en términos de políticas públicas	
12104	11246	001080255	Violaciones al derecho a la libertad de asociación en términos de legislación	
12105	12104	001080255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la libertad de asociación	
12106	12104	001080255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la libertad de asociación	
12107	12104	001080255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la libertad de asociación	
12108	12104	001080255020	Caso específico de no realización del derecho a la libertad de asociación en términos de legislación	
12109	11246	001080260	Violaciones al derecho a la libertad de asociación en términos de resoluciones judiciales	
12111	12109	001080260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la libertad de asociación	
12112	12109	001080260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de asociación	
12113	12109	001080260020	Caso específico de no realización del derecho a la libertad de asociación en términos de resoluciones judiciales	
12114	11249	001085250	Violaciones al derecho a la libertad de reunión en términos de políticas públicas	
12115	12114	001085250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de reunión	
12116	12114	001085250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la libertad de reunión	
12117	12114	001085250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de reunión	
12118	12114	001085250020	Caso específico de no realización del derecho a la libertad de reunión en términos de políticas públicas	
12119	11249	001085255	Violaciones al derecho a la libertad de reunión en términos de legislación	
12120	12119	001085255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la libertad de reunión	
12121	12119	001085255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la libertad de reunión	
12122	12119	001085255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la libertad de reunión	
12123	12119	001085255020	Caso específico de no realización del derecho a la libertad de reunión en términos de legislación	
12124	11249	001085260	Violaciones al derecho a la libertad de reunión en términos de resoluciones judiciales	
12125	12124	001085260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de reunión	
12126	12124	001085260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la libertad de reunión	
12127	12124	001085260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de reunión	
12128	12124	001085260020	Caso específico de no realización del derecho a la libertad de reunión en términos de resoluciones judiciales	
12129	11250	001090250	Violaciones al derecho a beneficiarse del progreso científico y sus aplicaciones en términos de políticas públicas	
12130	12129	001090250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a beneficiarse del progreso científico y sus aplicaciones	
12131	12129	001090250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a beneficiarse del progreso científico y sus aplicaciones	
12132	12129	001090250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a beneficiarse del progreso científico y sus aplicaciones	
12133	12129	001090250020	Caso específico de no realización del derecho a beneficiarse del progreso científico y sus aplicaciones en términos de políticas públicas	
12134	11250	001090255	Violaciones al derecho a beneficiarse del progreso científico y sus aplicaciones en términos de legislación	
12135	12134	001090255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a beneficiarse del progreso científico y sus aplicaciones	
12136	12134	001090255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a beneficiarse del progreso científico y sus aplicaciones	
12137	12134	001090255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a beneficiarse del progreso científico y sus aplicaciones	
12138	12134	001090255020	Caso específico de no realización del derecho a beneficiarse del progreso científico y sus aplicaciones en términos de legislación	
12139	11250	001090260	Violaciones al derecho a beneficiarse del progreso científico y sus aplicaciones en términos de resoluciones judiciales	
12141	12139	001090260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a beneficiarse del progreso científico y sus aplicaciones	
12142	12139	001090260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a beneficiarse del progreso científico y sus aplicaciones	
12144	11046	001095250	Derecho a fundar una familia en términos de políticas públicas	
12146	11046	001095255	Derecho a fundar una familia en términos de legislación	
12147	11046	001095260	Derecho a fundar una familia en términos de resoluciones judiciales	
12148	11047	001100250	Derecho a la libertad de conciencia y religión en términos de políticas públicas	
12149	11047	001100255	Derecho a la libertad de conciencia y religión en términos de legislación	
12150	11047	001100260	Derecho a la libertad de conciencia y religión en términos de resoluciones judiciales	
12151	11251	001095250	Violaciones al derecho a fundar una familia en términos de políticas públicas	
12152	12151	001095250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a fundar una familia	
12153	12151	001095250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a fundar una familia	
12154	12151	001095250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a fundar una familia	
12155	12151	001095250020	Caso específico de no realización del derecho a fundar una familia en términos de políticas públicas	
12156	11251	001095255	Violaciones al derecho a fundar una familia en términos de legislación	
12157	12156	001095255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a fundar una familia	
12158	12156	001095255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a fundar una familia	
12159	12156	001095255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a fundar una familia	
12276	11054	001135255	Derecho a participar en los asuntos públicos en términos de legislación	
12160	12156	001095255020	Caso específico de no realización del derecho a fundar una familia en términos de legislación	
12161	11251	001095260	Violaciones al derecho a fundar una familia en términos de resoluciones judiciales	
12162	12161	001095260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a fundar una familia	
12163	12161	001095260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a fundar una familia	
12164	12161	001095260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a fundar una familia	
12165	12161	001095260020	Caso específico de no realización del derecho a fundar una familia en términos de resoluciones judiciales	
12166	11252	001100250	Violaciones al derecho a la libertad de conciencia y religión en términos de políticas públicas	
12167	12166	001100250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de conciencia y religión	
12168	12166	001100250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la libertad de conciencia y religión	
12169	12166	001100250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de conciencia y religión	
12170	12166	001100250020	Caso específico de no realización del derecho a la libertad de conciencia y religión en términos de políticas públicas	
12171	11252	001100255	Violaciones al derecho a la libertad de conciencia y religión en términos de legislación	
12172	12171	001100255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la libertad de conciencia y religión	
12173	12171	001100255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la libertad de conciencia y religión	
12174	12171	001100255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la libertad de conciencia y religión	
12175	12171	001100255020	Caso específico de no realización del derecho a la libertad de conciencia y religión en términos de legislación	
12176	11252	001100260	Violaciones al derecho a la libertad de conciencia y religión en términos de resoluciones judiciales	
12177	12176	001100260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de conciencia y religión	
12178	12176	001100260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la libertad de conciencia y religión	
12179	12176	001100260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de conciencia y religión	
12180	12176	001100260020	Caso específico de no realización del derecho a la libertad de conciencia y religión en términos de resoluciones judiciales	
12181	11253	001105005	Retenes	
12182	11253	001105250	Violaciones al derecho a la libertad de tránsito en términos de políticas públicas	
12183	12182	001105250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de tránsito	
12185	12182	001105250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la libertad de tránsito	
12186	12182	001105250020	Caso específico de no realización del derecho a la libertad de tránsito en términos de políticas públicas	
12187	11253	001105255	Violaciones al derecho a la libertad de tránsito en términos de legislación	
12188	12187	001105255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la libertad de tránsito	
12189	12187	001105255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la libertad de tránsito	
12190	12187	001105255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la libertad de tránsito	
12191	12187	001105255020	Caso específico de no realización del derecho a la libertad de tránsito en términos de legislación	
12192	11253	001105260	Violaciones al derecho a la libertad de tránsito en términos de resoluciones judiciales	
12193	12192	001105260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de tránsito	
12195	12192	001105260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de tránsito	
12196	12192	001105260020	Caso específico de no realización del derecho a la libertad de tránsito en términos de resoluciones judiciales	
12197	11254	001110250	Violaciones al derecho a la nacionalidad en términos de políticas públicas	
12198	12197	001110250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la nacionalidad	
12200	12197	001110250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la nacionalidad	
12201	12197	001110250020	Caso específico de no realización del derecho a la nacionalidad en términos de políticas públicas	
12202	11254	001110255	Violaciones al derecho a la nacionalidad en términos de legislación	
12203	12202	001110255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la nacionalidad	
12204	12202	001110255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la nacionalidad	
12205	12202	001110255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la nacionalidad	
12206	12202	001110255020	Caso específico de no realización del derecho a la nacionalidad en términos de legislación	
12207	11254	001110260	Violaciones al derecho a la nacionalidad en términos de resoluciones judiciales	
12208	12207	001110260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la nacionalidad	
12211	12207	001110260020	Caso específico de no realización del derecho a la nacionalidad en términos de resoluciones judiciales	
12212	11255	001115250	Violaciones al derecho de asilo en términos de políticas públicas	
12213	12212	001115250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de asilo	
12214	12212	001115250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de asilo	
11711	154	170	Reintegrado(a) al empleo	
12215	12212	001115250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de asilo	
12216	12212	001115250020	Caso específico de no realización del derecho de asilo en términos de políticas públicas	
12217	11255	001115255	Violaciones al derecho de asilo en términos de legislación	
12218	12217	001115255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de asilo	
12219	12217	001115255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de asilo	
12220	12217	001115255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho de asilo	
12221	12217	001115255020	Caso específico de no realización del derecho de asilo en términos de legislación	
12222	11255	001115260	Violaciones al derecho de asilo en términos de resoluciones judiciales	
12223	12222	001115260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de asilo	
12224	12222	001115260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de asilo	
12225	12222	001115260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de asilo	
12226	12222	001115260020	Caso específico de no realización del derecho de asilo en términos de resoluciones judiciales	
12227	11256	001120250	Violaciones al derecho de residencia en términos de políticas públicas	
12228	12227	001120250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de residencia	
12229	12227	001120250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de residencia	
12230	12227	001120250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de residencia	
12231	12227	001120250020	Caso específico de no realización del derecho de residencia en términos de políticas públicas	
12232	11256	001120255	Violaciones al derecho de residencia en términos de legislación	
12233	12232	001120255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de residencia	
12234	12232	001120255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de residencia	
12235	12232	001120255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho de residencia	
12236	12232	001120255020	Caso específico de no realización del derecho de residencia en términos de legislación	
12237	11256	001120260	Violaciones al derecho de residencia en términos de resoluciones judiciales	
12238	12237	001120260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de residencia	
12239	12237	001120260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de residencia	
12240	12237	001120260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de residencia	
12241	12237	001120260020	Caso específico de no realización del derecho de residencia en términos de resoluciones judiciales	
12242	11257	001125250	Violaciones al derecho a salir del país en términos de políticas públicas	
12244	12242	001125250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a salir del país	
12245	12242	001125250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a salir del país	
12246	12242	001125250020	Caso específico de no realización del derecho a salir del país en términos de políticas públicas	
12247	11257	001125255	Violaciones al derecho a salir del país en términos de legislación	
12249	12247	001125255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a salir del país	
12250	12247	001125255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a salir del país	
12251	12247	001125255020	Caso específico de no realización del derecho a salir del país en términos de legislación	
12252	11257	001125260	Violaciones al derecho a salir del país en términos de resoluciones judiciales	
12253	12252	001125260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a salir del país	
12254	12252	001125260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a salir del país	
12255	12252	001125260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a salir del país	
12256	12252	001125260020	Caso específico de no realización del derecho a salir del país en términos de resoluciones judiciales	
12257	11048	001105250	Derecho a la libertad de tránsito en términos de políticas públicas	
12258	11048	001105255	Derecho a la libertad de tránsito en términos de legislación	
12259	11048	001105260	Derecho a la libertad de tránsito en términos de resoluciones judiciales	
12260	11049	001110250	Derecho a la nacionalidad en términos de políticas públicas	
12261	11049	001110255	Derecho a la nacionalidad en términos de legislación	
12262	11049	001110260	Derecho a la nacionalidad en términos de resoluciones judiciales	
12263	11050	001115250	Derecho de asilo en términos de políticas públicas	
12264	11050	001115255	Derecho de asilo en términos de legislación	
12265	11050	001115260	Derecho de asilo en términos de resoluciones judiciales	
12266	11051	001120250	Derecho de residencia en términos de políticas públicas	
12267	11051	001120255	Derecho de residencia en términos de legislación	
12268	11051	001120260	Derecho de residencia en términos de resoluciones judiciales	
12269	11052	001125250	Derecho a salir del país en términos de políticas públicas	
12270	11052	001125255	Derecho a salir del país en términos de legislación	
12271	11052	001125260	Derecho a salir del país en términos de resoluciones judiciales	
12273	11053	001130255	Derecho a la no discriminación en términos de legislación	
12274	11053	001130260	Derecho a la no discriminación en términos de resoluciones judiciales	
12275	11054	001135250	Derecho a participar en los asuntos públicos en términos de políticas públicas	
11707	154	160	Refugiado(a)	
12277	11054	001135260	Derecho a participar en los asuntos públicos en términos de resoluciones judiciales	
12278	11055	001140250	Derecho a votar en términos de políticas públicas	
12279	11055	001140255	Derecho a votar en términos de legislación	
12280	11055	001140260	Derecho a votar en términos de resoluciones judiciales	
12281	11056	001145250	Derecho a postularse a cargos electivos en términos de políticas públicas	
12282	11056	001145255	Derecho a postularse a cargos electivos en términos de legislación	
12283	11056	001145260	Derecho a postularse a cargos electivos en términos de resoluciones judiciales	
12284	11057	001150250	Derecho a formar partidos políticos en términos de políticas públicas	
12285	11057	001150255	Derecho a formar partidos políticos en términos de legislación	
12286	11057	001150260	Derecho a formar partidos políticos en términos de resoluciones judiciales	
12287	11058	001155250	Derecho a militar en partidos políticos en términos de políticas públicas	
12288	11058	001155255	Derecho a militar en partidos políticos en términos de legislación	
12289	11058	001155260	Derecho a militar en partidos políticos en términos de resoluciones judiciales	
12290	11059	001160250	Derecho al acceso a la función pública en términos de políticas públicas	
12292	11059	001160260	Derecho al acceso a la función pública en términos de resoluciones judiciales	
12293	11060	001165250	Derecho a elecciones libres y democráticas en términos de políticas públicas	
12295	11060	001165260	Derecho a elecciones libres y democráticas en términos de resoluciones judiciales	
12296	11258	001130250	Violaciones al derecho a la no discriminación en términos de políticas públicas	
12297	12296	001130250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la no discriminación	
12298	12296	001130250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la no discriminación	
12299	12296	001130250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la no discriminación	
12300	12296	001130250020	Caso específico de no realización del derecho a la no discriminación en términos de políticas públicas	
12301	11258	001130255	Violaciones al derecho a la no discriminación en términos de legislación	
12302	12301	001130255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la no discriminación	
12303	12301	001130255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la no discriminación	
12304	12301	001130255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la no discriminación	
12305	12301	001130255020	Caso específico de no realización del derecho a la no discriminación en términos de legislación	
12306	11258	001130260	Violaciones al derecho a la no discriminación en términos de resoluciones judiciales	
12308	12306	001130260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la no discriminación	
12309	12306	001130260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la no discriminación	
12311	11259	001135250	Violaciones al derecho a participar en los asuntos públicos en términos de políticas públicas	
12313	12311	001135250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a participar en los asuntos públicos	
12314	12311	001135250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a participar en los asuntos públicos	
12315	12311	001135250020	Caso específico de no realización del derecho a participar en los asuntos públicos en términos de políticas públicas	
12316	11259	001135255	Violaciones al derecho a participar en los asuntos públicos en términos de legislación	
12317	12316	001135255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a participar en los asuntos públicos a participar en los asuntos públicos	
12318	12316	001135255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a participar en los asuntos públicos	
12319	12316	001135255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a participar en los asuntos públicos	
12320	12316	001135255020	Caso específico de no realización del derecho a participar en los asuntos públicos en términos de legislación	
12321	11259	001135260	Violaciones al derecho a participar en los asuntos públicos en términos de resoluciones judiciales	
12322	12321	001135260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a participar en los asuntos públicos	
12323	12321	001135260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a participar en los asuntos públicos	
12324	12321	001135260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a participar en los asuntos públicos	
12325	12321	001135260020	Caso específico de no realización del derecho a participar en los asuntos públicos en términos de resoluciones judiciales	
12326	11260	001140250	Violaciones al derecho a votar en términos de políticas públicas	
12327	12326	001140250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a votar	
12328	12326	001140250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a votar	
12329	12326	001140250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a votar	
12331	11260	001140255	Violaciones al derecho a votar en términos de legislación	
12332	12331	001140255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a votar	
12333	12331	001140255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a votar	
12334	12331	001140255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a votar	
12335	12331	001140255020	Caso específico de no realización del derecho a votar en términos de legislación	
12336	11260	001140260	Violaciones al derecho a votar en términos de resoluciones judiciales	
12337	12336	001140260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a votar	
12338	12336	001140260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a votar	
12339	12336	001140260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a votar	
12340	12336	001140260020	Caso específico de no realización del derecho a votar en términos de resoluciones judiciales	
12341	11261	001145250	Violaciones al derecho a postularse a cargos electivos en términos de políticas públicas	
12342	12341	001145250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a postularse a cargos electivos	
12343	12341	001145250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a postularse a cargos electivos	
12344	12341	001145250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a postularse a cargos electivos	
12345	12341	001145250020	Caso específico de no realización del derecho a postularse a cargos electivos en términos de políticas públicas	
12346	11261	001145255	Violaciones al derecho a postularse a cargos electivos en términos de legislación	
12347	12346	001145255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a postularse a cargos electivos	
12348	12346	001145255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a postularse a cargos electivos	
12349	12346	001145255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a postularse a cargos electivos	
12350	12346	001145255020	Caso específico de no realización del derecho a postularse a cargos electivos en términos de legislación	
12351	11261	001145260	Violaciones al derecho a postularse a cargos electivos en términos de resoluciones judiciales	
12352	12351	001145260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a postularse a cargos electivos	
12354	12351	001145260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a postularse a cargos electivos	
12355	12351	001145260020	Caso específico de no realización del derecho a postularse a cargos electivos en términos de resoluciones judiciales	
12356	11262	001150250	Violaciones al derecho a formar partidos políticos en términos de políticas públicas	
12357	12356	001150250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a formar partidos políticos	
12358	12356	001150250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a formar partidos políticos	
12359	12356	001150250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a formar partidos políticos	
12361	11262	001150255	Violaciones al derecho a formar partidos políticos en términos de legislación	
12362	12361	001150255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a formar partidos políticos	
12363	12361	001150255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a formar partidos políticos	
12364	12361	001150255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a formar partidos políticos	
12365	12361	001150255020	Caso específico de no realización del derecho a formar partidos políticos en términos de legislación	
12366	11262	001150260	Violaciones al derecho a formar partidos políticos en términos de resoluciones judiciales	
12367	12366	001150260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a formar partidos políticos	
12368	12366	001150260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a formar partidos políticos	
12369	12366	001150260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a formar partidos políticos	
12370	12366	001150260020	Caso específico de no realización del derecho a formar partidos políticos en términos de resoluciones judiciales	
12371	11263	001155250	Violaciones al derecho a militar en partidos políticos en términos de políticas públicas	
12372	12371	001155250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a militar en partidos políticos	
12382	12381	001155260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a militar en partidos políticos	
12383	12381	001155260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a militar en partidos políticos	
12384	12381	001155260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a militar en partidos políticos	
12385	12381	001155260020	Caso específico de no realización del derecho a militar en partidos políticos en términos de resoluciones judiciales	
12386	11264	001160250	Violaciones al derecho al acceso a la función pública en términos de políticas públicas	
12387	12386	001160250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho al acceso a la función pública	
12388	12386	001160250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho al acceso a la función pública	
12389	12386	001160250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho al acceso a la función pública	
12390	12386	001160250020	Caso específico de no realización del derecho al acceso a la función pública  en términos de políticas públicas	
12391	11264	001160255	Violaciones al derecho al acceso a la función pública en términos de legislación	
12392	12391	001160255005	Falta de adopción de legislación que respete, proteja y garantice el derecho al acceso a la función pública	
12393	12391	001160255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho al acceso a la función pública	
12394	12391	001160255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho al acceso a la función pública	
12395	12391	001160255020	Caso específico de no realización del derecho al acceso a la función pública en términos de legislación	
11701	154	155	Prófugo(a)	
12396	11264	001160260	Violaciones al derecho al acceso a la función pública en términos de resoluciones judiciales	
12397	12396	001160260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a la función pública	
12398	12396	001160260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho al acceso a la función pública	
12399	12396	001160260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a la función pública	
12400	12396	001160260020	Caso específico de no realización del derecho al acceso a la función pública en términos de resoluciones judiciales	
12401	11265	001165250	Violaciones al derecho a elecciones libres y democráticas en términos de políticas públicas	
12402	12401	001165250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a elecciones libres y democráticas	
12403	12401	001165250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a elecciones libres y democráticas	
12404	12401	001165250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a elecciones libres y democráticas	
12405	12401	001165250020	Caso específico de no realización del derecho a elecciones libres y democráticas en términos de políticas públicas	
12406	11265	001165255	Violaciones al derecho a elecciones libres y democráticas en términos de legislación a elecciones libres y democráticas	
12408	12406	001165255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a elecciones libres y democráticas	
12409	12406	001165255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a elecciones libres y democráticas	
12410	12406	001165255020	Caso específico de no realización del derecho a elecciones libres y democráticas en términos de legislación	
12411	11265	001165260	Violaciones al derecho a elecciones libres y democráticas en términos de resoluciones judiciales	
12412	12411	001165260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a elecciones libres y democráticas	
12414	12411	001165260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a elecciones libres y democráticas	
12415	12411	001165260020	Caso específico de no realización del derecho a elecciones libres y democráticas en términos de resoluciones judiciales	
12420	53	640	Transgénicos	
12421	53	430	Pobreza	
12430	53	050	Comisión Nacional de los Derechos Humanos - CNDH	
12433	53	060	Comisiones estatales de derechos humanos	
12435	53	080	Corrupción	
12441	5429	001005	Activista social	
12443	5429	001030	Combatiente	
12487	5431	002005	Afiliación a cooperativa	
12488	5431	002010	Afiliación a grupo de oposición armada	
12489	5431	002015	Afiliación a grupo o movimiento de resistencia civil	
12490	5431	002020	Afiliación a grupo religioso	
12491	5431	002025	Afiliación a movimiento de expresión cultural	
12492	5431	002030	Afiliación a movimiento político	
12493	5431	002035	Afiliación a movimiento social	
12494	5431	002040	Afiliación a organización campesina	
12496	5431	002050	Afiliación a organización de derechos humanos	
12497	5431	002055	Afiliación a organización de mujeres	
12498	5431	002060	Afiliación a organización ecologista	
12499	5431	002065	Afiliación a organización empresarial	
12500	5431	002070	Afiliación a organización estudiantil	
12501	5431	002075	Afiliación a organización indígena	
12502	5431	002080	Afiliación a partido o grupo político	
12503	5431	002085	Afiliación a sindicato	
12504	54	003	Características del grupo	
12522	160	001003	Cómplice pasivo en el acto	
12523	160	001004	Confirmado que estuvo presente durante la ejecución del acto	
12524	160	001005	Planeó el acto	
12525	160	001006	Se sospecha que está involucrado en el acto	
12533	159	005	Involucramiento de agentes del Estado por no brindar protección	
12534	12533	005001	No ejercicio de la autoridad sobre sus subordinados	
12535	12533	005002	Inactividad ante el conocimiento de que sus subordinados planeaban llevar a cabo un acto ilegal	
12536	12533	005003	No tomó las medidas necesarias para prevenir que se cometiera un acto ilegal	
12537	159	006	Involucramiento en términos de responsabilidad política general	
12538	11729	000	Legislación federal	
12539	12538	000001	Constitución Política de los Estados Unidos Mexicanos	
12540	12538	000002	Ley Federal	
12541	12538	000003	Código Federal	
12542	12538	000004	Reglamento, decreto federal	
12545	12544	033001	Constitución Política del Estado	
12546	12544	033002 	Ley del Estado	
12547	12544	033003	Código del Estado	
12548	12544	033004	Reglamento, decreto del Estado	
12550	11729	070	Derecho consuetudinario	
12551	12550	070001	Usos y costumbres	
12552	12550	070002	Reglamentos de comunidades	
12580	142	012	Lugar de vialidad	
12610	75	003	Relaciones de empleo	
12617	75	004	Relaciones entre entidades	
12623	11061	002005250	Derecho a la educación en términos de políticas públicas	
12624	11061	002005255	Derecho a la educación en términos de legislación	
12625	11061	002005260	Derecho a la educación en términos de resoluciones judiciales	
12626	11062	002010010	Derecho al consentimiento informado en tratamientos médicos	
13000	11062	002010250	Derecho a la salud en términos de políticas públicas	
13001	11062	002010255	Derecho a la salud en términos de legislación	
13002	11062	002010260	Derecho a la salud en términos de resoluciones judiciales	
13003	11069	002015250	Derecho al trabajo en términos de políticas públicas	
13004	11069	002015255	Derecho al trabajo en términos de legislación	
13005	11069	002015260	Derecho al trabajo en términos de resoluciones judiciales	
155	154	140	Muerto(a)	
13008	11070	002020255	Derecho a la alimentación adecuada en términos de legislación	
13009	11070	002020260	Derecho a la alimentación adecuada en términos de resoluciones judiciales	
13010	11071	002025250	Derecho a la vivienda adecuada en términos de políticas públicas	
13011	11071	002025255	Derecho a la vivienda adecuada en términos de legislación	
13012	11071	002025260	Derecho a la vivienda adecuada en términos de resoluciones judiciales	
13013	11072	002030250	Derecho a un medio ambiente sano en términos de políticas públicas	
13014	11072	002030255	Derecho a un medio ambiente sano en términos de legislación	
13015	11072	002030260	Derecho a un medio ambiente sano en términos de resoluciones judiciales	
13016	11073	002035250	Derecho a las prestaciones de seguridad social en términos de políticas públicas	
13017	11073	002035255	Derecho a las prestaciones de seguridad social en términos de legislación	
13018	11073	002035260	Derecho a las prestaciones de seguridad social en términos de resoluciones judiciales	
13020	11074	002040255	Derecho al acceso a los servicios públicos en términos de legislación	
13021	11074	002040260	Derecho al acceso a los servicios públicos en términos de resoluciones judiciales	
13022	11075	002045250	Derecho a la cultura en términos de políticas públicas	
13023	11075	002045255	Derecho a la cultura en términos de legislación	
13024	11075	002045260	Derecho a la cultura en términos de resoluciones judiciales	
13026	11078	002050255	Derecho al acceso a la propiedad pública en términos de legislación	
13027	11078	002050260	Derecho al acceso a la propiedad pública en términos de resoluciones judiciales	
13028	11079	002055250	Derecho a la propiedad en términos de políticas públicas	
13029	11079	002055255	Derecho a la propiedad en términos de legislación	
13030	11079	002055260	Derecho a la propiedad en términos de resoluciones judiciales	
13031	11267	002005005	Cuotas escolares prohibitivas	
13032	11267	002005010	Condiciones inadecuadas de escuelas y salones de clase	
13033	11267	002005015	Ubicación de la escuela a gran distancia de la casa del o la estudiante	
13034	11267	002005020	Alto número de alumnos por maestro	
13035	11267	002005250	Violaciones al derecho a la educación en términos de políticas públicas	
13036	11267	002005255	Violaciones al derecho a la educación en términos de legislación	
13037	11267	002005260	Violaciones al derecho a la educación en términos de resoluciones judiciales	
13038	11268	002010010	Violaciones al derecho al consentimiento informado en tratamientos médicos	
13039	11268	002010015	Costos prohibitivos de la atención médica	
13040	11268	002010020	Negación de subsidio a los servicios para personas que no pueden pagar la atención primaria a la salud	
13041	11268	002010025	Atención primaria de salud no proporcionada a comunidades específicas	
13042	11268	002010030	Negación del tratamiento adecuado	
13043	11268	002010250	Violaciones al derecho a la salud en términos de políticas públicas	
13044	11268	002010255	Violaciones al derecho a la salud en términos de legislación	
13045	11268	002010260	Violaciones al derecho a la salud en términos de resoluciones judiciales	
13046	11275	002015250	Violaciones al derecho al trabajo en términos de políticas públicas	
13047	11275	002015255	Violaciones al derecho al trabajo en términos de legislación	
13048	11275	002015260	Violaciones al derecho al trabajo en términos de resoluciones judiciales	
13049	11276	002020250	Violaciones al derecho a la alimentación adecuada en términos de políticas públicas	
13051	13035	002005250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la educación	
13052	13035	002005250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la educación	
13053	13035	002005250020	Caso específico de no realización del derecho a la educación en términos de políticas públicas	
13054	13036	002005255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la educación	
13055	13036	002005255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la educación	
13056	13036	002005255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la educación	
13057	13036	002005255020	Caso específico de no realización del derecho a la educación en términos de legislación	
13058	13037	002005260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la educación	
13059	13037	002005260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la educación	
13060	13037	002005260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la educación	
13061	13037	002005260020	Caso específico de no realización del derecho a la educación en términos de resoluciones judiciales	
13062	13043	002010250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la salud	
13063	13043	002010250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la salud	
13064	13043	002010250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la salud	
13065	13043	002010250020	Caso específico de no realización del derecho a la salud en términos de políticas públicas	
13066	13044	002010255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la salud	
13067	13044	002010255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la salud	
13068	13044	002010255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la salud	
13069	13044	002010255020	Caso específico de no realización del derecho a la salud en términos de legislación	
13070	13045	002010260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la salud	
13071	13045	002010260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la salud	
13255	13254	003027005	Derecho de las personas sentenciadas a los beneficios de la preliberación	
13072	13045	002010260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la salud	
13073	13045	002010260020	Caso específico de no realización del derecho a la salud en términos de resoluciones judiciales	
13074	13046	002015250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho al trabajo	
13076	13046	002015250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho al trabajo	
13077	13046	002015250020	Caso específico de no realización del derecho al trabajo en términos de políticas públicas	
13078	13047	002015255005	Falta de adopción de legislación que respete, proteja y garantice el derecho al trabajo	
13080	13047	002015255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho al trabajo	
13081	13047	002015255020	Caso específico de no realización del derecho al trabajo en términos de legislación	
13082	13048	002015260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho al trabajo	
13083	13048	002015260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho al trabajo	
13085	13048	002015260020	Caso específico de no realización del derecho al trabajo en términos de resoluciones judiciales	
13086	13049	002020250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la alimentación adecuada	
13087	13049	002020250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la alimentación adecuada	
13088	13049	002020250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la alimentación adecuada	
13089	13049	002020250020	Caso específico de no realización del derecho a la alimentación adecuada en términos de políticas públicas	
13090	11276	002020255	Violaciones al derecho a la alimentación adecuada en términos de legislación	
13091	13090	002020255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la alimentación adecuada	
13092	13090	002020255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la alimentación adecuada	
13093	13090	002020255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la alimentación adecuada	
13094	13090	002020255020	Caso específico de no realización del derecho a la alimentación adecuada en términos de legislación	
13095	11276	002020260	Violaciones al derecho a la alimentación adecuada en términos de resoluciones judiciales	
13096	13095	002020260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la alimentación adecuada	
13097	13095	002020260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la alimentación adecuada	
13098	13095	002020260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la alimentación adecuada	
13099	13095	002020260020	Caso específico de no realización del derecho a la alimentación adecuada en términos de resoluciones judiciales	
13101	11277	002025010	Negación de escrituras de vivienda	
13103	11277	002025250	Violaciones al derecho a la vivienda adecuada en términos de políticas públicas	
13104	13103	002025250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la vivienda adecuada	
13105	13103	002025250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la vivienda adecuada	
13106	13103	002025250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la vivienda adecuada	
13107	13103	002025250020	Caso específico de no realización del derecho a la vivienda adecuada en términos de políticas públicas	
13108	11277	002025255	Violaciones al derecho a la vivienda adecuada en términos de legislación	
13109	13108	002025255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la vivienda adecuada	
13110	13108	002025255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la vivienda adecuada	
13111	13108	002025255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la vivienda adecuada	
13112	13108	002025255020	Caso específico de no realización del derecho a la vivienda adecuada en términos de legislación a la vivienda adecuada	
13113	11277	002025260	Violaciones al derecho a la vivienda adecuada en términos de resoluciones judiciales	
13114	13113	002025260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a  la vivienda adecuada	
13115	13113	002025260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la vivienda adecuada	
13116	13113	002025260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la vivienda adecuada	
13117	13113	002025260020	Caso específico de no realización del derecho a la vivienda adecuada en términos de resoluciones judiciales	
13118	11278	002030005	Contaminación	
13119	11278	002030010	Exposición a sustancias peligrosas	
13120	11278	002030250	Violaciones al derecho a un medio ambiente sano en términos de políticas públicas	
13121	13120	002030250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a un medio ambiente sano	
13122	13120	002030250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a un medio ambiente sano	
13123	13120	002030250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a un medio ambiente sano	
13124	13120	002030250020	Caso específico de no realización del derecho a un medio ambiente sano en términos de políticas públicas	
13125	11278	002030255	Violaciones al derecho a un medio ambiente sano en términos de legislación	
13126	13125	002030255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a un medio ambiente sano	
13127	13125	002030255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a un medio ambiente sano	
11703	154	135	Liberado(a)	
13128	13125	002030255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a un medio ambiente sano	
13129	13125	002030255020	Caso específico de no realización del derecho a un medio ambiente sano en términos de legislación	
13130	11278	002030260	Violaciones al derecho a un medio ambiente sano en términos de resoluciones judiciales	
13131	13130	002030260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a un medio ambiente sano	
13133	13130	002030260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a un medio ambiente sano	
13134	13130	002030260020	Caso específico de no realización del derecho a un medio ambiente sano en términos de resoluciones judiciales	
13135	11279	002035250	Violaciones al derecho a las prestaciones de seguridad social en términos de políticas públicas	
13136	13135	002035250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a las prestaciones de seguridad social	
13137	13135	002035250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a las prestaciones de seguridad social	
13138	13135	002035250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a las prestaciones de seguridad social	
13139	13135	002035250020	Caso específico de no realización del derecho a las prestaciones de seguridad social en términos de políticas públicas	
13140	11279	002035255	Violaciones al derecho a las prestaciones de seguridad social en términos de legislación	
13141	13140	002035255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a las prestaciones de seguridad social	
13142	13140	002035255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a las prestaciones de seguridad social	
13143	13140	002035255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a las prestaciones de seguridad social	
13144	13140	002035255020	Caso específico de no realización del derecho a las prestaciones de seguridad social en términos de legislación	
13145	11279	002035260	Violaciones al derecho a las prestaciones de seguridad social en términos de resoluciones judiciales	
13146	13145	002035260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a las prestaciones de seguridad social	
13147	13145	002035260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a las prestaciones de seguridad social	
13148	13145	002035260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a las prestaciones de seguridad social	
13149	13145	002035260020	Caso específico de no realización del derecho a las prestaciones de seguridad social en términos de resoluciones judiciales	
13150	11280	002040250	Violaciones al derecho al acceso a los servicios públicos en términos de políticas públicas	
13151	13150	002040250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho al acceso a los servicios públicos	
13152	13150	002040250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho al acceso a los servicios públicos	
13153	13150	002040250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho al acceso a los servicios públicos	
13154	13150	002040250020	Caso específico de no realización del derecho al acceso a los servicios públicos en términos de políticas públicas	
13155	11280	002040255	Violaciones al derecho al acceso a los servicios públicos en términos de legislación	
13156	13155	002040255005	Falta de adopción de legislación que respete, proteja y garantice el derecho al acceso a los servicios públicos	
13158	13155	002040255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho al acceso a los servicios públicos	
13159	13155	002040255020	Caso específico de no realización del derecho al acceso a los servicios públicos en términos de legislación	
13160	11280	002040260	Violaciones al derecho al acceso a los servicios públicos en términos de resoluciones judiciales	
13161	13160	002040260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a los servicios públicos	
13162	13160	002040260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho al acceso a los servicios públicos	
13163	13160	002040260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a los servicios públicos	
13164	13160	002040260020	Caso específico de no realización del derecho al acceso a los servicios públicos en términos de resoluciones judiciales	
13165	11281	002045250	Violaciones al derecho a la cultura en términos de políticas públicas	
13166	13165	002045250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la cultura	
13167	13165	002045250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la cultura	
13168	13165	002045250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la cultura	
13169	13165	002045250020	Caso específico de no realización del derecho a la cultura en términos de políticas públicas	
13170	11281	002045255	Violaciones al derecho a la cultura en términos de legislación	
13171	13170	002045255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la cultura	
13172	13170	002045255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la cultura	
13173	13170	002045255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la cultura	
13174	13170	002045255020	Caso específico de no realización del derecho a la cultura en términos de legislación	
13175	11281	002045260	Violaciones al derecho a la cultura en términos de resoluciones judiciales	
13176	13175	002045260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la cultura	
13177	13175	002045260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la cultura	
13256	13254	003027010	Derecho de las personas sentenciadas a un trabajo productivo y apropiado	
13178	13175	002045260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la cultura	
13179	13175	002045260020	Caso específico de no realización del derecho a la cultura en términos de resoluciones judiciales	
13182	13180	002050250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho al acceso a la propiedad pública	
13183	13180	002050250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho al acceso a la propiedad pública	
13184	13180	002050250020	Caso específico de no realización del derecho al acceso a la propiedad pública en términos de políticas públicas	
13185	11284	002050255	Violaciones al derecho al acceso a la propiedad pública en términos de legislación	
13186	13185	002050255005	Falta de adopción de legislación que respete, proteja y garantice el derecho al acceso a la propiedad pública	
13187	13185	002050255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho al acceso a la propiedad pública	
13188	13185	002050255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho al acceso a la propiedad pública	
13189	13185	002050255020	Caso específico de no realización del derecho al acceso a la propiedad pública en términos de legislación	
13191	11284	002050260	Violaciones al derecho al acceso a la propiedad pública en términos de resoluciones judiciales	
13192	13191	002050260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a la propiedad pública	
13193	13191	002050260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho al acceso a la propiedad pública	
13194	13191	002050260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a la propiedad pública	
13195	13191	002050260020	Caso específico de no realización del derecho al acceso a la propiedad pública en términos de resoluciones judiciales	
13196	11285	002055005	Negación de título de propiedad de la tierra	
13197	11285	002055010	Expropiación arbitraria	
13198	11285	002055250	Violaciones al derecho a la propiedad en términos de políticas públicas	
13199	13198	002055250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la propiedad	
13200	13198	002055250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la propiedad	
13201	13198	002055250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la propiedad	
13202	13198	002055250020	Caso específico de no realización del derecho a la propiedad en términos de políticas públicas	
13203	11285	002055255	Violaciones al derecho a la propiedad en términos de legislación	
13204	13203	002055255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la propiedad	
13205	13203	002055255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la propiedad	
13206	13203	002055255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la propiedad	
13207	13203	002055255020	Caso específico de no realización del derecho a la propiedad en términos de legislación	
13208	11285	002055260	Violaciones al derecho a la propiedad en términos de resoluciones judiciales	
13209	13208	002055260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la propiedad	
13210	13208	002055260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la propiedad	
13211	13208	002055260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la propiedad	
13212	13208	002055260020	Caso específico de no realización del derecho a la propiedad en términos de resoluciones judiciales	
13213	11080	003005250	Derechos de las mujeres en términos de políticas públicas	
13215	11080	003005255	Derechos de las mujeres en términos de legislación	
13216	11080	003005260	Derechos de las mujeres en términos de resoluciones judiciales	
13221	11095	003015255	Derechos de las y los migrantes en términos de legislación	
13222	11095	003015260	Derechos de las y los migrantes en términos de resoluciones judiciales	
13223	11101	003020250	Derechos de los y las trabajadore(a)s en términos de políticas públicas	
13224	11101	003020255	Derechos de los y las trabajadore(a)s en términos de legislación	
13225	11101	003020260	Derechos de los y las trabajadore(a)s en términos de resoluciones judiciales	
13227	18	003025255	Derechos de las personas privadas de la libertad  en términos de legislación	
13229	11112	003030250	Derechos de las personas LGBT en términos de políticas públicas	
13230	11112	003030255	Derechos de las personas LGBT en términos de legislación	
13231	11112	003030260	Derechos de las personas LGBT en términos de resoluciones judiciales	
13233	11114	003035250	Derechos de las niñas y los niños en términos de políticas públicas	
13234	11114	003035255	Derechos de las niñas y los niños en términos de legislación	
13235	11114	003035260	Derechos de las niñas y los niños en términos de resoluciones judiciales	
13236	11119	003040250	Derechos de las personas con discapacidad en términos de políticas públicas	
13237	11119	003040255	Derechos de las personas con discapacidad en términos de legislación	
13238	11119	003040260	Derechos de las personas con discapacidad en términos de resoluciones judiciales	
13239	11124	003045250	Derechos de las personas adultas mayores en términos de políticas públicas	
13240	11124	003045255	Derechos de las personas adultas mayores en términos de legislación	
13241	11124	003045260	Derechos de las personas adultas mayores en términos de resoluciones judiciales	
13242	11126	003050250	Derechos de las y los extranjero(a)s en términos de políticas públicas	
13243	11126	003050255	Derechos de las y los extranjero(a)s en términos de legislación	
13244	11126	003050260	Derechos de las y los extranjero(a)s en términos de resoluciones judiciales	
13245	11129	003055255	Derechos de las personas desplazadas en términos de legislación	
13254	17	003027	Derechos de las personas sentenciadas	
13257	13254	003027250	Derechos de las personas sentenciadas en términos de políticas públicas	
13258	13254	003027255	Derechos de las personas sentenciadas en términos de legislación	
13259	13254	003027260	Derechos de las personas sentenciadas en términos de resoluciones judiciales	
13262	13260	003005250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las mujeres	
13263	13260	003005250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las mujeres	
13264	13260	003005250020	Caso específico de no realización de los derechos de las mujeres en términos de políticas públicas	
13266	13265	003005255005	Falta de adopción de legislación que respete, proteja y garanticen los derechos de las mujeres	
13267	13265	003005255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las mujeres	
13268	13265	003005255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las mujeres	
13269	13265	003005255020	Caso específico de no realización de los derechos de las mujeres en términos de legislación	
13271	13270	003005260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las mujeres	
13272	13270	003005260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las mujeres	
13273	13270	003005260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las mujeres	
13274	13270	003005260020	Caso específico de no realización de los derechos de las mujeres en términos de resoluciones judiciales	
13290	11307	003015250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las y los migrantes 	
13291	11307	003015250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las y los migrantes	
13292	11307	003015250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las y los migrantes	
13293	11307	003015250020	Caso específico de no realización de los derechos de las y los migrantes en términos de políticas públicas	
13294	11302	003015255	Violaciones a los derechos de las y los migrantes en términos de legislación	
13295	13294	003015255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las y los migrantes	
13296	13294	003015255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las y los migrantes	
13297	13294	003015255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las y los migrantes	
13298	13294	003015255020	Caso específico de no realización de derechos de las y los migrantes en términos de legislación	
13299	11302	003015260	Violaciones a los derechos de las y los migrantes en términos de resoluciones judiciales	
13300	13299	003015260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las y los migrantes	
13301	13299	003015260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las y los migrantes	
13302	13299	003015260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las y los migrantes	
13303	13299	003015260020	Caso específico de no realización de los derechos de las y los migrantes en términos de resoluciones judiciales	
13304	11308	003020005	No pago de salarios	
13305	11308	003020010	Negación del descanso, del tiempo libre y de la limitación razonable de la jornada laboral	
13306	11308	003020015	Negación de vacaciones periódicas con goce de sueldo	
13307	11308	003020020	Despido injustificado	
13308	11308	003020025	Negación de indemnización por despido injustificado	
13309	11308	003020030	Violaciones al derecho de los y las trabajadore(a)s a la sindicación	
13310	11308	003020035	Violaciones al derecho de los y las trabajadore(a)s a la democracia sindical	
13311	11308	003020040	Violaciones al derecho de los y las trabajadore(a)s a la huelga	
13314	13313	003020250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de los y las trabajadore(a)s	
13315	13313	003020250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de los y las trabajadore(a)s	
13316	13313	003020250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de los y las trabajadore(a)s	
13317	13313	003020250020	Caso específico de no realización de los derechos de los y las trabajadore(a)s en términos de políticas públicas	
13318	11308	003020255	Violaciones a los derechos de los y las trabajadore(a)s en términos de legislación	
13319	13318	003020255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de los y las trabajadore(a)s	
13320	13318	003020255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de los y las trabajadore(a)s	
13321	13318	003020255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de los y las trabajadore(a)s	
13322	13318	003020255020	Caso específico de no realización de los derechos de los y las trabajadore(a)s en términos de legislación	
13323	11308	003020260	Violaciones a los derechos de los y las trabajadore(a)s en términos de resoluciones judiciales	
13324	13323	003020260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de los y las trabajadore(a)s	
13325	13323	003020260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de los y las trabajadore(a)s	
13327	13323	003020260020	Caso específico de no realización de los derechos de los y las trabajadore(a)s en términos de resoluciones judiciales	
13328	11314	003025250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las personas privadas de la libertad	
13329	11314	003025250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las personas privadas de la libertad	
13505	13501	002027255020	Caso específico de no realización del derecho al agua en términos de legislación	
13330	11314	003025250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las personas privadas de la libertad	
13331	11314	003025250020	Caso específico de no realización de los derechos de las personas privadas de la libertad  en términos de políticas públicas	
13332	11313	003025255	Violaciones a los derechos de las personas privadas de la libertad  en términos de legislación	
13333	13332	003025255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las personas privadas de la libertad	
13334	13332	003025255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las personas privadas de la libertad	
13335	13332	003025255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las personas privadas de la libertad	
13336	13332	003025255020	Caso específico de no realización de los derechos de las personas privadas de la libertad en términos de legislación	
13337	11313	003025260	Violaciones a los derechos de las personas privadas de la libertad en términos de resoluciones judiciales	
13338	13337	003025260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas privadas de la libertad	
13339	13337	003025260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las personas privadas de la libertad 	
13340	13337	003025260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas privadas de la libertad	
13341	13337	003025260020	Caso específico de no realización de los derechos de las personas privadas de la libertad en términos de resoluciones judiciales	
13342	11320	003030250	Violaciones al derechos de las personas LGBT en términos de políticas públicas	
13343	13342	003030250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las personas LGBT	
13344	13342	003030250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las personas LGBT	
13345	13342	003030250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las personas LGBT	
13346	13342	003030250020	Caso específico de no realización de los derechos de las personas LGBT en términos de políticas públicas	
13347	11320	003030255	Violaciones al derechos de las personas LGBT en términos de legislación	
13348	13347	003030255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las personas LGBT	
13349	13347	003030255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las personas LGBT	
13350	13347	003030255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las personas LGBT	
13351	13347	003030255020	Caso específico de no realización de los derechos de las personas LGBT en términos de legislación	
13352	11320	003030260	Violaciones al derechos de las personas LGBT en términos de resoluciones judiciales	
13353	13352	003030260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas LGBT	
13354	13352	003030260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las personas LGBT	
13355	13352	003030260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas LGBT	
13356	13352	003030260020	Caso específico de no realización de los derechos de las personas LGBT en términos de resoluciones judiciales	
13358	11322	003035250	Violaciones a los derechos de las niñas y los niños en términos de políticas públicas	
13359	13358	003035250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las niñas y los niños	
13361	13358	003035250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las niñas y los niños	
13362	13358	003035250020	Caso específico de no realización de los derechos de las niñas y los niños en términos de políticas públicas	
13363	11322	003035255	Violaciones a los derechos de las niñas y los niños en términos de legislación	
13364	13363	003035255005	Falta de adopción de legislación que respete, proteja y garantice de los derechos de las niñas y los niños	
13365	13363	003035255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las niñas y los niños	
13366	13363	003035255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las niñas y los niños	
13367	13363	003035255020	Caso específico de no realización de los derechos de las niñas y los niños en términos de legislación	
13368	11322	003035260	Violaciones a los derechos de las niñas y los niños en términos de resoluciones judiciales	
13369	13368	003035260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las niñas y los niños	
13370	13368	003035260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las niñas y los niños	
13371	13368	003035260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las niñas y los niños	
13372	13368	003035260020	Caso específico de no realización de los derechos de las niñas y los niños en términos de resoluciones judiciales	
13373	11327	003040250	Violaciones a los derechos de las personas con discapacidad en términos de políticas públicas	
13375	13373	003040250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las personas con discapacidad	
13376	13373	003040250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las personas con discapacidad	
13377	13373	003040250020	Caso específico de no realización de los derechos de las personas con discapacidad en términos de políticas públicas	
13378	11327	003040255	Violaciones a los derechos de las personas con discapacidad en términos de legislación	
13379	13378	003040255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las personas con discapacidad	
13380	13378	003040255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las personas con discapacidad	
13381	13378	003040255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las personas con discapacidad	
13382	13378	003040255020	Caso específico de no realización de los derechos de las personas con discapacidad en términos de legislación	
13383	11327	003040260	Violaciones a los derechos de las personas con discapacidad en términos de resoluciones judiciales	
13384	13383	003040260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas con discapacidad	
13385	13383	003040260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las personas con discapacidad	
13386	13383	003040260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas con discapacidad	
13387	13383	003040260020	Caso específico de no realización de los derechos de las personas con discapacidad en términos de resoluciones judiciales	
13388	11332	003045250	Violaciones a los derechos de las personas adultas mayores en términos de políticas públicas	
13389	13388	003045250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las personas adultas mayores	
13391	13388	003045250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las personas adultas mayores	
13392	13388	003045250020	Caso específico de no realización de los derechos de las personas adultas mayores en términos de políticas públicas	
13393	11332	003045255	Violaciones a los derechos de las personas adultas mayores en términos de legislación	
13394	13393	003045255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las personas adultas mayores	
13395	13393	003045255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las personas adultas mayores	
13396	13393	003045255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las personas adultas mayores	
13397	13393	003045255020	Caso específico de no realización de los derechos de las personas adultas mayores en términos de legislación	
13398	11332	003045260	Violaciones a los derechos de las personas adultas mayores en términos de resoluciones judiciales	
13399	13398	003045260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas adultas mayores	
13400	13398	003045260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las personas adultas mayores	
13401	13398	003045260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas adultas mayores	
13402	13398	003045260020	Caso específico de no realización de los derechos de las personas adultas mayores en términos de resoluciones judiciales	
13405	11334	003050250	Violaciones a los derechos de las y los extranjero(a)s en términos de políticas públicas	
13406	13405	003050250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las y los extranjero(a)s	
13407	13405	003050250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las y los extranjero(a)s	
13408	13405	003050250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las y los extranjero(a)s	
13409	13405	003050250020	Caso específico de no realización de los derechos de las y los extranjero(a)s en términos de políticas públicas	
13410	11334	003050255	Violaciones a los derechos de las y los extranjero(a)s en términos de legislación	
13411	13410	003050255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las y los extranjero(a)s	
13412	13410	003050255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las y los extranjero(a)s	
13413	13410	003050255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las y los extranjero(a)s	
13414	13410	003050255020	Caso específico de no realización de los derechos de las y los extranjero(a)s en términos de legislación	
13415	11334	003050260	Violaciones a los derechos de las y los extranjero(a)s en términos de resoluciones judiciales	
13416	13415	003050260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las y los extranjero(a)s	
13417	13415	003050260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las y los extranjero(a)s	
13418	13415	003050260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las y los extranjero(a)s	
13419	13415	003050260020	Caso específico de no realización de los derechos de las y los extranjero(a)s en términos de resoluciones judiciales	
13420	11339	003055250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las personas desplazadas	
13421	11339	003055250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las personas desplazadas	
13423	11339	003055250020	Caso específico de no realización de los derechos de las personas desplazadas en términos de políticas públicas	
13424	11337	003055255	Violaciones a los derechos de las personas desplazadas en términos de legislación	
13425	13424	003055255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las personas desplazadas	
13426	13424	003055255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las personas desplazadas	
13427	13424	003055255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las personas desplazadas	
13428	13424	003055255020	Caso específico de no realización de los derechos de las personas desplazadas en términos de legislación	
13429	11337	003055260	Violaciones a los derechos de las personas desplazadas en términos de resoluciones judiciales	
13431	13429	003055260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las personas desplazadas	
13506	13495	002027260	Violaciones al derecho al agua en términos de resoluciones judiciales	
13432	13429	003055260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derechos de las personas desplazadas	
13433	13429	003055260020	Caso específico de no realización de los derechos de las personas desplazadas en términos de resoluciones judiciales	
13435	13434	003060005	Violaciones al derecho de las y los defensore(a)s a promover y procurar la protección y realización de los derechos humanos	
13436	13434	003060010	Violaciones al derecho de las y los defensore(a)s a hacer críticas y propuestas en materia de derechos humanos	
13437	13434	003060015	Violaciones al derecho de las y los defensore(a)s a recibir financiamiento para la defensa y promoción de los derechos humanos	
13453	11286	003027	Violaciones a los derechos de las personas sentenciadas	
13454	13453	003027010	Violaciones al derecho de las personas sentenciadas a un trabajo productivo y apropiado	
13455	13453	003027005	Violaciones al derecho de las personas sentenciadas a los beneficios de la preliberación	
13456	13453	003027250	Violaciones a los derechos de las personas sentenciadas en términos de políticas públicas	
13457	13456	003027250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las personas sentenciadas	
13458	13456	003027250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las personas sentenciadas	
13459	13456	003027250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las personas sentenciadas	
13460	13456	003027250020	Caso específico de no realización de los derechos de las personas sentenciadas en términos de políticas públicas	
13461	13453	003027255	Violaciones a los derechos de las personas sentenciadas en términos de legislación	
13462	13461	003027255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las personas sentenciadas	
13463	13461	003027255010	Adopción de  legislación regresiva en la protección, respeto y garantía los derechos de las personas sentenciadas	
13464	13461	003027255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las personas sentenciadas	
13465	13461	003027255020	Caso específico de no realización de los derechos de las personas sentenciadas en términos de legislación	
13466	13453	003027260	Violaciones a los derechos de las personas sentenciadas en términos de resoluciones judiciales	
13467	13466	003027260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas sentenciadas	
13468	13466	003027260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las personas sentenciadas	
13469	13466	003027260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas sentenciadas	
13470	13466	003027260020	Caso específico de no realización de los derechos de las personas sentenciadas en términos de resoluciones judiciales	
13471	10	001087	Violaciones al derecho a la objeción de conciencia	
13473	13472	001087250	Derecho a la objeción de conciencia en términos de políticas públicas	
13474	13472	001087255	Derecho a la objeción de conciencia en términos de legislación	
13475	13472	001087260	Derecho a la objeción de conciencia en términos de resoluciones judiciales	
13476	16	002027	Derecho al agua	
13477	13476	002027250	Derecho al agua en términos de políticas públicas	
13478	13476	002027255	Derecho al agua en términos de legislación	
13479	13476	002027260	Derecho al agua en términos de resoluciones judiciales	
13480	13471	001087250	Violaciones al derecho a la objeción de conciencia en términos de políticas públicas	
13481	13480	001087250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la objeción de conciencia	
13483	13480	001087250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la objeción de conciencia	
13484	13480	001087250020	Caso específico de no realización del derecho a la objeción de conciencia en términos de políticas públicas	
13485	13471	001087255	Violaciones al derecho a la objeción de conciencia en términos de legislación	
13486	13485	001087255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la objeción de conciencia	
13487	13485	001087255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la objeción de conciencia	
13488	13485	001087255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la objeción de conciencia	
13489	13485	001087255020	Caso específico de no realización del derecho a la objeción de conciencia en términos de legislación	
13490	13471	001087260	Violaciones al derecho a la objeción de conciencia en términos de resoluciones judiciales	
13492	13490	001087260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la objeción de conciencia	
13493	13490	001087260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la objeción de conciencia	
13494	13490	001087260020	Caso específico de no realización del derecho a la objeción de conciencia en términos de resoluciones judiciales	
13495	11266	002027	Violaciones al derecho al agua	
13496	13495	002027250	Violaciones al derecho al agua en términos de políticas públicas	
13497	13496	002027250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho al agua	
13499	13496	002027250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho al agua	
13500	13496	002027250020	Caso específico de no realización del derecho al agua en términos de políticas públicas	
13501	13495	002027255	Violaciones al derecho al agua en términos de legislación	
13502	13501	002027255005	Falta de adopción de legislación que respete, proteja y garantice el derecho al agua	
13503	13501	002027255010	Adopción de legislación regresiva en la protección, respeto y garantía del derecho al agua	
13504	13501	002027255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho al agua	
13689	56	008	Documento académico	
13507	13506	002027260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho al agua	
13508	13506	002027260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho al agua	
13509	13506	002027260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho al agua	
13510	13506	002027260020	Caso específico de no realización del derecho al agua en términos de resoluciones judiciales	
13511	94	020006	Demanda laboral	
13512	94	020008	Demanda agraria	
13513	92	002	Orientación y canalización	
13516	92	004	Asistencia proporcionada	
13527	1	R21	Tipos de Relaciones - Recíproco	
13528	94	020010	Demanda civil	
13529	94	020012	Demanda familiar	
13530	94	020014	Litigio nacional	
13531	94	020016	Solicitud de amparo	
13532	94	020018	Litigio internacional	
13533	13514	016002	Medidas de protección ante OPDH	
13534	13514	016004	Medidas de protección ante OIG	
13535	13516	004002	Asistencia jurídica	
13541	13516	004008	Asistencia educativa	
13546	13516	004006	Asistencia médica	
13550	13516	004010	Asistencia de otro tipo	
13554	13516	004004	Asistencia financiera	
13560	13513	002002	Asesoría legal	
13561	13513	002004	Asesoría política	
13562	13513	002006	Gestión para obtener información o ayuda	
13563	13562	002006002	Gestión telefónica para obtener información o ayuda	
13564	13562	002006004	Gestión escrita para obtener información o ayuda	
13565	13562	002006006	Gestión personal para obtener información o ayuda	
13566	13513	002008	Canalización	
13569	13566	002008006	Canalización a instancia de procuración de justicia	
13570	13566	002008008	Canalización a instancia judicial	
13571	13566	002008010	Canalización a otra autoridad	
13572	13571	002008010002	Canalización a autoridad autónoma	
13573	13571	002008010004	Canalización a autoridad comunitaria	
13574	13566	002008012	Canalización a organización no gubernamental, social o eclesial	
13602	1	T22	Relación entre casos	
13603	1	R22	Relación entre casos - Recíproco	
13618	57	002002	Acta administrativa	
13619	57	002004	Acta de asamblea oficial	
13620	57	002006	Acuerdo oficial	
13621	57	002008	Carta oficial	
13622	57	002010	Certificado de defunción 	
13623	57	002012	Certificado de derechos agrarios 	
13625	57	002016	Cinta de video o película oficial	
13626	57	002018	Cinta o pista de audio oficial	
13627	57	002020	Circular oficial	
13628	57	002022	Citatorio oficial	
13629	57	002024	Comunicado de prensa oficial	
13630	57	002026	Contrato de empleo oficial	
13631	57	002028	Credencial oficial	
13633	56	004	Documento de organización nacional	
13635	57	002034	Decreto o reglamento administrativo	
13636	57	002036	Denuncia penal	
13637	57	002038	Dictamen pericial oficial	
13638	57	002040	Documento de afiliación a la seguridad social	
13639	57	002042	Documento de identificación personal  oficial	
13640	57	002044	Documento de recepción de apoyos sociales del gobierno 	
13641	57	002046	Documento de trámite fiscal	
13642	57	002048	Documento oficial traducido	
13643	57	002050	Encuesta oficial	
13644	57	002052	Escritura pública	
13646	57	002056	Expediente administrativo	
13647	57	002058	Expediente judicial 	
13648	57	002060	Folleto, material de propaganda oficial	
13649	57	002062	Fotografía oficial	
13650	57	002064	Informe oficial	
13651	57	002066	Ley	
13652	57	002068	Recibo oficial de bienes económicos o materiales	
13655	57	002074	Respuesta oficial a solicitud de información pública	
13656	57	002076	Resumen escrito oficial	
13657	13633	004002	Acción urgente de organización nacional	
13659	13633	004006	Acuerdo de organización nacional	
13660	13633	004008	Carta de organización nacional	
13661	13633	004010	Cartel, pancarta, pinta de organización nacional	
13662	13633	004012	Cinta de video o película de organización nacional	
13663	13633	004014	Cinta o pista de audio de organización nacional	
13666	13633	004020	Documento de organización nacional traducido	
13667	13633	004022	Encuesta de organización nacional	
13668	13633	004024	Folleto, material de propaganda de organización nacional	
13669	13633	004026	Fotografía de organización nacional	
13670	13633	004028	Informe de organización nacional	
13671	13633	004030	Resumen escrito de organización nacional	
13672	13633	004032	Solicitud de organización nacional de obtención de información pública 	
13673	58	006002	Acción urgente de organización internacional	
13674	58	006004	Acta de asamblea de organización internacional	
13675	58	006006	Acuerdo de organización internacional	
13676	58	006008	Carta de organización internacional	
13677	58	006010	Cartel, pancarta, pinta de organización internacional	
13678	58	006012	Cinta de video o película de organización internacional	
13679	58	006014	Cinta o pista de audio de organización internacional	
13680	58	006016	Comunicado de prensa de organización internacional	
13682	58	006020	Documento de organización internacional traducido	
13683	58	006022	Encuesta de organización internacional	
13684	58	006024	Folleto, material de propaganda de organización internacional	
13685	58	006026	Fotografía de organización internacional	
13686	58	006028	Informe de organización internacional	
13687	58	006030	Resumen escrito de organización internacional	
13691	13689	008004	Cinta o pista de audio académica	
13692	13689	008006	Comunicado de prensa académico	
13693	13689	008008	Documento académico traducido 	
13694	13689	008010	Encuesta académica	
13695	13689	008012	Estudio técnico y/o científico académico	
13696	13689	008014	Folleto, material de propaganda académico	
13697	13689	008016	Fotografía académica	
13698	13689	008018	Informe académico	
13699	13689	008020	Resumen escrito académico	
13701	56	010	Información de medios de comunicación 	
13702	13701	010002	Agencia de información 	
13703	13701	010004	Cinta de video o película de medio de comunicación	
13704	13701	010006	Cinta o pista de audio de medio de comunicación	
13705	13701	010008	Documento de medio de comunicación traducido	
13706	13701	010010	Encuesta de medio de comunicación	
13707	13701	010012	Folleto, material de propaganda de medio de comunicación	
13708	13701	010014	Fotografía de medio de comunicación	
13710	13701	010018	Periódico	
13712	13701	010022	Revista 	
13713	13701	010024	Televisión 	
13714	56	012	Documento personal o privado	
13715	13714	012002	Acta de asamblea privada	
13716	13714	012004	Acuerdo privado	
13717	13714	012006	Carta personal	
13718	13714	012008	Cartel, pancarta, pinta privada	
13720	13714	012012	Certificado médico psicológico privado	
13721	13714	012014	Cinta de video o película personal	
13722	13714	012016	Cinta o pista de audio personal	
13723	13714	012018	Circular privada	
13724	13714	012020	Contrato de empleo privado	
13725	13714	012022	Conversación telefónica privada	
13726	13714	012024	Credencial personal no oficial	
13728	13714	012028	Documento privado traducido 	
13729	13714	012030	Encuesta privada	
13730	13714	012032	Estudio técnico y/o científico privado	
13735	13714	012042	Reglamento interno privado	
13736	13714	012044	Resumen escrito privado	
13737	13714	012046	Solicitud personal de obtención de información pública	
13738	100	012	Autoridad autónoma	
13739	100	015	Autoridad comunitaria	
13740	100	018	Autoridad ejidal o de bienes comunales	
13741	100	021	Colega de trabajo de la víctima	
13742	100	024	Colega de trabajo del perpetrador	
13745	100	033	Institución gubernamental	
13747	100	039	Miembro de la misma comunidad que el perpetrador	
13748	100	042	Miembro de la misma comunidad que la víctima	
13749	100	045	Miembro de la misma organización que el perpetrador	
13750	100	048	Miembro de la misma organización que la víctima	
13751	100	051	Organización eclesial	
13753	100	057	Organización no gubernamental de derechos humanos	
13754	100	060	Perpetrador en el evento	
13759	100	075	Víctima en el evento	
13760	92	006	Denuncia pública	
13761	13760	006002	Acción urgente	
13762	13760	006004	Boletín de prensa	
13763	13760	006006	Informe	
13765	92	008	Comunicación con autoridades	
13766	13765	008002	Comunicación telefónica con autoridades	
13767	13765	008004	Comunicación escrita con autoridades	
13768	13765	008006	Comunicación personal con autoridades	
13769	92	010	Observación e investigación	
13770	13769	010002	Brigada de observación	
13771	13769	010004	Misión o delegación de investigación	
13774	13773	012002	Comunicación con Relatores ONU	
13779	92	016	Medidas de protección	
13785	92	020	Acción judicial en tribunal judicial o administrativo	
13786	13785	020002	Denuncia penal	
13787	13785	020004	Queja administrativa	
13788	13785	020006	Demanda laboral	
13789	13785	020008	Demanda agraria	
13790	13785	020010	Demanda civil	
13791	13785	020012	Demanda familiar	
13792	13785	020014	Litigio nacional	
13793	13785	020016	Solicitud de amparo	
13794	13785	020018	Litigio internacional	
13801	11416	010045035	Persona que abusa de su poder dentro de la iglesia	
13806	13803	020015	Personas vestidas de civil	
13807	138	001025065	Derecho a un recurso efectivo	
13808	17	003070	Derechos de las y los consumidores	
13810	13808	003070010	Derecho de las y los consumidores a la protección de los intereses económicos y sociales	
13811	13808	003070015	Derecho de las y los consumidores a la información	
13812	13808	003070020	Derecho de las y los consumidores a la educación y formación en materia de consumo	
13813	13808	003070025	Derecho de las y los consumidores de representación, consulta y participación	
13814	13808	003070030	Derecho de las y los consumidores a obtener protección ante cualquier situación que cause inferioridad, subordinación o indefensión	
13816	13808	003070250	Derechos de las y los consumidores en términos de políticas públicas	
13817	13808	003070255	Derechos de las y los consumidores en términos de legislación	
13818	13808	003070260	Derechos de las y los consumidores en términos de resoluciones judiciales	
13819	14	001015050	Revisión irregular o arbitraria	
13821	11191	001025065	Violaciones al derecho a un recurso efectivo	
13822	11282	002045005005	Violaciones al derecho a la propiedad intelectual	
13825	11286	003070	Violaciones a los derechos de las y los consumidores	
13826	13825	003070005	Violaciones al derechos de las y los consumidores a la protección de la salud y la seguridad	
13827	13825	003070010	Violaciones al derecho de las y los consumidores a la protección de los intereses económicos y sociales	
13828	13825	003070015	Violaciones al derecho de las y los consumidores a la información	
13823	11285	002055015	Robo	Usar también para despojo
13829	13825	003070020	Violaciones al derecho de las y los consumidores a la educación y formación en materia de consumo	
13830	13825	003070025	Violaciones al derecho de las y los consumidores de representación, consulta y participación	
13833	13825	003070250	Violaciones a los derechos de las y los consumidores en términos de políticas públicas	
13834	13833	003070250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las y los consumidores	
13835	13833	003070250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las y los consumidores	
13836	13833	003070250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las y los consumidores	
13837	13833	003070250020	Caso específico de no realización de los derechos de las y los consumidores en términos de políticas públicas	
13838	13825	003070255	Violaciones a los derechos de las y los consumidores en términos de legislación	
13839	13838	003070255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las y los consumidores	
13840	13838	003070255010	Adopción de  legislación regresiva en la protección, respeto y garantía los derechos de las y los consumidores	
13841	13838	003070255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las y los consumidores	
13842	13838	003070255020	Caso específico de no realización de los derechos de las y los consumidores en términos de legislación	
13843	13825	003070260	Violaciones a los derechos de las y los consumidores en términos de resoluciones judiciales	
13844	13843	003070260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las y los consumidores	
13845	13843	003070260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las y los consumidores	
13846	13843	003070260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de las y los consumidores	
13847	13843	003070260020	Caso específico de no realización de los derechos de las y los consumidores en términos de resoluciones judiciales	
14000	11730	005	Sistema universal – Instrumentos generales	
14002	14000	005010	Declaración Universal de los Derechos Humanos (1948)	
14004	14000	005020	Pacto Internacional de Derechos Civiles y Políticos (1966)	
14005	14000	005005	Carta de las Naciones Unidas (1945)	
14006	14000	005015	Pacto Internacional de Derechos Económicos, Sociales y Culturales (1966)	
14007	14000	005025	Segundo Protocolo facultativo del Pacto Internacional de Derechos Civiles y Políticos, destinado a abolir la pena de muerte (1990)	
14008	14000	005030	Declaración y Programa de Acción de Viena (1993)	
14009	11730	010	Sistema Interamericano – Instrumentos generales	
14010	14009	010005	Declaración Americana de los Derechos y Deberes del Hombre (1948)	
14011	14009	010010	Convención Americana sobre Derechos Humanos (Pacto de San José) (1969)	
14012	14009	010015	Protocolo de San Salvador adicional a la Convención Americana sobre Derechos Humanos en materia de derechos económicos, sociales y culturales (1988)	
14013	14009	010020	Protocolo a la Convención Americana sobre Derechos Humanos relativo a la abolición de la pena de muerte (1990)	
14014	11730	015	Alimentación	
14015	14014	015005	Declaración universal sobre la erradicación del hambre y la malnutrición (1974)	
14017	14014	015250	Jurisprudencia sobre alimentación	
14018	11730	020	Bioética	
14019	14018	020005	Declaración universal sobre el genoma humano y los derechos humanos (1997)	
14020	14018	020250	Jurisprudencia sobre bioética	
14021	11730	025	Conflicto armado (derecho humanitario)	
14022	14021	025005	Convenio de Ginebra para aliviar la suerte que corren los heridos y los enfermos de las fuerzas armadas en campaña (Convenio I) (1949)	
14023	14021	025010	Convenio de Ginebra para aliviar la suerte que corren los heridos, los enfermos y los náufragos de las fuerzas armadas en el mar (Convenio II) (1949)	
14024	14021	025015	Convenio de Ginebra relativo al trato debido a los prisioneros de guerra (Convenio III) (1949)	
14026	14021	025025	Protocolo adicional a los Convenios de Ginebra del 12 de agosto de 1949 relativo a la protección de las víctimas de los conflictos armados internacionales (Protocolo I) (1977)	
14027	14021	025030	Protocolo adicional a los Convenios de Ginebra del 12 de agosto de 1949 relativo a la protección de las víctimas de los conflictos armados sin carácter internacional (Protocolo II) (1977)	
14028	14021	025035	Declaración sobre la protección de la mujer y el niño en estados de emergencia o de conflicto armado (1974)	
14029	14021	025040	Convención para la protección de los bienes culturales en caso de conflicto armado (1954)	
14030	14021	025250	Jurisprudencia sobre conflicto armado (derecho humanitario)	
14031	11730	030	Defensores / Defensoras	
14033	14031	030010	Instituciones nacionales de promoción y protección de los derechos humanos (Principios de Paris) (1991)	
14034	14031	030250	Jurisprudencia sobre defensores / defensoras	
14035	11730	035	Delincuencia organizada trasnacional	
14036	14035	035005	Convención de las Naciones Unidas contra la delincuencia organizada transnacional – Convención de Palermo (2000)	
14038	11730	040	Derechos culturales	
14039	14038	040005	Convención universal sobre derechos de autor (1971)	
14040	14038	040010	Convención sobre las medidas que deben adoptarse para prohibir e impedir la importación, la exportación y la transferencia de propiedad ilícita de bienes culturales (1964)	
14041	14038	040015	Declaración de los principios de la cooperación cultural internacional (1966)	
14042	14038	040020	Convención sobre la protección del patrimonio mundial cultural y natural (1972)	
14043	14038	040250	Jurisprudencia sobre derechos culturales	
14044	11730	045	Desaparición forzada	
14045	14044	045005	Convención Interamericana sobre desaparición forzada de personas (1994)	
14046	14044	045010	Declaración sobre la protección de todas las personas contra las desapariciones forzadas (1992)	
14048	14044	045250	Jurisprudencia sobre desaparición forzada	
14049	11730	050	Desarrollo, progreso, bienestar social y paz	
14050	14049	050005	Declaración sobre el fomento entre la juventud de los ideales de paz, respeto mutuo y comprensión entre los pueblos (1965)	
14051	14049	050010	Declaración sobre el progreso y el desarrollo en lo social (1969)	
14052	14049	050015	Declaración sobre la utilización del progreso científico y tecnológico en interés de la paz y en beneficio de la humanidad (1975)	
14053	14049	050020	Declaración sobre el derecho de los pueblos a la paz (1984)	
14054	14049	050025	Declaración sobre el derecho al desarrollo (1986)	
14055	14049	050250	Jurisprudencia sobre desarrollo, progreso, bienestar social y paz	
14056	11730	055	Desplazamiento interno	
14057	14056	055005	Principios rectores de los desplazamientos internos (1998)	
14058	14056	055010	Convención para la protección de los bienes culturales en caso de conflicto armado (1954)	
14059	14056	055250	Jurisprudencia sobre desplazamiento interno	
14060	11730	060	Discapacidad	
14061	14060	060005	Declaración de los derechos del retrasado mental (1971)	
14062	14060	060010	Declaración de los derechos de los impedidos (1975)	
14063	14060	060015	Normas uniformes sobre la igualdad de oportunidades para las personas con discapacidad (1996)	
14064	14060	060020	Convención sobre los Derechos de las Personas con Discapacidad (2006)	
14066	14060	060250	Jurisprudencia sobre discapacidad	
14067	11730	065	Discriminación	
14068	14067	065005	Convención Internacional sobre la Eliminación de todas las Formas de Discriminación Racial (1965)	
14069	14067	065010	Declaración sobre la eliminación de todas las formas de intolerancia y discriminación fundadas en la religión o las convicciones (1981)	
14070	14067	065015	Convención relativa a la lucha contra las discriminaciones en la esfera de la enseñanza (1960)	
14071	14067	065020	Declaración sobre la raza y los prejuicios raciales (1978)	
14073	14067	065030	Convenio (No. 111) relativo a la discriminación en materia de empleo y ocupación (1958)	
14074	14067	065035	Convenio (No. 100) relativo a la igualdad de remuneración entre la mano de obra masculina y la mano de obra femenina por un trabajo de igual valor (1951)	
14075	14067	065040	Convenio (No. 156) relativo a la igualdad de oportunidades y de trato igual entre trabajadores y trabajadoras: Trabajadores con responsabilidades familiares (1981)	
14076	14067	065045	Conferencia Mundial contra el Racismo, 2001 (Declaración y Programa de acción)	
14078	11730	070	Educación	
14079	14078	070005	Recomendación sobre la educación para la comprensión, la cooperación y la paz internacionales y la educación relativa a los derechos humanos y las libertades fundamentales (1974)	
14080	14078	070250	Jurisprudencia sobre educación	
14081	11730	075	Empresas trasnacionales	
14083	14081	075250	Jurisprudencia sobre empresas trasnacionales	
14084	11730	080	Genocidio, crímenes de guerra y crímenes de lesa humanidad	
14085	14084	080005	Convención para la prevención y la sanción del delito de genocidio (1948)	
14037	14035	035250	Jurisprudencia sobre delincuencia organizada trasnacional	
14101	14097	090250	Jurisprudencia sobre Libertad de expresión e información	
14088	14084	080020	Estatuto de Roma de la Corte Penal Internacional (1998)	
14089	14084	080250	Jurisprudencia sobre genocidio, crímenes de guerra y crímenes de lesa humanidad	
14090	11730	085	Laboral y empleo	
14091	14090	085005	Convenio (No. 11) relativo a los derechos de asociación y de coalición de los trabajadores agrícolas (1921)	
14092	14090	085010	Convenio (No. 87) relativo a la libertad sindical y la protección del derecho de sindicación (1948)	
14093	14090	085015	Convenio (No. 98) relativo a la aplicación de los principios del derecho de sindicación y de negociación colectiva (1949)	
14094	14090	085020	Convenio (No. 141) sobre las organizaciones de trabajadores rurales y su papel en el desarrollo económico y social (1975)	
14095	14090	085025	Convenio (No. 168) sobre el fomento del empleo y la protección contra el desempleo (1988)	
14096	14090	085250	Jurisprudencia sobre laboral y empleo	
14097	11730	090	Libertad de expresión e información	
14098	14097	090005	Convención sobre el derecho internacional de rectificación (1952)	
14099	14097	090010	Principios rectores para la reglamentación de los ficheros computadorizados de datos personales (1990)	
14102	11730	095	Matrimonio	
14103	14102	095005	Convención sobre el consentimiento para el matrimonio, la edad mínima para contraer matrimonio y el registro de los matrimonios (1962)	
14104	14102	095010	Recomendación sobre el consentimiento para el matrimonio, la edad mínima para contraer matrimonio y el registro de los matrimonios (1965)	
14105	14102	095250	Jurisprudencia sobre matrimonio	
14106	11730	100	Medio ambiente	
14107	14106	100005	Protocolo de Kioto sobre el cambio climático (1997)	
14109	14106	100250	Jurisprudencia sobre medio ambiente	
14110	11730	105	Mercenarios	
14112	14110	105250	Jurisprudencia sobre mercenarios	
14113	11730	110	Migrantes y extranjeros	
14115	14113	110010	Convenio (No. 97) relativo a los trabajadores migratorios (1949)	
14116	14113	110015	Convenio (No. 143) sobre las migraciones en condiciones de abuso y la promoción de la igualdad de oportunidades y trato a los trabajadores migrantes (1975)	
14117	14113	110020	Declaración sobre los derechos humanos de los individuos que no son nacionales del país en que viven (1985)	
14119	14113	110030	Protocolo contra el tráfico ilícito de migrantes por tierra, mar y aire, que complementa la Convención de las Naciones Unidas contra la delincuencia organizada transnacional (2000)	
14120	14113	110250	Jurisprudencia sobre migrantes y extranjeros	
14121	11730	115	Mujeres	
14122	14121	115005	Convención sobre los derechos políticos de la mujer (1952)	
14123	14121	115010	Convención sobre la nacionalidad de la mujer casada (1957)	
14125	14121	115020	Declaración sobre la eliminación de la violencia contra la mujer (1993)	
14126	14121	115025	Convención sobre la nacionalidad de la mujer firmada en la Séptima Conferencia Internacional Americana (1933)	
14127	14121	115030	Convención Interamericana sobre la concesión de los derechos políticos a la mujer (1948)	
11694	154	130	Herido(a)	
14128	14121	115035	Convención Interamericana sobre la concesión de los derechos civiles a la mujer (1948)	
14129	14121	115040	Convención Interamericana para prevenir, sancionar y erradicar la violencia contra la mujer (Belem do Pará) (1994)	
14130	14121	115250	Jurisprudencia sobre mujeres	
14131	11730	120	Niñez y juventud	
14133	14131	120010	Protocolo facultativo de la Convención sobre los Derechos del Niño relativo a la participación de niños en los conflictos armados (1999)	
14137	14131	120030	Convenio (No. 182) sobre la prohibición de las peores formas de trabajo infantil y la acción inmediata para su eliminación (1999)	
14140	14131	120045	Convención Interamericana sobre tráfico internacional de menores (1994)	
14141	14131	120250	Jurisprudencia sobre niñez y juventud	
14142	11730	125	Personas mayores	
14144	14142	125250	Jurisprudencia sobre personas mayores	
14145	11730	130	Personas privadas de la libertad	
14146	14145	130005	Reglas mínimas para el tratamiento de los reclusos (1955)	
14147	14145	130015	Conjunto de Principios para la protección de todas las personas sometidas a cualquier forma de detención o prisión (1988)	
14148	14145	130020	Principios básicos para el tratamiento de los reclusos (1990)	
14149	14145	130025	Reglas de las Naciones Unidas para la protección de los menores privados de libertad (1990)	
14150	14145	130030	Salvaguardias para garantizar la protección de los derechos de los condenados a la pena de muerte (1984)	
14151	14145	130250	Jurisprudencia sobre personas privadas de la libertad	
14153	14152	135005	Código de conducta para funcionarios encargados de hacer cumplir la ley (1979)	
14154	14152	135010	Reglas mínimas de las Naciones Unidas para la administración de la justicia de menores (Reglas de Beijing) (1985)	
14155	14152	135015	Declaración sobre los principios fundamentales de justicia para las víctimas de delitos y del abuso de poder (1985)	
14156	14152	135020	Principios básicos relativos a la independencia de la judicatura (1985)	
14157	14152	135025	Principios básicos sobre el empleo de la fuerza y de armas de fuego por los funcionarios encargados de hacer cumplir la ley (1990)	
14158	14152	135030	Principios básicos sobre la función de los abogados (1990)	
14160	14152	135040	Reglas mínimas de las Naciones Unidas sobre las medidas no privativas de la libertad (Reglas de Tokio) (1990)	
14161	14152	135045	Directrices de las Naciones Unidas para la prevención de la delincuencia juvenil (Directrices de Riad) (1990)	
14162	14152	135055	Conjunto de principios actualizado para la protección y la promoción de los derechos humanos mediante la lucha contra la impunidad (2005)	
14164	11730	140	Pueblos Indígenas y minorías	
14166	14164	140010	Convenio (No. 169) sobre pueblos indígenas y tribales en países independientes (1989)	
14167	14164	140015	Convenio-marco para la protección de las minorías nacionales (1994)	
14168	14164	140020	Declaración de las Naciones Unidas sobre los Derechos de los Pueblos Indígenas (2007)	
14169	14164	140250	Jurisprudencia sobre pueblos indígenas y minorías	
14175	14131	120025	Convenio (No. 138) sobre la edad mínima de admisión al empleo (1973)	
14176	14152	135035	Directrices sobre la función de los fiscales (1990)	
14178	11730	145	Refugio y Asilo	
14179	14178	145005	Convención sobre asilo firmada en la Sexta Conferencia Internacional Americana (1928)	
14180	14178	145010	Convención sobre asilo político firmada en la Séptima Conferencia Internacional Americana (1933)	
14181	14178	145015	Convención de la OEA sobre asilo diplomático (1954)	
14182	14178	145020	Convención de la OEA sobre asilo territorial (1954)	
14183	14178	145025	Declaración sobre el asilo territorial (1967)	
14184	14178	145030	Estatuto de la Oficina del Alto Comisionado de las Naciones Unidas para los Refugiados (1950)	
14185	14178	145035	Convención sobre el estatuto de los refugiados (1951)	
14186	14178	145040	Protocolo sobre el estatuto de los refugiados (1966)	
14187	14178	145250	Jurisprudencia sobre refugio y asilo	
14188	11730	150	Salud	
14189	14188	150005	Principios para la protección de los enfermos mentales y el mejoramiento de la atención de la salud mental (1991)	
14190	14188	150010	Declaración de compromiso en la lucha contra el VIH/SIDA (2001)	
14192	11730	155	Seguridad social	
14193	14192	155005	Convenio (No. 102) relativo a la norma mínima de la seguridad social (1952)	
14194	14192	155250	Jurisprudencia seguridad social	
14195	11730	160	Tortura	
14197	14195	160010	Principios relativos a la investigación y documentación eficaces de la tortura y otros tratos o penas crueles, inhumanos o degradantes (2000)	
14201	14195	160030	Convención Interamericana para prevenir y sancionar la tortura (1985)	
14202	14195	160250	Jurisprudencia sobre tortura	
14203	11730	165	Trata de personas, esclavitud y trabajo forzado	
14204	14203	165005	Convención sobre la esclavitud firmada en Ginebra el 25 de septiembre de 1926 y modificada por el Protocolo (1926)	
14205	14203	165010	Convención suplementaria sobre la abolición de la esclavitud, la trata de esclavos y las instituciones y prácticas análogas a la esclavitud (1956)	
14206	14203	165015	Convenio para la represión de la trata de personas y de la explotación de la prostitución ajena (1949)	
14207	14203	165020	Convenio (No. 29) relativo al trabajo forzoso u obligatorio (1930)	
14208	14203	165025	Convenio (No. 105) relativo a la abolición del trabajo forzoso (1957)	
14300	53	015	Acciones de protesta	
14303	53	043	Balacera, enfrentamiento	
14306	53	105	Cultura	
14308	53	205	Democracia	
203	53	170	Empresas privadas locales y nacionales	
14313	53	675	Violencia	
293	2	001015	Académico(a) o investigador(a)	
294	2	001020	Agente comercial, de ventas	
295	2	001025	Agricultor(a)	
296	2	001030	Artesano(a)	
297	2	001035	Artista	
298	2	001040	Ayudante o peón	
299	2	001045	Comerciante	
300	2	001050	Comunicador(a) social	
301	2	001055	Conductor(a) de transporte	
302	2	001065	Deportista	
303	2	001070	Directivo(a) de organización política, sindical, asociación civil, ONG	
304	2	001075	Empleado(a) de banco o institución financiera	
305	2	001080	Empleado(a) de comercio	
335	2	001085	Empleado(a) de institución penitenciaria	
336	2	001090	Empleado(a) de organización política, sindical, asociación civil, ONG	
338	2	001095	Empleado(a) en la construcción	
308	2	001130	Empleado(a) judicial	
339	2	001100	Empleado(a) en la industria	
340	2	001105	Empleado(a) en mina o cantera	
341	2	001120	Empleado(a) en servicio de protección y vigilancia	
342	2	001125	Empleado(a) en servicio doméstico	
310	2	001140	Empresario(a)	
311	2	001145	Estudiante	
314	2	001160	Gerente, administrador(a) de empresa o comercio	
315	2	001165	Juez(a)	
316	2	001170	Labores  del hogar	
317	2	001175	Legislador(a)	
318	2	001180	Maestro(a)	
320	2	001200	Notario(a) público(a)	
321	2	001205	Oficinista	
322	2	001210	Operador(a) de maquinaria y equipo	
323	2	001215	Personal de la Marina	
324	2	001220	Pescador(a)	
327	2	001235	Portero(a), conserje	
328	2	001240	Prestamista	
329	2	001250	Profesional de la salud del sector público	
331	2	001260	Promotor(a)	
332	2	001265	Religioso(a)	
333	2	001275	Técnico(a)	
337	2	001285	Trabajador(a) dedicado a la prostitución	
343	2	001290	Trabajador(a) voluntario(a)	
344	2	001295	Trabajador(a), peón en el campo	
14318	2	001195	Narcotraficante	
14319	2	001245	Profesional de la salud del sector privado	
14323	14321	002010	Actividades legislativas	
14325	14321	002020	Administración pública	
14335	14321	002075	Procuración de justicia	
14336	14321	002080	Seguridad nacional	
14337	14321	002085	Seguridad pública	
12530	161	004001	Promovió la aplicación de la ley, resolución judicial o la implementación de la política violatoria de derechos humanos	
12531	161	004002	Apoyó la aplicación de la ley, resolución judicial o la implementación de la política violatoria de derechos humanos	
2	48	001	Ocupación de persona individual	
14350	5429	001010	Autoridad autónoma	
14349	5429	001015	Autoridad comunitaria	
12442	5429	001020	Campesino(a), ejidatario(a), comunero(a)	
14351	5429	001025	Ciudadano(a) común	
14353	5429	001040	Custodio(a)	
14354	5429	001045	Damnificado(a)	
12444	5429	001050	Defensor(a) de los derechos humanos	
12445	5429	001055	Desempleado(a)	
12446	5429	001060	Desplazado(a) interno(a)	
12447	5429	001065	Discapacitado(a)	
12449	5429	001075	Empleador(a)	
14355	5429	001080	Empresario(a)	
12450	5429	001085	Enfermo(a)	
12451	5429	001090	Enfermo(a) mental	
12467	5429	001095	Escolta, guardaespaldas	
12470	5429	001100	Estudiante	
12453	5429	001105	Exiliado(a)	
12454	5429	001110	Extranjero(a)	
12458	5429	001125	Indígena	
12459	5429	001130	Joven	
12460	5429	001135	Jubilado(a), retirado(a)	
12461	5429	001145	Líder de la comunidad	
12462	5429	001150	Manifestante	
12468	5429	001160	Menor en situación de calle	
12464	5429	001170	Militar	
12465	5429	001175	Mujer	
12466	5429	001180	Mujer embarazada	
12469	5429	001185	Objetor(a) de conciencia	
12472	5429	001190	Persona en situación de calle	
12473	5429	001195	Persona privada de la libertad	
12486	5429	001270	Víctima de VDH	
12485	5429	001265	Víctima de delito	
12484	5429	001260	Vecino de víctima	
12483	5429	001255	Transeúnte	
12481	5429	001250	Trabajador(a) migrante	
12482	5429	001245	Trabajador(a)	
12479	5429	001235	Solicitante de asilo	
12478	5429	001230	Sindicalista	
12477	5429	001225	Refugiado(a)	
12475	5429	001215	Presunto(a) delincuente	
14309	53	125	Desigualdad, inequidad	Incluye desigualdad e inequidad económica y de oportunidades
12452	5429	001210	Portador(a) de VIH/SIDA	
12474	5429	001205	Policía	
12480	5429	001240	Testigo(a)	
12521	12504	003150	Sindicato	
12520	12504	003130	Partido o grupo político	
12517	12504	003115	Organización empresarial	
12515	12504	003105	Organización de mujeres	
12514	12504	003100	Organización de derechos humanos	
12512	12504	003090	Organización campesina	
12509	12504	003065	Grupo religioso	
14358	12504	003005	Autoridades comunitarias	
14359	12504	003010	Comunidad	
14361	12504	003020	Comunidad o municipio autónomo	
14362	12504	003030	Fuerzas armadas	
14363	12504	003035	Fuerzas de seguridad pública e investigación	
14364	12504	003045	Grupo de seguridad privada	
14366	12504	003070	Institución penitenciaria	
14370	12504	003145	Poder legislativo	
14373	14371	004010	Entre 18 y 65 años	
11371	169	005010005	Congreso federal	
11375	11371	005010005020	Comisión legislativa federal	
11376	11371	005010005025	Fracción parlamentaria federal	
11415	167	010040	Agrupación	
13795	11415	010040005	Partido político	
13796	11415	010040010	Sindicato	
14386	167	010060	Otras personas individuales	
11706	154	180	Retornado(a) a su lugar de origen	
12554	154	175	Resguardado(a) en lugar privado seguro	
11696	154	125	Encontrado(a) después de haber estado desaparecido(a) un tiempo	
11704	154	090	Desplazado(a) interno(a)	
11710	154	085	Despedido(a) del empleo	
11695	154	080	Desaparecido(a)	
11708	154	075	Desalojado(a), sin techo	
11702	154	070	Deportado(a), extraditado(a), expulsado(a)	
14392	154	015	Bajo amenaza	
14393	154	095	Despojado(a), robado(a)	
12553	154	010	Afectado(a) sicológicamente	
14397	154	050	Con orden de aprehensión	
14400	154	100	Detenido(a)	
14401	154	105	Difamado(a)	
14408	154	195	Secuestrado(a)	
11697	154	025	Bajo investigación en libertad	
11698	154	035	Bajo proceso en libertad	
11699	154	030	Bajo proceso en detención	
173	172	130	Beneficiado(a) por promoción o ascenso	
11714	172	095	Procesado(a) y sancionado(a) con destitución	
11712	172	100	Procesado(a) y sancionado(a) con suspensión	
11713	172	020	Bajo investigación administrativa	
11718	172	045	Bajo proceso administrativo	
11725	172	025	Bajo investigación administrativa y penal	
14412	172	035	Bajo investigación penal en libertad	
14414	172	050	Bajo proceso administrativo y penal	
14417	172	105	Procesado(a) y sancionado(a) con inhabilitación	
14423	172	140	Transferido(a)	
14424	129	050	Religión menonita	
87	129	120	Ninguna religión	
74	129	110	Religión hinduista	
73	129	100	Religión budista	
72	129	090	Religión musulmana	
71	129	080	Religión judía	
85	129	060	Religión mormona	
86	129	040	Testigos de Jehová	
84	129	030	Religión cristiana	
6	129	020	Religión protestante y evangélica (históricas)	
5	129	010	Religión católica	
14427	14425	001036255	Derecho a la seguridad ciudadana en términos de legislación	
14428	14425	001036260	Derecho a la seguridad ciudadana en términos de resoluciones judiciales	
14430	14429	001037250	Derecho a la protección frente al abuso de poder en términos de políticas públicas	
14431	14429	001037255	Derecho a la protección frente al abuso de poder en términos de legislación	
14432	14429	001037260	Derecho a la protección frente al abuso de poder en términos de resoluciones judiciales	
12294	11060	001165255	Derecho a elecciones libres y democráticas en términos de legislación	
14435	15	001260	Derechos civiles y políticos en términos de resoluciones judiciales	
11720	172	065	Bajo proceso penal en detención	
11719	172	060	Bajo proceso penal en libertad	
11716	172	090	Procesado(a) y sancionado(a) con amonestación	
14421	172	125	Procesado(a) y sentenciado(a)	
14436	16	002250	Derechos económicos, sociales, culturales y ambientales en términos de políticas públicas	
14437	16	002255	Derechos económicos, sociales, culturales y ambientales en términos de legislación	
14439	51	004	Derechos de los pueblos	
14441	14440	004005250	Derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de políticas públicas	
14442	14440	004005255	Derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de legislación	
14443	14440	004005260	Derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de resoluciones judiciales	
14445	14444	004010250	Derecho de los pueblos a la autodeterminación en términos de políticas públicas	
14446	14444	004010255	Derecho de los pueblos a la autodeterminación en términos de legislación	
14447	14444	004010260	Derecho de los pueblos a la autodeterminación en términos de resoluciones judiciales	
14448	14439	004015	Derecho de los pueblos a la paz	
14449	14448	004015250	Derecho de los pueblos a la paz en términos de políticas públicas	
14450	14448	004015255	Derecho de los pueblos a la paz en términos de legislación	
14451	14448	004015260	Derecho de los pueblos a la paz en términos de resoluciones judiciales	
14453	14452	004020250	Derecho de los pueblos al desarrollo en términos de políticas públicas	
14454	14452	004020255	Derecho de los pueblos al desarrollo en términos de legislación	
14455	14452	004020260	Derecho de los pueblos al desarrollo en términos de resoluciones judiciales	
14460	14439	004030	Derechos de los pueblos indígenas	
14461	14460	004030005	Derecho de los pueblos indígenas a la autonomía política, económica y social	
14462	14460	004030010	Derecho de los pueblos indígenas a la consulta y participación	
14463	14460	004030015	Derecho de los pueblos indígenas a la jurisdicción indígena	
14464	14460	004030020	Derecho de los pueblos indígenas a la personería jurídica	
14465	14460	004030025	Derecho de los pueblos indígenas a la tierra y territorio	
14466	14460	004030030	Derecho de los pueblos indígenas a su cultura, identidad y educación	
14469	14460	004030260	Derechos de los pueblos indígenas en términos de resoluciones judiciales	
14470	14439	004250	Derechos de los pueblos en términos de políticas públicas	
14471	14439	004255	Derechos de los pueblos en términos de legislación	
14472	14439	004260	Derechos de los pueblos en términos de resoluciones judiciales	
14477	14476	001036250	Violaciones al derecho a la seguridad ciudadana en términos de políticas públicas	
14478	14477	001036250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la seguridad ciudadana	
14479	14477	001036250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la seguridad ciudadana	
14480	14477	001036250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la seguridad ciudadana	
14481	14477	001036250020	Caso específico de no realización del derecho a la seguridad ciudadana en términos de políticas públicas	
14482	14476	001036255	Violaciones al derecho a la seguridad ciudadana en términos de legislación	
14483	14482	001036255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la seguridad ciudadana	
14484	14482	001036255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la seguridad ciudadana	
14485	14482	001036255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la seguridad ciudadana	
14486	14482	001036255020	Caso específico de no realización del derecho a la seguridad ciudadana en términos de legislación	
14487	14476	001036260	Violaciones al derecho a la seguridad ciudadana en términos de resoluciones judiciales	
14488	14487	001036260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la seguridad ciudadana	
14490	14487	001036260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la seguridad ciudadana	
14491	14487	001036260020	Caso específico de no realización del derecho a la seguridad ciudadana en términos de resoluciones judiciales	
14493	14492	001037250	Violaciones al derecho a la protección frente al abuso de poder en términos de políticas públicas	
14494	14493	001037250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la protección frente al abuso de poder	
14495	14493	001037250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la protección frente al abuso de poder	
14496	14493	001037250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a la protección frente al abuso de poder	
14497	14493	001037250020	Caso específico de no realización del derecho a la protección frente al abuso de poder en términos de políticas públicas	
14498	14492	001037255	Violaciones al derecho a la protección frente al abuso de poder en términos de legislación	
14499	14498	001037255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a la protección frente al abuso de poder	
14500	14498	001037255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la protección frente al abuso de poder	
14501	14498	001037255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la protección frente al abuso de poder	
14502	14498	001037255020	Caso específico de no realización del derecho a la protección frente al abuso de poder en términos de legislación	
14503	14492	001037260	Violaciones al derecho a la protección frente al abuso de poder en términos de resoluciones judiciales	
14504	14503	001037260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho protección frente al abuso de poder	
14505	14503	001037260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho protección frente al abuso de poder	
14506	14503	001037260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho protección frente al abuso de poder	
14507	14503	001037260020	Caso específico de no realización del derecho protección frente al abuso de poder en términos de resoluciones judiciales	
14509	11253	001105010	Bloqueo de vías de comunicación	
12330	12326	001140250020	Caso específico de no realización del derecho a votar en términos de políticas públicas	
14512	10	001250	Violaciones a los derechos civiles y políticos en términos de políticas públicas	
14513	14512	001250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos civiles y políticos	
14515	14512	001250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos civiles y políticos	
14516	14512	001250020	Caso específico de no realización de los derechos civiles y políticos en términos de políticas públicas	
14517	10	001255	Violaciones a los derechos civiles y políticos en términos de legislación	
14518	14517	001255005	Falta de adopción de legislación que respete, proteja y garantice los derechos civiles y políticos	
14519	14517	001255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos civiles y políticos	
14520	14517	001255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos civiles y políticos	
14521	14517	001255020	Caso específico de no realización de los derechos civiles y políticos en términos de legislación	
14522	10	001260	Violaciones a los derechos civiles y políticos en términos de resoluciones judiciales	
14523	14522	001260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos civiles y políticos	
14524	14522	001260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos civiles y políticos	
14525	14522	001260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos civiles y políticos	
14526	14522	001260020	Caso específico de no realización de los derechos civiles y políticos en términos de resoluciones judiciales	
14527	11275	002015005	Falta de oportunidades de empleo	
14528	11277	002025020	Destrucción de vivienda	
14529	11266	002250	Violaciones a los derechos económicos, sociales, culturales y ambientales en términos de políticas públicas	
14532	14529	002250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos económicos, sociales, culturales y ambientales	
14533	14529	002250020	Caso específico de no realización de los derechos económicos, sociales, culturales y ambientales en términos de políticas públicas	
14534	11266	002255	Violaciones a los derechos económicos, sociales, culturales y ambientales en términos de legislación	
14535	14534	002255005	Falta de adopción de legislación que respete, proteja y garantice los derechos económicos, sociales, culturales y ambientales	
14536	14534	002255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos económicos, sociales, culturales y ambientales	
14537	14534	002255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos económicos, sociales, culturales y ambientales	
9030	8022	016103	Venustiano Carranza	
14538	14534	002255020	Caso específico de no realización de los derechos económicos, sociales, culturales y ambientales en términos de legislación	
14539	11266	002260	Violaciones a los derechos económicos, sociales, culturales y ambientales en términos de resoluciones judiciales	
14541	14539	002260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos económicos, sociales, culturales y ambientales	
14542	14539	002260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos económicos, sociales, culturales y ambientales	
14543	14539	002260020	Caso específico de no realización de los derechos económicos, sociales, culturales y ambientales en términos de resoluciones judiciales	
11323	11322	003035005	Violaciones al derecho de las niñas y los niños a expresarse y ser escuchada(o)s	
14544	135	004	Violaciones a los derechos de los pueblos	
14546	14545	004005005	Concesión de licencias para la explotación de recursos naturales, limitando su acceso a las poblaciones locales	
14547	14545	004005250	Violaciones al derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de políticas públicas	
14549	14547	004005250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14550	14547	004005250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14551	14547	004005250020	Caso específico de no realización del derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de políticas públicas	
14552	14545	004005255	Violaciones al derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de legislación	
14553	14552	004005255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14554	14552	004005255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14555	14552	004005255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el  derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14556	14552	004005255020	Caso específico de no realización del derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de legislación	
14557	14545	004005260	Violaciones al derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de resoluciones judiciales	
14558	14557	004005260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14559	14557	004005260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14560	14557	004005260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14561	14557	004005260020	Caso específico de no realización del derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales en términos de resoluciones judiciales	
14563	14562	004010250	Violaciones al derecho de los pueblos a la autodeterminación en términos de políticas públicas	
14564	14563	004010250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos a la autodeterminación	
14565	14563	004010250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de los pueblos a la autodeterminación	
14566	14563	004010250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos a la autodeterminación	
14567	14563	004010250020	Caso específico de no realización del derecho de los pueblos a la autodeterminación en términos de políticas públicas	
14568	14562	004010255	Violaciones al derecho de los pueblos a la autodeterminación en términos de legislación	
14569	14568	004010255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de los pueblos a la autodeterminación	
14570	14568	004010255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de los pueblos a la autodeterminación	
14571	14568	004010255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el  derecho de los pueblos a la autodeterminación	
14572	14568	004010255020	Caso específico de no realización del derecho de los pueblos a la autodeterminación en términos de legislación	
14573	14562	004010260	Violaciones al derecho de los pueblos a la autodeterminación en términos de resoluciones judiciales	
14574	14573	004010260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos a la autodeterminación	
14575	14573	004010260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de los pueblos a la autodeterminación	
14576	14573	004010260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos a la autodeterminación	
14577	14573	004010260020	Caso específico de no realización del derecho de los pueblos a la autodeterminación en términos de resoluciones judiciales	
14578	14544	004015	Violaciones al derecho de los pueblos a la paz	
14579	14578	004015250	Violaciones al derecho de los pueblos a la paz en términos de políticas públicas	
14580	14579	004015250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos a la paz	
14581	14579	004015250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de los pueblos a la paz	
14582	14579	004015250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos a la paz	
14584	14578	004015255	Violaciones al derecho de los pueblos a la paz en términos de legislación	
14585	14584	004015255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de los pueblos a la paz	
14586	14584	004015255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de los pueblos a la paz	
14587	14584	004015255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el  derecho de los pueblos	
14588	14584	004015255020	Caso específico de no realización del derecho de los pueblos a la paz en términos de legislación	
14589	14578	004015260	Violaciones al derecho de los pueblos a la paz en términos de resoluciones judiciales	
14590	14589	004015260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos a la paz	
14591	14589	004015260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de los pueblos a la paz	
14592	14589	004015260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos a la paz	
14593	14589	004015260020	Caso específico de no realización del derecho de los pueblos a la paz en términos de resoluciones judiciales	
14595	14594	004020005	No adopción de medidas contra la bioprospección hecha sin la participación de las poblaciones locales 	
14596	14594	004020250	Violaciones al derecho de los pueblos al desarrollo en términos de políticas públicas	
14597	14596	004020250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos al desarrollo	
14598	14596	004020250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de los pueblos al desarrollo	
14599	14596	004020250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos al desarrollo	
14600	14596	004020250020	Caso específico de no realización del derecho de los pueblos al desarrollo en términos de políticas públicas	
14601	14594	004020255	Violaciones al derecho de los pueblos al desarrollo en términos de legislación	
14602	14601	004020255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de los pueblos al desarrollo	
14603	14601	004020255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de los pueblos al desarrollo	
14604	14601	004020255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el  derecho de los pueblos al desarrollo	
14605	14601	004020255020	Caso específico de no realización del derecho de los pueblos al desarrollo en términos de legislación	
14606	14594	004020260	Violaciones al derecho de los pueblos al desarrollo en términos de resoluciones judiciales	
14608	14606	004020260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de los pueblos al desarrollo	
14609	14606	004020260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos al desarrollo	
14610	14606	004020260020	Caso específico de no realización del derecho de los pueblos al desarrollo en términos de resoluciones judiciales	
14627	14544	004030	Violaciones a los derechos de los pueblos indígenas	
14628	14627	004030005	Violaciones al derecho de los pueblos indígenas a la autonomía política, económica y social	
14629	14627	004030010	Violaciones al derecho de los pueblos indígenas a la consulta y participación	
14630	14627	004030015	Violaciones al derecho de los pueblos indígenas a la jurisdicción indígena	
14631	14627	004030020	Violaciones al derecho de los pueblos indígenas a la personería jurídica	
14632	14627	004030025	Violaciones al derecho de los pueblos indígenas a la tierra y territorio	
14633	14627	004030030	Violaciones al derecho de los pueblos indígenas a su cultura, identidad y educación	
14634	14627	004030250	Violaciones a los derechos de los pueblos indígenas en términos de políticas públicas	
14635	14634	004030250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de los pueblos indígenas	
14636	14634	004030250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de los pueblos indígenas	
14637	14634	004030250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de los pueblos indígenas	
14638	14634	004030250020	Caso específico de no realización de los derechos de los pueblos indígenas en términos de políticas públicas	
14639	14627	004030255	Violaciones a los derechos de los pueblos indígenas en términos de legislación	
14640	14639	004030255005	Falta de adopción de legislación que respete, proteja y garanticen los derechos de los pueblos indígenas	
14641	14639	004030255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de los pueblos indígenas	
14642	14639	004030255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de los pueblos indígenas	
14643	14639	004030255020	Caso específico de no realización de los derechos de los pueblos indígenas en términos de legislación	
14644	14627	004030260	Violaciones a los derechos de los pueblos indígenas en términos de resoluciones judiciales	
14645	14644	004030260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de los pueblos indígenas	
14646	14644	004030260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de los pueblos indígenas	
14647	14644	004030260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de los pueblos indígenas	
14648	14644	004030260020	Caso específico de no realización de los derechos de los pueblos indígenas en términos de resoluciones judiciales	
14649	14544	004250	Violaciones a los derechos de los pueblos en términos de políticas públicas	
14650	14649	004250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de los pueblos	
14652	14649	004250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de los pueblos	
14653	14649	004250020	Caso específico de no realización de los derechos de los pueblos en términos de políticas públicas	
14654	14544	004255	Violaciones a los derechos de los pueblos en términos de legislación	
9042	8015	004002	Campeche	
14655	14654	004255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de los pueblos	
14656	14654	004255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de los pueblos	
14657	14654	004255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de los pueblos	
14658	14654	004255020	Caso específico de no realización de los derechos de los pueblos en términos de legislación	
14659	14544	004260	Violaciones a los derechos de los pueblos en términos de resoluciones judiciales	
14660	14659	004260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de los pueblos	
14661	14659	004260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de los pueblos	
14662	14659	004260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de los pueblos	
14663	14659	004260020	Caso específico de no realización de los derechos de los pueblos en términos de resoluciones judiciales	
13249	13247	003060010	Derecho de las y los defensore(a)s a hacer críticas y propuestas en materia de derechos humanos	
14468	14460	004030255	Derechos de los pueblos indígenas en términos de legislación	
14467	14460	004030250	Derechos de los pueblos indígenas en términos de políticas públicas	
11491	11490	003	Familia	
11495	11490	018	Población en general	
22	127	009	Amuzgo	Oaxaca. Usado por: Tzjonnon, tzo'tyio, tzañcue
11	127	006	Akateko	
28	127	012	Awakateko	Originarios de Aguacatán, Huehuetenango, Guatemala
11483	127	213	Zoque	Usado por: O'depüt
11481	127	207	Yaqui	Usado por: Yoremes
11479	127	201	Tseltal	Usado por Tzeltal, Winikatel, k'op
11478	127	198	Triqui	Usado por: Triquis, driquis, Tinujei, driki
11476	127	192	Tojolabal	Usado por: Tojolwinik'otik
11475	127	189	Tlahuica	Usado por: Ocuilteco
11473	127	183	Tepehuano del sur	Usado por: O'dam
11471	127	177	Tepehua	Usado por: Hamasipine
11470	127	174	Teko	Usado por: Teco, tectitecos
11469	127	171	Tarasco	Usado por: Purépecha
11467	127	165	Seri	Usado por: Konkaak, conca'ac, Konkaak
11464	127	156	Q’eqchí’	Originarios de Alta Verapaz, Guatemala. Usado por: Kekchi, Kekchí
11461	127	147	Popoloca	
11462	127	150	Popoluca de la Sierra	Veracruz. Usado por: Popoluca. Ver también: Oluteco,  Sayulteco y Texistepequeño
11460	127	144	Pima	Usado por: O'oob, Otam
11457	127	135	Paipai	
11458	127	138	Pame	Incluye: Pames de Querétaro, Pames de San Luis Potosí. Usado por: Xi'ui
11454	127	123	Náhuatl	
11453	127	120	Mixteco	Guerrero, Puebla y Oaxaca. Usado por: Nuusavi
11451	127	114	Mestizo	
11452	127	117	Mixe	norte de Oaxaca. Usado por: Ayuukjä'äy, ayuuk, ayook
11449	127	108	Mazateco	Oaxaca. Usado por: Hashutaenima
67	127	099	Maya	Quintana Roo, Campeche y Yucatán
65	127	093	Mam	Campeche, Quintana Roo y Chiapas. Originarios de los Altos Cuchumatanes, Huehuetenango, Guatemala . Usado por: Mame,  Qyool
64	127	090	Lacandón	Chiapas. Usado por: Hach winik, hachtan
63	127	087	Kumiai	Usado por: Ti'pai, kamia
61	127	081	Kiliwa	Usado por: Chikapw, kikapooa
60	127	078	Kickapoo	Coahuila. Usado por: Kikapú, Kikapúes, Chikapw, kikapooa
46	127	063	Ixcateco	
45	127	060	Huichol	Jalisco, Nayarit, Zacatecas y Durango. Usado por: Wirraritari, wixarika
44	127	057	Huave	Oaxaca. Usado por: Meroikook
41	127	048	Cuicateco	Usado por: Nduuduyo
38	127	042	Cora	Nayarit. Usado por: Nayeri, nayeeri
36	127	036	Chontal de Tabasco	Usado por: Chontal; Yokot'anob, yokot'an,fane
35	127	033	Chontal de Oaxaca	Usado por: Chontal; Slijuala xanuc'
32	127	024	Chinanteco	Oaxaca. Usado por: Tsajujmí'
29	127	015	Ayapaneco	
30	127	018	Chatino	sur de Oaxaca. Usado por Kitsecha'tnio, cha'cña
14665	127	126	Otro origen étnico	
11675	11670	006	Dirección temporal	
11674	11670	005	Dirección anterior	
11673	11670	004	Dirección alternativa	
101	100	003	Abogado(a) de la víctima	
102	100	006	Amigo(a) o conocido(a) de la víctima	
103	100	009	Amigo(a) o conocido(a) del perpetrador	
13746	100	036	Investigador(a)	
13756	100	066	Proveedor(a) de servicio médico	
13757	100	069	Reportero(a)	
13758	100	072	Testigo(a) del evento	
14666	100	031	Funcionario(a) público(a)	
13634	57	002030	Declaración firmada 	
13654	57	002072	Recomendación de organismo intergubernamental de derechos humanos	
13653	57	002070	Recomendación de organismo público de derechos humanos	
14668	57	002078	Sentencia de tribunal administrativo o judicial	
14673	13689	008001	Artículo académico	
13568	13566	002008004	Canalización a organismo público de derechos humanos	
13772	13769	010006	Visita in situ de organismo intergubernamental de derechos hummanos	
13773	92	012	Comunicación con organismos intergubernamentales	
14315	2	001010	Abogado(a), Defensor(a) público(a)	Se utiliza para el defensor(a) de oficio
159	1	T18	Grado de involucramiento	
307	2	001115	Empleado(a) en procuraduría	
14314	2	001005	Abogado(a) particular	
312	2	001150	Fiscal	Procurador(a), Ministerio Público
319	2	001185	Militar (general, jefe u oficial)	Usar para: General, Mayor, Teniente Coronel y Coronel, Subteniente, Teniente, Capitán Segundo y Capitán Primero
325	2	001225	Policía	Usar para todos los tipos de policía: tránsito, seguridad pública, etc.; excepto investigadora 
326	2	001230	Policía investigador(a)	AFI, Policía Ministerial, Policía Judicial
330	2	001255	Profesionista	Cualquier otro profesionista que no esté especificado en la lista
9051	8015	004011	Candelaria	
14321	48	002	Actividad de persona colectiva	Las actividades colectivas están sacadas del INEGI: Sistema de Clasificación Industrial de América del Norte 2002 (SCIAN 2002), desglosando la clasificación de Actividades de gobierno y añadiendo las actividades de la delincuencia
14327	14321	002030	Comercio al mayoreo y menudeo	Incluyendo materias primas y la intermediación y comercio al por mayor por medios masivos de comunicación y otros medios
14329	14321	002040	Delincuencia común	Aplica a todo tipo de delincuencia, excepto a delincuencia organizada
14330	14321	002050	Electricidad, agua y suministro de gas	Incluye generación, transmisión y suministro de energía eléctrica, captación tratamiento y suministro de agua, suministro de gas por ductos al consumidor final
14331	14321	002055	Impartición de justica	Aplica a actividad judicial
14332	14321	002060	Industria extractiva	Incluye, extracción de petróleo y gas, minería de carbón mineral, minerales metálicos y no metálicos y servicios relacionados con la minería
14333	14321	002065	Industria manufacturera	Industrias: alimentaria, bebidas y tabaco, insumos textiles, confección de productos textiles,  prendas de vestir, industria de la madera (aserradero, fabricación de laminados ya glutinados, otros productos), impresión e industrias conexas, fabricación de productos derivados del petróleo y del carbón, industria química y farmacéutica, industria del plástico y el hule, productos a base de minerales no metálicos (vidrio, arcillas, cemento, cal, yeso), industrias metálicas básicas (hierro, acero, aluminio, metales no ferrosos), fabricación de productos metálicos, fabricación de maquinaria y equipo (incluyendo equipo de computo, comunicación, y componentes y accesorios electrónicos),  equipo de generación eléctrica, fabricación de equipo de transporte (todo tipo de vehículos de tierra, aire y agua), fabricación de muebles y productos relacionados, fabricación de equipo y material para uso médico, dental y para laboratorio y otras industrias manufactureras
14676	14321	002045	Delincuencia organizada	Ej. Narcotráfico, Trata de personas, Tráfico de personas
14328	14321	002035	Construcción	Edificación, trabajos especializados para la construcción, construcción de obras de ingeniería civil u obra pesada
14339	14321	002095	Servicios de apoyo a los negocios y manejo de desechos y servicios de remediación (en el contexto de la contaminación)	Administración de negocios, de apoyo en instalaciones, servicios de empleo, servicios de apoyo secretarial, fotocopiados, cobranza, investigación crediticia y similares. Agencias de viajes y servicios de reservaciones, de investigación, protección y seguridad, de limpieza, manejo de desechos y remediación
14347	14321	002135	Transportes, correos y almacenamiento	Terrestre, aéreo o por agua, transporte de carga, mudanzas. Transporte por ductos (petróleo, gas y otros productos), transporte turístico, servicios relacionados con el transporte. Servicios de mensajería y paquetería. Servicios de almacenamiento
13776	92	014	Petición a otras ONG	
13777	13776	014002	Petición a otras ONG nacionales	
13778	13776	014004	Petición a otras ONG internacionales	
13780	13779	016002	Medidas de protección ante organismo público de derechos humanos	
13781	13779	016004	Medidas de protección ante organismo intergubernamental de derechos humanos	
13783	13782	018002	Queja o petición ante organismo público de derechos humanos	
13784	13782	018004	Queja o petición ante organismo intergubernamental de derechos humanos	
113	1	T48	Tipo de fecha	
13517	11728	005	Caso urgente	
13518	11728	010	Caso de prioridad alta	
13519	11728	015	Caso de prioridad media	
13520	11728	020	Caso de prioridad baja	
13521	11728	025	Expediente cerrado	
278	131	016	En sociedad de convivencia	
277	131	014	Con compañero(a)	
276	131	012	En unión libre	
275	131	010	Divorciado(a)	
274	131	008	Separado(a)	
273	131	006	Viudo(a)	
126	131	004	Casado(a)	
132	131	002	Soltero(a)	
287	124	030	Carrera técnica o comercial	
291	124	042	Doctorado	
290	124	039	Maestría	
289	124	036	Profesional	
288	124	033	Profesional incompleta	
286	124	027	Normal	
284	124	021	Preparatoria o bachillerato incompleto	
283	124	018	Secundaria completa	
282	124	015	Secundaria incompleta	
281	124	012	Primaria completa	
280	124	009	Primaria incompleta	
279	124	006	Preescolar	
125	124	003	Ninguna instrucción escolar	
14674	11670	003	Dirección institucional	
121	1	T15	Países	
11609	121	001000000	Otros países (África, Asia y Oceanía)	
53	1	T01	Temas	
127	1	T13	Origen étnico	
56	1	T16	Fuente de información	
100	1	T19	Conexión de la fuente con la información	
92	1	T20	Tipo de intervención	
54	1	T23	Características relevantes	
154	1	T25	Estatus de la víctima	
172	1	T26	Estatus del perpetrador	
147	1	T41	Estatus de la VDH	
117	1	T43	Monitoreo del caso	
14675	12544	033005	Reglamento, decreto municipal	
50	1	T70	Edad de la víctima cuando ocurrió acto	
14345	14321	002125	Servicios inmobiliarios y de alquiler	Servicios inmobiliarios y de alquiler de bienes muebles e inmuebles, alquiler de automóviles, camiones y otros transportes terrestres, alquiler de artículos, bienes raíces
14344	14321	002120	Servicios financieros y de seguros	Bancos, instituciones de intermediación crediticia y financiera, actividades bursátiles, compañías de fianzas, seguros y pensiones, actividades cambiarias
14342	14321	002110	Servicios de salud y asistencia social	Servicios médicos, dentales, laboratorios médicos y de diagnóstico, enfermería a domicilio, ambulancias, bancos de órganos, servicios auxiliares de tratamiento médico, hospitales, residencias de asistencia social y para el cuidado de la salud, asilos, orfanatos, servicios de orientación y trabajo social, servicios comunitarios de alimentación, refugio y emergencia, de capacitación para el trabajo para personas desempleadas, subempleadas o discapacitadas, guarderías
14399	154	060	Cooptado(a)	Controlado o asimilado a las políticas del gobierno o empresa a cambio de cargos, favores o coerción
9059	8018	012008	Atenango del Río	
14334	14321	002070	Información en medios masivos	Edición de publicaciones y software, industria fílmica, de video y del sonido, radio y televisión, por cable y satélite, creación y difusión de contenido a través de Internet, telefonía, telegrafía, servicios de satélite, servicios de búsqueda por Internet, procesamiento electrónico de información, hospedaje de páginas web y otros servicios relacionados
14341	14321	002105	Servicios de reparación y mantenimiento y servicios personales	Reparación y mantenimiento en general, salones y clínicas de belleza, baños públicos, lavanderías y tintorerías, servicios funerarios, administración de cementerios, estacionamientos y pensiones para automóviles, revelado de fotografías
14326	14321	002025	Agricultura, ganadería, aprovechamiento forestal, pesca y caza	Incluye cultivo de granos y semillas, hortalizas, frutas y nueces, en invernaderos y viveros, floricultura, otros cultivos. Explotación de bovinos, porcinos, avícola, ovinos y caprinos, acuicultura animal, otros animales. Silvicultura, viveros forestales y recolección de productos forestales, tala de árboles. Pesca y caza. Servicios relacionados con las actividades agropecuarias y forestales
14324	14321	002015	Actividades políticas, sindicales, y cívicas	Asociaciones comerciales, laborales, profesionales, y recreativas, religiosas, políticas y civiles
345	2	001300	Vendedor(a) ambulante	Persona que vende mercancías ya sea en un puesto en la calle, o de casa en casa
14317	2	001190	Militar de tropa	Usar para Soldado, Cabo, Sargento Segundo y Sargento Primero
306	2	001110	Empleado(a) en otro oficio	Diferente a construcción, industria, mina y cantera, prostitución, trabajo doméstico, protección y vigilancia y peón en el campo
12544	11729	033	Legislación estatal	Abrir esta categoría para reglamentos, etc. de nivel municipal
12549	11729	050	Leyes, declaraciones, códigos, reglamentos y decretos de entidades no estatales	Ej: Municipios autónomos
14173	14067	065025	Declaración sobre los principios fundamentales relativos a la contribución de los medios de comunicación de masas al fortalecimiento de la paz y la comprensión internacional, a la promoción de los derechos humanos y a la lucha contra el racismo, el apartheid y la incitación a la guerra (1978)	
14174	14131	120020	Declaración sobre los principios sociales y jurídicos relativos a la protección y el bienestar de los niños, con particular referencia a la adopción y la colocación en hogares de guarda, en los planos nacional e internacional (1986)	
14159	14145	130010	Principios de ética médica aplicables a la función del personal de salud, especialmente los médicos, en la protección de personas presas y detenidas contra la tortura y otros tratos o penas crueles, inhumanos o degradantes (1982)	
14177	14152	135050	Principios y directrices básicos sobre el derecho de las víctimas de violaciones manifiestas de las normas internacionales de derechos humanos y de violaciones graves del derecho internacional humanitario a interponer recursos y obtener reparaciones (2005)	
14198	14195	160015	Protocolo de Estambul (1999)	Nombre completo: Manual para la investigación y documentación eficaces de la tortura y otros tratos o penas crueles, inhumanos o degradantes
14212	14203	165030	Protocolo para prevenir, reprimir y sancionar la trata de personas, especialmente mujeres y niños, que complementa la Convención de las Naciones Unidas contra la delincuencia organizada transnacional (2000)	
13632	57	002032	Declaración oficial	Aplica a posicionamiento final conjunto
13665	13633	004018	Declaración de organización nacional	Aplica a posicionamiento final conjunto
14670	13633	004031	Servicio de información de organización nacional	Aplica a servicios de noticias o información elaborados o  recopilados y distribuidos por una organización nacional
13681	58	006018	Declaración de organización internacional	Aplica a posicionamiento final conjunto
14672	58	006031	Servicio de información de organización internacional	Aplica a servicios de noticias o información elaborados o  recopilados y distribuidos por una organización internacional
13709	13701	010016	Información en internet	Aplica a información en internet diferente a la especificada en la lista de información de medios de comunicación.  Incluye Wikipedia y otras fuentes de información que sólo se encuentran en internet
13711	13701	010020	Radio	Incluye información de radios comunitarias
11547	11488	111	Mixe	Usado por: Ayook o ayuuk. Pertenece a la Familia mixe-zoque
11549	11488	117	Náhuatl	Pertenece a la Familia yuto-nahua
11551	11488	123	Otomí	Usado por: Ñahñú o hñä hñü. Pertenece a la Familia oto-mangue
11553	11488	132	Pame	Usado por: Pame del norte; Pame del sur; Xigüe o Xi´ui. Pertenece a la Familia oto-mangue
11556	11488	141	Popoloca	Usado por: Popolocano, Lenguas popolocas. Pertenece a la Familia oto-mangue
11558	11488	147	Q’anjob’al	Usado por: Kanjobal; k´anjobal. Pertenece a la Familia maya
11562	11488	159	Seri	Pertenece a la Familia seri
11563	11488	162	Tarahumara	Usado por: Rarámuri. Pertenece a la Familia yuto-nahua
11564	11488	165	Tarasco	Usado por: Purépecha. Pertenece a la Familia tarasca
11567	11488	174	Tepehuano del norte	Ver también: Tepehuano del sur. Pertenece a la Familia yuto-nahua 
11570	11488	183	Tlahuica	Usado por: Ocuilteco. Pertenece a la Familia oto-mangue
11571	11488	186	Tojolabal	Usado por: Tojolwinik otik. Pertenece a la Familia maya
11574	11488	195	Tseltal	Usado por: Tzeltal; K´op o winik atel. Pertenece a la Familia maya
11576	11488	201	Yaqui	Usado por: Yoreme. Pertenece a la Familia yuto-nahua
11578	11488	207	Zoque	Usado por: O´de püt; Zoque de Chiapas; Zoque de Oaxaca. Pertenece a la Familia mixe-zoque
11487	11486	005	Alemán	
11496	11486	010	Árabe	
11497	11486	015	Búlgaro	
11498	11486	020	Checo	
11499	11486	025	Chino	
11500	11486	030	Coreano	
11501	11486	035	Español	
11502	11486	040	Francés	
11503	11486	045	Húngaro	
11504	11486	050	Inglés	
11505	11486	055	Italiano	
11506	11486	060	Japonés	
11507	11486	065	Lenguaje de signos	
11508	11486	070	Persa	
11509	11486	075	Portugués	
11510	11486	080	Rumano	
11511	11486	085	Ruso	
14394	154	020	Bajo investigación en detención	Arraigado
14395	154	040	Clausurado	Aplica a personas colectivas
14396	154	045	Con derechos suspendidos	Aplica a personas colectivas
14398	154	055	Con registro suspendido	Aplica a personas colectivas
14402	154	110	Disuelto(a), desmantelado(a), desarticulado(a)	Aplica a personas colectivas
14403	154	115	En litigio	Aplica a personas individuales y colectivas
14404	154	120	En quiebra	Aplica a personas colectivas
14405	154	145	Ocupado(a), tomado(a)	Aplica a personas colectivas
14406	154	150	Privatizado(a)	Aplica a personas colectivas
14407	154	165	Regresó a su condición original	Aplica cuando la víctima es restituida a la situación previa a la VDH o al acto. Ej. Una persona que resultó herida, pero se curó sin secuelas físicas posteriores. No aplica a "Liberado(a)"; "Encontrado(a) después de estar desaparecido (a) un tiempo"; "Reintegrado(a) al empleo"; "Retornado(a) a su lugar de origen"
14409	154	200	Vandalizado(a), dañado(a)	Aplica a personas colectivas. Aplica a casos donde lugares físicos de personas colectivas son afectados.  Ej. Oficina asaltada y destruida parcialmente
14410	154	205	Vulnerado(a) en su legalidad, deslegitimado(a), debilitado(a)	Aplica a casos donde organizaciones o personas ven afectada o vulnerada su legitimidad o legalidad, o se ven debilitadas como consecuencia de una violación a los derechos humanos. Ej. El líder de una organización es falsamente acusado y detenido lo cual afecta su legitimidad. Una organización se ve debilitada después de una serie de amenazas recibidas
12571	142	001	Lugar relacionado con la víctima	Casa de la víctima, casa de familiar de la víctima; casa de una persona relacionada con la víctima; lugar de trabajo de la víctima; negocio propiedad de la víctima; tierra propiedad de la víctima o donde desarrolla trabajo de campo agrícola o ganadero: parcela, potrero, trabajadero
12572	142	002	Lugar de servicio o actividad comercial, industrial o financiera	Excepto cuando se trate de un lugar relacionado con la víctima. Ej. Institución pública de prestación de servicios; institución de servicio privada con fines de lucro; institución de servicio privada sin fines de lucro, incluyendo ONG; empresa comercial; oficina o instalación de negocios; banco o institución financiera; fábrica o centro industrial; centro comercial; tienda; hotel, restaurante, bar o establecimiento similar
144	142	005	Instalación de fuerzas de seguridad civiles y/o militares y de instituciones de procuración de justicia	
146	144	005005	Instalación militar	
12556	146	005005010	Cuartel militar	
12557	146	005005015	Campo o base militar	
5422	144	005010	Oficina de procuración de justicia o instalación de policía	
12574	142	004	Oficinas o instalaciones de gobierno	Oficinas o instalaciones de gobierno que no sean de prestación de servicios, educativas, de salud, de justicia o de seguridad. Incluye instalaciones federales, estatales, municipales y comunitarias
12555	146	005005005	Puesto de control militar 	Se asume móvil o temporal. (Retenes militares)
12559	5422	005010010	Puesto de control policial	Se asume móvil o temporal. (Retenes policiacos)
12560	144	005015	Oficina o instalación migratoria	
12561	12560	005015005	Estación migratoria 	
12562	12560	005015010	Puesto de control migratorio	Se asume móvil o temporal. (Retenes migratorios)
12563	144	005020	Oficina o instalación del servicio de inteligencia o servicio secreto	
145	143	006005	Centro de reclusión	
12564	145	006005005	CERESO	
12565	145	006005010	CEFERESO	
12566	143	006010	Cárcel civil	Se refiere a las cárceles distritales, cárcel preventiva, cárceles municipales
12567	143	006015	Cárcel militar	Centro de reclusión en instalaciones militares
12568	143	006020	Cárcel especial	Las utilizadas de manera clandestina o ilegal
12569	143	006025	Cárcel comunitaria	Las utilizadas por las comunidades o pueblos como parte de sus usos y costumbres incluidas las de entidades no Estatales
12570	143	006030	Casa de seguridad	
14677	11488	126	Otra lengua	
14679	143	006035	Centro de arraigo	
11512	11488	006	Amuzgo	Usado por: Amuzga;  Amuzgo de Guerrero; Amuzgo de Oaxaca; Lenguas amuzgas; Tzañcue o tzjon noan. Pertenece a la Familia oto-mangue
11514	11488	012	Ayapaneco	Pertenece a la Familia mixe-zoque
11518	11488	024	Chocholteco	Usado por: Chocho; Chocholteca. Pertenece a la Familia oto-mangue
11521	11488	033	Chontal de Tabasco	Usado por: Chontal; Yokot´an. Pertenece a la Familia maya
11519	11488	027	Ch'ol	Usado por: Chol; Chol, Chiapas y Tabasco; Lenguas choles; Winik. Pertenece a la Familia maya
11524	11488	042	Cucapá	Usado por: Es-pei. Pertenece a la Familia cochimí-yumana
11526	11488	048	Guajirío	Usado por: Varojío o macurawe. Pertenece a la Familia yuto-nahua
11528	11488	054	Huave	Usado por: Mero ikooc. Pertenece a la Familia huave
11530	11488	060	Ixcateco	Usado por: Ixcateca; Mero ikooa. Pertenece a la Familia oto-mangue
11533	11488	069	K’iche’	Usado por: Quiché. Pertenece a la Familia maya
11535	11488	075	Kickapoo	Usado por: Kikapú; Kikapoo; Kikapoa. Pertenece a la Familia álgica
11537	11488	081	Ku'ahl	Pertenece a la Familia cochimí-yumana
11539	11488	087	Lacandón	Usado por: Hach t´an o hach winik. Pertenece a la Familia maya
11542	11488	096	Maya	Pertenece a la Familia maya
11544	11488	102	Mazahua	Usado por: Jñatjo. Pertenece a la Familia oto-mangue
14680	143	006040	Institución para menores	Se aplica a cualquier institución donde se encuentren menores privados de su libertad
12575	142	007	Tribunal	Cualquier tribunal o juzgado de cualquier materia y nivel (federal, estatal, municipal), incluso los administrativos
12578	142	010	Lugar para la libre expresión, asociación o reunión	Local para reuniones; local sindical; local de partido político; local de ONG; local de organización de derechos humanos; local de medio de comunicación; local de institución religiosa o lugar de culto; centro de recreación (deportes, arte y cultura)
12579	142	011	Espacio público, baldío o desocupado	Monumento; plaza; parque, jardín, campo de juegos; calle, avenida, banqueta; cementerio; lote baldío; edificio desocupado; lugar ocupado sin autorización; drenaje, desagüe
12581	142	013	Centro u oficina de transporte	Estación de tren, sitio de taxis, aeropuerto, estación o terminal de autobuses, estación de metro o monorriel, muelle, puerto o embarcadero, estacionamiento
12583	142	015	Lugar internacional o sede diplomática	Oficina de organización intergubernamental (ej. Delegación ONU); embajada, consulado, cruce fronterizo
13452	13448	003060260020	Caso específico de no realización de los derechos de las y los defensore(a)s en términos de resoluciones judiciales	
9072	8018	012021	Coyuca de Benítez	
12585	142	017	Lugar relacionado con grupos armados irregulares	Campo de entrenamiento "militar" de grupos armados irregulares de oposición, de grupos delictivos, de grupos paramilitares, instalación guerrillera, lugar secreto, especial o clandestino de alguno de estos grupos, incluyendo casas de seguridad de narcotraficantes o secuestradores
14682	14681	018005	País	Ej. Privatización de PEMEX
14686	14681	018025	Comunidad	Ej. Agresión a toda una comunidad
14690	142	019	Lugar privado	Lugar privado no comercial. Ej. Casa particular, rancho particular. No usar para  lugares relacionados con la víctima, ni para lugares de servicio o comerciales
12438	53	100	Criminalización de la protesta social	Se entiende como la judicialización de los conflictos sociales, es decir acusar y enjuiciar a integrantes de movimientos sociales a causa de sus protestas
250	53	330	Migración internacional	Se entiende a la migración en sentido amplio y por tanto comprende la transmigración
138	15	001025	Derecho al acceso a la justicia	Incluye debido proceso, recurso efectivo y garantías judiciales. Cfr. Artículo Ligia Bolívar, IIDH.  Se aplica tanto a los acusados como a las víctimas del delito y de violación a derechos humanos.  Hay derechos generales que aplican a ambos, como fiscal y tribunal imparcial, y existen algunos que sólo aplican a los acusados (ej. Presunción de inocencia) y otros sólo a las víctimas del delito o de violaciones a los derechos humanos (ej. reparación del daño)
11105	11101	003020045	Derecho de los y las trabajadore(a)s a la negociación colectiva	Incluye contratación colectiva
13248	13247	003060005	Derecho de las y los defensore(a)s a promover y procurar la protección y realización de los derechos humanos	Derecho a defender los derechos humanos
14440	14439	004005	Derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	Este derecho aplica tanto al pueblo de México en general, como a los Pueblos indígenas en particular
14444	14439	004010	Derecho de los pueblos a la autodeterminación	Este derecho aplica tanto al pueblo de México en general, como a los Pueblos indígenas en particular
11177	13	001010035	Uso desproporcionado o indebido de la fuerza pública	Se utiliza independientemente de si el uso de la fuerza es justificado o no, legal o no, cuando este uso de la fuerza es desproporcionado (cuando no es proporcional a lo estrictamente necesario). La utilización de la fuerza debe ser una medida excepcional. Cfr. Código de conducta para funcionarios encargados de hacer cumplir la ley. Adoptado por la Asamblea General en su resolución 34/169, de 17 de diciembre de 1979
89	53	020	Agrario, campo	Comprende todo lo que se refiere a la problemática económica y política que sucede en el campo, incluidos los conflictos de tierra
14302	53	037	Asesinatos en contexto de inseguridad	Asesinatos / ejecuciones cometidas por parte de la delincuencia organizada o de cuerpos de seguridad aliados a ella
14311	53	275	Laboral	Comprende todo lo relacionado al mundo laboral: legislación, políticas y condiciones laborales, etc. Para el tema de "Empleo, desempleo", usa dicha categoría incluida en esta misma lista
222	53	300	Medio ambiente	Incluye lo que se refiere a problemas de contaminación. Para recursos naturales, asigna alguna de las categorías en esta misma lista "Agua" o "Recursos naturales"
241	53	340	Militarización	Supone la presencia cada vez más amplia de militares en ámbitos de responsabilidad que deben ser exclusivos de civiles
14312	53	375	Operativos	Asigna también otros temas para especificar el tipo de operativo: Militarización, Narcotráfico, etc.
11191	10	001025	Violaciones al derecho al acceso a la justicia	Incluye debido proceso, recurso efectivo y garantías judiciales. Cfr. Artículo Ligia Bolívar, IIDH.  Se aplica tanto a los acusados como a las víctimas del delito y de violación a derechos humanos.  Hay derechos generales que aplican a ambos, como fiscal y tribunal imparcial, y existen algunos que sólo aplican a los acusados (ej. Presunción de inocencia) y otros sólo a las víctimas del delito o de violaciones a los derechos humanos (ej. reparación del daño)
14681	142	018	Áreas geográficas: país, estado, municipio, comunidad	
14683	14681	018010	Estado	
14684	14681	018015	Municipio	
14685	14681	018020	Cabecera municipal	
14687	14681	018030	Área comunal	
14688	14681	018035	Barrio, colonia, paraje, ranchería	
14476	10	001036	Violaciones al derecho a la seguridad ciudadana	Aplica a actos de omisión de la autoridad, que no previene y no proporciona seguridad pública
14492	10	001037	Violaciones al derecho a la protección frente al abuso de poder	 Aplica a situaciones donde la autoridad o particulares utilizan de forma arbitraria o injustificada el poder (ya sea económico, político, etc.) que legalmente poseen. No se trata de actos ilegales, sino de que empleando sus facultades, las utilizan arbitrariamente, ejerciendo acciones innecesarias, intimidatorias con una gran carga de discrecionalidad. Ej. El caso del General Gallardo, al cual se le abrieron 13 averiguaciones previas, cada una después de una exoneración de la anterior. No puede hablarse de acciones ilegales, pero sí arbitrarias y discrecionales, con una intencionalidad de castigar.  Otro ejemplo son los operativos injustificados o arbitrarios, que nuevamente no son ilegales porque la autoridad tiene facultades para realizar operativos, pero cuando se hacen sin causa que amerite el operativo, como denuncias específicas o pruebas de que es necesario el operativo, causan molestia a la población y pueden ser utilizados para intimidar a comunidades
11845	11839	001025060030	Derecho a interponer recursos internacionales por VDH y VDI	"VDH":Violaciones a los derechos humanos, "VDI": Violación al derecho internacional
11158	12	001005030	Muerte en contexto de operaciones militares	Pérdida de la vida durante acciones dirigidas, ordenadas, planeadas, organizadas y ejecutadas por las Fuerzas Armadas.  Para los operativos de seguridad pública ejecutados por militares, usa "Muerte en contexto de operativos de seguridad pública".
11807	138	001025010	Derecho a un tribunal independiente e imparcial	
11036	15	001055	Derecho a la inviolabilidad de domicilio	Incluye lugar de residencia o asentamiento, puede aplicar a una comunidad , población desplazada, etc.  Ej. Incursión arbitraria/injustificada del ejército o policía en una comunidad. Si registras este derecho también puedes registrar el "Derecho a la vida privada".
11241	11239	001065010	Restricciones para publicar o difundir información	Ej. Recolectar o comprar todos los ejemplares de un periódico o una revista evitando el acceso a la misma
13102	11277	002025015	Expropiación arbitraria de la vivienda	Incluye expropiación de tierras
13312	11308	003020045	Violaciones al derecho de los y las trabajadore(a)s la negociación colectiva	Incluye contratación colectiva
14545	14544	004005	Violaciones al derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	Este derecho aplica tanto al pueblo de México en general, como a los Pueblos indígenas en particular
14562	14544	004010	Violaciones al derecho de los pueblos a la autodeterminación	Este derecho aplica tanto al pueblo de México en general, como a los Pueblos indígenas en particular
14664	11490	009	Institución pública	Aplica a cualquier  persona colectiva del sector público del poder ejecutivo, legislativo o judicial, de cualquier nivel, incluyendo las fuerzas armadas, empresas paraestatales, y organismos autónomos, descentralizados y desconcentrados
11493	11490	012	Comunidad	Aplica a comunidades geográficas, como comunidades rurales e indígenas, colonias, etc.  No aplica a otro tipo de comunidades como la comunidad gay
14348	160	001007	Encubrió el acto 	Obstruyó la investigación, cambió pruebas, etc.
162	159	003	Involucramiento en términos de legislación, resoluciones judiciales o establecimiento de políticas	El término legislación incluye reglamentos. Ej. Estaciones migratorias
12526	162	003001	Promovió la ley, resolución judicial o política violatoria de derechos humanos	Ej. Controversia constitucional de la CNDH y la PGR en contra de la despenalización del aborto en el DF.
161	159	004	Involucramiento en la implementación de leyes, resoluciones judiciales o políticas violatorias de los derechos humanos	Incluye aplicación de reglamentos. Incluye resoluciones judiciales generales sobre la aplicación de leyes y reglamentos. Ej. Legalización del Anatocismo (usura) por parte de la Suprema Corte en 1998
13752	100	054	Organización no gubernamental	No aplica a Organización gubernamental de derechos humanos. Ver categoría separada
13567	13566	002008002	Canalización a institución pública	Excepto organismo público de derechos humanos
13575	13566	002008014	Canalización a entidad privada	Diferente a organización no gubernamental, social o eclesial
12456	5429	001120	Funcionario(a) público(a)	Directores(as), Secretarios(as) de Estado, subsecretarios(as), Directores generales
14356	5429	001200	Población en general	Se utiliza para situaciones que afectan a toda la población. Ej. Privatización de PEMEX
14365	12504	003060	Grupo racista o de "odio"	Ej. Grupo antiinmigrante, homofóbico
14367	12504	003075	Institución pública	Ej. UNAM, CNDH, IFE, IFAI
14372	14371	004005	Menor de 18 años	Menor, niño, niña
14374	14371	004015	Mayor de 65 años	Persona adulta mayor
14411	172	030	Bajo investigación penal en detención	Arraigo
14413	172	040	Bajo investigación civil	Aplica a personas individuales y colectivas
14415	172	055	Bajo proceso civil	Aplica a personas individuales y colectivas
11494	11490	015	Grupo específico	Aplica a un grupo amplio de personas que comparten una característica común como puede ser género, grupo de edad, preferencia sexual, etnia o características de tipo económico, profesional, gremial o similares. No aplica a grupos organizados
11722	172	070	Sin sanción por sobreseimiento de proceso	Aplica a personas individuales y colectivas
11715	172	075	Procesado(a) y absuelto(a)	Aplica a personas individuales y colectivas
11717	172	080	Procesado(a) y sancionado(a) 	Aplica a personas individuales y colectivas
14418	172	110	Procesado(a) y sancionado(a) con multa	Aplica a personas individuales y colectivas
14419	172	115	Procesado(a) y sancionado(a) con suspensión de registro	Aplica a personas colectivas
14420	172	120	Procesado(a) y sancionado(a) con suspensión de derechos	Aplica a personas colectivas
14422	172	135	Beneficiado(a) con prerrogativas	Aplica a personas colectivas
174	172	145	Sin consecuencia alguna	Aplica a personas individuales y colectivas
114	113	002	Fecha aproximada	Aplica cuando se conoce la fecha con una aproximación de 3 días anteriores o posteriores
11349	171	005005005015	Institución pública federal	Excepto las instituciones y organismos desconcentrados, descentralizados y autónomos federales
11353	171	005005005030	Fuerzas federales de seguridad pública	Ej. PFP
11422	171	005005005035	Institución federal encargada de la procuración de justicia penal	Ej. PGR
11678	11422	005005005035005	Institución federal de investigación penal	Ej. AFI
14375	171	005005005055	Instancia de administración de justicia del ejecutivo federal / tribunal administrativo	Ej. Junta Federal de Conciliación y Arbitraje, Tribunal Superior Agrario, Tribunal Federal de Justicia Fiscal y Administrativa
11356	170	005005010015	Institución pública estatal	Excepto las instituciones y organismos desconcentrados, descentralizados y autónomos estatales.  Ej. DIF Estatal
11358	170	005005010025	Fuerzas estatales de seguridad pública	Policía de seguridad pública estatal
14376	170	005005010050	Instancia de administración de justicia del ejecutivo estatal / tribunal administrativo	Ej. Junta local de Conciliación y Arbitraje, Tribunal Estatal de lo contencioso administrativo
11362	11359	005005015015	Institución pública municipal	Ej.: Dif municipal
14378	14377	005005025005	Fuerzas de seguridad mixtas	Ej. BOM´s, Sistema Nacional de Seguridad Pública
14377	168	005005025	Autoridades combinadas/mixtas	Usar cuando interviene más de un nivel de gobierno
11383	11382	005015005005	Corte Suprema	Aplica únicamente a la SCJN
11384	11382	005015005010	Tribunal federal	Aplica únicamente a otro que NO sea la SCJN, ej.: TRIFE
11233	10	001055	Violaciones al derecho a la inviolabilidad de domicilio	Incluye lugar de residencia o asentamiento, puede aplicar a una comunidad , población desplazada, etc.  Ej. Incursión arbitraria/injustificada del ejército o policía en una comunidad.  Si registras actos vinculados al derecho a la inviolabilidad de domicilio también puedes registrar "Violaciones al derecho a la vida privada".
11389	166	005020	Organismos e instituciones descentralizadas, desconcentradas y autónomas federales	Si el organismo o la institución federal no caen dentro de la clasificación, se escoge este nivel más general. Ej.: Aeropuertos y Servicios Auxiliares, Administración General de Aduanas, etc.
11390	11389	005020005	Organismos públicos de derechos humanos federales	Ej.: CNDH, CONAPRED, CONDUSEF, IFAI, CONAMED, CDI
11391	11389	005020010	Organismos electorales autónomos federales	Aplica únicamente al IFE
11392	11389	005020015	Organismos financieros autónomos federales	Ej.: BANXICO, BANOBRAS, BANCOMEXT, BANRURAL, NACIONAL FINANCIERA, FONDOS, FIDEICOMISOS, ETC.
11393	11389	005020020	Organismos de seguridad social federales	Ej.: IMSS, ISSSTE, INFONAVIT
14352	5429	001035	Comunicador(a) social	Aplica a periodista, locutor(a) de radio comunitaria, etc.
11395	11389	005020030	Organismos de producción y servicios públicos federales	Ej.: PEMEX, CFE, CONAGUA
11396	11389	005020035	Instituciones nacionales de educación e investigación	Ej.: UNAM, IPN, UAM, CIESAS
11686	166	005025	Organismos e instituciones descentralizadas, desconcentradas y autónomas estatales	Si el organismo o la institución estatal no caen dentro de la clasificación se escoge este nivel más general
11687	11686	005025005	Organismos públicos de derechos humanos estatales	Aplica a las comisiones y procuradurías estatales de derechos humanos
11688	11686	005025010	Organismos electorales autónomos estatales	Aplica a los IEEs
11689	11686	005025015	Organismos de seguridad social estatales	Ej.:  ISSSTELeón
11692	11686	005025030	Instituciones estatales de educación e investigación	Aplica a universidades públicas estatales
14379	166	005030	Funcionario(a)s público(a)s en lo individual	
14381	14379	005030010	Prestador(a) de servicios públicos	De cualquier tipo de servicios. Ej. Médico del IMSS
14382	14379	005030015	Funcionario(a) público(a)	Son funcionario(a)s de alto nivel en las instituciones. Ej. Director(a) del IMSS
14383	14379	005030025	Empleado(a) público(a)	Excepto empleado(a)s público(a)s en prestación de servicios
14380	14379	005030005	Abogado(a) / Defensor(a) público(a)	Defensor(a) de oficio
11400	11397	010005010	Empresa privada nacional	Ej.: Grupo México
11402	11398	010010005	Institución financiera intergubernamental	Ej.: BM, FMI
11403	11398	010010010	Institución financiera trasnacional	Ej.: HSBC, CityBank, Santander Serfín
11404	11398	010010015	Institución financiera nacional	Ej.: Banorte
11405	11398	010010020	Institución financiera local	Ej.: Cajas de ahorro, Grupos Grameen
11406	167	010015	Autoridad autónoma	Ej.: Juntas de Buen Gobierno
11408	167	010025	Organización paramilitar	Pro status quo. Ej.: OPDDIC, Paz y Justicia
11409	167	010030	Grupo armado de oposición	Ej.: EPR
11411	11410	010035005	Grupo de narcotraficantes	Incluye Cárteles y narcomenudistas. Ej.: Cártel del Golfo
13797	11415	010040015	Organización civil	ONG
13798	11415	010040020	Institución y organización asistencial	Realizan trabajo asistencial independientemente de su figura legal
14384	13802	010045040005	Grupo de choque, porro, golpeador	Organización o miembro de organización de corte fascista que persigue intereses particulares, políticos o económicos basados en la violencia organizada contra diferentes tipos de organizaciones: estudiantiles, sindicales, etc.
11440	167	010055	Multitud o muchedumbre	Por ejemplo en linchamientos
14387	14386	010060005	Abogado(a) particular	
14388	14386	010060010	Presunto(a) delincuente común	Cuando se sospecha que el acto no es puramente de carácter delictivo
14390	14386	010060020	Sicario(a)	Asesino(a) a sueldo
11443	11441	015010	Organizaciones intergubernamentales	Ej.: OEA, ONU. No aplica a organismos financieros intergubernamentales como el Banco Mundial y el FMI
13803	165	020	Personas no identificadas	Sólo se usa si se vio a las personas pero no se puede identificar su pertenencia. Si nadie vio a las personas no se ingresa el dato
13804	13803	020005	Parapolicías	Personas civiles que operan de manera conjunta con cuerpos policíacos. No están organizados
13805	13803	020010	Personas encapuchadas	Personas que ocultan su rostro
13247	17	003060	Derechos de las y los defensore(a)s	
13252	13247	003060255	Derechos de las y los defensore(a)s en términos de legislación	
13251	13247	003060250	Derechos de las y los defensore(a)s en términos de políticas públicas	
13253	13247	003060260	Derechos de las y los defensore(a)s en términos de resoluciones judiciales	
13434	11286	003060	Violaciones a los derechos de las y los defensore(a)s	
13443	13434	003060255	Violaciones a los derechos de las y los defensore(a)s en términos de legislación	
13445	13443	003060255010	Adopción de  legislación regresiva en la protección, respeto y garantía de los derechos de las y los defensore(a)s	
13447	13443	003060255020	Caso específico de no realización de los derechos de las y los defensore(a)s en términos de legislación	
13444	13443	003060255005	Falta de adopción de legislación que respete, proteja y garantice los derechos de las y los defensore(a)s	
13446	13443	003060255015	Falta de cumplimiento de la legislación que respete, proteja y garantice los derechos de las y los defensore(a)s	
13438	13434	003060250	Violaciones a los derechos de las y los defensore(a)s en términos de políticas públicas	
13442	13438	003060250020	Caso específico de no realización de los derechos de las y los defensore(a)s en términos de políticas públicas	
13440	13438	003060250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las y los defensore(a)s	
13439	13438	003060250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las y los defensore(a)s	
13441	13438	003060250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las y los defensore(a)s	
13448	13434	003060260	Violaciones a los derechos de las y los defensore(a)s en términos de resoluciones judiciales	
13450	13448	003060260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía de los derechos de las y los defensore(a)s	
13449	13448	003060260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las y los defensore(a)s	
13451	13448	003060260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derechos de las y los defensore(a)s	
13604	13602	001	Este caso es previo a otro caso	Aplica a un caso que ocurre antes de otro caso relacionado directa e inequívocamente
13605	13602	002	Este caso es de mayor alcance y abarca uno o más casos reducidos	Aplica a casos grandes que comprenden casos más pequeños directa e inequívocamente relacionados. Ej. Caso Oaxaca (2006)  
13606	13602	003	Este caso ocasiona la ocurrencia de otro caso	Aplica a casos que son la causa de un caso posterior de forma directa e inequívoca
13607	13602	004	Este caso ocurre en paralelo con otro caso	Aplica a casos que están relacionados directa e inequívocamente y que ocurren en forma paralela, y son registrados por separado
13608	13602	005	Este caso es más reducido y es abarcado por un caso de mayor alcance	Aplica a casos que son de forma directa e inequívoca parte de un caso mayor
13609	13602	006	Este caso sucede a otro caso	Aplica a un caso que ocurre después de otro caso relacionado directa e inequívocamente
13610	13602	007	Este caso es consecuencia de otro caso	Aplica a casos que son resultado o producto de otro caso relacionado directa e inequívocamente
13613	13603	003	Este caso es consecuencia de otro caso	Aplica a casos que son resultado o producto de otro caso relacionado directa e inequívocamente
13615	13603	005	Este caso es de mayor alcance y abarca uno o más casos reducidos	Aplica a casos grandes que comprenden casos más pequeños directa e inequívocamente relacionados. Ej. Caso Oaxaca (2006)  
13612	13603	002	Este caso es más reducido y es abarcado por un caso de mayor alcance	Aplica a casos que son de forma directa e inequívoca parte de un caso mayor
13616	13603	006	Este caso es previo a otro caso	Aplica a un caso que ocurre antes de otro caso relacionado directa e inequívocamente
13617	13603	007	Este caso ocasiona la ocurrencia de otro caso	Aplica a casos que son la causa de un caso posterior de forma directa e inequívoca
13614	13603	004	Este caso ocurre en paralelo con otro caso	Aplica a casos que están relacionados directa e inequívocamente y que ocurren en forma paralela, y son registrados por separado
13611	13603	001	Este caso sucede a otro caso	Aplica a un caso que ocurre después de otro caso relacionado directa e inequívocamente
133	123	001	No confiable	Se aplica cuando: a) se trate de un documento dejado en recepción o enviado por otra vía, del cual se desconoce la fuente y/o no hay contacto personal con el denunciante; b) la fuente no estuvo presente en el evento y asegura la veracidad del mismo con base en rumores o versiones de supuestos testigos presenciales (FRAYBA)
11658	123	002	Poco confiable	Se aplica cuando: a) la información se obtiene de notas de prensa; b) la fuente no estuvo presente en el evento y asegura la veracidad del mismo por información de terceros; c) la fuente manifiesta capacidades físicas y/o mentales disminuidas, o patología psíquica evidente; c) la fuente muestra clara inclinación de simpatía u hostilidad hacia la víctima y/o el evento (FRAYBA)
11660	123	004	Probablemente confiable	Se aplica: cuando a) la fuente estuvo presente en el evento, su información es clara y coherente; b) la fuente tiene un nivel público de confianza y/o un nivel de compromiso personal, por ejemplo líder de la comunidad; c) los motivos y objetivos de la fuente son consistentes (FRAYBA)
11659	123	003	Confiabilidad dudosa o incierta	Se aplica: cuando a) hay incoherencia en la narración de los hechos; b) hay contradicción entre varios testimonios; c) la fuente es clave pero manifiesta alteraciones psíquicas o mentales; d) el documento ha sido enviado por una organización cuya credibilidad se desconoce (FRAYBA)
11814	138	001025045	Derecho a un(a) fiscal imparcial y objetivo(a)	
11815	138	001025050	Derecho a examinar testigo(a)s o peritos (careos)	
11816	138	001025055	Derechos de lo(a)s acusado(a)s	
11819	11816	001025055015	Derecho a ser llevado(a) sin demora ante un(a) juez(a)	
11820	11816	001025055020	Derecho a ser procesado(a) sin demora o puesto(a) en libertad	
11834	11816	001025055085	Derecho a un(a) intérprete	
11099	11095	003015015	Derecho de las y los migrantes a ser comunicado(a)s con las autoridades consulares de su Estado en caso de ser detenido(a)s	
13232	11114	003035025	Derecho de las niñas y los niños a no carearse con el inculpado(a) en caso que los pueda afectar	
11128	11126	003050010	Derecho de las y los extranjero(a)s a no ser deportado(a) a un lugar donde puedan sufrir violaciones a los derechos humanos	
13815	13808	003070035	Derecho de las y los consumidores a la reparación de daños y prejuicios que les causen	
14456	14439	004025	Derecho de los pueblos a la resistencia	"La resistencia hace referencia a la rebelión, a los movimientos revolucionarios que pretenden derrocar un gobernante o un sistema despótico y autoritario. Es diferente al derecho a la protesta, que no quiere cambiar de régimen, sino interpelarlo (Tesis M. Chamberlin)"
14458	14456	004025255	Derecho de los pueblos a la resistencia en términos de legislación	
14457	14456	004025250	Derecho de los pueblos a la resistencia en términos de políticas públicas	
14459	14456	004025260	Derecho de los pueblos a la resistencia en términos de resoluciones judiciales	
11861	11191	001025050	Violaciones al derecho a examinar testigo(a)s o peritos (careos)	
11862	11191	001025055	Violaciones a los derechos de los acusado(a)s	
11865	11862	001025055015	Violaciones al derecho a ser llevado(a) sin demora ante un(a) juez(a)	
11866	11862	001025055020	Violaciones al derecho a ser procesado(a) sin demora o puesto(a) en libertad	
11879	11862	001025055085	Violaciones al derecho a un(a) intérprete	
13265	11287	003005255	Violaciones a los derechos de las mujeres en términos de legislación	
13260	11287	003005250	Violaciones a los derechos de las mujeres en términos de políticas públicas	
13270	11287	003005260	Violaciones a los derechos de las mujeres en términos de resoluciones judiciales	
9086	8018	012035	Iguala de la Independencia	
11306	11302	003015015	Violaciones al derecho de las y los migrantes a ser comunicado(a)s con las autoridades consulares de su Estado en caso de ser detenido(a)s	
13357	11322	003035025	Violaciones al derecho de las niñas y los niños a no carearse con el inculpado(a) en caso que los pueda afectar	
11336	11334	003050010	Violaciones al derecho de las y los extranjero(a)s a no ser deportado(a)s a un lugar donde puedan sufrir violaciones a los derechos humanos	
13832	13825	003070035	Violaciones al derecho de las y los consumidores a la reparación de daños y prejuicios que les causen	
14612	14611	004025250	Violaciones al derecho de los pueblos a la resistencia en términos de políticas públicas	
14613	14612	004025250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos a la resistencia	
14614	14612	004025250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho de los pueblos a la resistencia	
14615	14612	004025250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos a la resistencia	
14616	14612	004025250020	Caso específico de no realización del derecho de los pueblos a la resistencia en términos de políticas públicas	
14617	14611	004025255	Violaciones al derecho de los pueblos a la resistencia en términos de legislación	
14618	14617	004025255005	Falta de adopción de legislación que respete, proteja y garantice el derecho de los pueblos a la resistencia	
14619	14617	004025255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho de los pueblos a la resistencia	
14620	14617	004025255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho de los pueblos a la resistencia	
14621	14617	004025255020	Caso específico de no realización del derecho de los pueblos a la resistencia en términos de legislación	
14622	14611	004025260	Violaciones al derecho de los pueblos a la resistencia en términos de resoluciones judiciales	
14623	14622	004025260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos a la resistencia	
14624	14622	004025260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho de los pueblos a la resistencia	
14625	14622	004025260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos a la resistencia	
14626	14622	004025260020	Caso específico de no realización del derecho de los pueblos a la resistencia en términos de resoluciones judiciales	
76	75	001	Relaciones entre personas	Relaciones entre individuos
77	76	001005	Cónyuge	Aplica cuando estén casados por lo civil
12586	76	001010	Pareja	Aplica cuando no estén casados por lo civil, por ejemplo cuando si estén casados por la iglesia, estén en unión libre o en sociedad de convivencia
78	76	001015	Hermano(a)	
79	76	001020	Padre / Madre	
14611	14544	004025	Violaciones al derecho de los pueblos a la resistencia	"La resistencia hace referencia a la rebelión, a los movimientos revolucionarios que pretenden derrocar un gobernante o un sistema despótico y autoritario. Es diferente al derecho a la protesta, que no quiere cambiar de régimen, sino interpelarlo. (Tesis M. Chamberlin)"
11112	17	003030	Derechos de las personas lesbianas, gays, bisexuales, transexuales y transgénero (LGBT)	
11320	11286	003030	Violaciones a los derechos de las personas lesbianas, gays, bisexuales, transexuales y transgénero (LGBT)	
12603	76	001105	Proveedor(a) de servicio	
12602	76	001100	Cliente(a) o receptor(a) de servicio	
12601	76	001095	Compañero(a) en una organización	
12599	76	001085	Patrón(a), jefe(a) o superior(a)	
12598	76	001080	Compañero(a) de trabajo 	
12597	76	001075	Persona que vive en la misma comunidad	
12596	76	001070	Vecino(a)	
12595	76	001065	Persona que habita en la misma casa o edificio	
12594	76	001060	Estudiante	
12593	76	001055	Maestro(a)	
12592	76	001050	Compañero(a) de estudios	
12591	76	001045	Amigo(a)	
12590	76	001040	Novio(a)	
12589	76	001035	Pariente lejano(a)	
12588	76	001030	Otro(a) pariente cercano(a)	
12600	76	001090	Empleado(a) o subordinado(a)	
12587	76	001025	Hijo(a)	
12609	80	002040	Grupo u organización de la cual es vocero(a) o representante	
12608	80	002035	Grupo u organización de la cual es dirigente	
12607	80	002030	Grupo u organización de la cual es miembro	
12606	80	002025	Grupo u organización de la cual es simpatizante	
81	80	002005	Simpatizante del grupo u organización	Se utiliza cuando se identifica a la persona únicamente como simpatizante pero no como miembro acreditado o de facto del grupo, por ejemplo: simpatizante del EZLN, simpatizante del PRD. Incluye “adherente” a movimientos amplios
82	80	002010	Miembro del grupo u organización	Se utiliza cuando la persona es miembro acreditado del grupo, o la persona de facto se identifica como tal. Incluye a “militantes”
12604	80	002015	Dirigente del grupo u organización	Se utiliza cuando la persona no tiene un cargo directivo formal en el grupo u organización pero se le  identifica como “líderes morales”.  Ej. Pedro Chulín en la OPDDIC
14124	14121	115015	Convención sobre la Eliminación de Todas las Formas de Discriminación Contra la Mujer (1979)	
12605	80	002020	Vocero(a) o representante del grupo u organización	No está claramente definida esta categoría pero se incluyó únicamente para aquellos casos en que la representación del grupo u organización haya sido delegada en una persona que no es miembro, empleada, funcionaria, ni dirigente, y habla a nombre del grupo u organización. El registro debe explicarse en las notas aclaratorias
12613	12610	003015	Directivo(a) de la entidad	
12616	12610	003030	Entidad de la cual es directivo(a)	
12615	12610	003025	Entidad de la cual es funcionario(a)	
12614	12610	003020	Entidad de la cual es empleado(a) o trabajador(a)	
12612	12610	003010	Funcionario(a) de la entidad	
12611	12610	003005	Empleado(a) o trabajador(a) de la entidad	
12622	12617	004025	Organización asociada o aliada	
12621	12617	004020	Organización de la cual es miembro	Aplica en casos de federaciones, centrales sindicales, etc.
12620	12617	004015	Organización miembro	Aplica en casos de federaciones, centrales sindicales, etc.
12619	12617	004010	Organización mayor u oficinas centrales	Aplica a organizaciones “madre” o de mayor alcance o cobertura, por ejemplo nacionales cuando hay estatales, entidades federales o estatales cuando hay oficinas regionales o locales, etc.
12618	12617	004005	Sucursal, agencia, delegación o división	
13583	13527	001105	Cliente(a) o receptor(a) de servicio	
13597	13527	003030	Directivo(a) de la entidad	
13590	13527	002035	Dirigente del grupo u organización	
13580	13527	001085	Empleado(a) o subordinado(a)	
13595	13527	003020	Empleado(a) o trabajador(a) de la entidad	
13594	13527	003015	Entidad de la cual es directivo(a)	
13592	13527	003005	Entidad de la cual es empleado(a) o trabajador(a)	
13593	13527	003010	Entidad de la cual es funcionario(a)	
13578	13527	001055	Estudiante	
13596	13527	003025	Funcionario(a) de la entidad	
13586	13527	002015	Grupo u organización de la cual es dirigente	
13585	13527	002010	Grupo u organización de la cual es miembro	
13584	13527	002005	Grupo u organización de la cual es simpatizante	
13587	13527	002020	Grupo u organización de la cual es vocero(a) o representante	
13576	13527	001020	Hijo(a)	
13579	13527	001060	Maestro(a)	
13589	13527	002030	Miembro del grupo u organización	
13600	13527	004015	Organización de la cual es miembro	
13598	13527	004005	Organización mayor u oficinas centrales	
13601	13527	004020	Organización miembro	
13577	13527	001025	Padre / Madre	
13581	13527	001090	Patrón(a), jefe(a) o superior(a)	
13582	13527	001100	Porveedor(a) de servicio	
13588	13527	002025	Simpatizante del grupo u organización	
13599	13527	004010	Sucursal, agencia, delegación o división	
13591	13527	002040	Vocero(a) o representante del grupo u organización	
11426	170	005005010030	Institución estatal encargada de la procuración de justicia penal	Procuradurías, fiscalías, ministerios públicos
11680	11426	005005010030005	Institución estatal de investigación penal	Policía ministerial, policía judicial, etc.
11682	11359	005005015030	Entidad municipal encargada de la administración de justicia	Juzgados municipales, tribunales contenciosos-administrativos
11432	11387	005015010010	Tribunal estatal especializado 	Excepto Penal   Ej. Civil, de lo Familiar, Fiscal. No aplica a tribunales administrativos que dependen del ejecutivo
11412	11410	010035010	Grupo traficante de personas o que se dedica a la trata de personas	Ej.: polleros
11413	11410	010035015	Grupo de traficantes de armas y/o mercancías	
11433	11417	010045005005	Cónyuge, pareja	
13799	11416	010045025	Persona que abusa de su poder público y político	Funcionario(a) público(a) que abusa de su poder como tal para obtener beneficio personal.  Familiares y amigo(a)s de funcionarios que abusan del poder que les da ser familiares o amigo(a)s de lo(a)s funcionario(a)s
13800	11416	010045030	Persona que abusa de su poder económico y/o financiero	Empresario(a)s, banquero(a)s o miembros de una empresa o institución financiera
13802	11416	010045040	Persona que abusa del poder de la agrupación	Golpeadore(a)s de un sindicato, personal de centro de rehabilitación que abusa de los interno(a)s
14385	13802	010045040010	Grupo de servidores públicos que abusan de su poder	Ej. Personal de centro de rehabilitación que abusa de los interno(a)s
14389	14386	010060015	Prestador(a) de servicios privados	Diferente de empleado(a) público(a) en prestación de servicios, tampoco incluye servicios de seguridad privada
12448	5429	001070	Empleado(a) público(a)	Se utiliza para cualquier empleado(a) público(a) excepto los funcionario(a)s de alto nivel
12455	5429	001115	Familiar o pareja de víctima	
12471	5429	001155	Menor en institución	Aplica a centro para menores infractores, casa hogar
12457	5429	001140	Lesbianas, gays, bisexuales, transexuales y transgénero (LGBT)	
12495	5431	002045	Afiliación a organización de comunicadore(a)s	
14357	5431	002017	Afiliación a grupo racista o de "odio"	Ej. Grupo antiinmigrante, grupo homofóbico
14371	54	004	Rango de edad de la víctima cuando ocurrió el acto	Esta categoría sirve solamente para separar menores, adultos y adultos mayores. Para un mejor desagregado por edad utilizar el campo "Edad de la víctima cuando ocurrió el acto". Si no se conoce la edad exacta utilizar 'edad aproximada' en ese mismo campo. 
11721	172	005	Denunciado(a) públicamente	Aplica a personas individuales y colectivas
11723	172	010	Denunciado(a) judicialmente	Aplica a personas individuales y colectivas
11724	172	015	Denunciado(a) administrativamente	
14691	172	016	Denunciado(a) ante organismo público de derechos humanos	Aplica a personas individuales y colectivas
14692	172	017	Con recomendación de organismo público de derechos humanos	Aplica a personas individuales y colectivas
13743	100	027	Familiar o pareja de la víctima	
13744	100	030	Familiar o pareja del perpetrador	
14132	14131	120005	Convención sobre los Derechos del Niño (1989)	
14138	14131	120035	Convención Interamericana sobre la restitución internacional de menores (1989)	
14139	14131	120040	Convenio Interamericano sobre conflictos de leyes en materia de adopción de menores (1987)	
160	159	001	Involucramiento en actos violentos, coercitivos o violatorios a los derechos humanos	Incluye actos que atenten contra los DESCA como la contaminación del medio ambiente. También incluye la emisión de resoluciones judiciales que directamente afecten los derechos humanos de alguna persona o colectivo como un acto que un juez lleva a cabo. Para los demás involucrados (apoyo, promoción e inactividad en la emisión de resoluciones) se utiliza "involucramiento en términos de legislación, resoluciones judiciales o establecimiento de políticas y sus vástagos
12528	162	003003	Inactividad en términos de promulgación de leyes, resoluciones judiciales o establecimiento de políticas	Ej. Falta de cambios en la legislación relativa a medios de comunicación (Cambios parados en el congreso después de que la Suprema Corte echó para atrás la Ley Televisa)
12573	142	003	Tierra, mina, área natural, protegida o arqueológica	Tierra propiedad privada; tierra propiedad comunal; tierra propiedad ejidal; tierras recuperadas, tierras baldías, área natural protegida; Mina, área minera; río, arroyo, ojo de agua, laguna, etc.; presa, represa; área reservada o restringida (ej. lugar donde se encuentran los ductos de PEMEX); zona arqueológica. No usar para  lugares relacionados con la víctima
12558	5422	005010005	Estación de policía	Instalaciones policiacas no dependientes del ministerio público.  Ej. Separos de seguridad pública federal, estatal, municipal, comunitaria donde no exista un ministerio público
12577	142	009	Institución o instalación de salud o asistencia	Cualquier institución o instalación de salud, pública o privada. Hospitales o clínicas públicas o privadas. Casa hogar o institución similar para huérfano(a)s, personas adultas mayores, personas con discapacidad física, para enfermo(a)s mentales, albergues para víctimas del delito
12584	142	016	Lugar de albergue, refugio, etc.	Campamento de refugiado(a)s, campamento de personas desplazadas internas, albergue para personas damnificadas, centro de acopio
12582	142	014	Medio de transporte	Autobús; automóvil; barco, bote, barcaza, lancha; bicicleta; motocicleta; camión de carga; metro o monorriel; taxi; tren
14678	5422	005010015	Instalación de procuración de justicia	Agencias del ministerio público y sus lugares de detención
14667	57	002063	Información en página web de institución pública	Aplica a información en página web de institución pública diferente a los documentos oficiales especificados en la lista. Ej. Organigramas, directorios, etc.
14669	13633	004027	Información en página web de organización nacional	Aplica a información de página web de organización nacional distinta a los documentos de organización nacional especificados en la lista.  Ej.  Información sobre la organización (quiénes somos), blogs, etc.
14671	58	006027	Información en página web de organización internacional	Aplica a información de página web de organización internacional distinta a los documentos de organización internacional especificados en la lista.  Ej.  Información sobre la organización (quiénes somos), blogs, etc.
13727	13714	012026	Declaración personal	Aplica a posicionamiento conjunto. Ej. Posicionamiento familiar
11587	11000	002002045	Nicaragua	
11616	11609	003001080	Taiwán	
12439	53	110	Defensore(a)s de derechos humanos	Incluye a defensore(a)s del medio ambiente
237	53	280	LGBT	Lesbianas, gays, bisexuales, transexuales y transgénero
233	53	320	Migración interna	Comprende fundamentalmente a las familias de jornalero(a)s migrantes
14316	2	001060	Delincuente común	Excepto narcotraficante y sicario(a)
309	2	001135	Empleado(a) público(a)	Excepto de empleado(a) en procuraduría, empleado(a) judicial  y en institución penitenciaria
14693	172	150	Muerto(a)	
313	2	001155	Funcionario(a) público(a)	Directores(as), Secretarios(as) de Estado, subsecretarios(as), Directores generales.  Excepto Juez(a), Legislador(a) y Fiscal
14320	2	001270	Sicario(a)	Asesino(a) a sueldo
334	2	001280	Trabajador(a) ambulante	Excepto vendedor(a) ambulante. Trabajador(a) que ofrece sus servicios de casa en casa, o en la calle: afilador(a) de cuchillos, bolero(a), plomero(a), etc.
14338	14321	002090	Servicios de alojamiento temporal y de preparación de alimentos y bebidas	Hoteles, moteles y similares; campamentos y albergues recreativos; pensiones y casas de huéspedes, departamentos y casas amuebladas con servicio de hotelería, restaurantes con servicios de  mesero(a)s, restaurantes de autoservicios y de comida para llevar, servicios de preparación de alimentos por encargo, centros nocturnos, bares, cantinas y similares
14340	14321	002100	Servicios de esparcimiento, culturales, deportivos y otros servicios recreativos	Compañías y grupos de espectáculos, deportistas y equipos deportivos profesionales y semiprofesionales, promotore(a)s y agentes de espectáculos artísticos, deportivos y similares, artistas y técnicos independientes, museos, sitios históricos, jardines botánicos y similares, servicios de entretenimiento, parques con instalaciones recreativas, casas de juego electrónicos
14343	14321	002115	Servicios educativos	Educación básica, media y especial, post bachillerato no universitario, educación superior, escuelas comerciales, de computación y capacitación para ejecutivo(a)s, escuelas de oficios, otros servicios educativos y de apoyo a la educación
14346	14321	002130	Servicios profesionales, científicos y técnicos	Servicios legales, de contabilidad, auditoría, arquitectura, ingeniería, diseño especializado, consultoría en computación, consultoría administrativa, científica y técnica, de investigación científica y desarrollo, de publicidad y actividades relacionadas. Otros servicios profesionales, científicos o técnicos
14025	14021	025020	Convenio de Ginebra relativo a la protección debida a las personas civiles en tiempo de guerra (Convenio IV) (1949)	
14047	14044	045015	Convención Internacional para la Protección de Todas las Personas contra las Desapariciones Forzadas (2006)	
14065	14060	060025	Convención Interamericana para la eliminación de todas las formas de discriminación contra las personas con discapacidad (1999)	
14082	14081	075005	Normas de las Naciones Unidas sobre la responsabilidad de las empresas en la esfera de los derechos humanos (2003)	
14100	14097	090015	Declaración de Principios de libertad de expresión de la Comisión Interamericana de Derechos Humanos (2000)	
14108	14106	100010	Declaración de Río sobre el medio ambiente y el desarrollo (1992)	
14111	14110	105005	Convención internacional contra el reclutamiento, la utilización, la financiación, y el entrenamiento de los mercenarios (1989)	
14114	14113	110005	Convención Internacional sobre la Protección de los Derechos de Todos los Trabajadores Migratorios y de sus Familiares (1990)	
14118	14113	110025	Convención sobre la condición de los extranjeros (OEA) (1928)	
14143	14142	125005	Plan de Acción Internacional sobre el envejecimiento y actividades conexas (2002)	
14152	11730	135	Procuración y administración de Justicia / Impunidad	
14191	14188	150250	Jurisprudencia sobre salud	
14196	14195	160005	Declaración sobre la protección de todas las personas contra la tortura y otros tratos o penas crueles, inhumanos o degradantes (1975)	
14199	14195	160020	Convención Contra la Tortura y Otros Tratos o Penas Crueles, Inhumanos o Degradantes (1984)	
14200	14195	160025	Protocolo Facultativo de la Convención contra la Tortura y Otros Tratos o Penas Crueles, Inhumanos o Degradantes (2002)	
148	147	001	Confirmado que no es una VDH	Se conocen los hechos y no existe una VDH
11662	147	002	Improbable que sea una VDH	Es poco probable que exista una VDH pero no se puede confirmar que no es una VDH
153	147	003	Posible que sea una VDH	Tanto puede ser como no ser una VDH
152	147	004	Probable que sea una VDH	Es muy probable que sea una VDH
11663	147	005	Confirmado que si es una VDH	Se conocen los hechos y se tiene la certeza de que existe una VDH
12513	12504	003095	Organización de comunicadore(a)s	
1	0	rootnode	Vocabularios	
10	135	001	Violaciones a los derechos civiles y políticos	
21	15	001015	Derecho a la libertad y seguridad personales	
116	113	004	Se desconoce el día y el mes	
134	15	001020	Derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico	
206	53	230	Instituto Federal de Acceso a la Información - IFAI	
8023	40	017	Morelos	
8030	40	002	Baja California	
8041	40	028	Tamaulipas	
8053	8020	014002	Acatlán de Juárez	
8066	8020	014015	Autlán de Navarro	
8077	8020	014026	Concepción de Buenos Aires	
8093	8020	014042	Huejuquilla el Alto	
8108	8020	014057	La Manzanilla de la Paz	
8121	8020	014070	El Salto	
8131	8020	014080	San Sebastián del Oeste	
8147	8020	014096	Tizapán el Alto	
8160	8020	014109	Unión de San Antonio	
8169	8020	014118	Yahualica de González Gallo	
8182	8033	021005	Acteopan	
8183	8033	021006	Ahuacatlán	
8193	8033	021016	Aquixtla	
12505	12504	003025	Cooperativa	
12506	12504	003050	Grupo o movimiento de expresión cultural	
12507	12504	003055	Grupo o movimiento de resistencia civil	
12508	12504	003040	Grupo de oposición armada	
12510	12504	003080	Movimiento político	
12511	12504	003085	Movimiento social	
12516	12504	003110	Organización ecologista	
12518	12504	003120	Organización estudiantil	
12519	12504	003125	Organización indígena	
8205	8033	021028	Camocuautla	
8214	8033	021037	Coyotepec	
8225	8033	021048	Chiautzingo	
8240	8033	021063	Esperanza	
8253	8033	021076	Hueytamalco	
8276	8033	021099	Cañada Morelos	
8286	8033	021109	Pahuatlán	
8295	8033	021118	Los Reyes de Juárez	
8306	8033	021129	San José Miahuatlán	
8318	8033	021141	San Pedro Yeloixtlahuaca	
8322	8033	021145	San Sebastián Tlacotepec	
8338	8033	021161	Tepanco de López	
8354	8033	021177	Tlacotepec de Benito Juárez	
8371	8033	021194	Venustiano Carranza	
8385	8033	021208	Zacatlán	
8397	8023	017002	Atlatlahucan	
8410	8023	017015	Miacatlán	
8421	8023	017026	Tlayacapan	
8434	8027	031006	Buctzotz	
8444	8027	031016	Chacsinkín	
8457	8027	031029	Dzilam González	
8469	8027	031041	Kanasín	
8478	8027	031050	Mérida	
8487	8027	031059	Progreso	
8496	8027	031068	Sinanché	
8507	8027	031079	Tekax	
8516	8027	031088	Teya	
8525	8027	031097	Tunkás	
8533	8027	031105	Yaxkukul	
8544	8049	007010	Bejucal de Ocampo	
8560	8049	007026	Chenalhó	
8573	8049	007039	Huitiupán	
8584	8049	007050	La Libertad	
8593	8049	007059	Ocosingo	
8600	8049	007066	Pantelhó	
8601	8049	007067	Pantepec	
8602	8049	007068	Pichucalco	
8615	8049	007081	Simojovel	
8625	8049	007091	Tapilula	
8632	8049	007099	La Trinitaria	
8643	8049	007110	San Lucas	
8657	8032	026005	Arivechi	
8666	8032	026014	Baviácora	
8679	8032	026027	Fronteras	
8690	8032	026038	Moctezuma	
8704	8032	026052	Sahuaripa	
8716	8032	026064	Trincheras	
8730	8028	032004	Benito Juárez	
8740	8028	032014	General Francisco R. Murguía	
8743	8028	032017	Guadalupe	
8751	8028	032025	Luis Moya	
8766	8028	032040	Sain Alto	
8779	8028	032053	Villa González Ortega	
8794	8038	009011	Tláhuac	
8804	8019	013004	Agua Blanca de Iturbide	
8816	8019	013016	Cuautepec de Hinojosa	
8831	8019	013031	Jacala de Ledezma	
8850	8019	013050	Progreso de Obregón	
8863	8019	013063	Tepeji del Río de Ocampo	
8876	8019	013076	Tula de Allende	
8884	8019	013084	Zimapán	
8894	8041	028010	Cruillas	
8903	8041	028019	Llera	
8912	8041	028028	Nuevo Morelos	
8926	8041	028042	Villagrán	
8938	8022	016011	Briseñas	
8949	8022	016022	Charo	
8958	8022	016031	Epitacio Huerta	
8971	8022	016044	Jiménez	
8983	8022	016056	Nahuatzen	
8995	8022	016068	Peribán	
9098	8018	012047	Pedro Ascencio Alquisiras	
9115	8018	012064	Tlalchapa	
9128	8018	012077	Marquelia	
9136	8044	024004	Armadillo de los Infante	
9151	8044	024019	Lagunillas	
9161	8044	024029	San Martín Chalchicuautla	
9178	8044	024046	Villa de Arriaga	
9194	8039	008004	Aquiles Serdán	
9205	8039	008015	Coyame del Sotol	
9212	8039	008022	Dr. Belisario Domínguez	
9229	8039	008039	López	
9238	8039	008048	Namiquipa	
9248	8039	008058	San Francisco de Conchos	
9267	8036	022009	Jalpan de Serra	
9279	8016	010003	Coneto de Comonfort	
9290	8016	010014	Mezquital	
9292	8016	010016	Nombre de Dios	
9304	8016	010028	San Juan del Río	
9317	8029	003002	Mulegé	
9334	8017	011014	Dolores Hidalgo Cuna de la Independencia Nacional	
9360	8017	011040	Tierra Blanca	
9371	8021	015005	Almoloya de Juárez	
9383	8021	015017	Ayapango	
9389	8021	015023	Coyotepec	
9402	8021	015036	Hueypoxtla	
9415	8021	015049	Joquicingo	
9428	8021	015062	Ocoyoacac	
9439	8021	015073	San Antonio la Isla	
9449	8021	015083	Temamatla	
9462	8021	015096	Tequixquiac	
9473	8021	015107	Tonatico	
9478	8021	015112	Villa del Carbón	
9493	8046	027002	Cárdenas	
9505	8046	027014	Paraíso	
9513	8030	002005	Playas de Rosarito	
9528	8042	025015	Salvador Alvarado	
9539	8034	020008	Asunción Tlacolulita	
9554	8034	020023	Cuilápam de Guerrero	
9563	8034	020032	Fresnillo de Trujano	
9570	8034	020039	Heroica Ciudad de Huajuapan de León	
9588	8034	020057	Matías Romero Avendaño	
9603	8034	020072	San José del Progreso	
9619	8034	020088	San Andrés Cabecera Nueva	
9632	8034	020101	San Andrés Zabache	
9645	8034	020114	San Baltazar Yatzachi el Bajo	
9664	8034	020133	San Esteban Atatlahuca	
9677	8034	020146	San Francisco Logueche	
9683	8034	020152	San Francisco Tlapancingo	
9691	8034	020160	San Jerónimo Silacayoapilla	
8455	8027	031027	Dzidzantún	
9708	8034	020177	San Juan Bautista Cuicatlán	
9727	8034	020196	San Juan Evangelista Analco	
9744	8034	020213	San Juan Quiahije	
9757	8034	020226	San Lorenzo Albarradas	
9772	8034	020241	San Martín Lachilá	
9785	8034	020254	San Mateo Río Hondo	
9787	8034	020256	San Mateo Tlapiltepec	
9788	8034	020257	San Melchor Betaza	
9802	8034	020271	San Miguel Mixtepec	
9803	8034	020272	San Miguel Panixtlahuaca	
9818	8034	020287	San Miguel Tulancingo	
9827	8034	020296	San Pablo Macuiltianguis	
9842	8034	020311	San Pedro Jaltepetongo	
9857	8034	020326	San Pedro Sochiápam	
9868	8034	020337	San Pedro y San Pablo Ayutla	
9887	8034	020356	Santa Ana del Valle	
9898	8034	020367	Santa Catarina Mechoacán	
9915	8034	020384	Santa Cruz Xitla	
9922	8034	020391	Santa Lucía Miahuatlán	
9927	8034	020396	Santa María la Asunción	
9944	8034	020413	Santa María Huatulco	
9955	8034	020424	Santa María Ozolotepec	
9968	8034	020437	Santa María Tlahuitoltepec	
9987	8034	020456	Santiago Cacaloxtepec	
9988	8034	020457	Santiago Camotlán	
10019	8034	020488	Santiago Tepetlapa	
10030	8034	020499	Santiago Yolomécatl	
10032	8034	020501	Santiago Yucuyachi	
10042	8034	020511	Santo Domingo Nuxaá	
10043	8034	020512	Santo Domingo Ozolotepec	
10052	8034	020521	Santo Domingo Tonaltepec	
10060	8034	020529	Santos Reyes Yucuná	
10061	8034	020530	Santo Tomás Jalieza	
10099	8034	020568	Zapotitlán Palmas	
10114	8024	018013	San Pedro Lagunillas	
10128	8025	019007	Aramberri	
10140	8025	019019	San Pedro Garza García	
10144	8025	019023	Gral. Treviño	
10166	8025	019045	Salinas Victoria	
10172	8025	019051	Villaldama	
10180	8035	005007	Cuatro Ciénegas	
10189	8035	005016	Lamadrid	
10198	8035	005025	Piedras Negras	
10205	8035	005032	San Juan de Sabinas	
10217	8014	023005	Benito Juárez	
10230	8040	029010	Chiautempan	
10237	8040	029017	Mazatecochco de José María Morelos	
10270	8040	029050	San Francisco Tetlanohcan	
10286	8031	001006	Pabellón de Arteaga	
10297	8026	030006	Acultzingo	
10308	8026	030017	Apazapan	
10315	8026	030024	Tlaltetela	
10328	8026	030037	Coahuitlán	
10336	8026	030045	Cosamaloapan de Carpio	
10350	8026	030059	Chinameca	
10363	8026	030072	Huayacocotla	
10374	8026	030083	Ixhuatlán de Madero	
10391	8026	030100	Manlio Fabio Altamirano	
10404	8026	030113	Naranjal	
10415	8026	030124	Papantla	
10422	8026	030131	Poza Rica de Hidalgo	
10439	8026	030148	Soledad de Doblado	
10446	8026	030155	Tantoyuca	
10448	8026	030157	Castillo de Teayo	
10463	8026	030172	Texistepec	
10476	8026	030185	Tlilapan	
10483	8026	030192	Vega de Alatorre	
10493	8026	030202	Zontecomatlán de López y Fuentes	
10512	8051	006008	Minatitlán	
11035	15	001050	Derecho al respeto de la honra y reputación	
11054	15	001135	Derecho a participar en los asuntos públicos	
11064	11063	002010005005	Derecho a no ser objeto de esterilización sin consentimiento informado	
11080	17	003005	Derechos de las mujeres	
11081	11080	003005005	Derecho de las mujeres a gozar de permiso por maternidad	
11106	18	003025250	Derechos de las personas privadas de la libertad en términos de políticas públicas	
11121	11119	003040010	Derecho de las personas con discapacidad a la asistencia	
11122	11119	003040015	Derecho de las personas con discapacidad a la integración o reintegración social	
11123	11119	003040020	Derecho de las personas con discapacidad al empleo adecuado	
11124	17	003045	Derechos de las personas adultas mayores	
11238	11236	001060010	Violación a la confidencialidad de las comunicaciones	
11259	10	001135	Violaciones al derecho a participar en los asuntos públicos	
11282	11281	002045005	Violaciones al derecho a la protección de los intereses morales y materiales	
11314	11313	003025250	Violaciones a los derechos de las personas privadas de la libertad en términos de políticas públicas	
11330	11327	003040015	Violaciones al derecho de las personas con discapacidad a la integración o reintegración social	
11342	11337	003055010	Violaciones al derecho de las personas desplazadas a la protección contra la destrucción, apropiación, ocupación o uso arbitrario e ilegal de sus bienes que hayan abandonado	
11439	11420	010045020005	Terrateniente, ranchero, finquero, cacique	
11606	11000	002003060	Venezuela	
11613	11609	003001028	Japón	
11626	11609	003005027	Israel	
11640	11627	004003019	Croacia	
11647	11627	004003064	Serbia, República de (a partir de junio 2006)	
11679	11422	005005005035010	Institución federal de investigación pericial 	
11736	20	001010260	Derecho a la integridad personal en términos de resoluciones judiciales	
11755	11754	001005260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la vida	
11759	13	001010250	Violaciones al derecho a la integridad personal en términos de políticas públicas	
11771	11769	001010260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la integridad personal	
11785	11781	001015255020	Caso específico de no realización del derecho a la libertad y seguridad personales en términos de legislación	
10031	8034	020500	Santiago Yosondúa	
11786	14	001015260	Violaciones al derecho a la libertad y seguridad personales en términos de resoluciones judiciales	
11805	11801	001020260020	Caso específico de no realización del derecho a no ser sometido(a) a esclavitud,  servidumbre, trata o tráfico en términos de resoluciones judiciales	
11824	11816	001025055040	Derecho a la libertad bajo fianza	
11825	11816	001025055045	Derecho a no declarar en su contra	
11872	11862	001025055050	Violaciones al derecho a tener acceso a asistencia letrada durante el interrogatorio	
11888	11884	001025060020	Violaciones al derecho a la protección contra actos de intimidación y represalia, para sí y su familia antes, durante y después de los procedimientos	
11893	11884	001025060045	Violaciones al derecho a la atención médica y sicológica de urgencia	
11895	11894	001025250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho al acceso a la justicia	
11937	11040	001075250	Derecho al acceso a la información pública y a la información personal en términos de políticas públicas	
11953	11949	001030250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la seguridad jurídica	
11971	11969	001035255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a la verdad	
12035	12034	001055260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la inviolabilidad de domicilio	
12052	12049	001060260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la inviolabilidad de las comunicaciones	
12084	11243	001075250	Violaciones al derecho al acceso a la información pública y a la información personal en términos de políticas públicas	
12097	12094	001075260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho al acceso a la información pública y a la información personal	
12110	12109	001080260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la libertad de asociación	
12140	12139	001090260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a beneficiarse del progreso científico y sus aplicaciones	
12143	12139	001090260020	Caso específico de no realización del derecho a beneficiarse del progreso científico y sus aplicaciones en términos de resoluciones judiciales	
12184	12182	001105250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la libertad de tránsito	
12194	12192	001105260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la libertad de tránsito	
12199	12197	001110250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la nacionalidad	
12209	12207	001110260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la nacionalidad	
12210	12207	001110260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho a la nacionalidad	
12243	12242	001125250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a salir del país	
12248	12247	001125255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a salir del país	
12272	11053	001130250	Derecho a la no discriminación en términos de políticas públicas	
12291	11059	001160255	Derecho al acceso a la función pública en términos de legislación	
12006	12004	001045260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la vida privada	
12307	12306	001130260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la no discriminación	
12310	12306	001130260020	Caso específico de no realización del derecho a la no discriminación en términos de resoluciones judiciales	
12312	12311	001135250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a participar en los asuntos públicos	
12353	12351	001145260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a postularse a cargos electivos	
12360	12356	001150250020	Caso específico de no realización del derecho a formar partidos políticos en términos de políticas públicas	
12373	12371	001155250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a militar en partidos políticos	
12374	12371	001155250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen el derecho a militar en partidos políticos	
12375	12371	001155250020	Caso específico de no realización del derecho a militar en partidos políticos en términos de políticas públicas	
12376	11263	001155255	Violaciones al derecho a militar en partidos políticos en términos de legislación	
12377	12376	001155255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a militar en partidos políticos	
12378	12376	001155255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho a militar en partidos políticos	
12379	12376	001155255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a militar en partidos políticos	
12380	12376	001155255020	Caso específico de no realización del derecho a militar en partidos políticos en términos de legislación	
12381	11263	001155260	Violaciones al derecho a militar en partidos políticos en términos de resoluciones judiciales	
12407	12406	001165255005	Falta de adopción de legislación que respete, proteja y garantice el derecho a elecciones libres y democráticas	
12413	12411	001165260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a elecciones libres y democráticas	
13006	11070	002020250	Derecho a la alimentación adecuada en términos de políticas públicas	
13019	11074	002040250	Derecho al acceso a los servicios públicos en términos de políticas públicas	
13025	11078	002050250	Derecho al acceso a la propiedad pública en términos de políticas públicas	
13050	13035	002005250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho a la educación	
13075	13046	002015250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho al trabajo	
13079	13047	002015255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho al trabajo	
13084	13048	002015260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen el derecho al trabajo	
13132	13130	002030260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a un medio ambiente sano	
13157	13155	002040255010	Adopción de  legislación regresiva en la protección, respeto y garantía del derecho al acceso a los servicios públicos	
13180	11284	002050250	Violaciones al derecho al acceso a la propiedad pública en términos de políticas públicas	
13181	13180	002050250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho al acceso a la propiedad pública	
13228	18	003025260	Derechos de las personas privadas de la libertad en términos de resoluciones judiciales	
13246	11129	003055260	Derechos de las personas desplazadas en términos de resoluciones judiciales	
13261	13260	003005250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las mujeres	
13313	11308	003020250	Violaciones a los derechos de los y las trabajadore(a)s en términos de políticas públicas	
13326	13323	003020260015	Falta de cumplimiento de resoluciones judiciales que respeten, protejan y garanticen los derechos de los y las trabajadore(a)s	
13360	13358	003035250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las niñas y los niños	
13374	13373	003040250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos de las personas con discapacidad	
13390	13388	003045250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de las personas adultas mayores	
13422	11339	003055250015	Falta de implementación de políticas públicas que respeten, protejan y garanticen los derechos de las personas desplazadas	
13430	13429	003055260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos de las personas desplazadas	
13482	13480	001087250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho a la objeción de conciencia	
13491	13490	001087260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la objeción de conciencia	
13498	13496	002027250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía del derecho al agua	
13624	57	002014	Certificado médico legista físico o psicológico	
13645	57	002054	Estudio técnico y/o científico oficial	
13658	13633	004004	Acta de asamblea de organización nacional	
13664	13633	004016	Comunicado de prensa de organización nacional	
13688	58	006032	Solicitud de organización internacional de obtención de información pública 	
13719	13714	012010	Certificado médico físico privado	
13731	13714	012034	Folleto, material de propaganda privado	
13732	13714	012036	Fotografía personal	
13733	13714	012038	Informe privado	
13734	13714	012040	Recibo privado de bienes económicos o materiales	
13775	13773	012004	Comunicación con Relatores CIDH	
13782	92	018	Queja o petición	
13809	13808	003070005	Derecho de las y los consumidores a la protección de la salud y la seguridad	
13831	13825	003070030	Violaciones al derecho de las y los consumidores a obtener protección ante cualquier situación que cause inferioridad, subordinación o indefensión	
14016	14014	015010	Directrices Voluntarias en apoyo de la realización progresiva del derecho a una alimentación adecuada en el contexto de la seguridad alimentaria nacional (2004)	
14032	14031	030005	Declaración sobre el derecho y el deber de los individuos, los grupos y las instituciones de promover y proteger los derechos humanos y las libertades fundamentales universalmente reconocidos (1998)	
14086	14084	080010	Convención sobre la imprescriptibilidad de los crímenes de guerra y de los crímenes de lesa humanidad (1968)	
14087	14084	080015	Principios de cooperación internacional en la identificación, detención, extradición y castigo de los culpables de crímenes de guerra, o de crímenes de lesa humanidad (1973)	
14134	14131	120015	Protocolo facultativo de la Convención sobre los Derechos del Niño relativo a la venta de niños, la prostitución infantil y la utilización de niños en la pornografía (1999)	
14163	14152	135250	Jurisprudencia sobre procuración y administración de justicia / Impunidad	
14165	14164	140005	Declaración sobre los derechos de las personas pertenecientes a minorías nacionales o étnicas, religiosas y lingüísticas (1992)	
14211	14203	165250	Jurisprudencia sobre trata de personas, esclavitud y trabajo forzado	
265	53	610	Sociedad civil, ONG, OSC	
14322	14321	002005	Actividades administrativas de instituciones públicas de bienestar social 	
12527	162	003002	Apoyó la promulgación de la ley, resolución judicial o política violatoria de derechos humanos	
12463	5429	001165	Migrante	
12476	5429	001220	Presunto(a) narcotraficante	
14360	12504	003015	Comunidad o grupo indígena	
14368	12504	003135	Poder ejecutivo	
14369	12504	003140	Poder judicial	
11700	154	190	Sancionado(a), sentenciado(a)	
14416	172	085	Procesado(a) y sancionado(a) con apercibimiento	
70	129	070	Religión cristiana ortodoxa	
14426	14425	001036250	Derecho a la seguridad ciudadana en términos de políticas públicas	
14433	15	001250	Derechos civiles y políticos en términos de políticas públicas	
14434	15	001255	Derechos civiles y políticos en términos de legislación	
14438	16	002260	Derechos económicos, sociales, culturales y ambientales en términos de resoluciones judiciales	
13220	11095	003015250	Derechos de las y los migrantes en términos de políticas públicas	
14489	14487	001036260010	Adopción de resoluciones judiciales regresivas en el respeto, protección y garantía del derecho a la seguridad ciudadana	
14514	14512	001250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos civiles y políticos	
14530	14529	002250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen los derechos económicos, sociales, culturales y ambientales	
14531	14529	002250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos económicos, sociales, culturales y ambientales	
14540	14539	002260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen los derechos económicos, sociales, culturales y ambientales	
14548	14547	004005250005	Falta de establecimiento de políticas públicas que respeten, protejan y garanticen el derecho de los pueblos a gozar y disponer plena y libremente de sus riquezas y recursos naturales	
14583	14579	004015250020	Caso específico de no realización del derecho de los pueblos a la paz en términos de políticas públicas	
14607	14606	004020260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho de los pueblos al desarrollo	
14651	14649	004250010	Establecimiento de políticas públicas regresivas en cuanto al respeto, protección y garantía de los derechos de los pueblos	
13250	13247	003060015	Derecho de las y los defensore(a)s a recibir financiamiento para la defensa y promoción de los derechos humanos	
13755	100	063	Proveedor(a) de servicio financiero	
13764	13760	006008	Difusión (entrevistas medios comunicación, campañas, carteles, postales, página web)	
285	124	024	Preparatoria o bachillerato completo	
165	1	T24	Tipo de perpetrador	
14391	154	005	Afectado(a) físicamente	Diferente de herido(a). Aplica a daño físico permanente como secuela de heridas 
12576	142	008	Institución o instalación educativa	Cualquier institución educativa de cualquier nivel, pública y privada 
11421	167	010050	Grupo o persona que da servicio de seguridad privada	Ej.: Policía privada, guardaespaldas, escolta 
14694	14021	025031	Protocolo adicional a los Convenios de Ginebra del 12 de agosto de 1949 relativo a la aprobación de un signo distintivo adicional (Protocolo III) (2005)	
15000	1	AyudaContextual	Ayuda contextual	
15001	15000	frame2	Manejo de casos	
42	127	051	Guarijío	sureste de Sonora. Usado por: Makurawe, macoragüi, warijo, varojio
15301	15247	staticText2,Estado	Casos/Datos generales/Nueva localización / Localización - Estado	Haz clic en la flechita para que aparezcan todos los estados de la república. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar". Para borrar el estado, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Aguascalientes" 
15583	15515	FPAddLengua	Personas individual/Detalles/Lengua predominante / (+) signo de más	Haz clic aquí para agregar una lengua indígena. Si ya hay una lengua indígena registrada y quieres agregar otra, haz clic aquí y selecciónala. Las lenguas indígenas que selecciones aparecerán en la ventana de al lado.
15623	15513	staticPersona	Personas todas/Datos biográficos/Agregar dato biográfico / [#] Nombre de la persona	Esta es la persona activa a quien se le está agregando un nuevo dato biográfico relacionado con otra persona. Si quieres trabajar sobre una persona distinta, oprime el botón "Cancelar", regresa a la pestaña "Datos generales" y selecciona una persona diferente
15624	15513	staticText2	Personas todas/Datos biográficos/Agregar dato biográfico / Relacionada como	Ingresa a la ventana de abajo "Tipos de relaciones" para especificar el tipo de relación de la persona activa con una segunda persona, la cual deberás seleccionar posteriormente. Por ejemplo, si estás relacionando a Ildefonso Zamora con su hijo Aldo, la relación se establece desde Ildefonso (el papá), quien es la persona activa
15627	15513	nuevaPersona	Personas todas/Datos biográficos/Agregar dato biográfico / Nueva persona	Haz clic aquí para ingresar una nueva  persona al sistema y relacionarla con la persona activa. Cuando hayas ingresado los datos, la persona recién creada aparecerá en el listado de abajo. Selecciona su nombre y elije el tipo de relación que la vincula a la persona activa
15546	15515	CPPais	Personas individual/Datos generales/País de nacimiento	País en donde nació esta persona. México aparece por omisión pero se puede cambiar haciendo clic en el signo de más (+) ubicado al lado del campo. Únicamente se puede ingresar un país de nacimiento para cada persona
15599	15514	staticText2	Personas todas/Detalles/Dirección(es) / Dirección	Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección". Ingresa la dirección en el orden normal de calle, número exterior, número interior, colonia, ciudad, estado, código postal y país (si  la dirección no es en México). Ingresa aquí una sola dirección, si quieres registrar otra, primero guarda esta y luego repite el procedimiento para agregar una nueva
15495	15247	staticText3, MuniSearch	Casos/Datos generales/Nueva localización / Localización - Municipio	En "seleccionar" aparecen todos los municipios del estado seleccionado arriba. Puedes también escribir unas letras del nombre del municipio que te interesa en la cajita que dice "buscar". Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Puedes escribir una breve nota de más o menos 20 palabras al lado del municipio seleccionado. Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar". Para borrar el municipio, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes del primer municipio 
15300	15247	staticText1,btnPais,Pais	Casos/Datos generales/Nueva localización / Localización - País	México aparece por omisión pero se puede cambiar haciendo clic en el signo de más (+) al lado de "País". Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar" 
15339	15001	LC3, LC14	Actos/Información general/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente 
15347	15001	staticText74	Actos/Información general/Perpetradores	Lista de los perpetradores ya registrados en el acto activo. Están ordenados alfabéticamente por su nombre. Para ver los detalles del perpetrador, o modificar sus datos, debes hacer clic en la pestaña de arriba que dice "Perpetradores" 
15357	15001	delCaracRel	Actos/Información general/Características relevantes / (x) signo de multiplicación	Haz clic aquí para borrar la característica de la persona que se encuentre seleccionada. Para seleccionarla haz clic sobre la característica que quieras borrar.
15370	15001	txtLongFAObs	Actos/Información general/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son 20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15441	15255	listBoxPersona	Fuentes/Fuente personal/Agregar fuente personal / Seleccionar una persona	Busca el nombre de la fuente personal, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15543	15515	CPSexo	Personas individual/Datos generales/Sexo	Haz clic en la flechita para seleccionar el sexo de la persona. Para borrar el dato, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Hombre". Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15548	15515	btnFPPais	Personas individual/Datos generales/País de nacimiento / (+) signo de más	Si quieres cambiar "México" por otro país,  haz clic aquí y selecciona un país diferente de la lista que aparece. Utiliza el cursor para moverte hacia abajo o hacia arriba, y haz clic en el signo de más (+) para abrir la lista. Cuando encuentres el país que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". El país seleccionado aparecerá en el campo. Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un país de nacimiento para cada persona
15550	15515	btnRemoveFPPais	Personas individual/Datos generales/País de nacimiento / (x) signo de multiplicación	Haz clic aquí para borrar el país de nacimiento de esta persona
15584	15515	delLengua	Personas individual/Detalles/Lengua predominante / (x) signo de multiplicación	Haz clic aquí para borrar la lengua que está seleccionada en la ventana de al lado
15600	15514	staticText3	Personas todas/Detalles/Dirección(es) / Teléfono	Ingresa el número de teléfono, y de preferencia las claves necesarias para llamar desde tu lugar de origen. Puedes ingresar varios números. Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección"
15355	15001	staticText45	Actos/Información general/Características relevantes	Son las características de la persona que fueron motivo para su victimización en este acto o VDH. Ingresa más de una característica SÓLO en el caso de que exista claramente más de una característica relevante que fuera el motivo para la victimización de la persona en el acto o VDH específico.
15367	15001	staticTextEdadOcurreActo	Actos/Información general/Edad cuando ocurrió el acto	Edad de la víctima cuando ocurrió el acto. Primero selecciona si la edad es precisa o aproximada y luego ingresa la edad de la víctima. Para borrar esta información, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba.
15598	15514	staticText1	Personas todas/Detalles/Dirección(es) / Tipo de dirección	Es el tipo de lugar de la dirección de esta persona, por ejemplo, "casa", "trabajo" o "dirección temporal" (que puede ser una cárcel). También puede ser la "dirección institucional" de una entidad o grupo. Únicamente puedes seleccionar un "tipo de dirección" para cada dirección que ingreses. Haz clic en la flechita para seleccionar el tipo de esta dirección. Cuando encuentres el tipo de dirección que buscas, selecciónala y el término aparecerá en el campo. Para borrar el dato, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15445	15001	staticText24	Fuentes/Fuente personal/Nombre de la fuente personal	Nombre de la persona o entidad que aporta la información
43	127	054	Huasteco	Usado por: Teenek. Incluye: Huasteco de San Luis Potosí; Huasteco de Veracruz
15365	15001	buttonEstatusdelavictima	Actos/Información general/Estatus de la víctima / (+) signo de más	Haz clic aquí para agregar el término que represente de la mejor manera el ÚLTIMO estatus conocido de la víctima. Únicamente se puede ingresar un término. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente.
15368	15001	staticText73	Actos/Información general/Localización	Indicación de dónde ocurrió este acto: país, estado, municipio y localidad. Únicamente se puede ingresar una localización para cada acto. Las opciones de localización que aparecen aquí, son las que se registraron en el campo "Localización" de la pestaña "Datos generales" del caso. Para seleccionar la localización de este acto, haz clic en la flechita y selecciona la localización que buscas. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona una localización diferente. Para borrar una localización elegida, selecciona el espacio en blanco que aparece al inicio de la lista.
15369	15001	staticText48	Actos/Información general/Observaciones	Registra aquí cualquier información adicional sobre el acto que no esté ingresada en otro campo, y/o información que ayude a comprender el contexto en el que sucede este acto, antecedentes relevantes, etc. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15373	15001	LA14	Actos/Normatividad/Acto: Víctima / Acto	Este es el acto que está activo para ingresar nueva normatividad, o para modificar datos ya registrados. Si no tienes un acto activo  no podrás ingresar información en esta pantalla. Para activar un acto, regresa a la pestaña "Información general" de "Actos" y selecciónalo con doble clic.
15374	15001	FALegis	Actos/Normatividad/Legislación nacional / Lista	Lista en orden alfabético de toda la legislación nacional ingresada para el acto activo. Para registrar una nueva legislación, oprime el signo de más (+) al lado de "Legislación nacional"
15375	15001	btnActoLegislacion	Actos/Normatividad/Legislación nacional / (+) signo de más	Haz clic aquí  y para seleccionar el tipo de legislación que aplique a este acto. Cuando encuentres el tipo que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Puedes ingresar toda la legislación relevante para este acto o VDH.
15376	15001	FAlegislacion_nacional_notas	Actos/Normatividad/Notas de Legislación nacional	Aquí puedes ingresar el nombre y los artículos específicos de la legislación que seleccionaste. Para moverte hacia arriba o hacia abajo dentro del texto, utiliza el cursor o la barra de desplazamiento. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH. La información que ingreses aquí, corresponderá a la legislación que esté activa. Para activar una legislación, haz doble clic sobre la misma.
15378	15001	btnInfoLegis	Actos/Normatividad/Legislación nacional / I (letra I)	Datos de la creación y actualización del registro de legislación nacional. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15385	15001	LC4	Actos/Perpetradores/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15386	15001	LA2	Actos/Perpetradores/Acto: Víctima / Acto	Este es el acto que está activo para ingresar un nuevo perpetrador, o para modificar datos ya registrados para este perpetrador. Si quieres trabajar en otro acto, regresa a la pestaña de "Información general" de "Actos" y selecciónalo en la ventana "Actos registrados", o  ingresa uno nuevo
15391	15001	btnInfoInvol	Actos/Perpetradores/I (letra I)	Datos de la creación y actualización del registro de este perpetrador. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15352	15001	btnDPersonaVictima	Actos/Información general/P?	Haz clic aquí para ir al registro completo de esta persona. Desde la pestaña de "Personas" puedes regresar a este mismo lugar  oprimiendo el botón "Pantalla anterior"
15359	15001	buttonSelecTipodelugar	Actos/Información general/Tipo de lugar / (+) signo de más	Haz clic aquí para agregar un término que represente de la mejor manera el lugar en donde ocurrió este acto. Únicamente se puede ingresar un tipo de lugar para cada acto. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15361	15001	staticText46	Actos/Información general/Estatus VDH	Indicación de si se trata de una violación a los derechos humanos confirmada o potencial, y la probabilidad que tiene de ser confirmada
15362	15001	buttonSelectEstatusVDH	Actos/Información general/Estatus VDH / (+) signo de más	Haz clic aquí para agregar el término que represente de la mejor manera la probabilidad de que este acto se pueda confirmar como una VDH. Únicamente se puede ingresar un estatus para cada acto o VDH. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15299	15001	btnLocMasInfo	Casos/Datos generales/Más información	Haz clic aquí para ver las notas aclaratorias registradas en esta localización.
15303	15001	delLocalizacion	Casos/Datos generales/Borrar localización	Haz clic aquí para borrar los datos de la localización sobre la cual se encuentre el cursor. Antes de poder borrar una localización del caso debes borrarla en los actos correspondientes. Si un acto tiene la localización asignada, cuando intentes borrar esa localización te aparecerá una alerta y los datos no serán borrados
15393	15001	staticText50	Actos/Perpetradores/Nombre del perpetrador	Nombre de la persona responsable del acto. Puede ser una persona individual como "Pérez, Juan",  o una entidad como "Ejército Mexicano"
15394	15001	btnDPersonaPerpetrador	Actos/Perpetradores/P?	Haz clic aquí para ir al registro completo de esta persona y agregar o modificar datos, por ejemplo, corregir la ortografía del nombre. Desde la pestaña de "Personas" puedes regresar a este mismo lugar  oprimiendo el botón "Pantalla anterior"
15398	15001	staticText53	Actos/Perpetradores/Tipo de perpetrador	Identificación genérica de este perpetrador, ya sea una persona individual o una entidad, por ejemplo si es una Entidad estatal como "Fuerzas federales de seguridad pública", o una "Persona que abusa de su poder dentro de la familia"
15447	15001	staticText12	Fuentes/Fuente personal/Persona sobre quien se aporta información	Nombre de la persona sobre quien la fuente personal aportó información. Utiliza este campo cuando la información proporcionada sea sobre una persona en particular involucrada en el caso; por ejemplo: la víctima, el perpetrador, etc.
15494	15001	staticText31	Casos/Datos generales/Fecha final	Indicación de cuándo terminaron los hechos que se incluyen en este caso. Generalmente es la fecha cuando termina el último incidente o acto, o cuando se resuelve la situación. Si el caso no está cerrado o no ha terminado, NO ingreses ninguna fecha. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15399	15001	buttonSelTipoPerp	Actos/Perpetradores/Tipo de perpetrador / (+) signo de más	Haz clic aquí para agregar el término que represente de la mejor manera al  perpetrador en este acto. Únicamente se puede ingresar un término. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15401	15001	staticText54	Actos/Perpetradores/Último estatus del perpetrador	Indicación del último estatus conocido de este perpetrador, por ejemplo si está siendo investigado o fue sancionado
15404	15001	textCtrlINObservaciones	Actos/Perpetradores/Observaciones	Registra aquí cualquier información adicional sobre el grado de involucramiento del perpetrador en este acto. Ingresa aquí únicamente información que sea pertinente a este acto. Si tienes información general sobre la persona, ingrésala en el campo más apropiado de la pestaña de "Personas", o ingresa un nuevo dato biográfico. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15405	15001	txtLongInObs	Actos/Perpetradores/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son 20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15592	15515	CPNodependientes	Personas individual/Detalles/No. de dependientes	Número de hijos u otros dependientes de quienes esta persona es responsable. Únicamente puedes ingresar números, por ejemplo "5"
15387	15001	statixText50	Actos/Perpetradores/Perpetradores / Lista	Lista de los perpetradores ya registrados en el acto activo. Están ordenados alfabéticamente por su  nombre. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro de la lista. Cuando encuentres el perpetrador que buscas, haz doble clic para seleccionarlo. Una vez seleccionado, puedes modificar o agregar datos. Si quieres ingresar un nuevo perpetrador, utiliza el botón "Agregar un perpetrador". 
15298	15001	AddLocalizacion	Casos/Datos generales/Nueva localización	Haz clic aquí para ingresar el estado, municipio y localidad en donde ocurrieron los hechos. Puedes hacer varios ingresos, por ejemplo si la situación afecta a varias comunidades o a más de un municipio. Puedes también ingresar más de un estado si los hechos suceden en la frontera entre dos estados de la república. El país por omisión es México pero se puede cambiar, y también se puede ingresar más de un país si los hechos ocurren en zona fronteriza. Si los hechos ocurren en diferentes lugares, ingrésalos todos aquí, por ejemplo: si la detención ocurre en Puebla pero presentan al detenido en el D.F. y luego lo encarcelan en Jalisco, ingresa los tres lugares. Asegúrate de ingresar todas las localizaciones pertinentes ya que debes seleccionar este dato cuando ingreses actos específicos
15395	15001	staticText52	Actos/Perpetradores/Grado de involucramiento	Es la forma como una persona, en su rol de perpetrador, está involucrada en este acto, es decir su grado de responsabilidad en cuanto al acto o VDH registrado  
15396	15001	buttonSelGradoInvol	Actos/Perpetradores/Grado de involucramiento / (+) signo de más	Haz clic aquí para agregar el término que represente de la mejor manera el grado de responsabilidad del perpetrador en este acto. Únicamente se puede ingresar un término.  Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15500	15001	Comentarios	Casos/Información administrativa/Comentarios	Anotaciones internas del trabajo institucional sobre el caso, por ejemplo: identificación de información que falta, que no está clara o que es contradictoria; pistas para la investigación; ubicación de probables testigos; opiniones o información no corroborada sobre los motivos o causas de los hechos; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el mouse para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH 
15312	15001	staticText79, choiceMonitoreo	Casos/Información administrativa/Estatus del caso	Indicación de si la organización está trabajando activamente sobre este caso y la prioridad que tiene. Por ejemplo, si el caso ya está resuelto, puedes seleccionar "Expediente cerrado", pero si el caso está sucediendo y es grave, puedes seleccionar "Caso urgente" 
15309	15001	staticText75, FCproyecto_grupo	Casos/Información administrativa/Proyecto local	Nombre de la campaña o proyecto en el que está trabajando tu organización, y para el cual este caso es relevante. Los proyectos pueden ser temas como "Sistema penitenciario", o productos como "Informe anual". También pueden ser seguimiento de ciertas entidades como "Ejército mexicano en el estado", situaciones como "Atenco" o "Zona norte", o un proceso judicial que lleva la organización. El nombre de proyecto se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos 
15310	15001	staticText77, FCproyecto_se	Casos/Información administrativa/Proyecto SE	Nombre de la campaña o proyecto en el que está trabajando la Secretaría Ejecutiva, y para el cual este caso es relevante.  Para los proyectos de toda La RedTDT, utilizar el campo "Proyecto conjunto". Los proyectos de la Secretaría Ejecutiva pueden ser productos como "Informe anual" o "Casos para la CIDH", temas, seguimiento de ciertas entidades, situaciones o procesos. El nombre de proyecto se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos 
15311	15001	txtLongAdmComent	Casos/Información administrativa/# espacios en Comentarios	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios.
15446	15001	btnDPersonaFuente	Fuentes/Fuente personal/Nombre de la fuente personal / P?	Haz clic aquí para ir al registro completo de esta persona y agregar o modificar datos, por ejemplo, corregir la ortografía del nombre. Desde la pestaña de "Personas" puedes regresar a este mismo lugar  oprimiendo el botón "Pantalla anterior"
15511	15001	staticText4	Casos/Información administrativa/Archivos	Indicación del archivo o archivos físicos o electrónicos en donde se puede encontrar la información y documentación sobre el caso, por ejemplo: número de expediente, ruta y nombre de archivo en la computadora, etc. También se debe indicar si existe y se puede obtener información en archivos de otra institución, sitio de Internet, etc. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15313	15001	txtLongAdmArch	Casos/Información administrativa/# espacios en Archivos	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15315	15001	LC7	Casos/Información narrativa/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15568	15515	CPOcupacion	Personas individual/Detalles/Ocupación	Ocupación, trabajo o actividad profesional que desempeña la persona activa. Únicamente se puede ingresar una ocupación para cada persona
15581	15515	CPLengua	Personas individual/Detalles/Lengua que habla	Lengua o lenguas indígenas que habla esta persona. Se puede ingresar varias lenguas para cada persona. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15308	15001	LC9	Casos/Información administrativa/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15497	15001	staticText75	Casos/Información administrativa/Proyecto local	Nombre de la campaña o proyecto en el que está trabajando tu organización, y para el cual este caso es relevante. Los proyectos pueden ser temas como "Sistema penitenciario", o productos como "Informe anual". También pueden ser seguimiento de ciertas entidades como "Ejército mexicano en el estado", situaciones como "Atenco" o "Zona norte", o un proceso judicial que lleva la organización. El nombre de proyecto se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos separándolos con comas, punto, o punto y coma.
15402	15001	buttonSelUltStatusPerp	Actos/Perpetradores/Último estatus del perpetrador / (+) signo de más	Haz clic aquí para agregar el término que represente de la mejor manera el último estatus conocido del perpetrador. Únicamente se puede ingresar un término. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15317	15001	staticText35, textCtrlResumen	Casos/Información narrativa/Resumen de la descripción	Para moverte dentro del texto, utiliza el mouse para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH, por ejemplo la descripción narrativa de arriba
15328	15001	staticText109, btnTipoRelCaso	Casos/Relaciones/Relación entre casos	La relación que existe entre el caso activo y el caso relacionado. Si hay más de una relación, la información es de la relación sobre la cual está el cursor. Si quieres modificar el tipo de relación, haz clic en el signo de más (+) para seleccionar otra relación. La relación se establece desde el caso activo 
15322	15001	staticText107, listBoxCasoRel	Casos/Relaciones/Relacionado con	Lista alfabética de todas las relaciones que el caso activo tiene con otros casos registrados en el sistema. Utiliza el cursor o la barra de desplazamiento para moverte hacia abajo o hacia arriba, o hacia la derecha o la izquierda dentro de la lista. Cuando encuentres el caso que buscas, haz doble clic para seleccionarlo y modificar o agregar datos. Si quieres ingresar una nueva relación, utiliza el botón "Nueva relación" 
15335	15001	staticText8, listBoxTemas	Casos/Tipificaciones/Temas	Lista alfabética de los temas principales que describen el conjunto de la información de este caso. Para moverte dentro de la lista hacia abajo o hacia arriba, utiliza el cursor o la barra de desplazamiento. Para registrar un nuevo tema, oprime el botón "Agregar tema" 
15314	15001	buttonActualizarCaso3	Casos/Información administrativa/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo, guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15316	15001	txtLongNarra	Casos/Información narrativa/# espacios en Descripción narrativa	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15318	15001	txtLongResDesc	Casos/Información narrativa/# espacios en Resumen de la descripción	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aquí tienes un límite de 1,000 palabras, más o menos 6,000 espacios.
15319	15001	txtLongObs	Casos/Información narrativa/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15320	15001	buttonActualizarCaso2	Casos/Información narrativa/Guardar	Haz clic aquí para guardar la información cuando hayas ingresado o modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo, guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15504	15001	staticText107	Casos/Relaciones/Relacionado con	Lista en orden alfabético de todas las relaciones que el caso activo tiene con otros casos registrados en el sistema. Utiliza el cursor o la barra de desplazamiento para moverte dentro de la lista. Cuando encuentres el caso relacionado que buscas, haz doble clic para seleccionarlo y modificar o agregar datos. Si quieres ingresar una nueva relación, utiliza el botón "Nueva relación"
15480	15001	staticText63	Fuentes/Fuente documental/Idioma	Idioma en el cual está el documento. Haz clic en la flechita  para que aparezca la lista de idiomas.  Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el idioma que buscas, haz clic para seleccionarlo, y aparecerá en  el campo. Para borrar el idioma, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Alemán". Únicamente se puede ingresar un idioma para cada fuente
15508	15001	staticText106	Casos/Relaciones/Comentarios	Anotaciones internas del trabajo institucional sobre la relación entre los dos casos. Por ejemplo, características comunes o discrepancias notables entre los casos, opiniones o información no corroborada sobre la relación, etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. La información que registres aquí, corresponderá a la relación que está activa. Para activar una relación, haz doble clic en el caso relacionado que aparece en el recuadro de arriba.
15329	15001	btnInfoCasoRel	Casos/Relaciones/I (letra I)	Datos de la creación y actualización del registro de la relación entre casos. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización.
15331	15001	LC2	Casos/Tipificaciones/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15334	15001	delDerecho	Casos/Tipificaciones/Borrar derecho	Haz clic aquí para borrar el derecho seleccionado. Antes de poder borrar un derecho debes borrar los actos correspondientes. Si un acto tiene una violación al derecho que quieres borrar, cuando intentes borrarlo te aparecerá una alerta y los datos no serán borrados
15483	15001	txtLongFDObs	Fuentes/Fuente documental/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15499	15001	staticText77	Casos/Información administrativa/Proyecto SE	Nombre de la campaña o proyecto en el que está trabajando la Secretaría Ejecutiva, y para el cual este caso es relevante.  Para los proyectos de toda La RedTDT, utilizar el campo "Proyecto conjunto". Los proyectos de la Secretaría Ejecutiva pueden ser productos como "Informe anual" o "Casos para la CIDH", temas, seguimiento de ciertas entidades, situaciones o procesos. El nombre de proyecto se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos separándolos con comas, punto, o punto y coma.
15332	15001	buttonCasoDerechoafectado	Casos/Tipificaciones/Agregar derecho	Haz clic aquí para agregar un nuevo derecho que esté afectado por los hechos que ocurren en el caso. Recuerda que únicamente podrás seleccionar actos relacionados con los derechos que hayas ingresado en esta "Tipificación" del caso. Puedes ingresar todos los derechos que consideres relevantes
15330	15001	crGuardar	Casos/Relaciones/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo, guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15463	15001	LC15	Fuentes/Fuente documental/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar una nueva fuente documental, o para modificar datos ya registrados para esta fuente. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15466	15001	delFuenteDoc	Fuentes/Fuente documental/Borrar fuente documental	Haz clic aquí para borrar del sistema la fuente documental seleccionada
15467	15001	btnInfoDoc	Fuentes/Fuente documental/I (letra I)	Datos de la creación y actualización de este registro de fuente documental. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15468	15001	staticText57	Fuentes/Fuente documental/Exportar fuente documental	Despalomea "Exportar fuente documental" si quieres que la fuente documental activa de este caso, no se exporte. Haz clic en la casilla para palomear o despalomear esta opción.
15469	15001	staticText55	Fuentes/Fuente documental/Identificación	Nombre o identificación de esta fuente. Se recomienda que sea corta pero informativa, por ejemplo: La Jornada, Expediente judicial, Testimonio de Ramón, etc.
15470	15001	staticText56	Fuentes/Fuente documental/Datos de la fuente	La información indispensable para poder localizar o citar un documento, por ejemplo: Título (del artículo, capítulo, programa radial, etc.); Título del libro, periódico, noticiero, etc.; Autor; Lugar de edición o publicación; Editorial; Edición, etc.
15471	15001	txtLongFDDatos	Fuentes/Fuente documental/# espacios en Datos de la fuente	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aquí tienes un límite de 550 espacios, más o menos 75  palabras
15472	15001	staticText58	Fuentes/Fuente documental/Fecha de la fuente	Fecha original de la fuente documental, por ejemplo fecha de publicación de un periódico, de emisión de un programa de radio, de difusión de un comunicado, etc. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15476	15001	staticText59	Fuentes/Fuente documental/Nombre del sitio	Nombre del sitio de Internet en donde se encuentra el documento. Puedes escribir el nombre en texto libre y además poner la liga general al sitio, por ejemplo: La Jornada (http://www.jornada.unam.mx/ultimas/)
15477	15001	staticText60	Fuentes/Fuente documental/Liga a la fuente	Liga precisa al documento que se está registrando, por ejemplo: http://www.jornada.unam.mx/ultimas/2009/01/11/hallan-ejecutado-en-sonora-a-policia-municipal-de-guasave-sinaloa
15478	15001	btnAbrirLiga	Fuentes/Fuente documental/Abrir liga	Si hay dato registrado en el campo, haz clic en este botón y la liga se abrirá en tu navegador de manera automática. Si no es posible abrir la liga, aparecerá una Alerta. Haz clic en aceptar y verifica que no haya caracteres de más, por ejemplo < > al inicio o al final de la liga, punto final, etc.
15479	15001	staticText61	Fuentes/Fuente documental/Fecha de consulta	Fecha en que se consulta la fuente documental, especialmente en Internet. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15481	15001	staticText64	Fuentes/Fuente documental/Lengua indígena	Lengua indígena en la cual está el documento. Haz clic en el botón (+) para que aparezcla la lista de lenguas indígenas. Únicamente se puede ingresar una lengua para cada fuente.
15488	15001	staticText68	Fuentes/Fuente documental/Confiabilidad	Evaluación de la confiabilidad de la información proporcionada por la fuente, por ejemplo "Poco confiable". Haz clic en el botón (+)  para agregar un término que represente de la mejor manera la relación entre la fuente y la información que proporcionó. Únicamente se puede ingresar un carácter de confiabilidad para cada fuente. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente.
15491	15001	txtLongFDComent	Fuentes/Fuente documental/# espacios en Comentarios	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15338	15001	delTema	Casos/Tipificaciones/Borrar tema	Haz clic aquí para borrar el tema que se encuentre seleccionado. Para seleccionar un tema haz clic sobre él
15444	15001	staticText23	Fuentes/Fuente personal/Exportar fuente personal	Despalomea "Exportar fuente personal" si quieres que la fuente personal activa de este caso, no se exporte. Haz clic en la casilla para palomear o despalomear esta opción. 
15451	15001	staticText25	Fuentes/Fuente personal/Conexión con la información	Relación que existe entre la persona que aporta la información (la fuente personal) y la información proporcionada sobre el caso, por ejemplo: "Víctima del evento", "Testigo(a) del evento", "Autoridad comunitaria", etc.
15474	15001	btnPubTipoPub	Fuentes/Fuente documental/Tipo de fuente / (+) signo de más	Haz clic aquí para seleccionar el tipo de fuente que corresponda. Únicamente se puede ingresar un tipo de fuente para cada registro. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15482	15001	staticText65	Fuentes/Fuente documental/Observaciones	Registra aquí cualquier información adicional sobre la fuente documental de donde se tomó la información sobre el caso. Si es relevante, indica sobre qué o quién proporcionó información esta fuente. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15485	15001	buttonPubAddPerson	Fuentes/Fuente documental/Sobre quién se aporta información / (+) signo de más	Haz clic aquí  para seleccionar el nombre de la persona sobre quien la fuente documental aportó información. Si ya hay un nombre registrado y lo quieres sustituir, haz clic aquí y selecciona a una persona diferente
15486	15001	buttonPubRemovePerson	Fuentes/Fuente documental/Sobre quién se aporta información / (x) signo de multiplicación	Haz clic aquí para borrar el nombre de esta persona. Si quieres sustituir a la persona, utiliza el signo de más (+)
15490	15001	staticText69	Fuentes/Fuente documental/Comentarios	Anotaciones internas del trabajo institucional sobre el documento, por ejemplo: información que falta, no está clara o es contradictoria; otras fuentes documentales que haga falta consultar para corroborar los datos aportados por esta fuente;  opiniones sobre la fuente;  etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15492	15001	btnSavePub	Fuentes/Fuente documental/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo, guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15457	15001	txtLongFPObs	Fuentes/Fuente personal/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15459	15001	btnDelFteConfiabilidad	Fuentes/Fuente personal/Confiabilidad / (x) signo de multiplicación	Haz clic aquí para borrar el dato
15461	15001	txtLongFPComent	Fuentes/Fuente personal/# espacios en Comentarios	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15473	15001	staticText62	Fuentes/Fuente documental/Tipo de fuente	El tipo más representativo de esta fuente documental, por ejemplo: "Certificado de defunción", "Acción urgente de organización internacional", etc.  Únicamente se puede ingresar un tipo para cada fuente documental
15489	15001	btnDelPubConfiabilidad	Fuentes/Fuente documental/Confiabilidad / (x) signo de multiplicación	Haz clic aquí para borrar el dato.
15440	15001	buttonFteNueva	Fuentes/Fuente personal/Agregar fuente personal	Haz clic aquí para agregar una nueva fuente personal. Aparecerá una ventana en la que debes seleccionar el nombre de la persona que proporciona información del caso.
15442	15001	delFuentePer	Fuentes/Fuente personal/Borrar fuente personal	Haz clic aquí para borrar del sistema la fuente personal seleccionada. Únicamente se borra el registro de la persona como fuente de información en el caso activo. Su registro general de persona no se borra
15432	15001	txtLongIntImp	Interven-ciones/Pantalla única/# espacios en Impacto	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15434	15001	txtLongIntObs	Interven-ciones/Pantalla única/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15436	15001	txtLongIntComent	Interven-ciones/Pantalla única/# espacios en Comentarios	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15443	15001	btnInfoFte	Fuentes/Fuente personal/I (letra I)	Datos de la creación y actualización de este registro de fuente personal. Se indica la persona que ingresó el registro la primera vez, así como la persona qué hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15448	15001	btnAddFtePersonaRel	Fuentes/Fuente personal/Persona sobre quien se aporta información / (+) signo de más	Haz clic aquí  para seleccionar el nombre de la persona sobre quien la fuente personal aportó información; por ejemplo, la víctima o el perpetrador. Si ya hay un nombre registrado y lo quieres sustituir, haz clic aquí y selecciona a una persona diferente
15449	15001	btnRemoveFtePersonaRel	Fuentes/Fuente personal/Persona sobre quien se aporta información / (x) signo de multiplicación	Haz clic aquí para borrar el nombre de esta persona. Si quieres sustituir a la persona, utiliza el signo de más (+)
15450	15001	btnDPersonaRel	Fuentes/Fuente personal/Persona sobre quien se aporta información / P?	Haz clic aquí para ir al registro completo de esta persona. Desde la pestaña de "Personas" puedes regresar a este mismo lugar  oprimiendo el botón "Pantalla anterior"
15454	15001	staticText26	Fuentes/Fuente personal/Idioma	Idioma en el cual está la información proporcionada por la fuente, por ejemplo el audio o transcripción de una entrevista o testimonio. Haz clic en la flechita para que aparezca la lista de idiomas. Cuando encuentres el idioma que buscas, selecciónalo y aparecerá en  el campo. Para borrar el idioma, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba. Únicamente se puede ingresar un idioma para cada fuente.
15455	15001	staticText28	Fuentes/Fuente personal/Lengua indígena	Lengua indígena en la cual está la información proporcionada por la fuente, por ejemplo el audio o transcripción de una entrevista o testimonio. Haz clic en el botón (+) para que aparezca la lista de lenguas indígenas. Únicamente se puede ingresar una lengua para cada fuente.
15456	15001	staticText33	Fuentes/Fuente personal/Observaciones	Registra aquí cualquier información adicional sobre la persona que proporcionó información sobre el caso. Si es relevante, indica sobre qué o quién proporcionó información esta persona. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15462	15001	buttonFteActualizarDatos	Fuentes/Fuente personal/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo, guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15487	15001	btnDPersonaRel2	Fuentes/Fuente documental/Sobre quién se aporta información / P?	Haz clic aquí para ir al registro completo de esta persona. Desde la pestaña de "Personas" puedes regresar a este mismo lugar  oprimiendo el botón "Pantalla anterior"
15425	15001	staticText9	Interven-ciones/Pantalla única/A quién se le dirigió esta intervención	Persona o entidad a quién se le dirigió esta intervención, por ejemplo: "Comisión Interamericana de Derechos Humanos", el nombre de un gobernador, etc.
15427	15001	buttonRemoveAquien	Interven-ciones/Pantalla única/A quién se le dirigió esta intervención / (x) signo de multiplicación	Haz clic aquí para borrar el nombre de esta persona. Si quieres sustituir a la persona, utiliza el signo de más (+)
15430	15001	txtLongIntRes	Interven-ciones/Pantalla única/# espacios en Respuesta	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15414	15001	staticText15	Interven-ciones/Pantalla única/Exportar intervención	Despalomea "Exportar intervención" si quieres que la intervención activa de este caso, no se exporte. Haz clic en la casilla para palomear o despalomear esta opción. 
15420	15001	staticText72	Interven-ciones/Pantalla única/Fecha de la intervención	Fecha en que se realiza esta intervención, por ejemplo fecha del boletín de prensa o cuando se inicia la acción urgente, denuncia penal, etc. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15421	15001	staticText21	Interven-ciones/Pantalla única/Sobre quién se interviene	Nombre de la persona, generalmente la víctima del acto, a favor de quien se hace esta intervención
15423	15001	buttonRemoveDequien	Interven-ciones/Pantalla única/Sobre quién se interviene / (x) signo de multiplicación	Haz clic aquí para borrar el nombre de la persona "Sobre quién se interviene". Si quieres sustituir a la persona, utiliza el signo de más (+)
15424	15001	btnDPersonaSobre	Interven-ciones/Pantalla única/Sobre quién se interviene / P?	Haz clic aquí para ir al registro completo de esta persona. Desde la pestaña de "Personas" puedes regresar a este mismo lugar  oprimiendo el botón "Pantalla anterior"
15426	15001	buttonAQuien	Interven-ciones/Pantalla única/A quién se le dirigió esta intervención / (+) signo de más	Haz clic aquí  para seleccionar el nombre de la persona o entidad a quien se le dirigió  la intervención, por ejemplo "Amnistía Internacional".
15428	15001	btnDPersonaAquien	Interven-ciones/Pantalla única/A quién se le dirigió esta intervención / P?	Haz clic aquí para ir al registro completo de esta persona. Desde la pestaña de "Personas" puedes regresar a este mismo lugar  oprimiendo el botón "Pantalla anterior"
15429	15001	staticText86	Interven-ciones/Pantalla única/Respuesta a la intervención	Indicación de la reacción o respuesta que hubo a la intervención, en general, o en particular de la persona o entidad a quien se le dirigió esta intervención. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15431	15001	staticText84	Interven-ciones/Pantalla única/Impacto de la intervención	Indicación de la magnitud o envergadura de la intervención así como de la manera en que la intervención afectó la situación. Por ejemplo: un impacto positivo es que la persona detenida fue liberada como consecuencia de la intervención; un impacto negativo puede ser que la persona detenida fue trasladada a un penal lejano a su lugar de origen, o que fue amenazada como consecuencia de la intervención. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15617	15001	Pguardar3	Personas todas/Información administrativa/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo, guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15433	15001	staticText88	Interven-ciones/Pantalla única/Observaciones	Registra aquí cualquier información adicional sobre la intervención. Indica si la intervención se hizo en relación a un acto particular dentro del caso, sobre una persona o sobre el caso en su conjunto. También puedes indicar el grado de publicidad generado y el interés de la prensa, así como datos adicionales que no estén ingresados en otros campos. También puedes utilizar este espacio para incluir el texto y los destinatarios de la intervención. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15435	15001	staticText85	Interven-ciones/Pantalla única/Comentarios	Anotaciones internas del trabajo institucional sobre la intervención, por ejemplo: información sobre el uso y agotamiento de los recursos internos; estrategias para el seguimiento de las acciones; otras personas a quien se puede enviar la intervención; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15437	15001	buttonIntervencionActualizar	Interven-ciones/Pantalla única/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo, guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15619	15001	staticText20	Personas todas/Datos biográficos/Datos biográficos / Lista	Lista de los datos biográficos registrados para la persona activa. Están ordenados alfabéticamente por la descripción del dato biográfico y/o por el nombre de la persona relacionada seguido del tipo de relación. Para moverte dentro de la lista utiliza el cursor o las barras de desplazamiento. Cuando encuentres el dato que buscas, haz clic para seleccionarlo. Una vez seleccionado, puedes modificar o agregar datos. Si quieres ingresar un nuevo dato biográfico, utiliza el botón "Agregar dato biográfico" 
15413	15001	btnInfoInterv	Interven-ciones/Pantalla única/I (letra I)	Datos de la creación y actualización de este registro de intervención. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15417	15001	staticText83	Interven-ciones/Pantalla única/Quién inicia o realiza esta intervención	Persona individual o entidad que inicia o es responsable de esta intervención
15422	15001	buttonDeQuien	Interven-ciones/Pantalla única/Sobre quién se interviene / (+) signo de más	Haz clic aquí  para seleccionar el nombre de la persona a favor de quien se hace la intervención o para sustituir un dato ya registrado
15523	15001	listBoxPersonaBrowser	Personas todas/Datos generales/Lista de personas / Lista	Lista en orden alfabético de todas las personas registradas en el sistema. Para moverte dentro de la lista, utiliza el cursor o las barras de desplazamiento. Cuando encuentres la persona que buscas, selecciónala con doble clic. Una vez seleccionada, puedes agregar o modificar sus datos. Para ingresar una nueva persona, utiliza el botón "Nueva persona". Si realizas una búsqueda rápida o exhaustiva, esta lista mostrará sólo las personas que coincidan con los criterios de tu búsqueda.
15528	15001	delPersona	Personas todas/Datos generales/Borrar persona	Haz clic aquí para borrar del sistema el registro de la persona seleccionada. Para borrar a la persona debes borrar todas las relaciones que tenga asociadas; ya sea como víctima, perpetrador, fuente personal o en algún registro de intervención o fuente documental. Si la persona aún tiene relaciones, cuando intentes borrarla te aparecerá una alerta y el registro no será borrado.
15529	15001	btnRepsPersona	Personas todas/Datos generales/Reportes	Haz clic aquí para moverte a la pantalla de "Reportes" en donde podrás generar diferentes tipos de reportes
15534	15001	CPTipo	Personas colectivas/Datos generales/Tipo de grupo	Término que mejor define a la entidad o grupo, por ejemplo: "Comunidad", "Familia", "Grupo, organización o institución"
15535	15001	btnAddFPTipo	Personas colectivas/Datos generales/Tipo de grupo / (+) signo de más	Haz clic aquí y, en la ventana que aparece, selecciona el término que mejor defina a la entidad o grupo que estás registrando. Únicamente se puede ingresar un tipo de grupo para cada entidad. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15566	15001	buttonPGuardar	Personas todas/Datos generales/Guardar	Haz clic aquí para guardar la información y actualizar el despliegue de datos. Recuerda que al cambiar de pestaña también se guarda la información pero no necesariamente se actualiza el nombre en la lista de personas
15595	15001	staticText67	Personas todas/Detalles/Dirección(es)	Información respecto a dónde vive, ha vivido o se puede localizar a esta persona o entidad. Puedes ingresar varias direcciones. Para moverte dentro de la lista, utiliza el cursor o las barras de desplazamiento
15597	15001	delDireccion	Personas todas/Detalles/Dirección(es) / (x) signo de multiplicación	Haz clic aquí para borrar la dirección que esté seleccionada en la ventana de al lado
15612	15001	longPerArch	Personas todas/Información administrativa/# espacios en Archivos	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15629	15001	btnInfoBio	Personas todas/Datos biográficos/I (letra I)	Datos de la creación y actualización de este registro de dato biográfico. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15419	15001	btnDPersonaParteInt	Interven-ciones/Pantalla única/Quién inicia o realiza esta intervención / P?	Haz clic aquí para ir al registro completo de esta persona y agregar o modificar datos, por ejemplo, corregir un error ortográfico en el nombre. Desde la pestaña de "Personas" puedes regresar a este mismo lugar  oprimiendo el botón "Pantalla anterior"
15630	15001	staticText92	Personas todas/Datos biográficos/Descripción	Es la descripción de un dato biográfico que NO sea una relación entre la persona activa y otra persona. Puede ser una declaración de algún funcionario, una publicación relevante de alguna organización, etc.
15631	15001	staticTxtTipoderelacion	Personas todas/Datos biográficos/Tipo de relación	Es el tipo de relación que existe entre la persona activa y la persona que aparece abajo en el campo "Persona relacionada"
15636	15001	staticText80	Personas todas/Datos biográficos/Fecha inicial	Indicación de cuándo inicia el dato biográfico que se está registrando o actualizando. Por ejemplo: cuándo inicia la relación de trabajo entre dos personas (fecha cuando un funcionario asume el puesto o cargo público en una institución). Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15637	15001	staticText10	Personas todas/Datos biográficos/Fecha final	Indicación de cuándo terminó el dato biográfico que se está registrando o actualizando. Por ejemplo, si es una relación de trabajo entre dos personas, la fecha cuando un funcionario es destituido o renuncia a su puesto o cargo público. Si la relación o el dato biográfico no ha terminado, NO ingreses ninguna fecha. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15618	15001	staticPersonaActual3	Personas todas/Datos biográficos/[#] Nombre de la persona	Esta es la persona activa a quien se le está agregando un nuevo dato biográfico relacionado con otra persona. Si quieres trabajar sobre una persona distinta, haz clic en el botón "Cancelar" para regresar a la pestaña "Datos generales" y selecciona una persona diferente
15634	15001	staticTxtPrelacionada	Personas todas/Datos biográficos/P. relacionada	Es el nombre de la persona que está relacionada con la persona activa por medio del "Tipo de relación" que aparece en el campo de arriba
15520	15001	txtTotalPersonas	Personas todas/Datos generales/# personas registradas	El número total de personas registradas en el sistema. El número no es igual al número de la última persona ingresada
15247	15000	DlgLocalidad	Localidad	
15248	15000	DlgCaso	Nuevo caso	
15249	15000	DerechoAfectado	Derecho afectado	
15250	15000	Temas	Temas	
15251	15000	Victima	Persona como victima	
15252	15000	TipoDeActo	Tipo De Acto	
15253	15000	dlgpersonaperpetrador	Persona como perpetrador	
15254	15000	DlgInterv	Nueva intervencion	
15255	15000	FuentePersonal	Fuente Personal	
15567	15001	staticPersonaActual1	Personas todas/Detalles/[#] Nombre de la persona	Esta es la persona que está activa para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar sobre otra persona, regresa a la pestaña "Datos generales" de "Personas" y selecciona una persona diferente.
15574	15515	CPIdioma	Personas individual/Detalles/Idioma que habla	Idioma que habla, lee y/o escribe esta persona. Se puede ingresar varios idiomas para cada persona. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15596	15001	FPAddDirecciones	Personas todas/Detalles/Dirección(es) / (+) signo de más	Haz clic aquí para agregar una nueva dirección. Aparecerá una ventana en la que debes ingresar los datos. Si quieres agregar una segunda dirección, haz clic aquí y repite el procedimiento. Para correjir o actualizar una dirección registrada, haz doble clic sobre ella y se abrirá la ventana que contiene sus datos respectivos para que los modifiques
15604	15001	CPMonitoreo	Personas todas/Detalles/Monitoreo	Indica si la organización está trabajando activamente sobre esta persona. Por ejemplo, selecciona "Activo" si se le está dando seguimiento cotidiano a la entidad "Ejército Mexicano" o a la Procuraduría de tu estado. Haz clic en la flechita para abrir la lista de opciones. Si quieres borrar un dato registrado, haz clic en el espacio en blanco que aparece al inicio de la lista.
15605	15001	Pguardar2	Personas todas/Detalles/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información
15606	15001	staticPersonaActual2	Personas todas/Información administrativa/[#] Nombre de la persona	Esta es la persona que está activa para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar sobre otra persona, regresa a la pestaña "Datos generales" de "Personas" y selecciona una persona diferente
15607	15001	CPObservaciones	Personas todas/Información administrativa/Observaciones	Registra aquí cualquier información adicional sobre la persona que no esté ingresada en otros campos o como dato biográfico adicional a la persona. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15608	15001	longPerObs	Personas todas/Información administrativa/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15609	15001	staticText38	Personas todas/Información administrativa/Comentarios	Anotaciones internas del trabajo institucional sobre la persona, por ejemplo: información que falta, que no está clara o es contradictoria; estrategias o fuentes adicionales para seguimiento o verificación; opiniones o información no corroborada sobre la persona; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15610	15001	longPerCom	Personas todas/Información administrativa/# espacios en Comentarios	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15615	15001	staticText100	Personas todas/Información administrativa/Proyecto conjunto RedTDT	Nombre de la campaña o  proyecto en el que está trabajando la RedTDT en su conjunto, y para el cual esta persona es relevante, por ejemplo: "Criminalización de la protesta social". Este nombre se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos siempre y cuando estén acordados en el marco del trabajo conjunto de La RedTDT
15293	15001	btnReps	Casos/Datos generales/Reportes	Haz clic aquí para moverte a la pantalla de "Reportes" en donde podrás generar diferentes tipos de reportes
15632	15001	btnTipoVinculo	Personas todas/Datos biográficos/Tipo de relación / (+) signo de más	Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí  y, en la ventana que aparece, selecciona un término diferente. Haz clic en los signos de más (+) para abrir las listas. Cuando encuentres la relación que buscas, haz clic para seleccionarla y oprime el botón "Seleccionar". El término seleccionado aparecerá en el campo. Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un tipo de relación para cada registro
15644	15001	staticText90	Personas todas/Datos biográficos/Rango	Identificación del rango militar o de las fuerzas de seguridad que tiene esta persona, por ejemplo "General de división", "Comandante"
15533	15001	staticPersonaActual0	Personas todas/Datos generales/[#] Nombre de la persona	Esta es la persona que está activa para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar sobre otra persona, búscala en la ventana de abajo y selecciónala
15326	15248	staticText1, casoIsearch	Casos/Relaciones/Nueva relación / Buscar	Para encontrar el caso que buscas, utiliza el mouse para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. También puedes escribir unas cuantas letras del nombre del caso que estás buscando. Ejemplo: "huelga" para ver todos los casos que tengan la palabra "huelga" como parte de su nombre. Si el nombre es muy largo y no puedes leerlo completo, utiliza el mouse para desplazar hacia la derecha o la izquierda la barra que está  abajo de la ventana. De los casos que aparecen, posiciona el cursor sobre el que quieras relacionar con el caso activo y oprime el botón "Establecer relación". Si quieres, puedes cancelar el ingreso haciendo clic en "Cancelar"
15324	15248	staticText109, btnTipoRelCaso	Casos/Relaciones/Nueva relación / Se relaciona como	Haz clic en el signo de más (+) para abrir la lista de tipos de relación entre casos. Utiliza el cursor para moverte hacia abajo o hacia arriba. Cuando encuentres la relación que buscas, haz clic para seleccionarla y oprime el botón "Seleccionar". La relación aparecerá en la ventana de registro. Si deseas cancelar la operación,  haz clic en "Cancelar"
15545	15516	CPfechanac	Personas colectivas/Datos generales/Fecha de creación	Fecha de creación, fundación o surgimiento de esta entidad, grupo o movimiento. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta" 
15540	15516	CPApellido	Personas colectivas/Datos generales/Nombre	Nombre completo de la entidad colectiva, de preferencia su nombre oficial, por ejemplo: "Ejército Mexicano"
15542	15516	staticText110	Personas colectivas/Datos generales/Otro nombre	Otro nombre por que el que se conozca a la entidad que estás registrando. Puede ser un nombre "corto" como "Frayba" o "Tlachi", o un nombre por el que se la conozca coloquialmente
15549	15516	btnFPPais	Personas colectivas/Datos generales/País de origen / (+) signo de más	Si quieres cambiar "México" por otro país,  haz clic aquí y selecciona un país diferente de la lista que aparece. Utiliza el cursor para moverte hacia abajo o hacia arriba, y haz clic en el signo de más (+) para abrir la lista. Cuando encuentres el país que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". El país seleccionado aparecerá en el campo. Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un país de origen para cada entidad
15551	15516	btnRemoveFPPais	Personas colectivas/Datos generales/País de origen / (x) signo de multiplicación	Haz clic aquí para borrar el país de origen de esta entidad, grupo o movimiento
15557	15516	CPLocalidad	Personas colectivas/Datos generales/Localidad de origen	Escribe el nombre de la comunidad o localidad en donde se crea, funda o surge esta entidad, grupo o movimiento. El nombre no debe ser más largo de unas 20 palabras. Para borrar la localidad, selecciona todo el nombre y oprime el botón de "suprimir" en tu teclado
15613	15001	staticText101	Personas todas/Información administrativa/Fecha de recepción	Fecha en que la organización tuvo conocimiento de los datos de esta persona por primera vez. Puede ser la fecha en que inicialmente se atendió la denuncia, la fecha original de la fuente de información, o la fecha cuando se consultó la fuente por primera vez. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15614	15001	staticText103	Personas todas/Información administrativa/Proyecto local	Nombre de la campaña o proyecto en el que está trabajando tu organización, y para el cual esta persona es relevante. Los proyectos pueden ser temas como "Sistema penitenciario", o productos como "Informe anual". También pueden ser seguimiento de ciertas entidades como "Ejército mexicano en el estado", situaciones como "Atenco" o "Zona norte", o un proceso judicial que lleva la organización. El nombre de proyecto se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos
15616	15001	staticText102	Personas todas/Información administrativa/Proyecto SE	Nombre de la campaña o proyecto en el que está trabajando la Secretaría Ejecutiva, y para el cual esta persona es relevante. Para los proyectos de toda La RedTDT, utilizar el campo "Proyecto conjunto". Los proyectos de la Secretaría Ejecutiva pueden ser productos como "Informe anual" o "Casos para la CIDH", temas, seguimiento de ciertas entidades, situaciones o procesos. El nombre de proyecto se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos 
15325	15248	staticText2	Casos/Relaciones/Nueva relación / Con el caso siguiente	Es el caso con el cual quieres establecer la relación. Para seleccionarlo, primero debes buscarlo en la ventana de abajo
15411	15254	staticText1	Interven-ciones/Pantalla única/Agregar una intervención / Agregar intervención - Tipo de intervención	Haz clic en el signo de más (+) al lado de "Tipo de intervención" y, en la ventana que aparece, selecciona el tipo que mejor describa la intervención. El tipo de intervención seleccionado aparecerá aquí. Oprime el botón "Seleccionar" para terminar la operación. Si deseas cancelar la operación, haz clic en "Cancelar"
15547	15516	CPPais	Personas colectivas/Datos generales/País de origen	País en donde se crea, funda o surge esta entidad, grupo o movimiento. México aparece por omisión pero se puede cambiar haciendo clic en el signo de más (+) ubicado al lado del campo. Únicamente se puede ingresar un país de origen para cada entidad
15295	15001	textDescripcion,staticText3	Casos/Datos generales/Nombre del caso	Nombre que identifica claramente el caso. El nombre debe ser único para cada caso. Puedes ingresar un nombre de más o menos 35 palabras 
15294	15001	btnInfoCaso	Casos/Datos generales/I (letra I)	Datos de la creación y actualización del registro del caso. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15305	15001	staticText29	Casos/Datos generales/Exportar caso	Despalomea "Exportar caso" si quieres que el caso activo no se exporte. Haz clic en la casilla para palomear o despalomear esta opción. 
15306	15001	staticText1	Casos/Datos generales/Exportar relaciones	Despalomea "Exportar relaciones" si quieres que las relaciones del caso activo no se exporten. Haz clic en la casilla para palomear o despalomear esta opción.
15307	15001	btnActualizarCaso1	Casos/Datos generales/Guardar	Haz clic aquí para guardar la información y actualizar el despliegue de datos. Recuerda que al cambiar de pestaña también se guarda la información pero no necesariamente se actualiza el nombre del caso en la lista de casos
15323	15001	btnAddRelacion	Casos/Relaciones/Nueva relación	Haz clic aquí para establecer una relación entre el caso activo y otro caso que ya esté registrado en el sistema. En la ventana que aparece, completa los datos necesarios: el caso con el que se relaciona y el tipo de relación.
15536	15516	btnDelFPTipo	Personas colectivas/Datos generales/Tipo de grupo / (x) signo de multiplicación	Haz clic aquí para borrar el tipo de entidad, grupo o movimiento
15538	15516	CPNombre	Personas colectivas/Datos generales/Sigla	Sigla, acrónimo o nombre corto de la entidad colectiva, por ejemplo "PGR"
15559	15516	CPCiudadania	Personas colectivas/Datos generales/País sede	País en el cual se encuentra esta entidad, grupo o movimiento. México aparece por omisión pero se puede cambiar haciendo clic en el botón con el signo de más (+) ubicado al lado del campo. Únicamente se puede ingresar un país sede para cada entidad
15561	15516	btnFPCiudadania	Personas colectivas/Datos generales/País sede / (+) signo de más	Si quieres cambiar "México" por otro país,  haz clic aquí y selecciona un país diferente de la lista que aparece. Utiliza el cursor para moverte hacia abajo o hacia arriba, y haz clic en los signos de más (+) para abrir las listas. Cuando encuentres el país que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". El país seleccionado aparecerá en el campo. Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un país sede para cada entidad o persona colectiva
15565	15516	CPEscolaridad	Personas colectivas/Datos generales/Nivel de escolaridad predominante	Indicación del nivel predominante de educación del grupo registrado, por ejemplo, "Normal" para los estudiantes de las Normales rurales. Únicamente se puede ingresar un término para cada grupo o entidad. Haz clic en la flechita para que aparezcan todos los niveles de escolaridad. Cuando encuentres el nivel que buscas, márcalo y el término aparecerá en el campo. Para borrar el nivel de escolaridad, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un nivel diferente.
15569	15516	CPOcupacion	Personas colectivas/Detalles/Ocupación predominante	Actividad predominante a la que se dedica la entidad, grupo o movimiento, por ejemplo la ocupación, trabajo o actividad a la que se dedican la mayoría de los miembros de un sindicato, o la actividad de una empresa que contamina. Únicamente se puede ingresar una ocupación para cada entidad colectiva
15576	15515	FPAddIdioma	Personas individual/Detalles/Idioma que habla / (+) signo de más	Haz clic aquí para agregar un idioma. El idioma o idiomas que selecciones aparecerán en la ventana de al lado.
15577	15516	FPAddIdioma	Personas colectivas/Detalles/Idioma predominante / (+) signo de más	Haz clic aquí para agregar un idioma. El idioma o idiomas que selecciones aparecerán en la ventana de al lado.
15578	15515	delIdioma	Personas individual/Detalles/Idioma que habla / (x) signo de multiplicación	Haz clic aquí para borrar el idioma que está seleccionado en la ventana de al lado
15579	15516	delIdioma	Personas colectivas/Detalles/Idioma predominante / (x) signo de multiplicación	Haz clic aquí para borrar el idioma que está seleccionado en la ventana de al lado
15593	15516	CPNodependientes	Personas colectivas/Detalles/No. de personas en el grupo	Número exacto o aproximado de personas que integran la entidad o grupo Únicamente puedes ingresar números, por ejemplo "5000" para una empresa que tiene cinco mil trabajadores
15594	15516	CPDescripciondelgrupo	Personas colectivas/Detalles/Descripción del grupo	Muy breve descripción del grupo de más o menos 8-10 palabras. Para información sustantiva sobre la entidad, utiliza el campo "Observaciones" en la pestaña de "Información administrativa"
15285	15001	txtCasosSeleccionados	Casos/Datos generales/# casos seleccionados	El número de casos localizados como resultado de una búsqueda, por ejemplo: 4 casos seleccionados
15288	15001	btnSerachExecute	Casos/Datos generales/Aplicar	Después de completar los criterios de búsqueda en "Búsqueda exhaustiva", haz clic aquí para obtener los resultados
15289	15001	btnShowAll	Casos/Datos generales/Mostrar todo	Haz clic aquí para que aparezcan todos los casos registrados en el sistema después de que hayas hecho una búsqueda rápida o exhaustiva
15333	15249	treeCtrl1	Casos/Tipificaciones/Agregar derecho / Derecho afectado	Utiliza el cursor para moverte hacia abajo o hacia arriba, y haz clic en el signo de más (+) para abrir la lista de derechos. Cuando encuentres el derecho que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar"
15340	15001	LA1	Actos/Información general/Acto: Víctima / Acto	Este es el acto que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro acto, selecciónalo en la ventana "Actos registrados", o  ingresa uno nuevo
15342	15001	buttonNuevoActo	Actos/Información general/Agregar acto	Haz clic aquí para agregar un nuevo acto. Aparecerá una ventana en la que debes ingresar el nombre de la víctima y el tipo de acto
15349	15001	staticText44	Actos/Información general/Tipo de acto o VDH	Es el tipo específico del acto o la violación que sufrió la víctima. Si quieres modificar el tipo de acto o VDH, haz clic en el signo de más (+) para seleccionar uno diferente. Recuerda que únicamente podrás seleccionar actos relacionados con los derechos que hayas ingresado en "Derechos afectados" de la "Tipificación" del caso
15351	15001	staticText13	Actos/Información general/Víctima	Es el nombre de la persona que sufrió el tipo específico de acto o VDH registrado.
15358	15001	staticText49	Actos/Información general/Tipo de lugar	El tipo más representativo de lugar en donde ocurrió este acto.  Únicamente se puede ingresar un tipo de lugar para cada acto
15360	15001	buttonRemoveTipodelugar	Actos/Información general/Tipo de lugar / (x) signo de multiplicación	Haz clic aquí para borrar el tipo de lugar en donde ocurrió este acto
15363	15001	buttonRemoveEstatusVDH	Actos/Información general/Estatus VDH / (x) signo de multiplicación	Haz clic aquí para borrar el estatus de la VDH
15364	15001	staticText47	Actos/Información general/Estatus de la víctima	Indicación del último estatus conocido de la víctima, por ejemplo si ya fue liberada en un acto de detención arbitraria o ilegal
15366	15001	buttonRemoveEstatusdelavictima	Actos/Información general/Estatus de la víctima / (x) signo de multiplicación	Haz clic aquí para borrar el estatus de víctima
15371	15001	ActualizarActo	Actos/Información general/Guardar	Haz clic aquí para guardar la información y actualizar el despliegue de datos. Recuerda que al cambiar de pestaña también se guarda la información pero no necesariamente se actualiza la lista de actos
15377	15001	delLegislacion	Actos/Normatividad/Legislación nacional / (x) signo de multiplicación	Haz clic aquí para borrar la Legislación nacional  seleccionada. Para seleccionarla coloca el cursor sobre la misma y haz un clic.
15379	15001	FAInstr	Actos/Normatividad/Instrumentos internacionales / Lista	Lista en orden alfabético de todos los instrumentos internacionales ingresados para el acto activo. Para registrar un nuevo instrumento, oprime el signo de más (+) al lado de "Instrumentos internacionales"
15381	15001	delInstrInt	Actos/Normatividad/Instrumentos internacionales / (x) signo de multiplicación	Haz clic aquí para borrar el Instrumento internacional seleccionado. Para seleccionarlo coloca el cursor sobre el mismo y haz un clic.
15382	15001	btnInfoInter	Actos/Normatividad/Instrumentos internacionales / I (letra I)	Datos de la creación y actualización del registro de instrumentos internacionales. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización.
15383	15001	staticText5	Actos/Normatividad/Exportar normatividad	Despalomea "Exportar normatividad" si quieres que la normatividad del acto activo no se exporte. Haz clic en la casilla para palomear o despalomear esta opción. 
15384	15001	GuardarNormatividad	Actos/Normatividad/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15388	15001	buttonAddPerpetrador	Actos/Perpetradores/Agregar un perpetrador	Haz clic aquí para agregar un nuevo perpetrador. Asegúrate que el acto correspondiente esté activo.
15390	15001	delPerpetrator	Actos/Perpetradores/Borrar un perpetrador	Haz clic aquí para borrar del sistema el perpetrador seleccionado en el acto activo. Únicamente se borra el registro de la persona como perpetrador en este acto. Su registro general de persona no se borra
15392	15001	staticText51	Actos/Perpetradores/Exportar perpetrador	Despalomea "Exportar perpetrador" si quieres que el perpetrador activo no se exporte en este acto. Haz clic en la casilla para palomear o despalomear esta opción. 
15397	15001	buttonRemoveGradoInvol	Actos/Perpetradores/Grado de involucramiento / (x) signo de multiplicación	Haz clic aquí para borrar el grado de involucramiento del perpetrador
15400	15001	buttonRemoveTipoPerp	Actos/Perpetradores/Tipo de perpetrador / (x) signo de multiplicación	Haz clic aquí para borrar el tipo de perpetrador
15575	15516	CPIdioma	Personas colectivas/Detalles/Idioma predominante	Idioma que la mayoría de las personas en el grupo hablan, leen y/o escriben. Se puede ingresar varios idiomas para cada entidad o persona colectiva. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15582	15516	CPLengua	Personas colectivas/Detalles/Lengua predominante	Lengua o lenguas indígenas que hablan las personas en el grupo. Se puede ingresar varias lenguas para cada entidad o persona colectiva, por ejemplo si en un grupo de desplazados internos hay personas que hablan Ch'ol y Tseltal. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15287	15001	btnSearch	Casos/Datos generales/Búsqueda exhaustiva	Haz clic aquí para realizar una búsqueda más detallada de algún caso que ya esté dado de alta en el sistema. Por ejemplo, un caso con una localización específica, registrado en un cierto periodo de tiempo, registrado bajo algún proyecto local.
15327	15001	delRelacion	Casos/Relaciones/Borrar relación	Haz clic aquí para borrar la relación seleccionada. Para seleccionarla coloca el cursor sobre la misma y haz un clic
15513	15000	DatoBio	Dato Bio	
15514	15000	Direcciones	Direcciones	
15515	15000	personaInd	Persona Individual	
15516	15000	personaCol	Persona Colectiva	
15517	15000	AltaPersonaCol	Alta Persona Colectiva	
15518	15000	AltaPersonaInd	Alta Persona Individual	
15519	15000	AltaPersona	Alta Persona	
15406	15001	buttonActualizarInvol	Actos/Perpetradores/Guardar	Haz clic aquí para guardar la información y actualizar el despliegue de datos. Recuerda que al cambiar de pestaña también se guarda la información pero no necesariamente se actualiza el nombre del perpetrador en la lista
15412	15001	delInterv	Interven-ciones/Pantalla única/Borrar una intervención	Haz clic aquí para borrar del sistema la intervención seleccionada
15510	15001	buttonRemoveFteConexionInf	Fuentes/Fuente personal/Conexión con la información / (x) signo de multiplicación	Haz clic aquí para borrar el dato
15475	15001	btnRemovePubTipoPub	Fuentes/Fuente documental/Tipo de fuente / (x) signo de multiplicación	Haz clic aquí para borrar el dato
15562	15515	btnRemoveFPCiudadania	Personas individual/Datos generales/Ciudadanía / (x) signo de multiplicación	Haz clic aquí para borrar el país del cual es ciudadano esta persona
15563	15516	btnRemoveFPCiudadania	Personas colectivas/Datos generales/País sede / (x) signo de multiplicación	Haz clic aquí para borrar el país en el cual tiene su sede esta entidad, grupo o movimiento
15571	15516	btnAddOcupacion	Personas colectivas/Detalles/Ocupación predominante / (+) signo de más	Haz clic aquí y, en la ventana que aparece, selecciona el término que mejor defina la ocupación, trabajo o actividad  predominante a la que se dedica la entidad, grupo o movimiento. Únicamente se puede ingresar una ocupación para cada entidad. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15573	15516	btnDelOcupacion	Personas colectivas/Detalles/Ocupación predominante / (x) signo de multiplicación	Haz clic aquí para borrar la ocupación
31	127	021	Chichimeco jonaz	Municipio de San Luis de la Paz, Guanajuato. Usado por: Chichimecas jonaz, Chimeco, Meco; Uza, (plural: ezar)
33	127	027	Chocholteco	Oaxaca. Usado por: Chocho, Runixa ngiigua
34	127	030	Ch'ol	norte de Chiapas. Usado por: Chol; Winik
15580	15001	CPHablayentiendeespanol	Personas todas/Detalles/Habla y entiende español	Indica si esta persona habla y entiende el español. Este dato es importante para situaciones en donde la persona es indígena o extranjera y se enfrenta, por ejemplo, a un juicio para el cual requiere traducción. Haz clic en la casilla para "palomearla" e indicar que SI habla y entiende español, o "despalomea" la casilla para indicar que NO lo habla ni lo entiende suficientemente.
15601	15514	staticText5	Personas todas/Detalles/Dirección(es) / Celular	Ingresa el número de celular completo. Puedes ingresar varios números. Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección"
15587	15516	FPAddOrigenEtnico	Personas colectivas/Detalles/Origen étnico / (+) signo de más	Haz clic aquí para agregar el origen étnico predominante. Si ya hay un orígen étnico registrado y quieres agregar otro que también sea predominante, haz clic aquí y selecciónalo. Los términos que selecciones aparecerán en la ventana de al lado.
15602	15514	staticText6	Personas todas/Detalles/Dirección(es) / Correo electrónico	Ingresa la dirección de correo electrónico. Puedes ingresar varias direcciones. Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección"
15588	15516	delOrigen	Personas colectivas/Detalles/Origen étnico / (x) signo de multiplicación	Haz clic aquí para borrar el origen étnico predominante que está seleccionado en la ventana de al lado
15603	15514	staticText4	Personas todas/Detalles/Dirección(es) / Página WEB	Ingresa la página web de esta persona tal como aparece en Internet. Puedes copiar y pegar el dato. Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección".
15621	15513	radioTipoRelacion	Personas todas/Datos biográficos/Agregar dato biográfico / Dato biográfico Tipo de dato biográfico	Marca una de las casillas según el tipo de dato biográfico que quieras ingresar:  "Relacionado con otra persona" o  "Sin relación con otra persona". Después completa los datos correspondientes
15628	15001	delDatoBio	Personas todas/Datos biográficos/Borrar dato biográfico	Haz clic aquí para borrar del sistema el dato biográfico que se encuentra seleccionado. Para seleccionarlo haz clic sobre él.
15633	15001	staticText89	Personas todas/Datos biográficos/Exportar	Despalomea "Exportar dato biográfico" si quieres que el dato biográfico activo  no se exporte. Haz clic en la casilla para palomear o despalomear esta opción.
15640	15001	longPerDBObs	Personas todas/Datos biográficos/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15403	15001	buttonRemoveUltStatusPerp	Actos/Perpetradores/Último estatus del perpetrador / (x) signo de multiplicación	Haz clic aquí para borrar el último estatus de este perpetrador
15525	15519	radioBoxIndividual	Personas todas/Datos generales/Nueva persona / Datos de una persona - Tipo	Selecciona el tipo de persona que corresponda a la nueva persona que estas ingresando, ya sea una persona individual o colectiva.
15646	15000	DlgAltaActo	Alta de Acto	
15647	15646	ActoVictima,staticText1	Acto Victima	Haz clic en el signo de más (+) al lado de "Víctima" para seleccionar el nombre de la víctima de la lista de personas que ya están registradas en el sistema, o para ingresar una nueva persona oprimiendo el botón "Nueva persona". Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones de la izquierda.  También puedes buscar escribiendo unas pocas letras del nombre de la persona que buscas. Cuando la persona que quieras ingresar aparezca marcada, oprime "Seleccionar". En esta ventana puedes cancelar el ingreso haciendo clic en "Cancelar". La persona que seleccionaste aparecerá en la ventana de ingreso, en donde también puedes cancelar el registro oprimiendo el botón "Cancelar"
15389	15253	personaIsearch, listBoxPersona	Actos/Perpetradores/Agregar un perpetrador / Seleccionar una persona	Selecciona el nombre del perpetrador de la lista de personas que ya están registradas en el sistema, o ingresa una nueva persona oprimiendo el botón "Nueva persona". Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones de la izquierda. También puedes buscar escribiendo unas pocas letras del nombre de la persona que buscas. Cuando la persona que quieras ingresar aparezca marcada, oprime "Seleccionar". Puedes cancelar el ingreso haciendo clic en "Cancelar". La persona que seleccionaste aparecerá en el campo "Nombre del perpetrador"
15343	15251	treeCtrl1	Actos/Información general/Agregar acto / Nuevo acto - Víctima	Haz clic en el signo de más (+) al lado de "Víctima" para seleccionar el nombre de la víctima de la lista de personas que ya están registradas en el sistema, o para ingresar una nueva persona oprimiendo el botón "Nueva persona". Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones de la izquierda. También puedes buscar escribiendo unas pocas letras del nombre de la persona que buscas. Cuando la persona que quieras ingresar aparezca marcada, oprime "Seleccionar". En esta ventana puedes cancelar el ingreso haciendo clic en "Cancelar". La persona que seleccionaste aparecerá en la ventana de ingreso, en donde también puedes cancelar el registro oprimiendo el botón "Cancelar"
15544	15515	CPfechanac	Personas individual/Datos generales/Fecha de nacimiento	Fecha de nacimiento de esta persona. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15558	15515	CPCiudadania	Personas individual/Datos generales/Ciudadanía	País del cual es ciudadano esta persona. México aparece por omisión pero se puede cambiar haciendo clic en el botón con el signo de más (+) ubicado al lado del campo. Únicamente se puede ingresar un país de ciudadanía para cada persona
15560	15515	btnFPCiudadania	Personas individual/Datos generales/Ciudadanía / (+) signo de más	Si quieres cambiar "México" por otro país,  haz clic aquí y selecciona un país diferente de la lista que aparece. Utiliza el cursor para moverte hacia abajo o hacia arriba, y haz clic en los signos de más (+) para abrir las listas. Cuando encuentres el país que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". El país seleccionado aparecerá en el campo. Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un país de ciudadanía para cada persona
37	127	039	Chuj	Originarios de los Altos Cuchumatanes, Huehuetenango, Guatemala
39	127	045	Cucapá	Se autonombran es-pei, viven en Mexicali y Ensenada, Baja California, y en Sonora; mientras que sus parientes cocopah viven sobre todo en Somerton, Arizona. Usado por: Es'pei, Es'pel
15564	15515	CPEscolaridad	Personas individual/Datos generales/Escolaridad	Indicación del nivel más alto de escolaridad que tiene esta persona. Únicamente se puede ingresar un término para cada persona. Haz clic en la flechita para que aparezcan todos los niveles de escolaridad. Cuando encuentres el nivel que buscas, márcalo y el término aparecerá en el campo. Para borrar un dato registrado, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un nivel diferente.
15638	15001	staticText70	Personas todas/Datos biográficos/Fecha de vigencia	Fecha en que el dato registrado es o fue vigente. Esta opción se utiliza cuando no se conocen las fechas exactas de inicio o final de un dato biográfico pero sí se sabe que es o fue vigente en una fecha específica. Es importante tratar de completar las fechas inicial y final del dato biográfico. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15643	15001	staticText93	Personas todas/Datos biográficos/Puesto o cargo	Nombre o descripción del puesto o cargo que ocupa esta persona, por ejemplo "Comandante de zona", "Trabajador en la planta de Puebla"
15645	15001	btnSaveVinculo	Personas todas/Datos biográficos/Guardar	Haz clic aquí para guardar la información cuando hayas modificado datos. Recuerda que al cambiar de pestaña también se guarda la información. Si estás ingresando un texto largo, guarda regularmente para evitar pérdidas de datos en caso de fallas de electricidad o de equipo
15537	15515	CPNombre	Personas individual/Datos generales/Nombre(s)	Nombre de pila de la persona que estás registrando. Siempre que puedas, trata de ingresar todos los nombres completos
15539	15515	CPApellido	Personas individual/Datos generales/Apellido(s)	Apellidos de la persona que estás registrando. Siempre que puedas, trata de ingresar los dos apellidos completos
15541	15515	staticText110	Personas individual/Datos generales/Otro nombre	Otro nombre utilizado por la persona que estás registrando. Puedes ingresar un apodo o un alias
15344	15252	treeCtrl1	Actos/Información general/Agregar acto / Nuevo acto - Tipo de acto	Haz clic en el signo de más (+) al lado de "Tipo de acto o vdh" y, en la ventana que aparece, selecciona el acto o la violación que corresponda. Utiliza el cursor para moverte hacia abajo o hacia arriba, y haz clic en el signo de más (+) para abrir la lista de VDHs. Cuando encuentres el acto que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". El acto seleccionado aparecerá en la ventana de registro. Oprime el botón "Asignar" para terminar la operación. Si deseas cancelar la operación, haz clic en "Cancelar". Recuerda que únicamente podrás seleccionar actos relacionados con los derechos que hayas ingresado en la "Tipificación" del caso
15302	15247	staticText4,Localidad1	Casos/Datos generales/Nueva localización / Localización - Localidad	Escribe el nombre de la comunidad o localidad en donde ocurrieron los hechos. El nombre no debe ser más largo de unas 20 palabras.  Puedes escribir una breve nota de más o menos 20 palabras al lado de la localidad. Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar". Para borrar la localidad, selecciona todo el nombre y oprime el botón de "suprimir" en tu teclado 
15648	15646	ActoVdh,staticText2	Acto Vdh	Haz clic en el signo de más (+) al lado de "Tipo de acto o VDH" y, en la ventana que aparece, selecciona el acto o la violación que corresponda. Utiliza el cursor para moverte hacia abajo o hacia arriba, y haz clic en el signo de más (+) para abrir la lista de VDHs. Cuando encuentres el acto que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". El acto seleccionado aparecerá en la ventana de registro. Oprime el botón "Asignar" para terminar la operación. Si deseas cancelar la operación, haz clic en "Cancelar". Recuerda que únicamente podrás seleccionar actos relacionados con los derechos que hayas ingresado en la "Tipificación" del caso
15297	15001	staticText2,listLocalizacion	Casos/Datos generales/Localización	Lista de los lugares donde ocurrieron los hechos que se incluyen en este caso: país, estado, municipio y localidad. Si los hechos ocurrieron en diferentes lugares, deben aparecer todos aquí, por ejemplo: si la detención ocurre en Puebla pero presentan al detenido en el D.F. y luego lo encarcelan en Jalisco, deben aparecer los tres lugares. Para moverte dentro de la lista hacia abajo o hacia arriba, o hacia la derecha o la izquierda, utiliza el cursor o las barras de desplazamiento. Cuando hay notas aclaratorias, verás un asterisco (*) al lado del país. Haz clic en la fila de ese dato y aparecerá el botón "Más información". Haz clic ahí y podrás leer las notas aclaratorias 
11489	11488	003	Akateko	Pertenece a la Familia maya
11513	11488	009	Awakateko	Usado por: Aguacateco y Aguateco (sic). Pertenece a la Familia maya
11515	11488	015	Chatino	Usado por: Cha´cña; Chatina; Lenguas chatinas;  Zenzontepec, Oaxaca. Pertenece a la Familia oto-mangue
11516	11488	018	Chichimeco jonaz	Usado por: Chichimeca; Chichimeca jonaz; Chichimeca, Guanajuato. Pertenece a la Familia oto-mangue
11517	11488	021	Chinanteco	Usado por: Chinanteca; ChinaNteca de la Sierra de Juárez; Chinanteco de Lalana; Chinanteco de Latani; Chinanteco de Ojitlán; Chinanteca Ojitlán; Chinanteco de Petlapa; Chinanteco de Usila; Chinanteca Usila; Chinanteca de Yolox; Chinanteca de Sochiapan; Chinanteco de Valle Nacional; Lenguas chinantecas; Tsa jujmí. Pertenece a la Familia oto-mangue
11520	11488	030	Chontal de Oaxaca	Usado por: Chontal. Lenguas chontales de Oaxaca; Slijuala xanuk. Pertenece a la Familia chontal de Oaxaca
11522	11488	036	Chuj	Pertenece a la Familia maya
11523	11488	039	Cora	Usado por: Cora, Nayarit; Lenguas coras; Naayeri. Pertenece a la Familia yuto-nahua
11525	11488	045	Cuicateco	Usado por: Lenguas cuicatecas; Nduudu yu. Pertenece a la Familia oto-mangue
11527	11488	051	Huasteco	Usado por: Huasteca; Huasteca de Veracruz; Huasteca de San Luis Potosí; Lenguas huaStecas; Teenek; Tének. Pertenece a la Familia maya
11529	11488	057	Huichol	Usado por: Huichol, Durango; Wirrárika. Pertenece a la Familia yuto-nahua
15572	15515	btnDelOcupacion	Personas individual/Detalles/Ocupación / (x) signo de multiplicación	Haz clic aquí para borrar la ocupación
15589	15515	CPReligion	Personas individual/Detalles/Religión	Religión que profesa la persona. Únicamente se puede ingresar una religión para cada persona. Haz clic en la flechita para que aparezcan todas las religiones. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres la religión que buscas, haz clic para seleccionarla, y la religión aparecerá en el campo. Para borrar la religión, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Religión católica". Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona una religión diferente
15591	15515	CPEstadocivil	Personas individual/Detalles/Estado civil	El estado civil o situación marital actual de la persona. Únicamente se puede ingresar un estado civil para cada persona. Haz clic en la flechita para que aparezcan todos los estados civiles. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado civil que buscas, haz clic para seleccionarlo, y el término aparecerá en el campo. Para borrar el estado civil, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Soltero". Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15556	15515	CPLocalidad	Personas individual/Datos generales/Localidad de nacimiento	Escribe el nombre de la comunidad o localidad en donde nació esta persona. El nombre no debe ser más largo de unas 20 palabras. Para borrar la localidad, selecciona todo el nombre y oprime el botón de "suprimir" en tu teclado
11531	11488	063	Ixil	Pertenece a la Familia maya
11532	11488	066	Jakalteko	Usado por: Abxubal; Jacalteca; Jacalteco. Pertenece a la Familia maya
11534	11488	072	Kaqchikel	Usado por: Cachiquero; Cakchiquel. Pertenece a la Familia maya
11536	11488	078	Kiliwa	Usado por: k´olew. Pertenece a la Familia cochimí-yumana
11538	11488	084	Kumiai	Usado por: Kamia o ti´pai. Pertenece a la Familia cochimí-yumana
11540	11488	090	Mam	Usado por: Mame; Qyool. Pertenece a la Familia maya
11541	11488	093	Matlatzinca	Usado por: Botuná o matlame. Pertenece a la Familia oto-mangue
11543	11488	099	Mayo	Usado por: Yoreme. Pertenece a la Familia yuto-nahua
11545	11488	105	Mazateco	Usado por: Ha shuta enima. Pertenece a la Familia oto-mangue
11546	11488	108	Me´phaa	Usado por: Tlapaneco y todas sus variaciones: del suroeste, del este, del sur, central bajo, del noroeste alto, del norte y del noroeste bajo, que corresponden a siete variantes dialectales. Pertenece a la Familia oto-mangue
11548	11488	114	Mixteco	Usado por: Mixteco; Mixteco de costa; Mixteco de la Mixteca alta; Mixteco de la Mixteca baja; Mixteco de la zona mazateca; Mixteco de Puebla; Ñuu Savi; y Tacuate. Pertenece a la Familia oto-mangue 
11550	11488	120	Oluteco	Usado por: Núntahá´yi o tuncapxe; Popoluca; Popoluca de Oluta y Popoluca de Texistepec. Ver también en la lista: Popoluca de la Sierra, Sayulteco y Texistepequeño. Pertenece a la Familia mixe-zoque
11552	11488	129	Paipai	Usado por: Akwa´ala; Pai pai. Pertenece a la Familia cochimí-yumana
11554	11488	135	Pápago	Usado por: Tono ooh´tam. Pertenece a la Familia yuto-nahua
11555	11488	138	Pima	Usado por: Otam u o'ob. Pertenece a la Familia yuto-nahua
11557	11488	144	Popoluca de la Sierra	Usado por: Popoluca. Ver también: Oluteco, Sayulteco y Texistepequeño. Pertenece a la IX Familia mixe-zoque
11559	11488	150	Q’eqchi'	Usado por: k´ekchí o queckchí o o quetzchí. Pertenece a la Familia maya
11560	11488	153	Qato’k	Usado por: Mocho, Mochó, Motozintleco y Motocintleco; Qatok. Pertenece a la Familia maya
11561	11488	156	Sayulteco	Usado por: Popoluca de Oluta. Ver también: Oluteco, Popoluca de la Sierra y Texistepequeño. Pertenece a la Familia mixe-zoque
11565	11488	168	Teko	Usado por: Teco. Se habla en el sureste de Chiapas, en los alrededores de Motozintla y Mazapa de Madero y en Textitlán y Cuilco, en Guatemala. Pertenece a la Familia maya
11566	11488	171	Tepehua	Usado por: Hamasipini. Pertenece a la Familia totonaco-tepehua
11568	11488	177	Tepehuano del sur	Ver también: Tepehuano del norte. Pertenece a la Familia yuto-nahua
11569	11488	180	Texistepequeño	Usado por: Popoluca; Popoluca de Texistepec. Ver también: Oluteco, Popoluca de la Sierra y Sayulteco. Pertenece a la Familia mixe-zoque
11572	11488	189	Totonaco	Usado por: Tachihuiin; Totonaca. Pertenece a la Familia totonaco-tepehua
11573	11488	192	Triqui	Usado por: Driki; Trique; Trique de Copala; Trique de Chicahuaxtla. Pertenece a la Familia oto-mangue
11575	11488	198	Tsotsil	Usado por: Tzotzil; Batzil K´op. Pertenece a la Familia maya
11577	11488	204	Zapoteco	Usado por: Ben´zaa o binnizá o bene xon; Zapoteco, Zapoteco de Cuixtla, Zapoteco de Ixtlán, Zapoteco del Istmo, Zapoteco del rincón, Zapoteco sureño, Zapoteco vallista y Zapoteco vijano. Pertenece a la Familia oto-mangue
11488	1	T66	Lengua indígena	La fuente principal para esta lista es el “Catálogo de las Lenguas Indígenas Nacionales: Variantes Lingüísticas de México con sus autodenominaciones y referencias geoestadísticas.” En: DOF, 14 enero 2008. <http://www.inali.gob.mx/pdf/CLIN_completo.pdf> (Sitio consultado 12 febrero 2008)
15650	15000	frameRep5	Reportes	
15665	15650	casoOpciones,button1	Casos/Datos generales/Reportes/Opciones 	Haz clic aquí para abrir la ventana de Opciones y generar un modelo de reporte. Podrás seleccionar los campos que desees eliminar de tu reporte. 
15658	15650	btnCasosSeleccionados	Casos/Datos generales/Reportes/Botón de impresora  / Reporte narrativo de casos visibles (boton)	Haz clic aquí para generar el Reporte narrativo de casos visibles.  
15659	15650	bitmapButton4	Casos/Datos generales/Reportes/Botón de impresora  / Reporte narrativo de caso activo (boton)	Haz clic aquí para generar el Reporte narrativo de caso activo. 
15660	15650	bitmapButton6	Casos/Datos generales/Reportes/Botón de impresora  / Reporte resumido de caso activo  (boton)	Haz clic aquí para generar el Reporte resumido de caso activo. 
15661	15650	btnRepCasos	Casos/Datos generales/Reportes/Botón de impresora  / Listado de casos  (boton)	Haz clic aquí para generar el Listado de casos. 
15663	15650	bitmapButton1	Casos/Datos generales/Reportes/Botón de impresora  / Derechos afectados/Estado/Caso (boton)	Haz clic aquí para generar el reporte de Derechos afectados/Estado/Caso
15664	15650	btnRepIntervenciones	Casos/Datos generales/Reportes/Botón de impresora  / Reporte de intervenciones  (boton)	Haz clic aquí para generar el Reporte de intervenciones. 
15620	15001	buttonVincular	Personas todas/Datos biográficos/Agregar dato biográfico	Haz clic aquí para agregar un nuevo dato biográfico. En la ventana que aparece, palomea la casilla correspondiente según el tipo de dato biográfico que quieras ingresar:  "Relacionado con otra persona" o  "Sin relación con otra persona". Después completa los datos necesarios en los campos que se activen y haz clic en el botón "Seleccionar" para que se grabe el registro.
15662	15650	bitmapButton5	Casos/Datos generales/Reportes/Botón de impresora  / Reporte narrativo de persona activa  (boton)	Haz clic aquí para generar el Reporte narrativo de persona activa. 
128	127	003	Afrodescendiente	Población ubicada principalmente en la Costa Chica de Guerrero, aunque también en otras zonas de Guerrero, Oaxaca y Veracruz y, en menor proporción, en Chiapas, Yucatán, Tabasco, Puebla, Colima, Michoacán, Sinaloa, Guanajuato, Querétaro y el Distrito Federal
47	127	066	Ixil	Originarios de los Altos Cuchumatanes, Huehuetenango, Guatemala
52	127	069	Jakalteko	Originarios de los Altos Cuchumatanes, Huehuetenango, Guatemala. Usado por: Jacalteco, Abxubal
55	127	072	K’iche’	Originarios de Totonicapán, Chimaltenango, Sololá y Sacatepéquez, y sectores de El Quiché, Quetzaltenango, Suchitépequez y Baja Verapaz en Guatemala. Usado por: Quiché
59	127	075	Kaqchikel	Originarios de Totonicapán, Chimaltenango, Sololá y Sacatepéquez, y sectores de El Quiché, Quetzaltenango, Suchitépequez y Baja Verapaz en Guatemala. Usado por: Cakchiquel
66	127	096	Matlatzinca	Estado de México. Usado por: Botuna, matlatzinka
68	127	102	Mayo	Sonora y Sinaloa. Usado por: Yoreme
69	127	105	Mazahua	Habitan en parte noroeste del Estado de México y en una pequeña área del oriente del estado de Michoacán. Usado por: Jnatio, mazahuas
11450	127	111	Me´phaa	Pueblo que habita entre la vertiente de la Sierra Madre del Sur y la costa del estado de Guerrero. Usado por: Tlapaneco
11455	127	129	Oluteco	Usado por: Popoluca, Popolucas, homshuk. Ver también: Popoluca de la Sierra,  Sayulteco y Texistepequeño
11456	127	132	Otomí	Incluye: Otomíes del Estado de México, Otomíes del Valle del Mezquital. Usado por: Hñahñu, hñä hñü
11459	127	141	Pápago	Sonora y Arizona. Tres divisiones principales: los hia'ched o'otham (areneños o gente de la arena); los akimel o'otham (gente del río), también conocidos como pimas gileños; y los tohono o'otham (gente del desierto). Usado por: Tohonoo'tham
11463	127	153	Q’anjob’al	Originarios de los Altos Cuchumatanes, Huehuetenango, Guatemala. Usado por: Kanjobal
11465	127	159	Qato’k	Usado por: Mocho, Mochó, Motozintleco y Motocintleco
11466	127	162	Sayulteco	Usado por: Popoluca y Popoluca de Oluta. Ver también: Oluteco, Popoluca de la Sierra y Texistepequeño
11472	127	180	Tepehuano del norte	Usado por: Odami
15654	15650	staticText12	Casos/Datos generales/Reportes/Emisión de reportes / Listado de casos 	Este es un listado de todos los casos capturados en el sistema que contiene la siguiente información: Nombre del caso, Fecha inicial y Resumen de los hechos. Para generar el listado, haz clic en el ícono que aparece a un lado.
15655	15650	staticText9	Casos/Datos generales/Reportes/Emisión de reportes / Reporte narrativo de persona activa 	Este es un reporte de control que contiene toda la información capturada  de la persona seleccionada ("persona activa") en la pantalla de Personas/Datos Generales.También incluye la información administrativa del caso. Para generar el reporte, haz clic en el ícono que aparece a un lado. Puedes también hacer clic en el botón de opciones para seleccionar los campos que quieres que aparezcan o se omitan en tu reporte.
15657	15650	staticText11	Casos/Datos generales/Reportes/Emisión de reportes / Reporte de intervenciones 	Este es un reporte que contiene una tabla con la lista de Intervenciones realizadas en los casos capturados en el sistema. Contiene además la siguiente información: Fecha, Quien realiza o inicia esta intervención, A quien se le dirigió esta intervención, Respuesta y Nombre del Caso. Para generar el reporte, haz clic en el ícono que aparece a un lado.
15666	15650	personaOpciones	Casos/Datos generales/Reportes/Opciones 	Haz clic aquí para abrir la ventana de Opciones y generar un modelo de reporte. Podrás seleccionar los campos que desees eliminar de tu reporte. 
15667	15650	staticText7	Casos/Datos generales/Reportes/Abrir con 	Puedes generar un reporte en diferentes aplicaciones (Word, Excel, etc.). Haz clic en la flechita y elige de la lista el programa con el cual deseas generar tu reporte. Luego de que generes tu reporte, podrás cambiarle el nombre y guardarlo en la carpeta que desees. 
15668	15650	fileBrowse	Casos/Datos generales/Reportes/Buscar	Haz clic aquí para buscar un archivo de reporte generado y guardado anteriormente. 
15669	15650	openRep	Casos/Datos generales/Reportes/Abrir reporte	Haz clic aquí para abrir el archivo que has seleccionado. 
15670	15650	staticText8	Casos/Datos generales/Reportes/Modelo de impresión 	Estos son los modelos de impresión que han sido guardados anteriormente. Si quieres abrir un reporte que contenga las opciones de algún modelo, haz clic en la flechita para ver la lista y selecciona el que deseas. Después abre tu reporte.
15672	15650	delModelo	Casos/Datos generales/Reportes/Borrar modelo 	Haz clic aquí para borrar un modelo de impresión seleccionado
15673	15650	btnLimpiarOpciones	Casos/Datos generales/Reportes/Limpiar opciones	Haz clic aquí para "limpiar" las opciones seleccionadas para la generación de un reporte. Todos los campos de "Opciones" volverán a estar palomeados.
15653	15650	staticText13	Casos/Datos generales/Reportes/Emisión de reportes / Reporte resumido de caso activo 	Este es un resumen del caso seleccionado en la pantalla de Casos/Datos Generales ("Caso activo") que contiene la siguiente información: Datos generales del caso, Resumen de los hechos, Actos, Víctimas, Perpetradores y las Intervenciones realizadas en el caso. Para generar el reporte, haz clic en el ícono que aparece a un lado.
11474	127	186	Texistepequeño	Usado por: Popoluca, Popoluca de Texistepec. Ver también: Oluteco, Popoluca de la Sierra y Sayulteco
11477	127	195	Totonaco	Usado por: Totonaca, Tachihuiin, totonaco (tu'tu nacu')
11480	127	204	Tsotsil	Incorrectamente, a veces se les llama “Chamulas” por ser los tsotsiles de Chamula los más conocidos (CDHFBC). Usado por: Tzotzil, Batsil winik'otik, batzilk'op
9316	8029	003001	Comondú	
15674	11729	000005	Jurisprudencia	
15675	11490	011	Organismo intergubernamental	
15714	15000	getTaxAltaInterTipoInt	alta intervencion: tipo de int	
15681	15000	getTaxonomyTreeTipoActo	tipo de acto	
15682	15000	getTaxonomyTreeTipodeLugar	tipo de lugar	
15683	15000	getTaxonomyTreeEstatusVDH	estatus vdh	
15684	15000	getTaxonomyTreeEstatusVictima	EstatusVictima	
15685	15000	DialogTipificaLegisNac	LegisNac	
15686	15000	DialogTipificaInstInt	Instrumentos Int 	
15687	15000	getTaxonomyTreeGradoInvol	Grado Invol 	
15688	15000	getTaxonomyTreeTipoPerp	Tipo Perpetrador	
15690	15000	getTaxUltimoStatusPerp	UltimoStatusPerp	
15691	15000	PersonaDlgAltaInter	PersonaDlg AltaInterv	
15692	15000	getTaxTipoIntervencion	Tipo de Intervencion 	
15693	15000	dlgpersonaParteInt	Parte Interv	
15694	15000	dlgpersonaDeQuien	persona sobre quien se interviene	
15695	15000	dlgpersonaAQuien	persona A Quien se dirige una interv	
15697	15000	dlgpersFtePersonaRelacionada	dlgpersFtePersonaRelacionada	
11482	127	210	Zapoteco	Incluye: Zapotecos del Istmo de Tehuantepec, Sierra Norte de Oaxaca, Valles Centrales, Oaxaca  
15698	15000	getTaxConexionInformacion	Conexion nformacion	
15699	15000	getTaxFteConfiabilidad	Fuente Confiabilidad	
15700	15000	getTaxFteLengua	Fuente Lengua	
15701	15000	MyDescripDoc	Descripcion de Fte Doc	
15702	15000	getTaxTipodeFuente	TipodeFuente pers	
15703	15000	PersonaDlgPubPersona	Persona ref en doc	
15704	15000	getTaxPubConfiabilidad	fte documental - Confiabilidad 	
15705	15000	DialogTipificaPersonaIdioma	Persona: Idioma 	
15706	15000	DialogTipificaPersonaLIndigena	Persona: L. Indigena	
15707	15000	DialogTipificaPersonaOEtnico	Persona: OEtnico 	
15708	15000	frameBusqueda	Busqueda ex	
15709	15000	condicion	condicion 	
15710	15000	MyDescripBusqueda	Busqueda de cadenas alfanumericas	
15711	15000	dlgUserBusqueda	Busqueda de usuarios	
15712	15000	condicionFecha	busqueda de Fechas	
15713	15000	printconfig	opciones de configuracion	
15678	15000	PersonaDlgVictima	seleccion de persona como victima	
15715	15000	getTaxTipoPersonaCol	alta persona: Tipo persona colectiva	
15716	15000	getTaxonomyTreeOcupacion	Tipo de ocupacion	
15717	15000	getTaxonomyTreeBusqueda	busqueda de taxonomias	
15718	15000	getTaxCaracRelevante	Caracteristica relevante	
15286	15001	CasoIsearch	Casos/Datos generales/Búsqueda rápida	Escribe unas cuantas letras del nombre del caso que estás buscando, por ejemplo: "huelga" para ver todos los casos que tengan la palabra "huelga" como parte de su nombre. Arriba de la ventana aparece en negritas el número de casos que coinciden con tu búsqueda, por ejemplo: 4 casos seleccionados. De los casos que aparecen en la ventana, selecciona con doble clic el que quieras trabajar. Si el nombre es muy largo y no puedes leerlo completo, utiliza el ratón para desplazar hacia la derecha o la izquierda la barra que está  abajo de la ventana
15719	15001	staticText105	Casos/Datos generales/Búsqueda rápida	Escribe unas cuantas letras del nombre del caso que estás buscando, por ejemplo: "huelga" para ver todos los casos que tengan la palabra "huelga" como parte de su nombre. Arriba de la ventana aparece en negritas el número de casos que coinciden con tu búsqueda, por ejemplo: 4 casos seleccionados. De los casos que aparecen en la ventana, selecciona con doble clic el que quieras trabajar. Si el nombre es muy largo y no puedes leerlo completo, utiliza el ratón para desplazar hacia la derecha o la izquierda la barra que está  abajo de la ventana
15290	15001	listaCasos	Casos/Datos generales/Lista de casos	Lista en orden alfabético de todos los casos registrados en el sistema. Para moverte dentro de la lista, utiliza el cursor o las barras de desplazamiento. Cuando encuentres el caso que buscas, haz doble clic para seleccionarlo. Una vez seleccionado, puedes modificar o agregar datos. Para ingresar un nuevo caso, utiliza el botón "Nuevo caso". Si realizas una búsqueda rápida o exhaustiva, esta lista te mostrará únicamente los casos que coincidan con los criterios de tu búsqueda
15720	15001	textDescripcion	Casos/Datos generales/Nombre del caso	Nombre que identifica claramente el caso. El nombre debe ser único para cada caso. Puedes ingresar un nombre de más o menos 35 palabras
15721	15001	staticText3	Casos/Datos generales/Nombre del caso	Nombre que identifica claramente el caso. El nombre debe ser único para cada caso. Puedes ingresar un nombre de más o menos 35 palabras
15722	15001	choiceTipoFechaInicial	Casos/Datos generales/Fecha inicial	Indicación de cuándo comenzaron los hechos que se incluyen en este caso. Generalmente es la fecha del primer incidente o acto, o la primera fecha significativa. Por ejemplo: la fecha inicial de un caso de tortura puede ser uno o varios días antes cuando la víctima fue detenida. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15676	15001	MP1	test	Palomea una de las casillas que aparecen en el recuadro para acotar el despliegue de personas registradas en el sistema. Pueden aparecer únicamente las "PERSONAS INDIVIDUALES", las "ENTIDADES COLECTIVAS" o las "PERSONAS DIRECTAMENTE RELACIONADAS CON EL CASO" activo. Puedes palomear "TODAS" si quieres que aparezca la lista completa de registros.
15283	15001	LC1	Casos/Datos generales/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, búscalo en la ventana de abajo y selecciónalo con doble clic
15725	15001	listLocalizacion	Casos/Datos generales/Localización	Lista de los lugares donde ocurrieron los hechos que se incluyen en este caso: país, estado, municipio y localidad. Si los hechos ocurrieron en diferentes lugares, deben aparecer todos aquí, por ejemplo: si la detención ocurre en Puebla pero presentan al detenido en el D.F. y luego lo encarcelan en Jalisco, deben aparecer los tres lugares. Para moverte dentro de la lista hacia abajo o hacia arriba, o hacia la derecha o la izquierda, utiliza el cursor o las barras de desplazamiento. Cuando hay notas aclaratorias, verás un asterisco (*) al lado del país. Haz clic en la fila de ese dato y aparecerá el botón "Más información". Haz clic ahí y podrás leer las notas aclaratorias
15726	15247	staticText1	Casos/Datos generales/Nueva localización / Localización - País	México aparece por omisión pero se puede cambiar haciendo clic en el signo de más (+) al lado de "País". Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar"
15728	15247	Pais	Casos/Datos generales/Nueva localización / Localización - País	México aparece por omisión pero se puede cambiar haciendo clic en el signo de más (+) al lado de "País". Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar"
15729	15247	staticText2	Casos/Datos generales/Nueva localización / Localización - Estado	Haz clic en la flechita para que aparezcan todos los estados de la república. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar". Para borrar el estado, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Aguascalientes"
15797	15001	textCtrlPubLigaSitio	Fuentes/Fuente documental/Liga a la fuente	Liga precisa al documento que se está registrando, por ejemplo: http://www.jornada.unam.mx/ultimas/2009/01/11/hallan-ejecutado-en-sonora-a-policia-municipal-de-guasave-sinaloa
15730	15247	Estado	Casos/Datos generales/Nueva localización / Localización - Estado	Haz clic en la flechita para que aparezcan todos los estados de la república. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar". Para borrar el estado, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Aguascalientes"
15731	15247	staticText3	Casos/Datos generales/Nueva localización / Localización - Municipio	En "(seleccionar)" aparecen todos los municipios del estado seleccionado arriba. Puedes escribir unas letras del nombre del municipio que te interesa en el campo que dice "(buscar)". Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Para borrar el municipio seleccionado, ingresa al campo que contiene la lista de municipios y haz clic sobre la línea en blanco que aparece al inicio. Después de hacer la selección, puedes escribir una breve nota de más o menos 20 palabras en el campo "Notas".
15732	15247	MuniSearch	Casos/Datos generales/Nueva localización / Localización - Municipio	En "(seleccionar)" aparecen todos los municipios del estado seleccionado arriba. Puedes escribir unas letras del nombre del municipio que te interesa en el campo que dice "(buscar)". Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Para borrar el municipio seleccionado, ingresa al campo que contiene la lista de municipios y haz clic sobre la línea en blanco que aparece al inicio. Después de hacer la selección, puedes escribir una breve nota de más o menos 20 palabras en el campo "Notas".
15733	15247	textMunicipio	Casos/Datos generales/Nueva localización / Localización - Municipio	En "(seleccionar)" aparecen todos los municipios del estado seleccionado arriba. Puedes escribir unas letras del nombre del municipio que te interesa en el campo que dice "(buscar)". Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Para borrar el municipio seleccionado, ingresa al campo que contiene la lista de municipios y haz clic sobre la línea en blanco que aparece al inicio. Después de hacer la selección, puedes escribir una breve nota de más o menos 20 palabras en el campo "Notas".
15734	15247	(buscar)	Casos/Datos generales/Nueva localización / Localización - Municipio	En "(seleccionar)" aparecen todos los municipios del estado seleccionado arriba. Puedes escribir unas letras del nombre del municipio que te interesa en el campo que dice "(buscar)". Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Para borrar el municipio seleccionado, ingresa al campo que contiene la lista de municipios y haz clic sobre la línea en blanco que aparece al inicio. Después de hacer la selección, puedes escribir una breve nota de más o menos 20 palabras en el campo "Notas".
15735	15247	staticText7	Casos/Datos generales/Nueva localización / Localización - Municipio	En "(seleccionar)" aparecen todos los municipios del estado seleccionado arriba. Puedes escribir unas letras del nombre del municipio que te interesa en el campo que dice "(buscar)". Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Para borrar el municipio seleccionado, ingresa al campo que contiene la lista de municipios y haz clic sobre la línea en blanco que aparece al inicio. Después de hacer la selección, puedes escribir una breve nota de más o menos 20 palabras en el campo "Notas".
15727	15247	btnPais	Casos/Datos generales/Nueva localización / Localización - País	México aparece por omisión pero se puede cambiar haciendo clic en el signo de más (+) al lado de "País". Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar"
15738	15247	Localidad1	Casos/Datos generales/Nueva localización / Localización - Localidad	Escribe el nombre de la comunidad o localidad en donde ocurrieron los hechos. El nombre no debe ser más largo de unas 20 palabras.  Puedes escribir una breve nota de más o menos 20 palabras al lado de la localidad. Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar". Para borrar la localidad, selecciona todo el nombre y oprime el botón de "suprimir" en tu teclado
15741	15001	FCproyecto_conjunto	Casos/Información administrativa/Proyecto conjunto RedTDT	Nombre de la campaña o  proyecto en el que está trabajando la RedTDT en su conjunto, y para el cual este caso es relevante, por ejemplo: "Criminalización de la protesta social". Este nombre se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos, separándolos con comas, punto, o punto y coma; siempre y cuando estén acordados en el marco del trabajo conjunto de la RedTDT.
15742	15001	staticText78	Casos/Información administrativa/Comentarios	Anotaciones internas del trabajo institucional sobre el caso, por ejemplo: identificación de información que falta, que no está clara o que es contradictoria; pistas para la investigación; ubicación de probables testigos; opiniones o información no corroborada sobre los motivos o causas de los hechos; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15743	15001	textCtrlCAComentarios	Casos/Información administrativa/Comentarios	Anotaciones internas del trabajo institucional sobre el caso, por ejemplo: identificación de información que falta, que no está clara o que es contradictoria; pistas para la investigación; ubicación de probables testigos; opiniones o información no corroborada sobre los motivos o causas de los hechos; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15744	15001	staticText79	Casos/Información administrativa/Estatus del caso	Indicación de si la organización está trabajando activamente sobre este caso y la prioridad que tiene. Por ejemplo, si el caso ya está resuelto, puedes seleccionar "Expediente cerrado", pero si el caso está sucediendo y es grave, puedes seleccionar "Caso urgente"
15745	15001	choiceMonitoreo	Casos/Información administrativa/Estatus del caso	Indicación de si la organización está trabajando activamente sobre este caso y la prioridad que tiene. Por ejemplo, si el caso ya está resuelto, puedes seleccionar "Expediente cerrado", pero si el caso está sucediendo y es grave, puedes seleccionar "Caso urgente"
15746	15001	textCtrlDescripcionNarrativa	Casos/Información narrativa/Descripción narrativa	Descripción general de los hechos. Debe proporcionar toda la información relevante de dónde, cuándo y cómo ocurrieron los hechos, así como sobre las víctimas, los presuntos responsables, y cuál fue el papel de las autoridades en caso de que hayan intervenido. La descripción puede ser breve y concisa, o puede ser extensa y redactada para que sirva como comunicado de prensa, acción urgente, etc. No hay un "límite" de espacio aquí pero es importante que el texto describa de la manera más clara y exacta posible el caso en su conjunto. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15737	15247	staticText4	Casos/Datos generales/Nueva localización / Localización - Localidad	Escribe el nombre de la comunidad o localidad en donde ocurrieron los hechos. El nombre no debe ser más largo de unas 20 palabras.  Puedes escribir una breve nota de más o menos 20 palabras al lado de la localidad. Cuando termines de ingresar todos los datos de localización, oprime "Asignar". Puedes cancelar el registro oprimiendo el botón "Cancelar". Para borrar la localidad, selecciona todo el nombre y oprime el botón de "suprimir" en tu teclado
15739	15001	textCtrlNoPersonasAfectadas	Casos/Datos generales/No. de personas afectadas	El número exacto o estimado de las personas, familias, comunidades, etc. que han sido afectadas por lo ocurrido en el caso, y una breve indicación de cómo fueron afectadas. Ejemplos: 400 trabajadores despedidos / 1 muerto y 2 heridos / 10,000 habitantes sin agua
15740	15001	FCtipo_frecepcion	Casos/Información administrativa/Fecha de recepción	Fecha en que la organización tuvo conocimiento del caso por primera vez. Puede ser la fecha en que inicialmente se atendió la denuncia, la fecha original de la fuente de información, o la fecha cuando se consultó la fuente por primera vez. Esta fecha no necesariamente coincide con las fechas del caso. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15748	15001	LC12	Casos/Relaciones/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15749	15248	staticText1	Casos/Relaciones/Nueva relación / Buscar	Para encontrar el caso que buscas, utiliza el cursor y las barras de desplazamiento para moverte dentro de la lista. También puedes escribir en el casillero de "Buscar" unas cuantas letras del nombre del caso que estás buscando. Por ejemplo, escribe "huelga" para ver todos los casos que tengan la palabra "huelga" como parte de su nombre. De los casos que aparecen, haz clic sobre el que quieras relacionar con el caso activo y oprime el botón "Establecer relación". Si quieres, puedes cancelar el ingreso haciendo clic en "Cancelar" 
15750	15248	casoIsearch	Casos/Relaciones/Nueva relación / Buscar	Para encontrar el caso que buscas, utiliza el cursor y las barras de desplazamiento para moverte dentro de la lista. También puedes escribir en el casillero de "Buscar" unas cuantas letras del nombre del caso que estás buscando. Por ejemplo, escribe "huelga" para ver todos los casos que tengan la palabra "huelga" como parte de su nombre. De los casos que aparecen, haz clic sobre el que quieras relacionar con el caso activo y oprime el botón "Establecer relación". Si quieres, puedes cancelar el ingreso haciendo clic en "Cancelar" 
15751	15248	listBoxCasos	Casos/Relaciones/Nueva relación / Buscar	Para encontrar el caso que buscas, utiliza el cursor y las barras de desplazamiento para moverte dentro de la lista. También puedes escribir en el casillero de "Buscar" unas cuantas letras del nombre del caso que estás buscando. Por ejemplo, escribe "huelga" para ver todos los casos que tengan la palabra "huelga" como parte de su nombre. De los casos que aparecen, haz clic sobre el que quieras relacionar con el caso activo y oprime el botón "Establecer relación". Si quieres, puedes cancelar el ingreso haciendo clic en "Cancelar" 
15752	15001	staticText109	Casos/Relaciones/Relación entre casos	Esta es la relación que existe entre el caso activo y el caso relacionado. Si quieres modificar el tipo de relación, haz clic en el signo de más (+) y selecciona una diferente. Si en el recuadro de arriba "Relacionado con", hay más de un caso registrado, haz doble clic en el que quieras modificar o agregar observaciones y comentarios.
15753	15001	btnTipoRelCaso	Casos/Relaciones/Relación entre casos	Esta es la relación que existe entre el caso activo y el caso relacionado. Si quieres modificar el tipo de relación, haz clic en el signo de más (+) y selecciona una diferente. Si en el recuadro de arriba "Relacionado con", hay más de un caso registrado, haz doble clic en el que quieras modificar o agregar observaciones y comentarios.
15754	15001	staticText108	Casos/Relaciones/Observaciones	Información adicional o explicación sobre la forma en que se relacionan los casos entre sí. Por ejemplo, puedes ingresar una breve explicación de la causa y efecto entre los dos casos.   La información que registres aquí, corresponderá a la relación que está activa. Para activar una relación, haz doble clic en el caso relacionado que aparece en el recuadro de arriba.
15755	15001	longObsRelCasos	Casos/Relaciones/# espacios en Observaciones	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15756	15001	FRCCasoRelComentarios	Casos/Relaciones/Comentarios	Anotaciones internas del trabajo institucional sobre la relación entre los dos casos. Por ejemplo, características comunes o discrepancias notables entre los casos, opiniones o información no corroborada sobre la relación, etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. La información que registres aquí, corresponderá a la relación que está activa. Para activar una relación, haz doble clic en el caso relacionado que aparece en el recuadro de arriba.
15757	15001	longComRelCasos	Casos/Relaciones/# espacios en Comentarios	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15509	15001	staticText7	Casos/Tipificaciones/Derechos afectados	Lista en orden alfabético de todos los derechos que están afectados por los hechos que ocurren en este caso. Para moverte dentro de la lista, utiliza el cursor y las barras de desplazamiento. Para registrar un nuevo derecho, oprime el botón "Agregar derecho"
15503	15001	staticText36	Casos/Información narrativa/Observaciones	Registra aquí cualquier información adicional sobre el caso que no esté ingresada en otro campo, y/o información que ayude a comprender el contexto en el que suceden los hechos, antecedentes relevantes, etc. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15747	15001	textCtrlObservaciones	Casos/Información narrativa/Observaciones	Registra aquí cualquier información adicional sobre el caso que no esté ingresada en otro campo, y/o información que ayude a comprender el contexto en el que suceden los hechos, antecedentes relevantes, etc. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15760	15001	button2	Casos/Tipificaciones/Agregar tema	Haz clic aquí para agregar los temas que describan el conjunto de información de este caso. Puedes ingresar todos los temas que consideres relevantes
15761	15001	LC3	Actos/Información general/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15763	15251	ActoVictima	Actos/Información general/Agregar acto / Nuevo acto - Víctima	Haz clic en el signo de más (+) al lado de "Víctima" para seleccionar el nombre de la víctima de la lista de personas que ya están registradas en el sistema, o para ingresar una nueva persona. La persona seleccionada aparecerá en esta ventana. Después de seleccionar el acto o la VDH que afectó a la víctima, haz clic en "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar"
15346	15001	btnInfoActo	Actos/Información general/I (letra I)	Datos de la creación y actualización del registro de este acto. Se indica la persona que ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15353	15001	staticText40	Actos/Información general/Fecha inicial	Indicación de cuándo inició este acto particular. Por ejemplo: la fecha inicial de la detención de una persona, la fecha en que inicia operaciones una empresa minera que contamina un río, la fecha en que entra en vigor una ley, etc. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15766	15001	FATipofechainicio	Actos/Información general/Fecha inicial	Indicación de cuándo inició este acto particular. Por ejemplo: la fecha inicial de la detención de una persona, la fecha en que inicia operaciones una empresa minera que contamina un río, la fecha en que entra en vigor una ley, etc. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15767	15001	FATipofechafin	Actos/Información general/Fecha final	Indicación de cuándo terminó este acto particular. Por ejemplo, la fecha cuando es liberada una persona que fue detenida arbitrariamente. Si el acto no está cerrado o no ha terminado, NO ingreses ninguna fecha. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15768	15001	FACaracRelevante	Actos/Información general/Características relevantes	Son las características de la persona que fueron motivo para su victimización en este acto o VDH. Ingresa más de una característica SÓLO en el caso de que exista claramente más de una característica relevante que fuera el motivo para la victimización de la persona en el acto o VDH específico.
15372	15001	LC14	Actos/Normatividad/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevos datos, o para modificar datos ya registrados. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona con doble clic un caso diferente
15758	15001	staticText8	Casos/Tipificaciones/Temas	Lista en orden alfabético de los temas principales que describen el conjunto de la información de este caso. Para moverte dentro de la lista, utiliza el cursor o la barra de desplazamiento. Para registrar un nuevo tema, oprime el botón "Agregar tema"
15759	15001	listBoxTemas	Casos/Tipificaciones/Temas	Lista en orden alfabético de los temas principales que describen el conjunto de la información de este caso. Para moverte dentro de la lista, utiliza el cursor o la barra de desplazamiento. Para registrar un nuevo tema, oprime el botón "Agregar tema"
15762	15001	listActos	Actos/Información general/Actos registrados	Lista de los actos ya registrados en el caso activo. Están ordenados alfabéticamente por el nombre de la víctima, seguido de una diagonal (/) y el tipo de acto, también ordenado alfabéticamente. Ejemplo: "Barajas Garibo, Raúl / Agresiones físicas" y "Barajas Garibo, Raúl / Detención arbitraria o ilegal". Utiliza el cursor o la barra de desplazamiento para moverte hacia abajo o hacia arriba dentro de la lista. Cuando encuentres el acto que buscas, selecciónalo con doble clic para que quede activo y puedas modificarlo o agregar datos. Para ingresar un nuevo acto utiliza el botón "Agregar acto". 
15771	15001	staticText95	Actos/Normatividad/Legislación nacional / Lista	Lista en orden alfabético de toda la legislación nacional ingresada para el acto activo. Para registrar una nueva legislación, oprime el signo de más (+) al lado de "Legislación nacional"
15764	15252	ActoVdh	Actos/Información general/Agregar acto / Nuevo acto - Tipo de acto	Haz clic en los signos de más (+) para abrir las listas de actos o VDHs. Selecciona un término y oprime el botón "Seleccionar". Si deseas cancelar la operación haz clic en "Cancelar".
15772	15001	staticText98	Actos/Normatividad/Notas de Legislación nacional	Aquí puedes ingresar el nombre y los artículos específicos de la legislación que seleccionaste. Para moverte hacia arriba o hacia abajo dentro del texto, utiliza el cursor o la barra de desplazamiento. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH. La información que ingreses aquí, corresponderá a la legislación que esté activa. Para activar una legislación, haz doble clic sobre la misma.
15773	15001	txtLongNorLeg	Actos/Normatividad/Notas de Legislación nacional / # espacios en notas	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son 20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15774	15001	staticText97	Actos/Normatividad/Instrumentos internacionales / Lista	Lista en orden alfabético de todos los instrumentos internacionales ingresados para el acto activo. Para registrar un nuevo instrumento, oprime el signo de más (+) al lado de "Instrumentos internacionales"
15380	15001	btnActoInstrInt	Actos/Normatividad/Instrumentos internacionales / (+) signo de más	Haz clic aquí  y, en la ventana que aparece, selecciona el instrumento internacional que aplique a este acto. Haz clic en el signo de más (+) para abrir la lista de todos los instrumentos sobre un tema. Cuando encuentres el instrumento que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Puedes ingresar todos los instrumentos relevantes para este acto o VDH.
15512	15001	FAinstrumentos_int_notas	Actos/Normatividad/Notas de Instrumentos internacionales	Aquí puedes ingresar los artículos específicos del instrumento internacional que seleccionaste. Para moverte hacia arriba o hacia abajo dentro del texto, utiliza el cursor o la barra de desplazamiento. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH. La información que ingreses aquí corresponderá al instrumento internacional que esté activo. Para activar un instrumento, haz doble clic sobre el mismo.
15775	15001	staticText96	Actos/Normatividad/Notas de Instrumentos internacionales	Aquí puedes ingresar los artículos específicos del instrumento internacional que seleccionaste. Para moverte hacia arriba o hacia abajo dentro del texto, utiliza el cursor o la barra de desplazamiento. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH. La información que ingreses aquí corresponderá al instrumento internacional que esté activo. Para activar un instrumento, haz doble clic sobre el mismo.
15776	15001	txtLongNorIns	Actos/Normatividad/Instrumentos internacionales / # espacios en notas	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son 20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15777	15253	personaIsearch	Actos/Perpetradores/Agregar un perpetrador / Seleccionar una persona	Busca el nombre del perpetrador en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas, o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Selecciona el nombre de la persona que quieras ingresar y haz clic en el botón "Seleccionar".
15778	15253	listBoxPersona	Actos/Perpetradores/Agregar un perpetrador / Seleccionar una persona	Busca el nombre del perpetrador en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas, o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Selecciona el nombre de la persona que quieras ingresar y haz clic en el botón "Seleccionar".
15779	15253	radioBoxTipoPersona	Actos/Perpetradores/Agregar un perpetrador / Seleccionar una persona	Busca el nombre del perpetrador en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas, o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Selecciona el nombre de la persona que quieras ingresar y haz clic en el botón "Seleccionar".
15780	15001	staticText14	Actos/Perpetradores/Observaciones	Registra aquí cualquier información adicional sobre el grado de involucramiento del perpetrador en este acto. Ingresa aquí únicamente información que sea pertinente a este acto. Si tienes información general sobre la persona, ingrésala en el campo más apropiado de la pestaña de "Personas", o ingresa un nuevo dato biográfico. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15770	15001	FAObservaciones	Actos/Información general/Observaciones	Registra aquí cualquier información adicional sobre el acto que no esté ingresada en otro campo, y/o información que ayude a comprender el contexto en el que sucede este acto, antecedentes relevantes, etc. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15409	15001	buttonAddIntervencion	Interven-ciones/Pantalla única/Agregar una intervención	Haz clic aquí para agregar una nueva intervención. Aparecerá una ventana en la que debes ingresar el nombre de la persona que inicia o realiza esta intervención y el tipo de intervención.
15410	15254	staticText2	Interven-ciones/Pantalla única/Agregar una intervención / Agregar intervención - Quién inicia o realiza esta intervención	Haz clic en el signo de más (+) al lado de "Quién inicia o realiza esta intervención" para seleccionar el nombre de la persona de la lista de personas que ya están registradas en el sistema. El nombre seleccionado aparecerá aquí. Elige el "Tipo de intervención" y haz clic en el botón "Seleccionar". Puedes cancelar el registro oprimiendo el botón "Cancelar"
15783	15001	txtIntRespuesta	Interven-ciones/Pantalla única/Respuesta a la intervención	Indicación de la reacción o respuesta que hubo a la intervención, en general, o en particular de la persona o entidad a quien se le dirigió esta intervención. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15794	15001	textCtrlPubDatos	Fuentes/Fuente documental/Datos de la fuente	La información indispensable para poder localizar o citar un documento, por ejemplo: Título (del artículo, capítulo, programa radial, etc.); Título del libro, periódico, noticiero, etc.; Autor; Lugar de edición o publicación; Editorial; Edición, etc.
15784	15001	txtIntObservaciones	Interven-ciones/Pantalla única/Observaciones	Registra aquí cualquier información adicional sobre la intervención. Indica si la intervención se hizo en relación a un acto particular dentro del caso, sobre una persona o sobre el caso en su conjunto. También puedes indicar el grado de publicidad generado y el interés de la prensa, así como datos adicionales que no estén ingresados en otros campos. También puedes utilizar este espacio para incluir el texto y los destinatarios de la intervención. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15785	15001	txtIntComentarios	Interven-ciones/Pantalla única/Comentarios	Anotaciones internas del trabajo institucional sobre la intervención, por ejemplo: información sobre el uso y agotamiento de los recursos internos; estrategias para el seguimiento de las acciones; otras personas a quien se puede enviar la intervención; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15786	15001	listBoxFte	Fuentes/Fuente personal/Fuentes de información / Lista	Lista en orden alfabético, de las fuentes personales registradas en el caso activo. Para moverte dentro de la lista , utiliza el cursor o las barras de desplazamiento. Cuando encuentres la fuente que buscas, haz clic para seleccionarla. Una vez seleccionada, puedes modificar o agregar datos. Si quieres ingresar una nueva fuente personal, utiliza el botón "Agregar fuente personal" 
15407	15001	LC5	Interven-ciones/Pantalla única/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar nuevas intervenciones, o para modificar datos ya registrados en esta intervención. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15781	15001	listBoxIntervenciones	Interven-ciones/Pantalla única/Intervenciones / Lista	Lista de las intervenciones ya registradas en el caso activo. Están ordenadas alfabéticamente por el tipo de intervención, seguido del nombre de la persona o entidad que inició o realizó la intervención, por ejemplo: "Denuncia penal / Barajas Garibo, Raúl". Para moverte dentro de la lista, utiliza el cursor o las barras de desplazamiento. Cuando encuentres la intervención que buscas, haz clic para seleccionarla. Una vez seleccionada, puedes modificar o agregar datos. Si quieres ingresar una nueva intervención, utiliza el botón "Agregar una intervención" 
15416	15001	buttonTipoIntervencion	Interven-ciones/Pantalla única/Tipo de intervención / (+) signo de más	Haz clic aquí para sustituir el tipo de intervención que está registrada. Únicamente se puede ingresar un tipo para cada intervención
15418	15001	btnIntPInt	Interven-ciones/Pantalla única/Quién inicia o realiza esta intervención / (+) signo de más	Haz clic aquí para sustituir a la persona "Quién inicia o realiza esta intervención".
15782	15001	choiceIntTipofecha	Interven-ciones/Pantalla única/Fecha de la intervención	Fecha en que se realiza esta intervención, por ejemplo fecha del boletín de prensa o cuando se inicia la acción urgente, denuncia penal, etc. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15452	15001	buttonFteConexionInformacion	Fuentes/Fuente personal/Conexión con la información / (+) signo de más	Haz clic aquí para agregar un término que represente de la mejor manera la relación entre la fuente y la información que proporcionó. Únicamente se puede ingresar un tipo de conexión para cada fuente. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente.
15790	15001	textCtrlFteObservaciones	Fuentes/Fuente personal/Observaciones	Registra aquí cualquier información adicional sobre la persona que proporcionó información sobre el caso. Si es relevante, indica sobre qué o quién proporcionó información esta persona. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15458	15001	staticText37	Fuentes/Fuente personal/Confiabilidad	Evaluación de la confiabilidad de la información proporcionada por la fuente, por ejemplo "Poco confiable". Únicamente se puede ingresar un término de confiabilidad para cada fuente. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente.
15791	15001	textCtrlFteComentarios	Fuentes/Fuente personal/Comentarios	Anotaciones internas del trabajo institucional en relación a la fuente personal, por ejemplo: información que falta, no está clara o es contradictoria; necesidad de volver a entrevistar a la misma fuente, o a otras personas para corroborar la información; cuestiones de seguridad para la persona que aportó información o sobre su presencia en la ratificación de denuncias, etc.  Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15792	15001	listBoxDocs	Fuentes/Fuente documental/Documentos / Lista	Lista en orden alfabético de las fuentes documentales registradas en el caso activo. Para moverte dentro de la lista, utiliza el cursor o las barras de desplazamiento. Cuando encuentres el documento que buscas, haz clic para seleccionarlo. Una vez seleccionado, puedes modificar o agregar datos. Si quieres ingresar una nueva fuente documental, utiliza el botón "Agregar fuente documental" 
15465	15001	btnAddDoc	Fuentes/Fuente documental/Agregar fuente documental	Haz clic aquí para agregar un nuevo documento. En la ventana que aparece, ingresa una breve descripción (aprox. 15-20 palabras) que te permita identificar claramente el documento. Al terminar oprime "Seleccionar". Puedes cancelar el ingreso haciendo clic en "Cancelar". La identificación aparecerá en el nuevo registro de fuente documental
15793	15001	textCtrlPubTituloParte	Fuentes/Fuente documental/Identificación	Nombre o identificación de esta fuente. Se recomienda que sea corta pero informativa, por ejemplo: La Jornada, Expediente judicial, Testimonio de Ramón, etc.
15796	15001	textCtrlPubNombreSitio	Fuentes/Fuente documental/Nombre del sitio	Nombre del sitio de Internet en donde se encuentra el documento. Puedes escribir el nombre en texto libre y además poner la liga general al sitio, por ejemplo: La Jornada (http://www.jornada.unam.mx/ultimas/)
15788	15255	radioBoxTipoPersona	Fuentes/Fuente personal/Agregar fuente personal / Seleccionar una persona	Busca el nombre de la fuente personal, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15789	15001	choiceFteTipoFecha	Fuentes/Fuente personal/Fecha de la información	Fecha original de la información, por ejemplo fecha cuando se realizó la entrevista o la fuente personal hizo la declaración. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15795	15001	choicePubTipoFecha	Fuentes/Fuente documental/Fecha de la fuente	Fecha original de la fuente documental, por ejemplo fecha de publicación de un periódico, de emisión de un programa de radio, de difusión de un comunicado, etc. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15484	15001	staticText66	Fuentes/Fuente documental/Sobre quién se aporta información	Nombre de la persona sobre quien la fuente documental aportó información. Utiliza este campo cuando la información proporcionada sea sobre una persona en particular involucrada en el caso; por ejemplo: la víctima, el perpetrador, etc.
15521	15001	staticText81	Personas todas/Datos generales/Búsqueda rápida	Escribe unas cuantas letras del nombre de la persona que estás buscando. Puedes utilizar minúsculas o mayúsculas. Por ejemplo, si escribes  "cast", en la ventana de abajo aparecerán todas las personas que tengan apellidos como "Castañeda", "Castaño", "Castellanos", "Castillo",  "Castrejón", "Castro", etc. De las personas que aparecen en la ventana, selecciona con doble clic la que quieras trabajar. Para moverte dentro de la lista hacia abajo o hacia arriba, o hacia la derecha o la izquierda, utiliza el cursor o las barras de desplazamiento
15800	15001	srchPersona	Personas todas/Datos generales/Búsqueda rápida	Escribe unas cuantas letras del nombre de la persona que estás buscando. Puedes utilizar minúsculas o mayúsculas. Por ejemplo, si escribes  "cast", en la ventana de abajo aparecerán todas las personas que tengan apellidos como "Castañeda", "Castaño", "Castellanos", "Castillo",  "Castrejón", "Castro", etc. De las personas que aparecen en la ventana, selecciona con doble clic la que quieras trabajar. Para moverte dentro de la lista hacia abajo o hacia arriba, o hacia la derecha o la izquierda, utiliza el cursor o las barras de desplazamiento
15522	15001	radioBoxSelectTipoPersona	Personas todas/Datos generales/Mostrar	Palomea una de las casillas que aparecen en el recuadro para acotar el despliegue de personas registradas en el sistema. Pueden aparecer únicamente las "PERSONAS INDIVIDUALES", las "ENTIDADES COLECTIVAS" o las "PERSONAS DIRECTAMENTE RELACIONADAS CON EL CASO" activo. Puedes palomear "TODAS" si quieres que aparezca la lista completa de registros.
15526	15518	staticTextNombrePersona	Personas todas/Datos generales/Nueva persona / Datos de una persona individual - Nombre(s) y Apellido(s)	En las casillas correspondientes ingresa el nombre de pila y los apellidos de la persona que estás registrando. Siempre que puedas, ingresa todos los nombres y apellidos completos
15801	15518	TxtNombrePersona	Personas todas/Datos generales/Nueva persona / Datos de una persona individual - Nombre(s) y Apellido(s)	En las casillas correspondientes ingresa el nombre de pila y los apellidos de la persona que estás registrando. Siempre que puedas, ingresa todos los nombres y apellidos completos
15802	15518	staticTextApellido_Org	Personas todas/Datos generales/Nueva persona / Datos de una persona individual - Nombre(s) y Apellido(s)	En las casillas correspondientes ingresa el nombre de pila y los apellidos de la persona que estás registrando. Siempre que puedas, ingresa todos los nombres y apellidos completos
15803	15518	TxtApellido	Personas todas/Datos generales/Nueva persona / Datos de una persona individual - Nombre(s) y Apellido(s)	En las casillas correspondientes ingresa el nombre de pila y los apellidos de la persona que estás registrando. Siempre que puedas, ingresa todos los nombres y apellidos completos
15804	15517	TxtNombrePersona	Personas todas/Datos generales/Nueva persona / Datos una persona colectiva - Sigla y Nombre	En las casillas correspondientes ingresa la sigla y el nombre completo de la entidad o persona colectiva que estás registrando. Siempre que puedas, ingresa la sigla o acrónimo y el nombre de la manera más completa posible
15805	15517	staticTextApellido_Org	Personas todas/Datos generales/Nueva persona / Datos una persona colectiva - Sigla y Nombre	En las casillas correspondientes ingresa la sigla y el nombre completo de la entidad o persona colectiva que estás registrando. Siempre que puedas, ingresa la sigla o acrónimo y el nombre de la manera más completa posible
15806	15517	TxtApellido	Personas todas/Datos generales/Nueva persona / Datos una persona colectiva - Sigla y Nombre	En las casillas correspondientes ingresa la sigla y el nombre completo de la entidad o persona colectiva que estás registrando. Siempre que puedas, ingresa la sigla o acrónimo y el nombre de la manera más completa posible
15807	15001	staticText87	Personas todas/Datos generales/Casos relacionados con esta persona / Lista	Lista de los casos directamente relacionados con la persona activa. Están ordenados alfabéticamente por el nombre del caso, seguido de una diagonal (/) y el rol que tiene la persona en el caso, por ejemplo: Víctima o Fuente personal. Cuando encuentres el caso que buscas, haz doble clic sobre él para navegar de manera automática hacia el caso seleccionado. Desde la pantalla "Datos Generales" de "Casos" puedes regresar aqui haciendo clic en el botón "Pantalla anterior", que aparecerá en el lado superior derecho
15808	15515	FPNombre	Personas individual/Datos generales/Nombre(s)	Nombre de pila de la persona que estás registrando. Siempre que puedas, trata de ingresar todos los nombres completos
15810	15515	FPApellido	Personas individual/Datos generales/Apellido(s)	Apellidos de la persona que estás registrando. Siempre que puedas, trata de ingresar los dos apellidos completos
15811	15516	FPApellido	Personas colectivas/Datos generales/Nombre	Nombre completo de la entidad colectiva, de preferencia su nombre oficial, por ejemplo: "Ejército Mexicano"
15812	15515	FPOtroNombre	Personas individual/Datos generales/Otro nombre	Otro nombre utilizado por la persona que estás registrando. Puedes ingresar un apodo o un alias
15813	15516	FPOtroNombre	Personas colectivas/Datos generales/Otro nombre	Otro nombre por que el que se conozca a la entidad que estás registrando. Puede ser un nombre "corto" como "Frayba" o "Tlachi", o un nombre por el que se la conozca coloquialmente
15814	15515	FPSexo	Personas individual/Datos generales/Sexo	Haz clic en la flechita para seleccionar el sexo de la persona. Para borrar el dato, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Hombre". Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15809	15516	FPNombre	Personas colectivas/Datos generales/Sigla	Sigla, acrónimo o nombre corto de la entidad colectiva, por ejemplo "PGR"
15817	15516	Cpfechanac	Personas colectivas/Datos generales/Fecha de creación	Fecha de creación, fundación o surgimiento de esta entidad, grupo o movimiento. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15818	15516	FPfechanac	Personas colectivas/Datos generales/Fecha de creación	Fecha de creación, fundación o surgimiento de esta entidad, grupo o movimiento. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15552	15515	CPEstado	Personas individual/Datos generales/Estado de nacimiento	Estado de la república en donde nació esta persona. Únicamente se puede ingresar un estado de nacimiento para cada persona. Haz clic en la flechita para que aparezcan todos los estados de la república. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado que buscas, haz clic para seleccionarlo, y el estado aparecerá en el campo. Para borrar el estado, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un estado diferente
15819	15515	FPEstado	Personas individual/Datos generales/Estado de nacimiento	Estado de la república en donde nació esta persona. Únicamente se puede ingresar un estado de nacimiento para cada persona. Haz clic en la flechita para que aparezcan todos los estados de la república. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado que buscas, haz clic para seleccionarlo, y el estado aparecerá en el campo. Para borrar el estado, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un estado diferente
15553	15516	CPEstado	Personas colectivas/Datos generales/Estado de origen	Estado de la república en donde se crea, funda o surge esta entidad, grupo o movimiento. Únicamente se puede ingresar un estado de origen para cada entidad. Haz clic en la flechita para que aparezcan todos los estados de la república. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado que buscas, haz clic para seleccionarlo, y el estado aparecerá en el campo. Para borrar el estado, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un estado diferente
15820	15516	FPEstado	Personas colectivas/Datos generales/Estado de origen	Estado de la república en donde se crea, funda o surge esta entidad, grupo o movimiento. Únicamente se puede ingresar un estado de origen para cada entidad. Haz clic en la flechita para que aparezcan todos los estados de la república. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado que buscas, haz clic para seleccionarlo, y el estado aparecerá en el campo. Para borrar el estado, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un estado diferente
15554	15515	CPMunicipio	Personas individual/Datos generales/Municipio de nacimiento	Municipio del estado seleccionado arriba en donde nació esta persona. Únicamente se puede ingresar un municipio de nacimiento para cada persona. Haz clic en la flechita para que aparezcan todos los municipios del estado seleccionado. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y el municipio aparecerá en el campo. Para borrar el municipio, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un municipio diferente
15821	15515	FPMunicipio	Personas individual/Datos generales/Municipio de nacimiento	Municipio del estado seleccionado arriba en donde nació esta persona. Únicamente se puede ingresar un municipio de nacimiento para cada persona. Haz clic en la flechita para que aparezcan todos los municipios del estado seleccionado. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y el municipio aparecerá en el campo. Para borrar el municipio, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un municipio diferente
15822	15516	FPMunicipio	Personas colectivas/Datos generales/Municipio de origen	Municipio del estado seleccionado arriba en donde se crea, funda o surge esta entidad, grupo o movimiento. Únicamente se puede ingresar un municipio de origen para cada entidad. Haz clic en la flechita para que aparezcan todos los municipios del estado seleccionado. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y el municipio aparecerá en el campo. Para borrar el municipio, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un municipio diferente.
15823	15515	FPLocalidad	Personas individual/Datos generales/Localidad de nacimiento	Escribe el nombre de la comunidad o localidad en donde nació esta persona. El nombre no debe ser más largo de unas 20 palabras. Para borrar la localidad, selecciona todo el nombre y oprime el botón de "suprimir" en tu teclado
15824	15516	FPLocalidad	Personas colectivas/Datos generales/Localidad de origen	Escribe el nombre de la comunidad o localidad en donde se crea, funda o surge esta entidad, grupo o movimiento. El nombre no debe ser más largo de unas 20 palabras. Para borrar la localidad, selecciona todo el nombre y oprime el botón de "suprimir" en tu teclado
15816	15515	FPfechanac	Personas individual/Datos generales/Fecha de nacimiento	Fecha de nacimiento de esta persona. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15828	15516	FPIdioma	Personas colectivas/Detalles/Idioma predominante	Idioma que la mayoría de las personas en el grupo hablan, leen y/o escriben. Se puede ingresar varios idiomas para cada entidad o persona colectiva. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15829	15515	FPLengua	Personas individual/Detalles/Lengua que habla	Lengua o lenguas indígenas que habla esta persona. Se puede ingresar varias lenguas para cada persona. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15833	15515	FPReligion	Personas individual/Detalles/Religión	Religión que profesa la persona. Únicamente se puede ingresar una religión para cada persona. Haz clic en la flechita para que aparezcan todas las religiones. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres la religión que buscas, haz clic para seleccionarla, y la religión aparecerá en el campo. Para borrar la religión, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Religión católica". Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona una religión diferente
15834	15516	FPReligion	Personas colectivas/Detalles/Religión predominante	Religión que profesa la mayoría de las personas en el grupo. Únicamente se puede ingresar una religión para cada entidad o persona colectiva. Haz clic en la flechita para que aparezcan todas las religiones. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres la religión que buscas, haz clic para seleccionarla, y la religión aparecerá en el campo. Para borrar la religión, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Religión católica". Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona una religión diferente
15835	15515	FPEstadocivil	Personas individual/Detalles/Estado civil	El estado civil o situación marital actual de la persona. Únicamente se puede ingresar un estado civil para cada persona. Haz clic en la flechita para que aparezcan todos los estados civiles. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el estado civil que buscas, haz clic para seleccionarlo, y el término aparecerá en el campo. Para borrar el estado civil, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Soltero". Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15836	15515	FPNodependientes	Personas individual/Detalles/No. de dependientes	Número de hijos u otros dependientes de quienes esta persona es responsable. Únicamente puedes ingresar números, por ejemplo "5"
15837	15516	FPNodependientes	Personas colectivas/Detalles/No. de personas en el grupo	Número exacto o aproximado de personas que integran la entidad o grupo Únicamente puedes ingresar números, por ejemplo "5000" para una empresa que tiene cinco mil trabajadores
15838	15516	FPDescripciondelgrupo	Personas colectivas/Detalles/Descripción del grupo	Muy breve descripción del grupo de más o menos 8-10 palabras. Para información sustantiva sobre la entidad, utiliza el campo "Observaciones" en la pestaña de "Información administrativa"
15839	15001	FPDirecciones	Personas todas/Detalles/Dirección(es)	Información respecto a dónde vive, ha vivido o se puede localizar a esta persona o entidad. Puedes ingresar varias direcciones. Para moverte dentro de la lista, utiliza el cursor o las barras de desplazamiento
15840	15514	choiceTipoDireccion	Personas todas/Detalles/Dirección(es) / Tipo de dirección	Es el tipo de lugar de la dirección de esta persona, por ejemplo, "casa", "trabajo" o "dirección temporal" (que puede ser una cárcel). También puede ser la "dirección institucional" de una entidad o grupo. Únicamente puedes seleccionar un "tipo de dirección" para cada dirección que ingreses. Haz clic en la flechita para seleccionar el tipo de esta dirección. Cuando encuentres el tipo de dirección que buscas, selecciónala y el término aparecerá en el campo. Para borrar el dato, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15841	15514	textCtrlDireccion	Personas todas/Detalles/Dirección(es) / Dirección	Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección". Ingresa la dirección en el orden normal de calle, número exterior, número interior, colonia, ciudad, estado, código postal y país (si  la dirección no es en México). Ingresa aquí una sola dirección, si quieres registrar otra, primero guarda esta y luego repite el procedimiento para agregar una nueva
15831	15515	FPOrigenEtnico	Personas individual/Detalles/Origen étnico	Origen étnico o pueblo indígena al que pertenece esta persona. Se puede ingresar varios términos para cada persona. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15842	15514	textCtrlTel	Personas todas/Detalles/Dirección(es) / Teléfono	Ingresa el número de teléfono, y de preferencia las claves necesarias para llamar desde tu lugar de origen. Puedes ingresar varios números. Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección"
15827	15515	FPIdioma	Personas individual/Detalles/Idioma que habla	Idioma que habla, lee y/o escribe esta persona. Se puede ingresar varios idiomas para cada persona. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15830	15516	FPLengua	Personas colectivas/Detalles/Lengua predominante	Lengua o lenguas indígenas que hablan las personas en el grupo. Se puede ingresar varias lenguas para cada entidad o persona colectiva, por ejemplo si en un grupo de desplazados internos hay personas que hablan Ch'ol y Tseltal. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15845	15514	textCtrlWeb	Personas todas/Detalles/Dirección(es) / Página WEB	Ingresa la página web de esta persona tal como aparece en Internet. Puedes copiar y pegar el dato. Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección".
15846	15001	FPMonitoreo	Personas todas/Detalles/Monitoreo	Indica si la organización está trabajando activamente sobre esta persona. Por ejemplo, selecciona "Activo" si se le está dando seguimiento cotidiano a la entidad "Ejército Mexicano" o a la Procuraduría de tu estado. Haz clic en la flechita para abrir la lista de opciones. Si quieres borrar un dato registrado, haz clic en el espacio en blanco que aparece al inicio de la lista.
15848	15001	FPComentarios	Personas todas/Información administrativa/Comentarios	Anotaciones internas del trabajo institucional sobre la persona, por ejemplo: información que falta, que no está clara o es contradictoria; estrategias o fuentes adicionales para seguimiento o verificación; opiniones o información no corroborada sobre la persona; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15849	15001	FPArchivos	Personas todas/Información administrativa/Archivos	Indicación del archivo o archivos físicos o electrónicos en donde se puede encontrar la información y documentación sobre la persona, por ejemplo: número de expediente, ruta y nombre de archivo en la computadora, etc. También se debe indicar si existe y se puede obtener información en archivos de otra institución, sitio de Internet, etc. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15850	15001	FPTipodefecharecepcion	Personas todas/Información administrativa/Fecha de recepción	Fecha en que la organización tuvo conocimiento de los datos de esta persona por primera vez. Puede ser la fecha en que inicialmente se atendió la denuncia, la fecha original de la fuente de información, o la fecha cuando se consultó la fuente por primera vez. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15851	15001	FPproyecto_grupo	Personas todas/Información administrativa/Proyecto local	Nombre de la campaña o proyecto en el que está trabajando tu organización, y para el cual esta persona es relevante. Los proyectos pueden ser temas como "Sistema penitenciario", o productos como "Informe anual". También pueden ser seguimiento de ciertas entidades como "Ejército mexicano en el estado", situaciones como "Atenco" o "Zona norte", o un proceso judicial que lleva la organización. El nombre de proyecto se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos
15852	15001	FPproyecto_conjunto	Personas todas/Información administrativa/Proyecto conjunto RedTDT	Nombre de la campaña o  proyecto en el que está trabajando la RedTDT en su conjunto, y para el cual esta persona es relevante, por ejemplo: "Criminalización de la protesta social". Este nombre se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos siempre y cuando estén acordados en el marco del trabajo conjunto de La RedTDT
15853	15001	FPproyecto_se	Personas todas/Información administrativa/Proyecto SE	Nombre de la campaña o proyecto en el que está trabajando la Secretaría Ejecutiva, y para el cual esta persona es relevante. Para los proyectos de toda La RedTDT, utilizar el campo "Proyecto conjunto". Los proyectos de la Secretaría Ejecutiva pueden ser productos como "Informe anual" o "Casos para la CIDH", temas, seguimiento de ciertas entidades, situaciones o procesos. El nombre de proyecto se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos 
15854	15001	listBoxVinculos	Personas todas/Datos biográficos/Datos biográficos / Lista	Lista de los datos biográficos registrados para la persona activa. Están ordenados alfabéticamente por la descripción del dato biográfico y/o por el nombre de la persona relacionada seguido del tipo de relación. Para moverte dentro de la lista utiliza el cursor o las barras de desplazamiento. Cuando encuentres el dato que buscas, haz clic para seleccionarlo. Una vez seleccionado, puedes modificar o agregar datos. Si quieres ingresar un nuevo dato biográfico, utiliza el botón "Agregar dato biográfico" 
15855	15513	TDB1	Personas todas/Datos biográficos/Agregar dato biográfico / Dato biográfico Sin relación con otra persona	"Palomea" esta casilla si el dato NO tiene relación con otra persona diferente a la persona activa. Por ejemplo, un dato "Sin relación con otra persona" puede ser la declaración que hace un funcionario sobre un tema que te interesa 
15856	15513	TDB2	Personas todas/Datos biográficos/Agregar dato biográfico / Dato biográfico Relacionado con otra persona	"Palomea" esta casilla si el dato que quieres ingresar es sobre la relación de la persona activa con otra persona, ya sea una entidad o una persona individual. Completa los datos necesarios en las ventanas de abajo
15857	15513	staticPersona2	Personas todas/Datos biográficos/Agregar dato biográfico / [#] Nombre de la persona	Esta es la persona activa a quien se le está agregando un nuevo dato biográfico relacionado con otra persona. Si quieres trabajar sobre una persona distinta, oprime el botón "Cancelar", regresa a la pestaña "Datos generales" y selecciona una persona diferente
15843	15514	textCtrlCelular	Personas todas/Detalles/Dirección(es) / Celular	Ingresa el número de celular completo. Puedes ingresar varios números. Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección"
15859	15513	listBoxPersonaBrowser	Personas todas/Datos biográficos/Agregar dato biográfico / Con qué persona o entidad se relaciona	En esta ventana selecciona a la segunda persona en esta relación, por ejemplo a Aldo Zamora como hijo de Ildefonso Zamora. En el casillero vacío ubicado al lado de "Nueva persona" puedes hacer una búsqueda rápida escribiendo el nombre de la persona. Si la persona no está registrada, puedes ingresarla haciendo clic en el botón "Nueva persona". Una vez que selecciones a la persona, asegúrate de haber establecido el tipo de relación que la vincula a la persona activa y haz clic en el botón "Seleccionar".
15861	15001	FBFechaInicialTipo	Personas todas/Datos biográficos/Fecha inicial	Indicación de cuándo inicia el dato biográfico que se está registrando o actualizando. Por ejemplo: cuándo inicia la relación de trabajo entre dos personas (fecha cuando un funcionario asume el puesto o cargo público en una institución). Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15862	15001	FBFechaFinalTipo	Personas todas/Datos biográficos/Fecha final	Indicación de cuándo terminó el dato biográfico que se está registrando o actualizando. Por ejemplo, si es una relación de trabajo entre dos personas, la fecha cuando un funcionario es destituido o renuncia a su puesto o cargo público. Si la relación o el dato biográfico no ha terminado, NO ingreses ninguna fecha. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15880	15682	treeCtrl1	Actos/Información general/Tipo de lugar / Selección de Tipo de lugar	Haz clic en los signos de más (+) para abrir la listas de tipos de lugar. Cuando encuentres el que buscas, selecciónalo y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un tipo de lugar para cada acto. 
15863	15001	FBFechaInfo_vigenteTipo	Personas todas/Datos biográficos/Fecha de vigencia	Fecha en que el dato registrado es o fue vigente. Esta opción se utiliza cuando no se conocen las fechas exactas de inicio o final de un dato biográfico pero sí se sabe que es o fue vigente en una fecha específica. Es importante tratar de completar las fechas inicial y final del dato biográfico. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15642	15001	longPerDBCom	Personas todas/Datos biográficos/# espacios en Comentarios	El número total de espacios (caracteres y espacios) que tiene el texto ingresado. Aproximadamente, 125 espacios son  20 palabras; 600 espacios son 100 palabras; 3,000 espacios son  500 palabras, y 6,000 espacios son 1,000 palabras. Una página tiene más o menos 500 palabras o 3,000 espacios
15866	15001	FBPuesto	Personas todas/Datos biográficos/Puesto o cargo	Nombre o descripción del puesto o cargo que ocupa esta persona, por ejemplo "Comandante de zona", "Trabajador en la planta de Puebla"
15867	15001	FBRango	Personas todas/Datos biográficos/Rango	Identificación del rango militar o de las fuerzas de seguridad que tiene esta persona, por ejemplo "General de división", "Comandante"
15858	15513	isearch	Personas todas/Datos biográficos/Agregar dato biográfico / Con qué persona o entidad se relaciona	En esta ventana selecciona a la segunda persona en esta relación, por ejemplo a Aldo Zamora como hijo de Ildefonso Zamora. En el casillero vacío ubicado al lado de "Nueva persona" puedes hacer una búsqueda rápida escribiendo el nombre de la persona. Si la persona no está registrada, puedes ingresarla haciendo clic en el botón "Nueva persona". Una vez que selecciones a la persona, asegúrate de haber establecido el tipo de relación que la vincula a la persona activa y haz clic en el botón "Seleccionar".
15860	15001	FBDescripcion	Personas todas/Datos biográficos/Descripción	Es la descripción de un dato biográfico que NO sea una relación entre la persona activa y otra persona. Puede ser una declaración de algún funcionario, una publicación relevante de alguna organización, etc.
15635	15001	btnPrelacionada	Personas todas/Datos biográficos/P. relacionada / (+) signo de más	Si ya hay una persona registrada y la quieres sustituir, haz clic aquí  para seleccionar el nombre de otra persona. Selecciona el nombre de la lista de personas que ya están registradas en el sistema, o ingresa una nueva persona oprimiendo el botón "Nueva persona".
15879	15718	treeCtrl1	Actos/Información general/Características relevantes / Selección de Características relevantes	Haz clic en los signos de más (+) para abrir las listas de Características relevantes. Cuando encuentres la que  buscas, márcala y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar".
15868	15650	casoOpciones	Casos/Datos generales/Reportes/Opciones 	Haz clic aquí para abrir la ventana de Opciones y generar un modelo de reporte. Podrás seleccionar los campos que desees eliminar de tu reporte. 
15870	15650	choicePrintCfg	Casos/Datos generales/Reportes/Modelo de impresión 	Estos son los modelos de impresión que han sido guardados anteriormente. Si quieres abrir un reporte que contenga las opciones de algún modelo, haz clic en la flechita para ver la lista y selecciona el que deseas. Después abre tu reporte.
15871	15247	Notas_municipio	Casos/Datos Generales/Nueva Localización / Localización - Municipio - Notas	Utiliza este espacio para registrar información adicional sobre el dato del Municipio o para hacer alguna aclaración. Ej: si es un Municipio autónomo o dos municipios colindantes, etc. 
15872	15247	staticText5	Casos/Datos Generales/Nueva Localización / Localización - Municipio - Notas	Utiliza este espacio para registrar información adicional sobre el dato del Municipio o para hacer alguna aclaración. Ej: si es un Municipio autónomo o dos municipios colindantes, etc. 
15656	15650	staticText2	Casos/Datos generales/Reportes/Emisión de reportes / Derechos afectados/Estado/Caso	Este es un reporte que contiene una tabla de los Derechos afectados que han sido asignados en los diferentes casos y además la información de los Estados, Fecha inicial, Nombre del caso y Número de personas afectadas correpondientes. Para generar el reporte, haz clic en el ícono que aparece a un lado.
15873	15247	staticText6	Casos/Datos Generales/Nueva Localización / Localización - Localidad - Notas	Utiliza este espacio para registrar información adicional sobre el dato de la Localidad o para hacer alguna aclaración. Ej: si los hechos ocurrieron  en algún camino o carretera cercano a la Localidad 
15874	15247	Notas_localidad	Casos/Datos Generales/Nueva Localización / Localización - Localidad - Notas	Utiliza este espacio para registrar información adicional sobre el dato de la Localidad o para hacer alguna aclaración. Ej: si los hechos ocurrieron  en algún camino o carretera cercano a la Localidad 
15875	15678	personaIsearch	Actos/Información general/Agregar acto / Selección de Víctima	Busca el nombre de la víctima en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la víctima que quieras ingresar y oprime el botón "Seleccionar". 
15876	15678	radioBoxTipoPersona	Actos/Información general/Agregar acto / Selección de Víctima	Busca el nombre de la víctima en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la víctima que quieras ingresar y oprime el botón "Seleccionar". 
15877	15678	listBoxPersona	Actos/Información general/Agregar acto / Selección de Víctima	Busca el nombre de la víctima en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la víctima que quieras ingresar y oprime el botón "Seleccionar". 
15951	15001	btnCambiaTipoPersona	Personas/Datos generales/Búsqueda Exhaustiva/Cambiar a colectiva/individual	Haz clic aquí para cambiar el tipo de persona a individual o colectiva, en caso de que se le haya asignado un "tipo" que no le corresponde
15881	15683	treeCtrl1	Actos/Información general/Estatus VDH / Selección Estatus de la VDH	Haz clic en uno de los términos que aparece en la lista y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un estatus para cada acto o VDH. 
15882	15684	treeCtrl1	Actos/Información general/Estatus de la víctima / Selección Estatus de la víctima	Haz clic en uno de los términos que aparece en la lista y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un estatus para cada víctima en relación al acto o VDH.
15869	15650	button1	Casos/Datos generales/Reportes/Opciones 	Haz clic aquí para abrir la ventana de Opciones y generar un modelo de reporte. Podrás seleccionar los campos que desees eliminar de tu reporte. 
15886	15687	treeCtrl1	Actos/Perpetradores/Grado de involucramiento / Selección Grado de involucramiento	 Haz clic en los signos de más (+) para abrir las listas. Cuando encuentres el término que  buscas, selecciónalo y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un término.
15887	15688	treeCtrl1	Actos/Perpetradores/Tipo de perpetrador / Selección Tipo de perpetrador	Haz clic en los signos de más (+) para abrir las listas. Cuando encuentres el tipo de perpetrador que  buscas, selecciónalo y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un término.
15888	15690	treeCtrl1	Actos/Perpetradores/Último estatus del perpetrador / Selección Último estatus del perpetrador	Haz clic en el término que buscas y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Únicamente se puede ingresar un término.
15890	15691	radioBoxTipoPersona	Intervenciones/Pantalla única/Agregar una intervención / Selección de Quién inicia o realiza esta intervención	Busca el nombre de la persona que inicia o realiza esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15891	15691	listBoxPersona	Intervenciones/Pantalla única/Agregar una intervención / Selección de Quién inicia o realiza esta intervención	Busca el nombre de la persona que inicia o realiza esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15878	15681	treeCtrl1	Actos/Información general/Agregar acto / Selección de Tipo de acto o VDH	Haz clic en los signos de más (+) para abrir las listas de actos o VDHs. Selecciona un término y oprime el botón "Seleccionar". Si deseas cancelar la operación haz clic en "Cancelar"
15671	15650	btnSaveCfg	Casos/Datos generales/Reportes/Guardar modelo 	Haz clic aquí para guardar los cambios hechos a un modelo de reporte ya existente. 
15895	15693	radioBoxTipoPersona	Intervenciones/Pantalla única/Quién inicia o realiza esta intervención / Selección de Quién inicia o realiza esta intervención	Busca el nombre de la persona que inicia o realiza esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15896	15693	listBoxPersona	Intervenciones/Pantalla única/Quién inicia o realiza esta intervención / Selección de Quién inicia o realiza esta intervención	Busca el nombre de la persona que inicia o realiza esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15884	15686	treeCtrl1	Actos/Normatividad /Insturmentos internacionales / Selección Instrumentos internacionales	Selecciona el instrumento internacional que aplique a este acto. Haz clic en los signos de más (+) para abrir las listas de los instrumentos que tratan cada tema. Cuando encuentres el instrumento que buscas, selecciónalo y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Puedes ingresar todos los instrumentos relevantes para este acto o VDH. 
15885	15001	buttonSelPerpetrador	Actos/Perpetradores/Nombre del Perpetrador / (+) Signo de más	Haz clic aquí para sustituir al perpetrador por otro, sólo cuando sea necesario.
15893	15692	treeCtrl1	Intervenciones/Pantalla única/Tipo de intervención / Selección de Tipo de intervención	Haz clic en los signos de más (+) para abrir las listas. Cuando encuentres la intervención que buscas, selecciónala y oprime el botón "Seleccionar". El tipo de intervención seleccionado sustituirá al ya existente.
15894	15693	personaIsearch	Intervenciones/Pantalla única/Quién inicia o realiza esta intervención / Selección de Quién inicia o realiza esta intervención	Busca el nombre de la persona que inicia o realiza esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15453	15001	staticText27	Fuentes/Fuente personal/Fecha de la información	Fecha original de la información, por ejemplo fecha cuando se realizó la entrevista o la fuente personal hizo la declaración. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15903	15697	personaIsearch	Fuentes/Fuente personal/Persona sobre quien se aporta información / Selección de Persona sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el campo vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Marca con un clic el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15904	15697	radioBoxTipoPersona	Fuentes/Fuente personal/Persona sobre quien se aporta información / Selección de Persona sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el campo vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Marca con un clic el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15905	15697	listBoxPersona	Fuentes/Fuente personal/Persona sobre quien se aporta información / Selección de Persona sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el campo vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Marca con un clic el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15899	15694	listBoxPersona	Intervenciones/Pantalla única/Sobre quien se interviene / Selección de Sobre quien se interviene	Busca el nombre de la persona sobre quien se interviene, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15901	15695	radioBoxTipoPersona	Intervenciones/Pantalla única/A quién se le dirigió esta intervención / Selección de A quién se le dirigió esta intervención	Busca el nombre de la persona a quien se le dirigió esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15902	15695	listBoxPersona	Intervenciones/Pantalla única/A quién se le dirigió esta intervención / Selección de A quién se le dirigió esta intervención	Busca el nombre de la persona a quien se le dirigió esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15906	15698	treeCtrl1	Fuentes/Fuente personal/Conexión con la información / Selección de Conexión con la información	Haz clic en el término que buscas y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un tipo de conexión con la información para cada fuente.
15910	15001	btnAddFteConfiabilidad	Fuentes/Fuente personal/Confiabilidad / (+) signo de más	Haz clic aquí para seleccionar el término que evalue la confiabilidad de la fuente. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente. 
15907	15001	btnAddFteLenguaIndigena	Fuentes/Fuente personal/Lengua indígena / [+] signo de mas	Haz clic aquí para agregar la lengua indígena. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente. 
15898	15694	radioBoxTipoPersona	Intervenciones/Pantalla única/Sobre quien se interviene / Selección de Sobre quien se interviene	Busca el nombre de la persona sobre quien se interviene, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15909	15001	btnDelFteLenguaIndigena	Fuentes/Fuente personal/Lengua indígena / (X) signo de multiplicación	Haz clic aquí para borrar el dato.
15914	15702	treeCtrl1	Fuentes/Fuente documental/Tipo de fuente / Selección de Tipo de fuente	Haz clic en los signos de más (+) para abrir las listas de Fuente de información. Cuando encuentres el tipo de fuente que buscas, márcalo y haz clic en el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un tipo de fuente para cada registro. 
15908	15700	treeCtrl1	Fuentes/Fuente personal/Lengua indígena / Selección de Lengua indígena	Marca el término que  buscas y haz clic en el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Únicamente se puede ingresar una lengua indígena por  cada fuente.
15922	15715	treeCtrl1	Personas colectivas/Datos generales/Tipo de grupo / Selección de Tipo de grupo	Marca el término que mejor defina a la entidad o grupo que estás registrando y haz clic en el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un tipo de grupo por cada entidad o grupo.
15915	15001	btnAddDocLenguaIndigena	Fuentes/Fuente documental/Lengua indígena / (+) signo de más	Haz clic aquí para agregar la lengua indígena del documento. Únicamente se puede ingresar una lengua indígena por cada fuente. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente. 
15918	15703	radioBoxTipoPersona	Fuentes/Fuente documental/Sobre quien se aporta la información / Selección de Sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones de la izquierda. También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15919	15703	listBoxPersona	Fuentes/Fuente documental/Sobre quien se aporta la información / Selección de Sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones de la izquierda. También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15920	15001	btnAddPubConfiabilidad	Fuentes/Fuente documental/Confiabilidad / (+) signo de más	Haz clic aquí para seleccionar el término que evalue la confiabilidad de la fuente. Únicamente se puede ingresar un nivel de confiabilidad por cada fuente. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente. 
15924	15705	treeCtrl1	Personas todas/Detalles/Idioma que habla/ Idioma predominante / Selección de Idioma	Haz clic en el idioma que buscas y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Si deseas agregar otro idioma, repite el procedimiento.
15926	15707	treeCtrl1	Personas todas/Detalles/Origen étnico/ Origen étnico predominante / Selección de Orígen étnico	Haz clic en el origen étnico que buscas y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Si deseas agregar otro orígen etnico, repite el procedimiento.
15928	15708	addCond	Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición	Haz clic aquí para seleccionar una por una las condiciones de tu búsqueda. Aparecerá la lista de todos los campos sobre los cuales puedes realizar una búsqueda. 
15921	15704	treeCtrl1	Fuentes/Fuente documental/Confiabilidad / Selección de Confiabilidad	Haz clic en el término y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Únicamente se puede ingresar un nivel de confiabilidad por cada fuente.
15911	15699	treeCtrl1	Fuentes/Fuente personal/Confiabilidad / Selección de Confiabilidad	Haz clic en el término que evalue la confiabilidad de la fuente personal y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un nivel de confiabilidad por cada fuente. 
15913	15701	textCtrl1	Fuentes/Fuente documental/Agregar fuente documental / Ingreso de Identificación	Ingresa una breve descripción (aprox. 15-20 palabras) que te permita identificar claramente el documento. Al terminar haz clic en "Seleccionar". Puedes cancelar el ingreso haciendo clic en "Cancelar". La identificación aparecerá en los campos de registro de Documentos e Identificación. 
15916	15001	btnDelDocLenguaIndigena	Fuentes/Fuente documental/Lengua indígena / (X) signo de multiplicación	Haz clic aquí para borrar el dato.
15925	15706	treeCtrl1	Personas todas/Detalles/Lengua que habla / Lengua predominante / Selección de Lengua Indígena	Haz clic en la lengua indígena que buscas y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Si deseas agregar otra lengua indígena, repite el procedimiento.
15934	15712	Condicion	Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición / Selección de Fecha	Selecciona la fecha que quieres incluir como condición en orden día, mes y año. Si es una fecha exacta, pon dicha fecha en ambos campos. Si es un periodo de tiempo, especifica entre qué fecha y qué fecha deseas hacer tu búsqueda.  
15935	15709	delCond	Casos/Datos generales/Búsqueda Exhaustiva/Borrar una condición	Haz clic aquí para borrar una condición. Previamente, selecciona de la ventana la condición que deseas borrar. 
15936	15709	delAll	Casos/Datos generales/Búsqueda Exhaustiva/Borrar todas	Haz clic aquí para borrar todas las condiciones que se encuentren en la ventana.
15937	15709	btnRegresar	Casos/Datos generales/Búsqueda Exhaustiva/Regresar	Haz clic aquí una vez que hayas establecido las condiciones de tu búsqueda. En la pantalla Casos/Datos generales, haz clic en "Aplicar" para obtener los resultados de tu búsqueda.
15939	15254	btnParteInt	Interven-ciones/Pantalla única/Agregar una intervención / Agregar intervención - Quién inicia o realiza esta intervención	Haz clic en el signo de más (+) al lado de "Quién inicia o realiza esta intervención" para seleccionar el nombre de la persona de la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones de la izquierda. También puedes escribir en el campo vacío las letras del nombre que buscas, si el nombre no aparece, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Marca el nombre de la víctima que quieras ingresar y haz clic en el botón "Seleccionar". La persona que seleccionaste aparecerá en la ventana de "Agregar intervención". Puedes cancelar el registro oprimiendo el botón "Cancelar"
15940	15254	btnTipoInt	Interven-ciones/Pantalla única/Agregar una intervención / Agregar intervención - Tipo de intervención	Haz clic en el signo de más (+) al lado de "Tipo de intervención" y, en la ventana que aparece, selecciona el tipo que mejor describa la intervención. Utiliza el cursor para moverte hacia abajo o hacia arriba, y haz clic en el signo de más (+) para abrir la lista. Cuando encuentres la intervención que buscas, haz clic para seleccionarla, y oprime el botón "Seleccionar". El tipo seleccionado aparecerá en la ventana de registro. Oprime el botón "Crear" para terminar la operación. Si deseas cancelar la operación, haz clic en "Cancelar"
15941	15001	txtIntImpacto	Interven-ciones/Pantalla única/Impacto de la intervención	Indicación de la magnitud o envergadura de la intervención así como de la manera en que la intervención afectó la situación, por ejemplo: un impacto positivo es que la persona detenida fue liberada como consecuencia de la intervención; un impacto negativo puede ser que la persona detenida fue trasladada a un penal lejano a su lugar de origen, o que fue amenazada como consecuencia de la intervención. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15942	15001	textCtrlPubComentarios	Fuentes/Fuente documental/Comentarios	Anotaciones internas del trabajo institucional sobre el documento, por ejemplo: información que falta, no está clara o es contradictoria; otras fuentes documentales que haga falta consultar para corroborar los datos aportados por esta fuente;  opiniones sobre la fuente;  etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15931	15710	textCtrl1	Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición / Ingreso de Descripción	Introduce el texto que quieres agregar como condición a la búsqueda, por ejemplo, un nombre. Palomea la casilla de "invertir condición" si deseas encontrar todos los registros, EXCEPTO el que contenga el texto que hayas escrito. Para terminar la operación haz clic en "Seleccionar". Para buscar los registros que tengan este campo vacío, sólo oprime el botón "Seleccionar" sin escribir ningún texto
15932	15711	DlgUser	Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición / Selección de Usuario	Haz clic en el usuario que quieres agregar como condición a la búsqueda. Palomea la casilla de "invertir condición" si deseas encontrar todos los registros, EXCEPTO los creados o actualizados por el usuario que hayas seleccionado. Para terminar la operación oprime el botón "Seleccionar".
15933	15717	treeCtrl1	Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición / Selección de término en listas estandarizadas	Haz clic en el término que quieres añadir como condición a la búsqueda. Haz clic en los signos de más (+) para abrir las listas cuando sea necesario. Palomea la casilla de "invertir condición" si deseas encontrar todos los registros que contengan algún término de la lista, EXCEPTO el que hayas seleccionado. Para terminar la operación oprime el botón "Seleccionar". Para buscar los registros que tengan este campo vacío, sólo oprime el botón "Seleccionar" sin hacer clic en ningún término
15938	15713	Regresar	Casos/Datos generales/Reportes/Regresar	Haz clic aquí una vez que hayas despalomeado los campos que no deseas que aparezcan en tu reporte. Regresarás a la pantalla de "Emisión de reportes"
15930	15710	staticText1	Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición / Ingreso de Descripción	Introduce el texto que quieres agregar como condición a la búsqueda, por ejemplo, un nombre. Palomea la casilla de "invertir condición" si deseas encontrar todos los registros, EXCEPTO el que contenga el texto que hayas escrito. Para terminar la operación haz clic en "Seleccionar". Para buscar los registros que tengan este campo vacío, sólo oprime el botón "Seleccionar" sin escribir ningún texto
15284	15001	txtTotalCasos	Casos/Datos generales/# casos registrados	El número total de casos registrados en el sistema. El número no es igual al número del último caso ingresado
15291	15001	AltaCaso	Casos/Datos generales/Nuevo caso	Haz clic aquí y, en la ventana que aparece, escribe el nombre del nuevo caso que quieres registrar. Escribe un nombre que identifique claramente el caso. El nombre debe ser único para cada caso. Puedes ingresar un nombre de más o menos 35 palabras. Cuando hayas ingresado el nombre del nuevo caso, haz clic en "Seleccionar". Si quieres, puedes cancelar el ingreso del nuevo caso haciendo clic en "Cancelar"
15292	15001	delCaso	Casos/Datos generales/Borrar caso	Haz clic aquí para borrar el caso seleccionado. Antes de poder borrar el caso debes borrar todas las relaciones asociadas a ese caso, incluyendo los actos, las fuentes y las intervenciones. Si el caso aún tiene relaciones, cuando intentes borrarlo te aparecerá una alerta y el caso no será borrado
15493	15001	staticText30	Casos/Datos generales/Fecha inicial	Indicación de cuándo comenzaron los hechos que se incluyen en este caso. Generalmente es la fecha del primer incidente o acto, o la primera fecha significativa. Por ejemplo: la fecha inicial de un caso de tortura puede ser uno o varios días antes cuando la víctima fue detenida. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15723	15001	choiceTipoFechaFinal	Casos/Datos generales/Fecha final	Indicación de cuándo terminaron los hechos que se incluyen en este caso. Generalmente es la fecha cuando termina el último incidente o acto, o cuando se resuelve la situación. Si el caso no está cerrado o no ha terminado, NO ingreses ninguna fecha. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15736	15247	Municipio	Casos/Datos generales/Nueva localización / Localización - Municipio	En "(seleccionar)" aparecen todos los municipios del estado seleccionado arriba. Puedes escribir unas letras del nombre del municipio que te interesa en el campo que dice "(buscar)". Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y aparecerá en la ventana de arriba. Para borrar el municipio seleccionado, ingresa al campo que contiene la lista de municipios y haz clic sobre la línea en blanco que aparece al inicio. Después de hacer la selección, puedes escribir una breve nota de más o menos 20 palabras en el campo "Notas".
15304	15001	staticText32	Casos/Datos generales/No. de personas afectadas	El número exacto o estimado de las personas, familias, comunidades, etc. que han sido afectadas por lo ocurrido en el caso, y una breve indicación de cómo fueron afectadas. Ejemplos: 400 trabajadores despedidos / 1 muerto y 2 heridos / 10,000 habitantes sin agua
15496	15001	staticText94	Casos/Información administrativa/Fecha de recepción	Fecha en que la organización tuvo conocimiento del caso por primera vez. Puede ser la fecha en que inicialmente se atendió la denuncia, la fecha original de la fuente de información, o la fecha cuando se consultó la fuente por primera vez. Esta fecha no necesariamente coincide con las fechas del caso. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15498	15001	staticText76	Casos/Información administrativa/Proyecto conjunto RedTDT	Nombre de la campaña o  proyecto en el que está trabajando la RedTDT en su conjunto, y para el cual este caso es relevante, por ejemplo: "Criminalización de la protesta social". Este nombre se utiliza para recuperar todos los registros de casos que estén relacionados con ese proyecto o campaña. Puedes ingresar varios nombres de proyectos, separándolos con comas, punto, o punto y coma; siempre y cuando estén acordados en el marco del trabajo conjunto de la RedTDT.
15502	15001	staticText35	Casos/Información narrativa/Resumen de la descripción	Escribe un resumen del caso de media cuartilla que contenga los datos indispensables (Fecha y lugar de los hechos), nombre de la(s) víctima(s), derechos violados, presuntos responsables. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH, por ejemplo la descripción narrativa de arriba.
15505	15248	staticText109	Casos/Relaciones/Nueva relación / Se relaciona como	Haz clic en el signo de más (+) para abrir la lista de tipos de relación entre casos. Utiliza el cursor para moverte hacia abajo o hacia arriba. Cuando encuentres la relación que buscas, haz clic para seleccionarla y oprime el botón "Seleccionar". La relación aparecerá en la ventana de registro. Si deseas cancelar la operación,  haz clic en "Cancelar"
15506	15001	staticText71	Casos/Relaciones/Caso relacionado	Este es el caso que se relaciona con el caso activo. Si quieres cambiar el caso relacionado, haz clic en el signo de más (+) y selecciona un caso diferente. Si en el recuadro de arriba "Relacionado con", hay más de un caso registrado, haz doble clic en el que quieras modificar o agregar observaciones y comentarios.
15945	15650	textCtrlFilename	Casos/Datos generales/Reportes/Archivo a generar	El reporte se genera por omisión con el nombre de 'salida' y se guarda en la carpeta "archivos" del SMDH, cada reporte que generes con ese nombre, sustituirá al anterior.  Puedes ingresar aquí un nombre distinto que no tenga espacios, ñ o números, usa el guión bajo para separar palabras. O bien, cuando abras tu reporte, renómbralo y guardarlo en la carpeta que desees (el formato será acorde con la aplicación que hayas usado para abrirlo)
15337	15250	treeCtrl1	Casos/Tipificaciones/Agregar tema / Temas	Utiliza el cursor para moverte hacia abajo o hacia arriba. Cuando encuentres el tema que buscas, haz clic para seleccionarlo, y oprime el botón "Seleccionar".  Puedes ingresar todos los temas que consideres relevantes. Si deseas cancelar la operación,  haz clic en "Cancelar"
15341	15001	staticText6	Actos/Información general/Actos registrados	Lista de los actos ya registrados en el caso activo. Están ordenados alfabéticamente por el nombre de la víctima, seguido de una diagonal (/) y el tipo de acto, también ordenado alfabéticamente. Ejemplo: "Barajas Garibo, Raúl / Agresiones físicas" y "Barajas Garibo, Raúl / Detención arbitraria o ilegal". Utiliza el cursor o la barra de desplazamiento para moverte hacia abajo o hacia arriba dentro de la lista. Cuando encuentres el acto que buscas, selecciónalo con doble clic para que quede activo y puedas modificarlo o agregar datos. Para ingresar un nuevo acto utiliza el botón "Agregar acto". 
15345	15001	delActo	Actos/Información general/Borrar acto	Haz clic aquí para borrar del sistema el acto seleccionado. Antes debes borrar todas las relaciones que tenga el acto, incluyendo los perpetradores y la normatividad. Si el acto aún tiene relaciones, cuando intentes borrarlo te aparecerá una alerta y el acto no será borrado
15348	15001	staticText39	Actos/Información general/Exportar acto	Despalomea "Exportar acto" si quieres que el acto activo no se exporte. Haz clic en la casilla para palomear o despalomear esta opción. 
15350	15001	btnTipodeacto	Actos/Información general/Tipo de acto o VDH / (+) signo de más	Haz clic aquí para modificar el tipo de acto o VDH. Recuerda que únicamente podrás seleccionar actos relacionados con los derechos que hayas ingresado en "Derechos afectados" en la "Tipificación" del caso
15354	15001	staticText41	Actos/Información general/Fecha final	Indicación de cuándo terminó este acto particular. Por ejemplo, la fecha cuando es liberada una persona que fue detenida arbitrariamente. Si el acto no está cerrado o no ha terminado, NO ingreses ninguna fecha. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15356	15001	BTNAgregarcaracrelevantes	Actos/Información general/Características relevantes / (+) signo de más	Haz clic aquí para agregar una característica de la persona, que pudo haber sido el motivo para su victimización. Ingresa más de una característica SÓLO en el caso de que exista claramente más de una característica relevante que motivó la victimización de la persona para el acto o VDH específico (no para el caso). Selecciona el término que represente la caracteristica más relevante. Por ejemplo, si se trata de un/a "Defensor/a de derechos humanos", no selecciones además "Activista social". Para sustituir una característica, seleccionala y haz clic en el signo de más (+) para seleccionar otra. Si deseas cancelar la operación,  haz clic en "Cancelar"
15769	15001	FALocalidad	Actos/Información general/Localización	Indicación de dónde ocurrió este acto: país, estado, municipio y localidad. Únicamente se puede ingresar una localización para cada acto. Las opciones de localización que aparecen aquí, son las que se registraron en el campo "Localización" de la pestaña "Datos generales" del caso. Para seleccionar la localización de este acto, haz clic en la flechita y selecciona la localización que buscas. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona una localización diferente. Para borrar una localización elegida, selecciona el espacio en blanco que aparece al inicio de la lista.
15408	15001	staticText11	Interven-ciones/Pantalla única/Intervenciones / Lista	Lista de las intervenciones ya registradas en el caso activo. Están ordenadas alfabéticamente por el tipo de intervención, seguido del nombre de la persona o entidad que inició o realizó la intervención, por ejemplo: "Denuncia penal / Barajas Garibo, Raúl". Para moverte dentro de la lista, utiliza el cursor o las barras de desplazamiento. Cuando encuentres la intervención que buscas, haz clic para seleccionarla. Una vez seleccionada, puedes modificar o agregar datos. Si quieres ingresar una nueva intervención, utiliza el botón "Agregar una intervención" 
15438	15001	LC6	Fuentes/Fuente personal/Caso [#]: Nombre del caso	Este es el caso que está activo para ingresar una nueva fuente personal, o para modificar datos ya registrados para esta fuente. Si quieres trabajar en otro caso, regresa a la pestaña "Datos generales" de "Casos" y selecciona un caso diferente
15439	15001	staticText22	Fuentes/Fuente personal/Fuentes de información / Lista	Lista en orden alfabético, de las fuentes personales registradas en el caso activo. Para moverte dentro de la lista , utiliza el cursor o las barras de desplazamiento. Cuando encuentres la fuente que buscas, haz clic para seleccionarla. Una vez seleccionada, puedes modificar o agregar datos. Si quieres ingresar una nueva fuente personal, utiliza el botón "Agregar fuente personal" 
15950	15708	btnRegresar	Casos/Datos generales/Búsqueda Exhaustiva/Regresar	Haz clic aquí una vez que hayas establecido las condiciones de tu búsqueda. En la pantalla Datos generales, haz clic en "Aplicar" para obtener los resultados de tu búsqueda.
15460	15001	staticText42	Fuentes/Fuente personal/Comentarios	Anotaciones internas del trabajo institucional en relación a la fuente personal, por ejemplo: información que falta, no está clara o es contradictoria; necesidad de volver a entrevistar a la misma fuente, o a otras personas para corroborar la información; cuestiones de seguridad para la persona que aportó información o sobre su presencia en la ratificación de denuncias, etc.  Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15464	15001	staticText43	Fuentes/Fuente documental/Documentos / Lista	Lista en orden alfabético de las fuentes documentales registradas en el caso activo. Para moverte dentro de la lista, utiliza el cursor o las barras de desplazamiento. Cuando encuentres el documento que buscas, haz clic para seleccionarlo. Una vez seleccionado, puedes modificar o agregar datos. Si quieres ingresar una nueva fuente documental, utiliza el botón "Agregar fuente documental" 
15798	15001	choicePubTipofechaconsulta	Fuentes/Fuente documental/Fecha de consulta	Fecha en que se consulta la fuente documental, especialmente en Internet. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día,  mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15524	15001	btnNuevaPersona	Personas todas/Datos generales/Nueva persona	Haz clic aquí para ingresar una nueva persona al sistema. Aparecerá una ventana en la que debes seleccionar si se trata de una persona individual o una entidad colectiva, e ingresar el nombre de la persona.
15527	15517	staticTextNombrePersona	Personas todas/Datos generales/Nueva persona / Datos una persona colectiva - Sigla y Nombre	En las casillas correspondientes ingresa la sigla y el nombre completo de la entidad o persona colectiva que estás registrando. Siempre que puedas, ingresa la sigla o acrónimo y el nombre de la manera más completa posible
15530	15001	btnInfoPersona	Personas todas/Datos generales/I (letra I)	Datos de la creación y actualización de este registro de persona. Se indica quién ingresó el registro la primera vez, así como la persona que hizo la última actualización. Al lado del nombre de cada persona aparece la fecha correspondiente a la creación y a la última actualización
15531	15001	staticText104	Personas todas/Datos generales/Exportar persona	Despalomea "Exportar persona" si quieres que la información de la persona activa, no se exporte. Si eliges no exportar a una persona, las entidades en las que tenga algún rol, tampoco se exportarán. Por ejemplo, si Juan Pérez tiene el rol de perpetrador y lo marcas como no exportable; el caso con el que se relaciona, se exportará sin ese dato de perpetrador. Haz clic en la casilla para palomear o despalomear esta opción. 
15532	15001	listPersonaVinculosDB	Personas todas/Datos generales/Casos relacionados con esta persona / Lista	Lista de los casos directamente relacionados con la persona activa. Están ordenados alfabéticamente por el nombre del caso, seguido de una diagonal (/) y el rol que tiene la persona en el caso, por ejemplo: Víctima o Fuente personal. Cuando encuentres el caso que buscas, haz doble clic sobre él para navegar de manera automática hacia el caso seleccionado. Desde la pantalla "Datos Generales" de "Casos" puedes regresar aqui haciendo clic en el botón "Pantalla anterior", que aparecerá en el lado superior derecho
15815	15515	Cpfechanac	Personas individual/Datos generales/Fecha de nacimiento	Fecha de nacimiento de esta persona. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15555	15516	CPMunicipio	Personas colectivas/Datos generales/Municipio de origen	Municipio del estado seleccionado arriba en donde se crea, funda o surge esta entidad, grupo o movimiento. Únicamente se puede ingresar un municipio de origen para cada entidad. Haz clic en la flechita para que aparezcan todos los municipios del estado seleccionado. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el municipio que buscas, haz clic para seleccionarlo, y el municipio aparecerá en el campo. Para borrar el municipio, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un municipio diferente.
15826	15516	FPEscolaridad	Personas colectivas/Datos generales/Nivel de escolaridad predominante	Indicación del nivel predominante de educación del grupo registrado, por ejemplo, "Normal" para los estudiantes de las Normales rurales. Únicamente se puede ingresar un término para cada grupo o entidad. Haz clic en la flechita para que aparezcan todos los niveles de escolaridad. Cuando encuentres el nivel que buscas, márcalo y el término aparecerá en el campo. Para borrar el nivel de escolaridad, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un nivel diferente.
15570	15515	btnAddOcupacion	Personas individual/Detalles/Ocupación / (+) signo de más	Haz clic aquí para seleccionar el término que mejor defina la ocupación, trabajo o actividad a la que se dedica esta persona. Únicamente se puede ingresar una ocupación para cada persona. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un término diferente
15590	15516	CPReligion	Personas colectivas/Detalles/Religión predominante	Religión que profesa la mayoría de las personas en el grupo. Únicamente se puede ingresar una religión para cada entidad o persona colectiva. Haz clic en la flechita para que aparezcan todas las religiones. Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres la religión que buscas, haz clic para seleccionarla, y la religión aparecerá en el campo. Para borrar la religión, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Religión católica". Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona una religión diferente
15844	15514	textCtrlCorreo	Personas todas/Detalles/Dirección(es) / Correo electrónico	Ingresa la dirección de correo electrónico. Puedes ingresar varias direcciones. Sólo podrás ingresar información después de haber seleccionado un "Tipo de dirección"
15847	15001	FPObservaciones	Personas todas/Información administrativa/Observaciones	Registra aquí cualquier información adicional sobre la persona que no esté ingresada en otros campos o como dato biográfico adicional a la persona. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15611	15001	CPArchivos	Personas todas/Información administrativa/Archivos	Indicación del archivo o archivos físicos o electrónicos en donde se puede encontrar la información y documentación sobre la persona, por ejemplo: número de expediente, ruta y nombre de archivo en la computadora, etc. También se debe indicar si existe y se puede obtener información en archivos de otra institución, sitio de Internet, etc. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15625	15513	treeCtrlVinculos	Personas todas/Datos biográficos/Agregar dato biográfico / Tipos de relaciones	En esta lista selecciona el término que mejor defina la relación que estás registrando, establecida desde la persona activa. Haz clic en los  signos de más (+) para abrir las listas. Cuando encuentres la relación que buscas, selecciónala y en el recuadro de la derecha, elige a la segunda persona en esta relación. Por ejemplo, el tipo de relación para Ildefonso Zamora debe ser "Padre / Madre" con respecto a Aldo Zamora que es su hijo.
15626	15513	staticText1	Personas todas/Datos biográficos/Agregar dato biográfico / Con qué persona o entidad se relaciona	En esta ventana selecciona a la segunda persona en esta relación, por ejemplo a Aldo Zamora como hijo de Ildefonso Zamora. En el casillero vacío ubicado al lado de "Nueva persona" puedes hacer una búsqueda rápida escribiendo el nombre de la persona. Si la persona no está registrada, puedes ingresarla haciendo clic en el botón "Nueva persona". Una vez que selecciones a la persona, asegúrate de haber establecido el tipo de relación que la vincula a la persona activa y haz clic en el botón "Seleccionar".
15651	15650	strCasosSeleccionados	Casos/Datos generales/Reportes/Emisión de reportes / Reporte narrativo de casos visibles 	Este es un reporte de control y contiene toda la información capturada en todos los casos que se encuentran visibles en la ventana de "Lista de Casos". Si realizaste una búsqueda, se creará un reporte con los casos resultado de tu búsqueda (casos visibles). Si no has realizado ninguna búsqueda, se creará un reporte con TODOS los casos que tengas en tu sistema. Los casos también contendrán la información administrativa de cada uno. Para generar el reporte, haz clic en el ícono que aparece a un lado. También puedes hacer clic en el botón de "Opciones" para seleccionar los campos que quieres que aparezcan o se omitan en tu reporte.
15652	15650	staticText10	Casos/Datos generales/Reportes/Emisión de reportes / Reporte narrativo de caso activo 	Este es un reporte de control que contiene toda la información capturada  del caso seleccionado ("caso activo") en la pantalla de Casos/Datos Generales.También incluye la información administrativa del caso. Para generar el reporte, haz clic en el ícono que aparece a un lado. Puedes también hacer clic en el botón de opciones para seleccionar los campos que quieres que aparezcan o se omitan en tu reporte.
15883	15685	treeCtrl1	Actos/Normatividad/Legislación nacional / Selección Legislación nacional	Selecciona el tipo de legislación que aplique a este acto. Haz clic en los signos de más (+) para abrir las listas de tipos de legislación. Cuando encuentres la que buscas, selecciónala y haz clic en el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Puedes ingresar toda la legislación relevante para este acto o VDH.
15889	15691	personaIsearch	Intervenciones/Pantalla única/Agregar una intervención / Selección de Quién inicia o realiza esta intervención	Busca el nombre de la persona que inicia o realiza esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15900	15695	personaIsearch	Intervenciones/Pantalla única/A quién se le dirigió esta intervención / Selección de A quién se le dirigió esta intervención	Busca el nombre de la persona a quien se le dirigió esta intervención, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15912	15701	staticText1	Fuentes/Fuente documental/Agregar fuente documental / Ingreso de Identificación	Ingresa una breve descripción (aprox. 15-20 palabras) que te permita identificar claramente el documento. Al terminar haz clic en "Seleccionar". Puedes cancelar el ingreso haciendo clic en "Cancelar". La identificación aparecerá en los campos de registro de Documentos e Identificación. 
15917	15703	personaIsearch	Fuentes/Fuente documental/Sobre quien se aporta la información / Selección de Sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones de la izquierda. También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15929	15709	ctrlCampo	Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición / Selección de Condición	En esta ventana aparece la lista de todas las condiciones de búsqueda del sistema. Haz clic en la condición que desees agregar a tu búsqueda y oprime el botón "Seleccionar". Una vez que selecciones la condición, podrás elegir el término preciso, la fecha, el usuario, etc. que deseas buscar. Sólo puedes seleccionar una condición de búsqueda a la vez, cada vez que agregues una condición nueva, debes entrar a esta ventana y repetir la operación. Al inicio de la lista de campos, aparecen las condiciones "O bien" "Y también". Selecciona "O bien..." para ampliar tu búsqueda con una nueva condición a otra(s) que hayas seleccionado previamente (El resultado serán los casos/personas que cumplan la condición A ó la Condición B). Selecciona "Y también..." para reducir tu búsqueda a los registros que cumplan con la condición que hayas seleccionado anteriormente y la nueva condición (El resultado serán los casos/personas que cumplan con la condicion A y además la Condición B).
15948	15708	delCond	Casos/Datos generales/Búsqueda Exhaustiva/Borrar una condición	Haz clic aquí para borrar una condición. Previamente, selecciona de la ventana la condición que deseas borrar. 
15949	15708	delAll	Casos/Datos generales/Búsqueda Exhaustiva/Borrar todas	Haz clic aquí para borrar todas las condiciones que se encuentren en la ventana.
15952	15650	staticText4	Casos/Datos generales/Reportes/Responsables involucrados en violaciones a los derechos humanos	Este es un reporte que muestra a los responsables de cometer actos o VDHs según el tipo de perpetrador, por ejemplo, si se trata de una "Entidad estatal", una "Empresa privada nacional", "Personas no identificadas", etc. Para generar el reporte haz clic en el ícono que aparece a un lado
15953	15650	staticText5	Casos/Datos generales/Reportes/Tipo de acto vs Características relevantes	Este es un reporte que muestra una tabla con las características relevantes de las víctimas en relación a los actos o VDHs cometidos, por ejemplo, el tipo de actos cometidos a las víctimas cuya característica relevante es ser "Defensor(a) de los derechos humanos". Para generar el reporte haz clic en el ícono que aparece a un lado
15954	15650	staticText3	Casos/Datos generales/Reportes/Personas y entidades responsables de violaciones de DH	Este es un reporte que muestra el total de personas y entidades responsables de cometer actos o VDHs. En este reporte aparecen los nombres exactos de cada perpetrador, por ejemplo, "Policía Estatal Preventiva de Campeche", "Samuel Salgado", "Comisión de Derechos Humanos del estado de Hidalgo", etc. Para generar el reporte haz clic en el ícono que aparece a un lado
15969	15000	Prelacionada	Prelacionada	
15507	15001	FRCCasoRelObservaciones	Casos/Relaciones/Observaciones	Información adicional o explicación sobre la forma en que se relacionan los casos entre sí. Por ejemplo, puedes ingresar una breve explicación de la causa y efecto entre los dos casos.   La información que registres aquí, corresponderá a la relación que está activa. Para activar una relación, haz doble clic en el caso relacionado que aparece en el recuadro de arriba.
15415	15001	staticText16	Interven-ciones/Pantalla única/Tipo de intervención	El tipo más representativo de esta intervención, por ejemplo: "Denuncia pública", "Acción urgente", "Denuncia penal", "Litigio internacional".  Únicamente se puede ingresar un tipo para cada intervención
15765	15001	listBoxPerpetradores	Actos/Información general/Perpetradores	Lista de los perpetradores ya registrados en el acto activo. Están ordenados alfabéticamente por su  nombre. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro de la lista. Cuando encuentres el perpetrador que buscas, haz doble clic para seleccionarlo. Una vez seleccionado, puedes modificar o agregar datos. Si quieres ingresar un nuevo perpetrador, utiliza el botón "Agregar un perpetrador". 
15787	15255	personaIsearch	Fuentes/Fuente personal/Agregar fuente personal / Seleccionar una persona	Busca el nombre de la fuente personal, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15724	15001	staticText2	Casos/Datos generales/Localización	Lista de los lugares donde ocurrieron los hechos que se incluyen en este caso: país, estado, municipio y localidad. Si los hechos ocurrieron en diferentes lugares, deben aparecer todos aquí, por ejemplo: si la detención ocurre en Puebla pero presentan al detenido en el D.F. y luego lo encarcelan en Jalisco, deben aparecer los tres lugares. Para moverte dentro de la lista hacia abajo o hacia arriba, o hacia la derecha o la izquierda, utiliza el cursor o las barras de desplazamiento. Cuando hay notas aclaratorias, verás un asterisco (*) al lado del país. Haz clic en la fila de ese dato y aparecerá el botón "Más información". Haz clic ahí y podrás leer las notas aclaratorias
15962	15000	getTaxonomyTreeCaracRelevante	getTaxonomyTreeCaracRelevante	
15964	15000	getTaxonomyTreeTipodeFuente	getTaxonomyTreeTipodeFuente	
15965	15000	getTaxonomyTreeTipoPersonaCol	getTaxonomyTreeTipoPersonaCol	
15501	15001	staticText34	Casos/Información narrativa/Descripción narrativa	Descripción general de los hechos. Debe proporcionar toda la información relevante de dónde, cuándo y cómo ocurrieron los hechos, así como sobre las víctimas, los presuntos responsables, y cuál fue el papel de las autoridades en caso de que hayan intervenido. La descripción puede ser breve y concisa, o puede ser extensa y redactada para que sirva como comunicado de prensa, acción urgente, etc. No hay un "límite" de espacio aquí pero es importante que el texto describa de la manera más clara y exacta posible el caso en su conjunto. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15966	15962	treeCtrl1	Actos/Información general/Características relevantes / Selección de Características relevantes	Haz clic en los signos de más (+) para abrir las listas de Características relevantes. Cuando encuentres la que  buscas, selecciónala y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar".
15968	15965	treeCtrl1	Personas colectivas/Datos generales/Tipo de grupo / Selección de Tipo de grupo	Haz clic en el término que mejor defina a la entidad o grupo que estás registrando y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un tipo de grupo por cada entidad o grupo.
15970	15969		Personas Todas/Datos biográficos/P. relacionada / Selección de Persona relacionada	Busca el nombre de la persona o entidad que se relaciona con la persona activa. Puedes buscar en todas las personas registradas, o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la víctima que quieras ingresar y oprime el botón "Seleccionar". 
15955	15650	staticText14	Casos/Datos generales/Reportes/Violaciones a los derechos humanos	Este es un reporte que muestra el total de actos/VDHs que han sido registrados en el sistema. Para generar el reporte haz clic en el ícono que aparece a un lado.
15960	15650	btnReporteActos	Casos/Datos generales/Reportes/Botón de impresora  / Violaciones a los derechos humanos	Haz clic aquí para generar el listado de Violaciones a los derechos humanos
15961	15650	btnListadodepersonas	Casos/Datos generales/Reportes/Botón de impresora  / Listado de Personas	Haz clic aquí para generar el listado de personas
15957	15650	btnPrin5	Casos/Datos generales/Reportes/Botón de impresora  / Responsables involucrados en violaciones a los derechos humanos	Haz clic aquí para generar el reporte de los responsables involucrados  en violaciones a los derechos humanos según el "Tipo de perpetrador"
15958	15650	bitmapButton3	Casos/Datos generales/Reportes/Botón de impresora  / Tipo de acto vs Características relevantes	Haz clic aquí para generar el reporte de Tipo de acto vs Características relevantes
15799	15001	textCtrlPubObservaciones	Fuentes/Fuente documental/Observaciones	Registra aquí cualquier información adicional sobre la fuente documental de donde se tomó la información sobre el caso. Si es relevante, indica sobre qué o quién proporcionó información esta fuente. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15825	15515	FPEscolaridad	Personas individual/Datos generales/Escolaridad	Indicación del nivel más alto de escolaridad que tiene esta persona. Únicamente se puede ingresar un término para cada persona. Haz clic en la flechita para que aparezcan todos los niveles de escolaridad. Cuando encuentres el nivel que buscas, márcalo y el término aparecerá en el campo. Para borrar un dato registrado, ingresa al campo y selecciona la línea en blanco que aparece al inicio de la lista. Si ya hay un dato registrado y lo quieres sustituir, haz clic aquí y selecciona un nivel diferente.
15897	15694	personaIsearch	Intervenciones/Pantalla única/Sobre quien se interviene / Selección de Sobre quien se interviene	Busca el nombre de la persona sobre quien se interviene, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15967	15964	treeCtrl1	Fuentes/Fuente documental/Tipo de fuente / Selección de Tipo de fuente	Haz clic en los signos de más (+) para abrir las listas de Fuente de información. Cuando encuentres el tipo de fuente que buscas, selecciónalo y oprime el botón "Seleccionar". Si deseas cancelar la operación, haz clic en "Cancelar". Únicamente se puede ingresar un tipo de fuente para cada registro. 
15944	15713	FN	Casos/Datos generales/Reportes/Opciones  / Selección de Opciones de impresión	Aquí aparecen TODOS los campos e información administrativa contenida en un caso, seleccionados (palomeados) por omisión. Lo que significa que por omisión generarás un reporte con todos los campos en los que has capturado información. Si lo que deseas es evitar que tu reporte contenga alguno de estos campos, lo que debes hacer es "despalomearlo". Puedes "despalomear" uno o más campos o toda una sección. Los nombres de las secciones son: Localización detallada, Actos, Intervenciones, Fuente personal, Fuente documental y Personas relacionadas con el caso. Para quitar de tu reporte el contenido de una sección completa, despalomea su nombre en la pantalla principal. Para ver el contenido de cada sección, haz clic en la pestaña con su mismo nombre, ubicada en la parte superior de la ventana. Los términos que se encuentran en letra mayúscula, no son campos sino títulos que aparecerán en tu reporte antes de la información correspondiente. Si no quieres que aparezcan esos títulos, debes despalomearlos.
15971	15000	dlgperFtePersonaRelacionada	dlgperFtePersonaRelacionada	
15972	15000	getTaxTreeFteLengua	getTaxTreeFteLengua	
15973	15000	getTaxonomyTreeFteLengua	getTaxonomyTreeFteLengua	
15974	15971	personaIsearch	Fuentes/Fuente personal/Persona sobre quien se aporta información / Selección de Persona sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15975	15971	radioBoxTipoPersona	Fuentes/Fuente personal/Persona sobre quien se aporta información / Selección de Persona sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15976	15971	listBoxPersona	Fuentes/Fuente personal/Persona sobre quien se aporta información / Selección de Persona sobre quien se aporta información	Busca el nombre de la persona sobre quien se aporta la información, en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Haz clic en el nombre de la persona que quieras ingresar y oprime el botón "Seleccionar".
15977	15972	treeCtrl1	Fuentes/Fuente personal/Lengua indígena / Selección de Lengua indígena	Haz clic en la lengua indígena que buscas y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Únicamente se puede ingresar una lengua indígena  para cada fuente.
15978	15973	treeCtrl1	Fuentes/Fuente documental/Lengua indígena / Selección de Lengua Indígena	Haz clic en el término que  buscas y oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar". Únicamente se puede ingresar una lengua indígena por  cada fuente.
15956	15650	txtListadodepersonas	Casos/Datos generales/Reportes/Listado de Personas	Este es un reporte que muestra un listado de las personas capturadas en el sistema. Para generar el listado haz clic en el ícono que aparece a un lado. Contiene el nombre de la persona, la ocupación o actividad, los roles que desempeña en los casos registrados, y para las entidades presenta el Tipo de grupo y su descripción. 
16001	15516	FPTipodefecha	Personas colectivas/Datos generales/Fecha de creación	Fecha de creación, fundación o surgimiento de esta entidad, grupo o movimiento. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15979	15001	textCtrlCAArchivos	Casos/Información administrativa/Archivos	Indicación del archivo o archivos físicos o electrónicos en donde se puede encontrar la información y documentación sobre el caso, por ejemplo: número de expediente, ruta y nombre de archivo en la computadora, etc. También se debe indicar si existe y se puede obtener información en archivos de otra institución, sitio de Internet, etc. Para moverte dentro del texto, utiliza el ratón para desplazar hacia arriba o hacia abajo la barra que aparece al lado derecho. Puedes hacer "recorte y pegote" desde tu procesador de texto, hoja de cálculo, correo-electrónico, etc., o desde otro campo del SMDH
15980	15001	btnCasoRel	Casos/Relaciones/Caso relacionado	Este es el caso que se relaciona con el caso activo. Si quieres cambiar el caso relacionado, haz clic en el signo de más (+) y selecciona un caso diferente. Si en el recuadro de arriba "Relacionado con", hay más de un caso registrado, haz doble clic en el que quieras modificar o agregar observaciones y comentarios.
15981	15001	listBoxDerechosafectados	Casos/Tipificaciones/Derechos afectados	Lista en orden alfabético de todos los derechos que están afectados por los hechos que ocurren en este caso. Para moverte dentro de la lista, utiliza el cursor y las barras de desplazamiento. Para registrar un nuevo derecho, oprime el botón "Agregar derecho"
15982	15001	choiceTipoEdad	Actos/Información general/Edad cuando ocurrió el acto	Edad de la víctima cuando ocurrió el acto. Primero selecciona si la edad es precisa o aproximada y luego ingresa la edad de la víctima. Para borrar esta información, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba.
15983	15253		Actos/Perpetradores/Agregar un perpetrador / Seleccionar una persona	Busca el nombre del perpetrador en la lista de personas que ya están registradas en el sistema. Puedes buscar en todas las personas, o únicamente en las individuales o las colectivas marcando el término correspondiente en las opciones del recuadro "Mostrar". También puedes escribir en el casillero vacío las letras del nombre que buscas, si el nombre no existe, regístralo haciendo clic en el botón "Nueva persona" que aparecerá cuando escribas la tercer letra. Selecciona el nombre de la persona que quieras ingresar y haz clic en el botón "Seleccionar".
15984	15650	btnSaveCfgAs	Casos/Datos generales/Reportes/Guardar modelo como 	Si generaste un reporte eliminando (despalomeando) campos en el botón de "Opciones", has generado también un modelo de impresión que puedes guardar para, posteriormente, hacer otros reportes con las mismas opciones. Haz clic en la flechita para ver la lista de Modelos de impresión que hayas guardado anteriormente.
15986	15001	choicePubIdioma	Fuentes/Fuente documental/Idioma	Idioma en el cual está el documento. Haz clic en la flechita  para que aparezca la lista de idiomas.  Utiliza el cursor para moverte hacia abajo o arriba. Cuando encuentres el idioma que buscas, haz clic para seleccionarlo, y aparecerá en  el campo. Para borrar el idioma, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Alemán". Únicamente se puede ingresar un idioma para cada fuente
15987	15001	choiceFteIdioma	Fuentes/Fuente personal/Idioma	Idioma en el cual está la información proporcionada por la fuente, por ejemplo el audio o transcripción de una entrevista o testimonio. Haz clic en la flechita para que aparezca la lista de idiomas. Cuando encuentres el idioma que buscas, selecciónalo y aparecerá en  el campo. Para borrar el idioma, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba. Únicamente se puede ingresar un idioma para cada fuente.
15993	15001	MP0	Personas todas/Datos generales/Mostrar	Palomea una de las casillas que aparecen en el recuadro para acotar el despliegue de personas registradas en el sistema. Pueden aparecer únicamente las "PERSONAS INDIVIDUALES", las "ENTIDADES COLECTIVAS" o las "PERSONAS DIRECTAMENTE RELACIONADAS CON EL CASO" activo. Puedes palomear "TODAS" si quieres que aparezca la lista completa de registros.
15994	15001	MP2	Personas todas/Datos generales/Mostrar	Palomea una de las casillas que aparecen en el recuadro para acotar el despliegue de personas registradas en el sistema. Pueden aparecer únicamente las "PERSONAS INDIVIDUALES", las "ENTIDADES COLECTIVAS" o las "PERSONAS DIRECTAMENTE RELACIONADAS CON EL CASO" activo. Puedes palomear "TODAS" si quieres que aparezca la lista completa de registros.
15995	15001	MP3	Personas todas/Datos generales/Mostrar	Palomea una de las casillas que aparecen en el recuadro para acotar el despliegue de personas registradas en el sistema. Pueden aparecer únicamente las "PERSONAS INDIVIDUALES", las "ENTIDADES COLECTIVAS" o las "PERSONAS DIRECTAMENTE RELACIONADAS CON EL CASO" activo. Puedes palomear "TODAS" si quieres que aparezca la lista completa de registros.
15996	15001	MP4	Personas todas/Datos generales/Mostrar	Palomea una de las casillas que aparecen en el recuadro para acotar el despliegue de personas registradas en el sistema. Pueden aparecer únicamente las "PERSONAS INDIVIDUALES", las "ENTIDADES COLECTIVAS" o las "PERSONAS DIRECTAMENTE RELACIONADAS CON EL CASO" activo. Puedes palomear "TODAS" si quieres que aparezca la lista completa de registros.
15997	15515	FPTipodefecha	Personas individual/Datos generales/Fecha de nacimiento	Fecha de nacimiento de esta persona. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15998	15515	PFNdia	Personas individual/Datos generales/Fecha de nacimiento	Fecha de nacimiento de esta persona. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
15999	15515	PFNmes	Personas individual/Datos generales/Fecha de nacimiento	Fecha de nacimiento de esta persona. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
16000	15515	PFNanio	Personas individual/Datos generales/Fecha de nacimiento	Fecha de nacimiento de esta persona. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
11890	11884	001025060030	Violaciones al derecho a interponer recursos internacionales por VDH y VDI	"VDH": Violaciones a los derechos humanos. "VDI": Violación al derecho internacional
16002	15516	PFNdia	Personas colectivas/Datos generales/Fecha de creación	Fecha de creación, fundación o surgimiento de esta entidad, grupo o movimiento. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
16003	15516	PFNmes	Personas colectivas/Datos generales/Fecha de creación	Fecha de creación, fundación o surgimiento de esta entidad, grupo o movimiento. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
16004	15516	PFNanio	Personas colectivas/Datos generales/Fecha de creación	Fecha de creación, fundación o surgimiento de esta entidad, grupo o movimiento. Selecciona primero el tipo de fecha, y luego ingresa los datos que conozcas en orden de día, mes y año. Selecciona "Fecha aproximada" cuando conozcas la fecha con una aproximación de 3 días anteriores o posteriores. Para borrar la fecha, ingresa al campo y selecciona la línea en blanco que aparece hasta arriba, antes de "Fecha exacta"
16005	15650	casoOpcionesVisibles	Casos/Datos generales/Reportes/Opciones 	Haz clic aquí para abrir la ventana de Opciones y generar un modelo de reporte. Podrás seleccionar los campos que desees eliminar de tu reporte. 
16006	15650	CasoOpcionesActivo	Casos/Datos generales/Reportes/Opciones 	Haz clic aquí para abrir la ventana de Opciones y generar un modelo de reporte. Podrás seleccionar los campos que desees eliminar de tu reporte. 
62	127	084	Ku’ahl	Baja California, Ensenada, comunidad indígena de Santa Catarina, El Aguajito (Mat Chip) [Rancho Matchip], Rancho Escondido, Rancho Wikualpuk (El Ranchito)
11661	123	005	Muy confiable	Se aplica: cuando a) la información de varias fuentes coincide; b) la información aporta evidencias y/o pruebas materiales o documentales que sustentan el caso; c) en los documentos hay consistencia dentro del contexto político social; d) hay eventos similares, ya sea recientes en el tiempo o por modus operandi (FRAYBA)
11709	154	065	Damnificado(a)	
14077	14067	065250	Jurisprudencia sobre discriminación	
11399	11397	010005005	Empresa privada transnacional	Ej.: Wal-Mart
12532	161	004003	Inactividad en términos de la aplicación de la ley o la implementación de la política que proteja o garantice los derechos humanos	Se refiere a la falta de actuación de los funcionarios públicos de acuerdo a lo establecido en reglamentos, leyes o  políticas públicas que protejan o garanticen derechos humanos.  Ej. La no investigación de acuerdo a la ley
11492	11490	006	Grupo, institución privada, organización o movimiento social	Usar para todos los siguientes: 1) entidades colectivas privadas como asociaciones civiles, ONG, fundaciones, etc.; 2) organizaciones y movimientos sociales (por ejemplo: campesinos, cooperativistas, estudiantiles, obreros, patronales, profesionales, de trabajadores y de liberación nacional); 3) empresas privadas con fines de lucro, etc.; 4) grupos de interés o de presión. Ejemplos para los cuales aplica este tipo de grupo: Activistas del Nivel de Educación Indígena; Alianza Mexicana por la Autodeterminación de los Pueblos (AMAP); Asamblea Permanente de Ejidatarios y Trabajadores del Carrizalillo; Federación Internacional de Derechos Humanos (FIDH); Grupo Televisa, S.A. de C.V. (Televisa); La Otra Campaña (La Otra); Centro de Derechos Indígenas Flor y Canto; Organización para el Futuro del Pueblo Mixteco (OFPM); Partido Acción Nacional (PAN); Sindicato Nacional de Trabajadores de la Educación - Sección 23 Puebla (SNTE 23 Puebla)
15586	15516	CPOrigenEtnico	Personas colectivas/Detalles/Origen étnico predominante	Origen étnico o pueblo indígena al que pertenecen la mayoría de las personas en el grupo. Se puede ingresar varios términos para cada entidad o persona colectiva, por ejemplo si en un grupo de desplazados internos hay personas que pertenecen a varios pueblos indígenas. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15892	15714	treeCtrl1	Intervenciones/Pantalla única/Agregar una intervención / Selección de Tipo de intervención	Haz clic en los signos de más (+) para abrir las listas. Cuando encuentres la intervención que buscas, selecciónala y oprime el botón "Seleccionar". Puedes cancelar el registro oprimiendo el botón "Cancelar". 
15923	15716	treeCtrl1	Personas todas/Detalles/Ocupación /Ocupación predominante / Selección de Ocupación 	Haz clic en los signos de más (+) para abrir las listas de ocupaciones. Busca en la lista de Ocupación, si es una persona individual, o en la de Actividad, si es una persona colectiva. Haz clic en la ocupación o actividad que buscas, oprime el botón "Seleccionar". Si deseas cancelar la operación,  haz clic en "Cancelar".
15946	15650	staticText6	Casos/Datos generales/Reportes/Archivo a generar	El reporte se genera por omisión con el nombre de 'salida' y se guarda en la carpeta "archivos" del SMDH, cada reporte que generes con ese nombre, sustituirá al anterior.  Puedes ingresar aquí un nombre distinto que no tenga espacios, ñ o números, usa el guión bajo para separar palabras. O bien, cuando abras tu reporte, renómbralo y guardarlo en la carpeta que desees (el formato será acorde con la aplicación que hayas usado para abrirlo)
15959	15650	bitmapButton2	Casos/Datos generales/Reportes/Botón de impresora  / Personas y entidades responsables de violaciones de DH	Haz clic aquí para generar el reporte de Personas y entidades responsables de violaciones de DH
15585	15515	CPOrigenEtnico	Personas individual/Detalles/Origen étnico	Origen étnico o pueblo indígena al que pertenece esta persona. Se puede ingresar varios términos para cada persona. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15832	15516	FPOrigenEtnico	Personas colectivas/Detalles/Origen étnico predominante	Origen étnico o pueblo indígena al que pertenecen la mayoría de las personas en el grupo. Se puede ingresar varios términos para cada entidad o persona colectiva, por ejemplo si en un grupo de desplazados internos hay personas que pertenecen a varios pueblos indígenas. Utiliza el cursor para moverte hacia abajo o hacia arriba dentro la lista.
15639	15001	staticText82	Personas todas/Datos biográficos/Observaciones	Registra aquí cualquier información adicional o explicación sobre el dato biográfico de la persona. Si el dato biográfico es la relación de la persona activa con otra persona, puedes ingresar información detallada sobre el tipo de relación. Tus notas también se guardarán en la ficha de la persona relacionada.
15864	15001	FBObservaciones	Personas todas/Datos biográficos/Observaciones	Registra aquí cualquier información adicional o explicación sobre el dato biográfico de la persona. Si el dato biográfico es la relación de la persona activa con otra persona, puedes ingresar información detallada sobre el tipo de relación. Tus notas también se guardarán en la ficha de la persona relacionada.
15641	15001	staticText91	Personas todas/Datos biográficos/Comentarios	Anotaciones internas del trabajo institucional sobre el dato biográfico, por ejemplo: información que falta, que no está clara o que es contradictoria; la fuente particular de donde se obtuvo el dato biográfico; pistas para mayor investigación; opiniones o información no corroborada; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Las notas también se guardarán en la ficha de la persona relacionada.
15865	15001	FBComentarios	Personas todas/Datos biográficos/Comentarios	Anotaciones internas del trabajo institucional sobre el dato biográfico, por ejemplo: información que falta, que no está clara o que es contradictoria; la fuente particular de donde se obtuvo el dato biográfico; pistas para mayor investigación; opiniones o información no corroborada; etc. Es recomendable que se ingrese la información de manera clara y resumida, y que el campo se actualice conforme se resuelven las cosas anotadas. Las notas también se guardarán en la ficha de la persona relacionada.
15947	15712		Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición / Selección de Fecha	Selecciona la fecha que quieres incluir como condición en orden día, mes y año. Si es una fecha exacta, pon dicha fecha en ambos campos. Si es un periodo de tiempo, especifíca entre qué fecha y qué fecha deseas hacer tu búsqueda. Palomea la casilla de "invertir condición" si deseas encontrar todos los registros, EXCEPTO los que tengan el periodo de tiempo que seleccionaste. Palomea "sin fecha" para encontar estos registros. Para terminar la operación oprime el botón "Seleccionar"
3	15516	FPAddLengua	Personas colectivas/Detalles/Lengua predominante / (+) signo de más	Haz clic aquí para agregar una lengua indígena. Si ya hay una lengua indígena registrada y quieres agregar otra, haz clic aquí y selecciónala. Las lenguas indígenas que selecciones aparecerán en la ventana de al lado.
4	15516	delLengua	Personas colectivas/Detalles/Lengua predominante / (x) signo de multiplicación	Haz clic aquí para borrar la lengua que está seleccionada en la ventana de al lado
7	15515	FPAddOrigenEtnico	Personas individual/Detalles/Origen étnico / (+) signo de más	Haz clic aquí para agregar el origen étnico de la persona. El término aparecerá en la ventana de al lado. Si ya hay un orígen étnico registrado y quieres agregar otro, haz clic aquí y selecciónalo. Los términos que selecciones aparecerán en la ventana de al lado.
8	15515	delOrigen	Personas individual/Detalles/Origen étnico / (x) signo de multiplicación	Haz clic aquí para borrar el origen étnico que está seleccionado en la ventana de al lado
16007	15000	CondicionExportar	Condicion Exportar	
16012	16007	checkBox1	Casos/Datos generales/Búsqueda Exhaustiva/Agregar condición / Selección de Exportar	Palomea la casilla de exportar, para buscar todos los registros marcados como exportables. Si deseas buscar los registros marcados como NO exportables, sólo haz clic en "Seleccionar", sin palomear la casilla
16013	15711		Casos/Datos generales/Búsqueda Exhaustiva/Agregar Condición / Selección de Usuario	Haz clic en el usuario que quieres agregar como condición a la búsqueda. Palomea la casilla de "invertir condición" si deseas encontrar todos los registros, EXCEPTO los creados o actualizados por el usuario que hayas seleccionado. Para terminar la operación oprime el botón "Seleccionar".
16014	16007		Casos/Datos generales/Búsqueda Exhaustiva/Agregar condición / Selección de Exportar	Palomea la casilla de exportar, para buscar todos los registros marcados como exportables. Si deseas buscar los registros marcados como NO exportables, sólo haz clic en "Seleccionar", sin palomear la casilla
16015	15650	staticText15	Casos/Datos generales/Reportes/Listado de Personas	Este es un reporte que muestra un listado de las personas capturadas en el sistema. Para generar el listado haz clic en el ícono que aparece a un lado. Contiene el nombre de la persona, la ocupación o actividad, los roles que desempeña en los casos registrados, y para las entidades presenta el Tipo de grupo y su descripción. 
16016	15650	btnPersonas	Casos/Datos generales/Reportes/Botón de impresora  / Listado de Personas	Haz clic aquí para generar el listado de personas
16017	15000	getTaxonomyTreeTipodeActo	Tipo de acto	
16018	16017	treeCtrl1	Actos/Información general/Tipo de acto o VDH / VDH Selección de Tipo de acto o VDH	Haz clic en los signos de más (+) para abrir las listas. Selecciona un término y oprime el botón "Seleccionar". El tipo de acto o VDH seleccionado sustituirá al ya existente.
15927	15622		Casos/Datos generales/Reportes/Opciones  / Selección de Opciones de impresión	
10285	8031	001005	Jesús María	
10193	8035	005020	Múzquiz	
9309	8016	010033	Súchil	
9064	8018	012013	Azoyú	
8099	8020	014048	Jesús María	
9722	8034	020191	San Juan Chicomezúchil	
9976	8034	020445	Santa María Yosoyúa	
8262	8033	021085	Izúcar de Matamoros	
8705	8032	026053	San Felipe de Jesús	
10382	8026	030091	Jesús Carranza	
8439	8027	031011	Celestún	
8528	8027	031100	Ucú	
9671	8034	020140	San Francisco Chindúa	
9903	8034	020372	Santa Catarina Yosonotú	
10257	8040	029037	Ziltlaltépec de Trinidad Sánchez Santos	
16051	8014	023009	Tulum	
90	53	030	Agua	Asigna también el tema "Recursos naturales" que aparece en esta misma lista. Para otros recursos naturales, usa dicha categoría
14301	53	035	Arraigo	Medida cautelar que durante la averiguación previa se impone con vigilancia de la autoridad al indiciado, en razón de la investigación de un hecho delictivo
12416	53	040	Autonomía	Comprende fundamentalmente lo relacionado con la autonomía indígena. Cuando sea este el caso, asigna también el tema "Pueblos indígenas" que aparece en esta misma lista
14304	53	046	Censura	Se entiende por el poder que ejerce el Estado, persona o grupo influyente, para limitar o controlar la libertad de expresión, especialmente en aquellos casos en los cuales se postule una opinión contraria al orden establecido
14305	53	065	Comunicadores(a)s sociales	Comprende toda persona que trabaje de manera profesional o voluntaria en cualquier medio de comunicación
12437	53	090	Crímenes del pasado	Comprende los crímenes cometidos por el Estado en la llamada "Guerra Sucia" desde finales de los 60's hasta principios de los 80's
14307	53	115	Delincuencia común	Es la delincuencia más ordinaria y comprende delitos cometidos por una o dos personas, sin mucha planeación y que no pretende operar a gran escala. Comprende todo tipo de delincuencia excepto "Delincuencia organizada"
207	53	200	Delincuencia organizada	Por grupo delictivo organizado se entenderá un grupo estructurado de tres o más personas que exista durante cierto tiempo y que actúe concertadamente con el propósito de cometer uno o más delitos graves (...) con miras a obtener, directa o indirectamente, un beneficio económico u otro beneficio de orden material (Convención de Palermo). Sus características son: uso de la fuerza o violencia y uso de la corrupción para aumentar la impunidad en su favor. Si el caso tiene que ver con narcotráfico, trata de personas o tráfico de personas, asigna también una de esas categorías incluidas en esta misma lista.
198	53	130	Discriminación	Incluye todo tipo de discriminación. Asigna también otros temas para especificar la discriminación, ej.: para casos de discriminación cultural, educativa, por género, preferencia sexual, por ser indígena, persona con discapacidad o paciente con VIH/SIDA, puedes asignar: "Discriminación" más otro tema de la misma lista como "Cultura", "Educación", "LGBT", "Personas con discapacidad", "Pueblos indígenas", "VIH/SIDA", etc.
199	53	150	Elecciones	Comprende todo lo relativo a procesos electorales, incluyendo precampañas.
14310	53	155	Empleo, desempleo	No incluye condiciones laborales, para registrar este tema utiliza la categoría "Laborales" que aparece en esta misma lista
202	53	160	Empresas públicas	Comprende toda empresa con participación mayoritaría del Estado. Pueden ser: a) Centralizadas.- Sus organismos se integran en una jerarquía que encabeza directamente el Presidente de la República, ej.: las secretarías de estado, Nacional Financiera (Nafinsa); b) Desconcentradas.- Tienen determinadas facultades de decisión limitada, que manejan su autonomía y presupuesto, pero sin que deje de existir su nexo de jerarquía. ej.: INBA;  c) Descentralizadas.- En las que se desarrollan actividades que competen al estado y que son de interés general, pero que están dotadas de personalidad, patrimonio y régimen jurídico propio. ej.: IMSS, CFE, PEMEX, Banco de México; d) Estatales.- Pertenecen íntegramente al estado, ej.: Ferrocarriles, DIF; e) Mixtas y Paraestatales.- Existe la coparticipación del estado y los particulares para producir bienes y servicios. Su objetivo es que el estado tienda a ser el único propietario tanto del capital como de los servicios de la empresa. Ej.: Aeropuertos y Servicios Auxiliares, Capufe.
204	53	190	Feminicidio	Homicidios de mujeres por el hecho de ser tales en un contexto social y cultural que las ubica en posiciones, roles o funciones subordinadas, contexto que, por tanto, favorece y las expone a multiples formas de violencia (Toledo Vásquez)
240	53	380	Organismos internacionales	Comprende la ONU, OEA, OIT, FMI, OMS, UNICEF, OMC, etc.
255	53	410	Penitenciario	Comprende las condiciones  de detención y régimen de sanciones al que se ven sometidas tanto las personas detenidas durante su proceso como aquellas que cumplen una sentencia. Si el caso es sobre las condiciones penitenciarias: hacinamiento, falta de medicamentos, riesgo de sufrir tortura, etc., usa este término.
248	53	460	Preso(a)s político(a)s o de conciencia	Preso de conciencia es la persona privada de su libertad por su origen étnico, sexo, color, idioma, origen social, situación económica, nacionalidad, orientación sexual, u otras características, y que no han utilizado la violencia, ni abogado por ella (AI). Preso político es la persona privada de su libertad a causa de sus actividades de oposición al orden político establecido.
253	53	540	Recursos naturales	Son todos los materiales, recursos y servicios de los ecosistemas que proporciona la naturaleza, algunos renovables y otros no renovables y limitados, que pueden ser utilizados para satisfacer las necesidades humanas, tanto las materiales (alimento, vestido, cobijo, medicamentos, energía) como las espirituales (placer estético, recreación). Incluye todos los recursos naturales: agua, aire, tierra (suelo, subsuelo, capa arable), bosques, flora y fauna silvestre, minerales, hidrocarburos, energía solar, recursos marinos, paisaje, biocombustibles, etc. Si el caso registrado es sobre agua, asigna también el tema específico “Agua” que aparece en esta misma lista
267	53	630	Tráfico de personas	Es la facilitación de la entrada ilegal de una persona en un Estado del cual dicha persona no sea nacional o residente permanente con el fin de obtener, directa o indirectamente, un beneficio financiero u otro beneficio de orden material (ONU). Asigna también el tema de "Delincuencia organizada" que aparece en esta misma lista
268	53	650	Trata de personas	Es la captación, el transporte, el traslado, la acogida o la recepción de personas, recurriendo a la amenaza o al uso de la fuerza u otras formas de coacción, al rapto, al fraude, al engaño, al abuso de poder o de una situación de vulnerabilidad o a la concesión o recepción de pagos o beneficios para obtener el consentimiento de una persona que tenga autoridad sobre otra, con fines de explotación. Esa explotación incluirá, como mínimo, la explotación de la prostitución ajena u otras formas de explotación sexual, los trabajos o servicios forzados, la esclavitud o las prácticas análogas a la esclavitud, la servidumbre o la extracción de órganos (ONU).  Asigna también el tema de "Delincuencia organizada" que aparece en esta misma lista
12434	53	070	Conflicto armado	1. Existe un conflicto armado internacional cuando se recurre a la fuerza armada entre dos o más Estados. 2. Los conflictos armados no internacionales son enfrentamientos armados prolongados que ocurren entre fuerzas armadas gubernamentales y las fuerzas de uno o más grupos armados, o entre estos grupos, que surgen en el territorio de un Estado. El enfrentamiento armado debe alcanzar un nivel mínimo de intensidad y las partes que participan en el conflicto deben poseer una organización mínima (CICR)
11160	12	001005040	Muerte resultado de otras VDH	"VDH": Violaciones a los derechos humanos
11284	11266	002050	Violaciones al derecho al acceso a la propiedad pública	Ocurre al restringirse el acceso a bienes de uso común, tales como: parques, caminos/vías públicas, playas, hospitales públicos, puentes.
11190	11184	001020030	Trabajo forzoso	Todo trabajo o servicio exigido a un individuo bajo la amenaza de una pena cualquiera y para el cual dicho individuo no se ofrece voluntariamente. Art. 2, Convenio sobre el Trabajo Forzoso (Convenio 29 de la OIT) OIT, Informe global con arreglo al seguimiento de la Declaración de la OIT relativa a los principios y derechos fundamentales en el trabajo, Ginebra 2005
11236	10	001060	Violaciones al derecho a la inviolabilidad de las comunicaciones	Si registras actos vinculados al derecho a la inviolabilidad de las comunicaciones también puedes registrar "Violaciones al derecho a la vida privada".
11919	11034	001045250	Derecho a la vida privada en términos de políticas públicas	
11998	11994	001045250020	Caso específico de no realización del derecho a la vida privada en términos de políticas públicas	
12002	11999	001045255015	Falta de cumplimiento de la legislación que respete, proteja y garantice el derecho a la vida privada	
17	51	003	Derechos de grupos específicos	Los derechos de las personas con VIH/SIDA están considerados en el derecho a la salud, no discriminación, etc.  Los derechos de los Pueblos indígenas están definidos desde los Derechos de los pueblos. Los derechos de los periodistas se desprenden de la libertad de expresión e información.
14594	14544	004020	Violaciones al derecho de los pueblos al desarrollo	Aplica tanto al pueblo de México en general, como a los pueblos indígenas en particular. El “Derecho al desarrollo” incluye el concepto de “desarrollo sustentable” (o sostenible), entendido como el proceso de desarrollo económico en el que la tecnología, la explotación de los recursos naturales y la organización social y política están orientadas a lograr la distribución equitativa de la riqueza y satisfacer las necesidades básicas o fundamentales del presente, sin comprometer la capacidad de satisfacer, en igual cantidad y calidad, las necesidades de las generaciones futuras.
14508	11233	001055015	Injerencias arbitrarias e ilegales en el domicilio	Incluye injerencias arbitrarias e ilegales en comunidades. Se refiere a interferencias o molestias no autorizadas por la ley o  realizadas como una medida innecesaria, irrazonable y desproporcionada, en el domicilio de una persona, ya sea en su residencia, o donde ejerce su ocupación habitual. Art. 11, Convención Americana sobre derechos humanos. Art. 16, Constitución Mexicana. Comité de Derechos Humanos, Observación General No. 16.
12005	12004	001045260005	Falta de adopción de resoluciones judiciales que respeten, protejan y garanticen el derecho a la vida privada	
11839	138	001025060	Derechos de las víctimas del delito y de VDH	"VDH":Violaciones a los derechos humanos
13404	11334	003050020	Extradición	Procedimiento a través del cual las autoridades de dos Estados llegan a un acuerdo, en virtud del cual uno de esos Estados procede a transferir una persona al otro para que resulte enjuiciada penalmente allí o para que cumpla y se ejecute la pena que le ha sido impuesta, si el juicio ya se hubiere producido. Convención Interamericana sobre Extradición.
14474	12	001005031	Muerte en contexto de operativos de seguridad pública	Pérdida de la vida durante acciones dirigidas, ordenadas, planeadas, organizadas y ejecutadas por fuerzas de policía, para combatir el delito y resguardar la seguridad. Usar para los operativos de seguridad pública efectuados tanto por agentes de la policía como por militares.
11163	12	001005045	Ejecución judicial por aplicación de la pena de muerte	Privación de la vida de una persona condenada por la comisión de los delitos más graves, en cumplimiento de una sentencia judicial emitida por los tribunales competentes y de conformidad con una ley que establezca tal pena, dictada con anterioridad a la comisión del delito.
11164	12	001005050	Muerte sospechosa	Muerte súbita e inesperada, sin causa exterior manifiesta, y que por las circunstancias en que ocurre y los indicios se cree que se trata de una privación arbitraria de la vida. Glosario del Centro de Derechos Humanos Fray Bartolomé de las Casas. En el caso de una muerte sospechosa ocurrida bajo custodia, utiliza "Muerte bajo custodia" incluída en esta misma lista.
11173	13	001010015	Violación sexual	Relación sexual sin consentimiento, por vía vaginal o anal, así como aquellos actos de penetración vaginales o anales, sin consentimiento de la víctima, mediante la utilización de otras partes del cuerpo del agresor u objetos. Asimismo se ha considerado que la penetración bucal mediante el miembro viril constituye violación sexual. Corte IDH. Caso del Penal Miguel Castro Castro Vs. Perú.
11153	14	001015060	Desaparición forzada	Se considera la privación de la libertad de una persona, cualquiera que fuere su forma, cometida por agentes del Estado o por personas o grupos de personas que actúen con la autorización, el apoyo o la aquiescencia del Estado, seguido de la falta de información o de la negativa a reconocer dicha privación de libertad o de informar sobre el paradero de la persona, con la cual se impide el ejercicio de recursos legales y de las garantías procesales pertinentes. Art. 2, Convención Interamericana sobre la Desaparición Forzada de Personas.
14429	15	001037	Derecho a la protección frente al abuso de poder	Aplica a situaciones donde la autoridad o particulares utilizan de forma arbitraria o injustificada el poder (ya sea económico, político, etc.) que legalmente poseen. No se trata de actos ilegales, sino de que empleando sus facultades, las utilizan arbitrariamente, ejerciendo acciones innecesarias, intimidatorias con una gran carga de discrecionalidad. Ej. El caso del General Gallardo, al cual se le abrieron 13 averiguaciones previas, cada una después de una exoneración de la anterior. No puede hablarse de acciones ilegales, pero sí arbitrarias y discrecionales, con una intencionalidad de castigar.  Otro ejemplo son los operativos injustificados o arbitrarios, que nuevamente no son ilegales porque la autoridad tiene facultades para realizar operativos, pero cuando se hacen sin causa que amerite el operativo, como denuncias específicas o pruebas de que es necesario el operativo, causan molestia a la población y pueden ser utilizados para intimidar a comunidades.
11034	15	001045	Derecho a la vida privada	Aplica a actos de injerencia arbitraria o ilegal en la vida privada de las personas.  Ej. examen de no ingravidez a mujeres que solicitan empleo, difusión de información médica, etc. Si registras éste derecho, es posible que quieras incluir el "Derecho a la inviolabilidad de domicilio" o el "Derecho a la inviolabilidad de las comunicaciones".
11037	15	001060	Derecho a la inviolabilidad de las comunicaciones	Si registras este derecho también puedes registrar el "Derecho a la vida privada".
13472	15	001087	Derecho a la objeción de conciencia	Es el derecho de las personas que en razón de una convicción profunda derivada de motivos religiosos, éticos, morales, humanitarios o similares se negasen a cumplir un deber jurídico. Comisión de Derechos Humanos, derechos civiles y políticos, incluida la cuestión de la objeción de conciencia al servicio militar (Informe de la Oficina del Alto Comisionado para los Derechos Humanos), E/CN.4/2004/55, 16 de febrero de 2004.
16	51	002	Derechos económicos, sociales, culturales y ambientales	
11078	16	002050	Derecho al acceso a la propiedad pública	Este derecho se viola al restringirse el acceso a bienes de uso común, tales como: parques, caminos/vías públicas, playas, hospitales públicos, puentes.
14452	14439	004020	Derecho de los pueblos al desarrollo	Este derecho aplica tanto al pueblo de México en general, como a los pueblos indígenas en particular. El “Derecho al desarrollo” incluye el concepto de “desarrollo sustentable” (o sostenible), entendido como el proceso de desarrollo económico en el que la tecnología, la explotación de los recursos naturales y la organización social y política están orientadas a lograr la distribución equitativa de la riqueza y satisfacer las necesidades básicas o fundamentales del presente, sin comprometer la capacidad de satisfacer, en igual cantidad y calidad, las necesidades de las generaciones futuras.
11155	12	001005015	Genocidio	Se entiende por genocidio cualquiera de los actos mencionados a continuación, perpetrados con la intención de destruir, total o parcialmente, a un grupo nacional, étnico, racial o religioso, como tal: a) Matanza de miembros del grupo; b) Lesión grave a la integridad física o mental de los miembros del grupo; c) Sometimiento intencional del grupo a condiciones de existencia que hayan de acarrear su destrucción física, total o parcial; d) Medidas destinadas a impedir los nacimientos en el seno del grupo; e) Traslado por fuerza de niños del grupo a otro grupo. Art. 2, Convención para la prevención y sanción del delito de genocidio  Art. 6, Estatuto de Roma de la Corte Penal Internacional
11156	12	001005020	Masacre	Privación arbitraria de la vida perpetrada en contra de varias personas, por lo general indefensas, realizadas en un mismo lugar y en un mismo momento, producida por ataque armado o cualquier otro medio, llevada a cabo de manera coordinada y organizada, por el agente identificado como perpetrador.  Se distingue del genocidio por que la definición no requiere a la intención de destruir a un grupo nacional, étnico, racial o religioso.
13100	11277	002025005	Desalojos forzosos o ilegales	El hecho de hacer salir con la fuerza o con coacción a personas, familias y/o comunidades de los hogares y/o las tierras que ocupan, en forma permanente o provisional, sin ofrecerles medios apropiados de protección legal o de otra índole ni permitirles su acceso a ellos, sin respetar los procedimientos internos que pueden excepcionalmente permitir el desalojo.  General Comment Nº 7 of the United Nations Committee on Economic, Social and Cultural Rights on Forced Eviction (E/C.12/1997/4  Folleto Informativo No. 25 sobre los Desalojos Forzosos y los Derechos Humanos de la ONU
11286	135	003	Violaciones a los derechos de grupos específicos	Los derechos de las personas con VIH/SIDA están considerados en el derecho a la salud, no discriminación, etc.  Los derechos de los Pueblos Indígenas están definidos desde los Derechos de los pueblos. Los derechos de los periodistas se desprenden de la libertad de expresión e información.
13403	11334	003050015	Expulsión	Medida administrativa individual con la cual el Estado obliga a una persona a abandonar el territorio del Estado donde se encuentra, sin el debido proceso legal.   Una persona extranjera con estatus legal puede ser expulsada solo por decisión fundada en la ley y no puede ser una expulsión colectiva. Un extranjero sin estatus legal puede ser expulsado, pero se le deben garantizar el derecho a la vida, a la integridad física y psíquica, al debido proceso, y a la familia. Corte IDH. Condición Jurídica y Derechos de los Migrantes Indocumentados Corte IDH. Asunto  Haitianos y Dominicanos de origen Haitiano en la República Dominicana respecto República Dominicana
24	14	001015005	Detención arbitraria o ilegal	La detención ilegal es la privación de la libertad personal por las causas, casos o circunstancias que no estén expresamente tipificadas en la ley, o sin la necesaria y estricta sujeción a los procedimientos objetivamente definidos por la ley. La detención arbitraria es la privación de la libertad personal por causas y métodos que —aun calificados de legales— puedan reputarse como incompatibles con el respeto a los derechos fundamentales del individuo por ser, entre otras cosas, irrazonables, imprevisibles, o no proporcionales. Art. 7, Convención Interamericana de Derechos Humanos Corte IDH. Caso Gangaram Panday Vs. Surinam. Corte IDH. Caso Chaparro Álvarez y Lapo Íñiguez. Vs. Ecuador. CIDH, Ferrer Mazorra y otros c. Estados Unidos de América, par 212
25	14	001015010	Retención arbitraria	En la legislación mexicana se entiende por retención la detención ante el Ministerio Público del presunto inculpado, antes que éste sea puesto a disposición del juez.  El presuntamente responsable puede ser detenido hasta por 48 horas por el Ministerio Público, y hasta por 96 horas en caso de delincuencia organizada.  Ver estándares sobre detención arbitraria. Art. 16 Constitución, Art. 23 Código Procedimiento Penales de Oaxaca
11180	14	001015020	Secuestro	Incluye privación de la libertad para obtener rescate, para obligar a un tercero a hacer o dejar de hacer algo o para causar daño a una tercera persona.
11181	14	001015025	Arraigo	Prohibición de que una persona abandone un domicilio o una determinada demarcación mientras se prepara el ejercicio de la acción penal, siempre que exista el riesgo fundado de que el inculpado se sustraiga a la acción de la justicia.
11182	14	001015030	Arresto domiciliario	Es una medida cautelar de privación de la libertad de movimientos y comunicación de un condenado o acusado que se cumple fuera de los establecimientos penitenciarios, ya sea en el propio domicilio, o en otro lugar fijado por el Juez a propuesta del afectado.  En México esta medida cautelar es decretada por el Ministerio Publico y está prevista para algunas categorías de personas, como las mujeres embarazadas, en sustitución de la detención prisión preventiva, o los adolescentes, cuando hay una averiguación previa del detenido y el Fiscal considera necesario el arresto domiciliario con vigilancia de la Policía Federal por un máximo de 48 horas, a efecto de estar en posibilidad de integrar la averiguación previa y en su caso ejercer acción penal. Artículo 52 de la Ley General de Justicia Penal para Adolescentes. Artículo 107 del Código de Procedimientos Penales para el Estado Libre y Soberano de Quintana Roo.
11183	14	001015035	Reclutamiento forzoso	Es la incorporación de una persona a las fuerzas armadas de un país en contra de su voluntad. Esta práctica puede ser realizada directamente por agentes estatales o con la aquiescencia del Estado.  Los tratados internacionales prohíben el reclutamiento forzoso para niños y lo definen como una de las peores formas de esclavitud. CIDH, caso Piché Cuca c. Guatemala, punto resolutivo No.1 (1993). Art. 3, Convenio 182 de la OIT (Convenio sobre la prohibición de las peores formas de trabajo infantil y la acción inmediata para su eliminación).
11774	14	001015040	Toque de queda	Se refiere a la prohibición, establecida por instituciones gubernamentales, de circular libremente por las calles de una ciudad. Los toques de queda constituyen estados de excepción durante los cuales se restringen garantías, por los cuales se deben respetar los estándares fijados en el art. 27 CADH según el cual, el alcance de las suspensiones debe ser el estrictamente necesario para paliar la situación de emergencia y eso implica limitar su alcance temporal, espacial y los derechos que se suspenden. CIDH, HONDURAS: DERECHOS HUMANOS Y GOLPE DE ESTADO, OEA/Ser.L/V/II. Doc. 55, 30 diciembre 2009 Art. 27, Convención Americana sobre Derechos Humanos.
11186	11184	001020010	Servidumbre	Es una institución semejante a la de la esclavitud; la diferencia radica en la existencia de una obligación (deuda), por la cual la persona deudora es objeto de una relación parecida a la del esclavo a favor del acreedor de la obligación, por un periodo de tiempo limitado mientras subsiste la obligación.  La CIDH y la OIT han identificado otra práctica de servidumbre forzada: consistente en “proporcionar medios de subsistencia a los trabajadores (…) mediante una deuda que debe saldarse con la producción de bienes y la prestación de servicios, sin ofrecerle un salario digno para pagar dichas deudas. Real Academia Española Art. 4 Declaración Universal de los Derechos Humanos Art. 1, Convención suplementaria sobre la abolición de la esclavitud, la trata de esclavos y las instituciones análogas a la esclavitud. CIDH, Informe sobre la situación de los derechos humanos en Brasil, párrs. 21-22, “Alto al trabajo forzoso”, Informe global con arreglo al seguimiento de la Declaración de la Organización Internacional del Trabajo (OIT), par. 66-81
11245	11243	001075010	Negación de la existencia de información	Rechazo o negativa de tener información de conocimiento público y no reservada como confidencial y por lo tanto es negado su conocimiento de manera injustificado por parte de un funcionario, servidor público o cualquier persona responsable de otorgar dicha información.
13824	11256	001120005	Desplazamiento	Acción llevada a cabo por personas o grupos de personas que se han visto forzadas u obligadas a escapar o huir de su hogar o de su lugar de residencia habitual, en particular como resultado o para evitar los efectos de un conflicto armado, situaciones de violencia generalizada, violaciones de los derechos humanos o catástrofes naturales o provocados por el ser humano, y que no han cruzado una frontera estatal internacionalmente reconocida. Art. 2 de los Principios Rectores de los Desplazamientos Internos, Naciones Unidas
11234	11233	001055005	Allanamiento	En el sistema penal mexicano es considerado delito de allanamiento de morada introducirse furtivamente o con engaño o violencia, o sin permiso de la persona autorizada para darlo, a un domicilio, departamento, vivienda, aposento o dependencias de una casa habitada sin motivo justificado, sin orden de autoridad competente y fuera de los casos en que la ley lo permita.
11235	11233	001055010	Cateo	El cateo es el ingreso a un domicilio con fines de investigación para buscar objetos o personas relacionadas con el delito. La orden de cateo podrá ser expedida solo, a solicitud del Ministerio Público, una orden fundada emitida por una autoridad judicial competente donde se establecen las razones de la medida adoptada y donde constan el lugar a allanarse y las cosas que serán objeto de secuestro.  Art. 16 Constitución Mexicana. Art 61- 65 Código Procedimientos Penales Federales
14425	15	001036	Derecho a la seguridad ciudadana	Aplica a actos de omisión de la autoridad, que no previenen y no proporcionan seguridad ciudadana.  El Instituto Interamericano de Derechos Humanos (IIDH) ha definido a la seguridad ciudadana como: aquella situación política y social en la que las personas tienen legal y efectivamente garantizado el goce pleno de sus derechos humanos y en la que existen mecanismos institucionales eficientes para prevenir y controlar las amenazas o coerciones ilegítimas que puedan lesionar tales derechos. El derecho a la seguridad ciudadana en un Estado democrático y de derecho, consiste en el conjunto de garantías que debe brindar el Estado a sus habitantes para el libre ejercicio de todos sus derechos.
11187	11184	001020015	Trata de personas	Es la captación, el transporte, el traslado, la acogida o la recepción de personas, recurriendo a la amenaza o al uso de la fuerza u otras formas de coacción, al rapto, al fraude, al engaño, al abuso de poder o de una situación de vulnerabilidad o a la concesión o recepción de pagos o beneficios para obtener el consentimiento de una persona que tenga autoridad sobre otra, con fines de explotación. Esa explotación incluirá, como mínimo, la explotación de la prostitución ajena u otras formas de explotación sexual, los trabajos o servicios forzados, la esclavitud o las prácticas análogas a la esclavitud, la servidumbre o la extracción de órgano. Art. 3, Protocolo para prevenir, reprimir y sancionar la trata de personas, especialmente mujeres y niños, que complementa la Convención de las Naciones Unidas contra la Delincuencia Organizada Transnacional.
13820	11184	001020020	Prostitución forzada	También "explotación sexual forzada". Consiste en hacer que una o más personas realicen uno o más actos de naturaleza sexual por la fuerza, o mediante la amenaza del uso de la fuerza, o mediante coacción, como la causada por el temor a la violencia, la intimidación, la detención, la opresión sicológica o el abuso de poder, o aprovechando un entorno de coacción o la incapacidad de esa(s) persona(s) de dar su libre consentimiento. Lo anterior con el propósito de obtener ventajas pecuniarias o de otro tipo a cambio de los actos de naturaleza sexual o en relación con ellos. Es considerada una forma de violencia contra la mujer y es considerada una forma de esclavitud. Definición de la Coordinación General del Programa de Equidad de Género del Poder Judicial de la Federación. Art. 2, Convención interamericana para prevenir, sancionar y erradicar la violencia contra la mujer. Relatora Especial de la Subcomisión de las Naciones Unidas sobre la violación sistemática, la esclavitud sexual y las prácticas análogas a la esclavitud en tiempos de conflicto armado, E/CN.4/Sub.2/1998/13, párr. 31 Consejo de Europa, RECOMENDACIÓN 1325 Relativa a la trata de mujeres y la prostitución forzada en los Estados miembros del Consejo de Europa, 1997
14511	11184	001020025	Tráfico de personas	Es la facilitación de la entrada ilegal de una persona en un Estado del cual dicha persona no sea nacional o residente permanente con el fin de obtener, directa o indirectamente, un beneficio financiero u otro beneficio de orden material. La OIT define el tráfico de personas incluyendo el tráfico dentro del mismo Estado, con el objeto de llevar a cabo un trabajo, bajo condiciones inferiores a las establecidas por la ley, siendo muy probablemente que la actividad o empleo desempeñado sea ilegal y en donde participe un agente, captador y transportista que obtendrá beneficios por su intervención. Art. 3 Protocolo contra el tráfico ilícito de migrantes por tierra, mar y aire. “Alto al trabajo forzoso”, Informe global con arreglo al seguimiento de la Declaración de la Organización Internacional del Trabajo (OIT), par. 141
11884	11191	001025060	Violaciones a los derechos de las víctimas del delito y de VDH	"VDH": Violaciones a los derechos humanos.
11226	10	001045	Violaciones al derecho a la vida privada	Aplica a actos de injerencia arbitraria o ilegal en la vida privada de las personas.  Ej. examen de no ingravidez a mujeres que solicitan empleo, difusión de información médica, etc.  Si registras actos vinculados al derecho a la vida privada, es posible que quieras incluir actos vinculados al "Derecho a la inviolabilidad de domicilio" o  al "Derecho a la inviolabilidad de las comunicaciones".
\.


--
-- PostgreSQL database dump complete
--

