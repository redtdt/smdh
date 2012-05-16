--
-- PostgreSQL database dump
--

SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- Name: plpgsql; Type: PROCEDURAL LANGUAGE; Schema: -; Owner: -
--

CREATE PROCEDURAL LANGUAGE plpgsql;


SET search_path = public, pg_catalog;

--
-- Name: acto_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE acto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: acto; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE acto (
    id integer DEFAULT nextval('acto_id_seq'::regclass) NOT NULL,
    caso_id integer not null,
    victima_id integer not null,
    confidencialidad integer,
    tipodeacto integer,
    tipofechainicio integer,
    tipofechafinal integer,
    tipolugar integer,
    estatusvdh integer,
    estatusvictima integer,
    observaciones text,
    fechainicio date,
    fechafin date,
    loginfo integer,
    localizacion_id integer,
    legislacion_nacional integer,
    instrumentos_internacionales integer,
    legislacion_nacional_notas text,
    instrumentos_internacionales_notas text,
    edad_victima integer,
    edad_victima_tipo integer,
    exportar integer,
    exportarnormatividad integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: caracrelevantes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE caracrelevantes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: caracrelevantes; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE caracrelevantes (
    id integer DEFAULT nextval('caracrelevantes_id_seq'::regclass) NOT NULL,
    acto_id integer,
    caracrelevantes_id integer,
    loginfo integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE caracrelevantes; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE caracrelevantes IS 'Caracteristicas relevantes en actos';


--
-- Name: caso_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE caso_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: caso; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE caso (
    id integer DEFAULT nextval('caso_id_seq'::regclass) NOT NULL,
    descripcion character varying NOT NULL,
    confidencialidad integer,
    fecha_inicio date,
    tipo_fecha_inicio integer,
    fecha_final date,
    tipo_fecha_final integer,
    descripcion_narrativa text,
    resumen_descripcion text,
    observaciones text,
    no_persona_afectadas text,
    comentarios text,
    archivos text,
    monitoreo integer,
    loginfo integer,
    proyecto_grupo text,
    proyecto_conjunto text,
    proyecto_se text,
    frecepcion date,
    tipo_frecepcion integer,
    exportar integer,
    exportarrelaciones integer,
    clavegrupo integer,
    clavestatus integer,
    clavestatusc3 integer,
    casorelacionadoc3 integer
);


--
-- Name: TABLE caso; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE caso IS 'Informacion general del caso';


--
-- Name: caso_vinculo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE caso_vinculo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: caso_vinculo; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE caso_vinculo (
    id integer DEFAULT nextval('caso_vinculo_id_seq'::regclass) NOT NULL,
    caso_1_id integer not null,
    caso_2_id integer not null,
    tipo_id integer,
    loginfo integer,
    observaciones text,
    comentarios text,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE caso_vinculo; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE caso_vinculo IS 'Relacion entre casos';


--
-- Name: configtdt_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE configtdt_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: configtdt; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE configtdt (
    id integer DEFAULT nextval('configtdt_id_seq'::regclass) NOT NULL,
    tipo character varying(30) NOT NULL,
    descripcion character varying(300) NOT NULL,
    contenido text
);


--
-- Name: TABLE configtdt; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE configtdt IS 'Informacion de configuracion';


--
-- Name: derechoviolado_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE derechoviolado_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: derechoviolado; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE derechoviolado (
    id integer DEFAULT nextval('derechoviolado_id_seq'::regclass) NOT NULL,
    acto_id integer not null,
    derechoviolado_id integer,
    loginfo integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE derechoviolado; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE derechoviolado IS 'Derechos violados en actos';


--
-- Name: evento_tipificacion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE evento_tipificacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: evento_tipificacion; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE evento_tipificacion (
    id integer DEFAULT nextval('evento_tipificacion_id_seq'::regclass) NOT NULL,
    evento_id integer,
    tesauro_id integer,
    codigo integer,
    acto_id integer,
    notas text,
    loginfo integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE evento_tipificacion; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE evento_tipificacion IS 'Tipificaciones de casos. ';


--
-- Name: fuente_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE fuente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: fuente; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE fuente (
    id integer DEFAULT nextval('fuente_id_seq'::regclass) NOT NULL,
    caso_id integer not null,
    persona_referenciada_id integer,
    persona_fuente_id integer,
    confidencialidad integer,
    tipofecha integer,
    fecha date,
    conexion_con_informacion integer,
    idioma integer,
    lengua_indigena integer,
    confiabilidad integer,
    observaciones text,
    comentarios text,
    loginfo integer,
    exportar integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE fuente; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE fuente IS 'Fuente personal';


--
-- Name: grupos; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE grupos (
    id integer NOT NULL,
    nombre character varying(150) NOT NULL,
    contacto character varying(150),
    sigla character varying(30),
    ultimolotet1fecha date,
    ultimolotet1archivo character varying(150),
    ultimolotet2fecha date,
    ultimolotet2archivo character varying(150),
    loginfo integer
);


--
-- Name: intervencion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE intervencion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: intervencion; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE intervencion (
    id integer DEFAULT nextval('intervencion_id_seq'::regclass) NOT NULL,
    evento_id integer not null,
    tesauro_id integer,
    persona_id_dequien integer,
    persona_id_aquien integer,
    persona_id_interviniente integer,
    loginfo integer,
    estatus_id integer,
    observaciones text,
    comentarios text,
    respuesta text,
    impacto text,
    fecha date,
    tipofecha integer,
    exportar integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE intervencion; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE intervencion IS 'Intervenciones';


--
-- Name: involucramiento_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE involucramiento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: involucramiento; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE involucramiento (
    id integer DEFAULT nextval('involucramiento_id_seq'::regclass) NOT NULL,
    acto_id integer not null,
    persona_id integer not null,
    tesauro_id integer,
    tipo_id integer,
    confidencialidad integer,
    gradoinvolucramiento integer,
    tipoperpetrador integer,
    ultimostatusperpetrador integer,
    observaciones text,
    loginfo integer,
    exportar integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE involucramiento; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE involucramiento IS 'Involucramiento de perpetradores en actos';


--
-- Name: localidad_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE localidad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: localidad; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE localidad (
    id integer DEFAULT nextval('localidad_id_seq'::regclass) NOT NULL,
    caso_id integer not null,
    pais_id integer,
    estado_id integer,
    municipio_id integer,
    notas_localidad character varying,
    notas_municipio character varying,
    localidad character varying,
    loginfo integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE localidad; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE localidad IS 'Localidades de casos';


--
-- Name: loginfo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE loginfo_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: loginfo; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE loginfo (
    org integer,
    id integer DEFAULT nextval('loginfo_id_seq'::regclass) NOT NULL,
    "fechaCreacion" date,
    "userCreacion" integer,
    "fechaActualizacion" date,
    "userActualizacion" integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE loginfo; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE loginfo IS 'Datos de creacion y ultima actualizacion de las entidades';


--
-- Name: persona_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE persona_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: persona; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE persona (
    id integer DEFAULT nextval('persona_id_seq'::regclass) NOT NULL,
    nombre character varying NOT NULL,
    apellido character varying NOT NULL,
    esindividual integer,
    otro_nombre character varying,
    sexo integer,
    fecha_nac_o_fund date,
    tipo_fecha_nac_o_fund integer,
    pais_nac_u_origen integer,
    estado_nac_u_origen integer,
    mpio_nac_u_origen integer,
    localidad_nac_u_origen character varying,
    ciudadania_o_sede integer,
    escolaridad integer,
    ocupacion integer,
    habla_lengua_local integer,
    religion integer,
    estado_civil integer,
    no_dependientes integer,
    descripcion_del_grupo character varying,
    observaciones text,
    monitoreo integer,
    comentarios text,
    proyecto_grupo text,
    proyecto_conjunto text,
    proyecto_se text,
    archivos text,
    loginfo integer,
    tipo integer,
    frecepcion date,
    tipo_frecepcion integer,
    exportar integer,
    exportardatosbio integer,
    confidencialidad integer,
    clavegrupo integer,
    clavestatus integer,
    personarelacionadac3 integer,
    clavestatusc3 integer
);


--
-- Name: TABLE persona; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE persona IS 'Personas individuales y colectivas';


--
-- Name: persona_tipificacion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE persona_tipificacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: persona_tipificacion; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE persona_tipificacion (
    id integer DEFAULT nextval('persona_tipificacion_id_seq'::regclass) NOT NULL,
    persona_id integer,
    tesauro_id integer,
    codigo integer,
    masinformacion character varying,
    telefono character varying,
    celular character varying,
    web character varying,
    correo_e character varying,
    loginfo integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE persona_tipificacion; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE persona_tipificacion IS 'Campos repetibles de personas';


--
-- Name: persona_vinculo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE persona_vinculo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: persona_vinculo; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE persona_vinculo (
    id integer DEFAULT nextval('persona_vinculo_id_seq'::regclass) NOT NULL,
    persona_1_id integer not null,
    persona_2_id integer,
    tipo_id integer,
    loginfo integer,
    "Fecha_inicial" date,
    tipofecha_inicial integer,
    "Fecha_final" date,
    tipofecha_final integer,
    observaciones text,
    puesto character varying(250),
    rango character varying(250),
    confidencialidad integer,
    comentarios text,
    fecha_info_vigente date,
    tipofecha_info_vigente integer,
    descripcion character varying(200),
    exportar integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE persona_vinculo; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE persona_vinculo IS 'Datos biograficos de personas';


--
-- Name: publicacion_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE publicacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: publicacion; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE publicacion (
    id integer DEFAULT nextval('publicacion_id_seq'::regclass) NOT NULL,
    caso_id integer not null,
    titulo_de_parte character varying(120),
    datos_publicacion character varying(500),
    tipofecha integer,
    fecha date,
    "Nombre_del_sitio" character varying(120),
    "Liga_publicacion" character varying(500),
    fecha_consulta date,
    tipopublicacion integer,
    idioma integer,
    lengua_indigena integer,
    confiabilidad integer,
    observaciones text,
    comentarios text,
    persona_referenciada_id integer,
    loginfo integer,
    tipofechaconsulta integer,
    exportar integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE publicacion; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE publicacion IS 'Fuente documental';


--
-- Name: tesauro_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tesauro_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: tesauro; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE tesauro (
    id integer DEFAULT nextval('tesauro_id_seq'::regclass) NOT NULL,
    parent_id integer NOT NULL,
    name character varying(30) NOT NULL,
    descripcion character varying(350) NOT NULL,
    notas text
);


--
-- Name: TABLE tesauro; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE tesauro IS 'Vocabularios y ayuda contextual';


--
-- Name: test1; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE test1 (
    id bigint NOT NULL,
    int2 bigint,
    nombre character varying(30),
    nombre2 character varying(30)
);


--
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE usuario_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: usuario; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE usuario (
    id integer DEFAULT nextval('usuario_id_seq'::regclass) NOT NULL,
    nombre character varying(30) NOT NULL,
    nivel integer,
    clavegrupo integer,
    clavestatus integer
);


--
-- Name: TABLE usuario; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE usuario IS 'Usuarios';


--
-- Name: acto_persona_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE acto_persona_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: biografia_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE biografia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: grupos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE grupos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: grupos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE grupos_id_seq OWNED BY grupos.id;


--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: test1_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE test1_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: test1_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE test1_id_seq OWNED BY test1.id;


--
-- Name: testtable_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE testtable_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: testtable_key2_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE testtable_key2_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE grupos ALTER COLUMN id SET DEFAULT nextval('grupos_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE test1 ALTER COLUMN id SET DEFAULT nextval('test1_id_seq'::regclass);


--
-- Name: acto_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_pkey PRIMARY KEY (id);


--
-- Name: caracrelevantes_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY caracrelevantes
    ADD CONSTRAINT caracrelevantes_pkey PRIMARY KEY (id);


--
-- Name: caso_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY caso
    ADD CONSTRAINT caso_pkey PRIMARY KEY (id);


--
-- Name: caso_vinculo_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY caso_vinculo
    ADD CONSTRAINT caso_vinculo_pkey PRIMARY KEY (id);


--
-- Name: configtdt_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY configtdt
    ADD CONSTRAINT configtdt_pkey PRIMARY KEY (id);


--
-- Name: derechoviolado_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY derechoviolado
    ADD CONSTRAINT derechoviolado_pkey PRIMARY KEY (id);


--
-- Name: evento_tipificacion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY evento_tipificacion
    ADD CONSTRAINT evento_tipificacion_pkey PRIMARY KEY (id);


--
-- Name: fuente_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_pkey PRIMARY KEY (id);


--
-- Name: grupos_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY grupos
    ADD CONSTRAINT grupos_pkey PRIMARY KEY (id);


--
-- Name: intervencion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY intervencion
    ADD CONSTRAINT intervencion_pkey PRIMARY KEY (id);


--
-- Name: involucramiento_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY involucramiento
    ADD CONSTRAINT involucramiento_pkey PRIMARY KEY (id);


--
-- Name: localidad_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY localidad
    ADD CONSTRAINT localidad_pkey PRIMARY KEY (id);


--
-- Name: loginfo_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY loginfo
    ADD CONSTRAINT loginfo_pkey PRIMARY KEY (id);


--
-- Name: persona_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_pkey PRIMARY KEY (id);


--
-- Name: persona_tipificacion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY persona_tipificacion
    ADD CONSTRAINT persona_tipificacion_pkey PRIMARY KEY (id);


--
-- Name: persona_vinculo_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY persona_vinculo
    ADD CONSTRAINT persona_vinculo_pkey PRIMARY KEY (id);


--
-- Name: publicacion_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_pkey PRIMARY KEY (id);


--
-- Name: tesauro_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY tesauro
    ADD CONSTRAINT tesauro_pkey PRIMARY KEY (id);


--
-- Name: test1_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY test1
    ADD CONSTRAINT test1_pkey PRIMARY KEY (id);


--
-- Name: usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- Name: acto_caso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_caso_id_fkey FOREIGN KEY (caso_id) REFERENCES caso(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_estatusvdh_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_estatusvdh_fkey FOREIGN KEY (estatusvdh) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_estatusvictima_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_estatusvictima_fkey FOREIGN KEY (estatusvictima) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_instrumentos_internacionales_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_instrumentos_internacionales_fkey FOREIGN KEY (instrumentos_internacionales) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_legislacion_nacional_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_legislacion_nacional_fkey FOREIGN KEY (legislacion_nacional) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_localizacion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_localizacion_id_fkey FOREIGN KEY (localizacion_id) REFERENCES localidad(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_tipodeacto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_tipodeacto_fkey FOREIGN KEY (tipodeacto) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_tipofechafinal_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_tipofechafinal_fkey FOREIGN KEY (tipofechafinal) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_tipofechainicio_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_tipofechainicio_fkey FOREIGN KEY (tipofechainicio) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_tipolugar_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_tipolugar_fkey FOREIGN KEY (tipolugar) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: acto_victima_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY acto
    ADD CONSTRAINT acto_victima_id_fkey FOREIGN KEY (victima_id) REFERENCES persona(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caracrelevantes_acto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caracrelevantes
    ADD CONSTRAINT caracrelevantes_acto_id_fkey FOREIGN KEY (acto_id) REFERENCES acto(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caracrelevantes_caracrelevantes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caracrelevantes
    ADD CONSTRAINT caracrelevantes_caracrelevantes_id_fkey FOREIGN KEY (caracrelevantes_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caracrelevantes_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caracrelevantes
    ADD CONSTRAINT caracrelevantes_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caso_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caso
    ADD CONSTRAINT caso_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caso_monitoreo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caso
    ADD CONSTRAINT caso_monitoreo_fkey FOREIGN KEY (monitoreo) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caso_tipo_fecha_final_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caso
    ADD CONSTRAINT caso_tipo_fecha_final_fkey FOREIGN KEY (tipo_fecha_final) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caso_tipo_fecha_inicio_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caso
    ADD CONSTRAINT caso_tipo_fecha_inicio_fkey FOREIGN KEY (tipo_fecha_inicio) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caso_vinculo_caso_1_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caso_vinculo
    ADD CONSTRAINT caso_vinculo_caso_1_id_fkey FOREIGN KEY (caso_1_id) REFERENCES caso(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caso_vinculo_caso_2_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caso_vinculo
    ADD CONSTRAINT caso_vinculo_caso_2_id_fkey FOREIGN KEY (caso_2_id) REFERENCES caso(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caso_vinculo_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caso_vinculo
    ADD CONSTRAINT caso_vinculo_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: caso_vinculo_tipo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY caso_vinculo
    ADD CONSTRAINT caso_vinculo_tipo_id_fkey FOREIGN KEY (tipo_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: derechoviolado_acto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY derechoviolado
    ADD CONSTRAINT derechoviolado_acto_id_fkey FOREIGN KEY (acto_id) REFERENCES acto(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: derechoviolado_derechoviolado_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY derechoviolado
    ADD CONSTRAINT derechoviolado_derechoviolado_id_fkey FOREIGN KEY (derechoviolado_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: derechoviolado_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY derechoviolado
    ADD CONSTRAINT derechoviolado_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: evento_tipificacion_evento_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY evento_tipificacion
    ADD CONSTRAINT evento_tipificacion_evento_id_fkey FOREIGN KEY (evento_id) REFERENCES caso(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: evento_tipificacion_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY evento_tipificacion
    ADD CONSTRAINT evento_tipificacion_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: evento_tipificacion_tesauro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY evento_tipificacion
    ADD CONSTRAINT evento_tipificacion_tesauro_id_fkey FOREIGN KEY (tesauro_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_caso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_caso_id_fkey FOREIGN KEY (caso_id) REFERENCES caso(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_conexion_con_informacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_conexion_con_informacion_fkey FOREIGN KEY (conexion_con_informacion) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_confiabilidad_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_confiabilidad_fkey FOREIGN KEY (confiabilidad) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_idioma_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_idioma_fkey FOREIGN KEY (idioma) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_lengua_indigena_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_lengua_indigena_fkey FOREIGN KEY (lengua_indigena) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_persona_fuente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_persona_fuente_id_fkey FOREIGN KEY (persona_fuente_id) REFERENCES persona(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_persona_referenciada_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_persona_referenciada_id_fkey FOREIGN KEY (persona_referenciada_id) REFERENCES persona(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fuente_tipofecha_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY fuente
    ADD CONSTRAINT fuente_tipofecha_fkey FOREIGN KEY (tipofecha) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: grupos_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY grupos
    ADD CONSTRAINT grupos_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: intervencion_estatus_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY intervencion
    ADD CONSTRAINT intervencion_estatus_id_fkey FOREIGN KEY (estatus_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: intervencion_evento_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY intervencion
    ADD CONSTRAINT intervencion_evento_id_fkey FOREIGN KEY (evento_id) REFERENCES caso(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: intervencion_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY intervencion
    ADD CONSTRAINT intervencion_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: intervencion_persona_id_aquien_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY intervencion
    ADD CONSTRAINT intervencion_persona_id_aquien_fkey FOREIGN KEY (persona_id_aquien) REFERENCES persona(id);


--
-- Name: intervencion_persona_id_dequien_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY intervencion
    ADD CONSTRAINT intervencion_persona_id_dequien_fkey FOREIGN KEY (persona_id_dequien) REFERENCES persona(id);


--
-- Name: intervencion_persona_id_interviniente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY intervencion
    ADD CONSTRAINT intervencion_persona_id_interviniente_fkey FOREIGN KEY (persona_id_interviniente) REFERENCES persona(id);


--
-- Name: intervencion_tesauro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY intervencion
    ADD CONSTRAINT intervencion_tesauro_id_fkey FOREIGN KEY (tesauro_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: involucramiento_acto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY involucramiento
    ADD CONSTRAINT involucramiento_acto_id_fkey FOREIGN KEY (acto_id) REFERENCES acto(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: involucramiento_gradoinvolucramiento_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY involucramiento
    ADD CONSTRAINT involucramiento_gradoinvolucramiento_fkey FOREIGN KEY (gradoinvolucramiento) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: involucramiento_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY involucramiento
    ADD CONSTRAINT involucramiento_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: involucramiento_persona_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY involucramiento
    ADD CONSTRAINT involucramiento_persona_id_fkey FOREIGN KEY (persona_id) REFERENCES persona(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: involucramiento_tesauro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY involucramiento
    ADD CONSTRAINT involucramiento_tesauro_id_fkey FOREIGN KEY (tesauro_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: involucramiento_tipoperpetrador_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY involucramiento
    ADD CONSTRAINT involucramiento_tipoperpetrador_fkey FOREIGN KEY (tipoperpetrador) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: involucramiento_ultimostatusperpetrador_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY involucramiento
    ADD CONSTRAINT involucramiento_ultimostatusperpetrador_fkey FOREIGN KEY (ultimostatusperpetrador) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: localidad_caso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY localidad
    ADD CONSTRAINT localidad_caso_id_fkey FOREIGN KEY (caso_id) REFERENCES caso(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: localidad_estado_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY localidad
    ADD CONSTRAINT localidad_estado_id_fkey FOREIGN KEY (estado_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: localidad_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY localidad
    ADD CONSTRAINT localidad_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id);


--
-- Name: localidad_municipio_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY localidad
    ADD CONSTRAINT localidad_municipio_id_fkey FOREIGN KEY (municipio_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: localidad_pais_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY localidad
    ADD CONSTRAINT localidad_pais_id_fkey FOREIGN KEY (pais_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_ciudadania_o_sede_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_ciudadania_o_sede_fkey FOREIGN KEY (ciudadania_o_sede) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_escolaridad_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_escolaridad_fkey FOREIGN KEY (escolaridad) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_estado_civil_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_estado_civil_fkey FOREIGN KEY (estado_civil) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_estado_nac_u_origen_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_estado_nac_u_origen_fkey FOREIGN KEY (estado_nac_u_origen) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_monitoreo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_monitoreo_fkey FOREIGN KEY (monitoreo) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_mpio_nac_u_origen_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_mpio_nac_u_origen_fkey FOREIGN KEY (mpio_nac_u_origen) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_ocupacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_ocupacion_fkey FOREIGN KEY (ocupacion) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_pais_nac_u_origen_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_pais_nac_u_origen_fkey FOREIGN KEY (pais_nac_u_origen) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_religion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_religion_fkey FOREIGN KEY (religion) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_sexo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_sexo_fkey FOREIGN KEY (sexo) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_tipificacion_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_tipificacion
    ADD CONSTRAINT persona_tipificacion_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_tipificacion_persona_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_tipificacion
    ADD CONSTRAINT persona_tipificacion_persona_id_fkey FOREIGN KEY (persona_id) REFERENCES persona(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_tipificacion_tesauro_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_tipificacion
    ADD CONSTRAINT persona_tipificacion_tesauro_id_fkey FOREIGN KEY (tesauro_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_tipo_fecha_nac_o_fund_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_tipo_fecha_nac_o_fund_fkey FOREIGN KEY (tipo_fecha_nac_o_fund) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_tipo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona
    ADD CONSTRAINT persona_tipo_fkey FOREIGN KEY (tipo) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_vinculo_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_vinculo
    ADD CONSTRAINT persona_vinculo_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_vinculo_persona_1_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_vinculo
    ADD CONSTRAINT persona_vinculo_persona_1_id_fkey FOREIGN KEY (persona_1_id) REFERENCES persona(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_vinculo_persona_2_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_vinculo
    ADD CONSTRAINT persona_vinculo_persona_2_id_fkey FOREIGN KEY (persona_2_id) REFERENCES persona(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_vinculo_tipo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_vinculo
    ADD CONSTRAINT persona_vinculo_tipo_id_fkey FOREIGN KEY (tipo_id) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_vinculo_tipofecha_final_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_vinculo
    ADD CONSTRAINT persona_vinculo_tipofecha_final_fkey FOREIGN KEY (tipofecha_final) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_vinculo_tipofecha_info_vigente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_vinculo
    ADD CONSTRAINT persona_vinculo_tipofecha_info_vigente_fkey FOREIGN KEY (tipofecha_info_vigente) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: persona_vinculo_tipofecha_inicial_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY persona_vinculo
    ADD CONSTRAINT persona_vinculo_tipofecha_inicial_fkey FOREIGN KEY (tipofecha_inicial) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publicacion_caso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_caso_id_fkey FOREIGN KEY (caso_id) REFERENCES caso(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publicacion_confiabilidad_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_confiabilidad_fkey FOREIGN KEY (confiabilidad) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publicacion_idioma_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_idioma_fkey FOREIGN KEY (idioma) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publicacion_lengua_indigena_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_lengua_indigena_fkey FOREIGN KEY (lengua_indigena) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publicacion_loginfo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_loginfo_fkey FOREIGN KEY (loginfo) REFERENCES loginfo(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publicacion_persona_referenciada_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_persona_referenciada_id_fkey FOREIGN KEY (persona_referenciada_id) REFERENCES persona(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publicacion_tipofecha_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_tipofecha_fkey FOREIGN KEY (tipofecha) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publicacion_tipopublicacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacion
    ADD CONSTRAINT publicacion_tipopublicacion_fkey FOREIGN KEY (tipopublicacion) REFERENCES tesauro(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- PostgreSQL database dump complete
--

