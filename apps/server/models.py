from typing import Optional
import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKeyConstraint, Index, Table, String, Text, Time
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Accesos(db.Model):
    __tablename__ = 'accesos'

    IDEACC: Mapped[int] = mapped_column(INTEGER(12), primary_key=True)
    DIRACC: Mapped[str] = mapped_column(String(16), nullable=False)
    FECACC: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    BROACC: Mapped[str] = mapped_column(String(254), nullable=False)
    USEACC: Mapped[Optional[int]] = mapped_column(INTEGER(5))


class Cap(db.Model):
    __tablename__ = 'cap'

    IDECAP: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    POBCAP: Mapped[str] = mapped_column(String(80), nullable=False)
    NCUCAP: Mapped[str] = mapped_column(String(50), nullable=False)
    HRTCAP: Mapped[str] = mapped_column(String(5), nullable=False)
    HTECAP: Mapped[str] = mapped_column(String(5), nullable=False)
    HPRCAP: Mapped[str] = mapped_column(String(5), nullable=False)
    FINCAP: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    FFNCAP: Mapped[Optional[datetime.date]] = mapped_column(Date)
    HINCAP: Mapped[Optional[str]] = mapped_column(String(10))
    HFNCAP: Mapped[Optional[str]] = mapped_column(String(10))
    LUGCAP: Mapped[Optional[str]] = mapped_column(String(50))
    RELDIA: Mapped[Optional[int]] = mapped_column(INTEGER(5))
    DIACAP: Mapped[Optional[str]] = mapped_column(String(150))
    VERIFC: Mapped[Optional[int]] = mapped_column(INTEGER(5))

    bib: Mapped[list['Bib']] = relationship('Bib', back_populates='cap')
    ext: Mapped[list['Ext']] = relationship('Ext', back_populates='cap')
    nec: Mapped[list['Nec']] = relationship('Nec', back_populates='cap')
    nro: Mapped[list['Nro']] = relationship('Nro', back_populates='cap')
    obj: Mapped[list['Obj']] = relationship('Obj', back_populates='cap')
    teccap: Mapped[list['Teccap']] = relationship('Teccap', back_populates='cap')
    tem: Mapped[list['Tem']] = relationship('Tem', back_populates='cap')


class Con(db.Model):
    __tablename__ = 'con'

    idecon: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    nomcon: Mapped[Optional[str]] = mapped_column(String(255))
    descon: Mapped[Optional[str]] = mapped_column(Text)
    tipcon: Mapped[Optional[str]] = mapped_column(String(45))


class Coo(db.Model):
    __tablename__ = 'coo'

    IDECOO: Mapped[str] = mapped_column(String(3), primary_key=True)
    NOMCOO: Mapped[str] = mapped_column(String(40), nullable=False)

    car: Mapped[list['Car']] = relationship('Car', back_populates='coo')


class Dia(db.Model):
    __tablename__ = 'dia'

    IDEDIA: Mapped[int] = mapped_column(INTEGER(4), primary_key=True)
    FECDIA: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    FECFIN: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    FECINI: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    PER_DIA: Mapped[Optional[str]] = mapped_column(String(30))

    val: Mapped[list['Val']] = relationship('Val', back_populates='dia')


class Emp(db.Model):
    __tablename__ = 'emp'

    IDEEMP: Mapped[int] = mapped_column(INTEGER(3), primary_key=True)
    APPEMP: Mapped[str] = mapped_column(String(20), nullable=False)
    APMEMP: Mapped[str] = mapped_column(String(20), nullable=False)
    NOMEMP: Mapped[str] = mapped_column(String(25), nullable=False)
    EMAEMP: Mapped[Optional[str]] = mapped_column(String(50))
    CELEMP: Mapped[Optional[str]] = mapped_column(String(15))
    CEL2EMP: Mapped[Optional[str]] = mapped_column(String(15))
    TELOFIEMP: Mapped[Optional[str]] = mapped_column(String(8))
    TELOFI2EMP: Mapped[Optional[str]] = mapped_column(String(8))
    EXTEMP: Mapped[Optional[str]] = mapped_column(String(3))
    FOTEMP: Mapped[Optional[str]] = mapped_column(String(150))

    per: Mapped[list['Per']] = relationship('Per', back_populates='emp')


class Jun(db.Model):
    __tablename__ = 'jun'

    IDEJUN: Mapped[int] = mapped_column(INTEGER(4), primary_key=True)
    FECJUN: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    LUGJUN: Mapped[str] = mapped_column(String(100), nullable=False)
    FEFJUN: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    MINJUN: Mapped[Optional[str]] = mapped_column(String(4))
    DIAJUN: Mapped[Optional[str]] = mapped_column(String(254))

    tem_jc: Mapped[list['TemJc']] = relationship('TemJc', back_populates='jun')


class Lug(db.Model):
    __tablename__ = 'lug'

    IDELUG: Mapped[int] = mapped_column(INTEGER(3), primary_key=True)
    NOMLUG: Mapped[str] = mapped_column(Text, nullable=False)

    rep: Mapped[list['Rep']] = relationship('Rep', back_populates='lug')


class Med(db.Model):
    __tablename__ = 'med'

    IDEMED: Mapped[int] = mapped_column(INTEGER(2), primary_key=True)
    NOMMED: Mapped[str] = mapped_column(String(100), nullable=False)
    IMGMED: Mapped[str] = mapped_column(String(100), nullable=False)

    pub: Mapped[list['Pub']] = relationship('Pub', back_populates='med')


class Org(db.Model):
    __tablename__ = 'org'

    IDEORG: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    NOMORG: Mapped[str] = mapped_column(String(50), nullable=False)
    DIRORG: Mapped[str] = mapped_column(Text, nullable=False)
    TELORG: Mapped[str] = mapped_column(String(15), nullable=False)

    ext: Mapped[list['Ext']] = relationship('Ext', back_populates='org')


class Pri(db.Model):
    __tablename__ = 'pri'

    IDEPRI: Mapped[int] = mapped_column(INTEGER(2), primary_key=True)
    NOMPRI: Mapped[str] = mapped_column(String(25), nullable=False)

    ses: Mapped[list['Ses']] = relationship('Ses', back_populates='pri')


class Tec(db.Model):
    __tablename__ = 'tec'

    IDETEC: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    TIPTEC: Mapped[str] = mapped_column(String(80), nullable=False)
    NOMTEC: Mapped[str] = mapped_column(String(80), nullable=False)

    teccap: Mapped[list['Teccap']] = relationship('Teccap', back_populates='tec')


class Ten(db.Model):
    __tablename__ = 'ten'

    IDETEN: Mapped[int] = mapped_column(INTEGER(3), primary_key=True)
    NOMTEN: Mapped[str] = mapped_column(Text, nullable=False)
    INCTEN: Mapped[int] = mapped_column(INTEGER(3), nullable=False)

    rie: Mapped[list['Rie']] = relationship('Rie', secondary='inc', back_populates='ten')


class Top(db.Model):
    __tablename__ = 'top'

    IDETOP: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    NMTTOP: Mapped[str] = mapped_column(String(80), nullable=False)
    DESTOP: Mapped[str] = mapped_column(Text, nullable=False)

    tac: Mapped[list['Tac']] = relationship('Tac', back_populates='top')


class Tpo(db.Model):
    __tablename__ = 'tpo'

    IDETPO: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    NOMTPO: Mapped[str] = mapped_column(String(80), nullable=False)
    TCATPO: Mapped[str] = mapped_column(String(25), nullable=False)

    nor: Mapped[list['Nor']] = relationship('Nor', back_populates='tpo')


class Bib(db.Model):
    __tablename__ = 'bib'
    __table_args__ = (
        ForeignKeyConstraint(['BIBCAP'], ['cap.IDECAP'], name='FK_BIB'),
        Index('FK_BIB', 'BIBCAP')
    )

    IDEBIB: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    TDOCBIB: Mapped[str] = mapped_column(String(100), nullable=False)
    NDOCBIB: Mapped[str] = mapped_column(String(100), nullable=False)
    FDOCBIB: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    EDOCBIB: Mapped[str] = mapped_column(String(100), nullable=False)
    BIBCAP: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    cap: Mapped['Cap'] = relationship('Cap', back_populates='bib')


class Car(db.Model):
    __tablename__ = 'car'
    __table_args__ = (
        ForeignKeyConstraint(['COOCAR'], ['coo.IDECOO'], name='FK_CAR'),
        Index('FK_CAR', 'COOCAR')
    )

    IDECAR: Mapped[int] = mapped_column(INTEGER(2), primary_key=True)
    NOMCAR: Mapped[str] = mapped_column(String(40), nullable=False)
    COOCAR: Mapped[str] = mapped_column(String(3), nullable=False)
    CARCAR: Mapped[int] = mapped_column(INTEGER(1), nullable=False)
    ORGCAR: Mapped[Optional[str]] = mapped_column(String(30))

    coo: Mapped['Coo'] = relationship('Coo', back_populates='car')
    per: Mapped[list['Per']] = relationship('Per', back_populates='car')


class Ext(db.Model):
    __tablename__ = 'ext'
    __table_args__ = (
        ForeignKeyConstraint(['EXTCAP'], ['cap.IDECAP'], name='FK_EXT'),
        ForeignKeyConstraint(['EXTORG'], ['org.IDEORG'], name='FK2_EXT'),
        Index('FK2_EXT', 'EXTORG'),
        Index('FK_EXT', 'EXTCAP')
    )

    IDEEXT: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    APCEXT: Mapped[str] = mapped_column(String(15), nullable=False)
    AMCEXT: Mapped[str] = mapped_column(String(15), nullable=False)
    NMCEXT: Mapped[str] = mapped_column(String(20), nullable=False)
    TEMEXT: Mapped[str] = mapped_column(String(40), nullable=False)
    EXTCAP: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    EXTORG: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    cap: Mapped['Cap'] = relationship('Cap', back_populates='ext')
    org: Mapped['Org'] = relationship('Org', back_populates='ext')


class Nec(db.Model):
    __tablename__ = 'nec'
    __table_args__ = (
        ForeignKeyConstraint(['NECCAP'], ['cap.IDECAP'], ondelete='CASCADE', onupdate='CASCADE', name='FK_NEC'),
        Index('FK_NEC', 'NECCAP')
    )

    IDENEC: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    EDINEC: Mapped[str] = mapped_column(String(40), nullable=False)
    DOCNEC: Mapped[str] = mapped_column(String(40), nullable=False)
    NECCAP: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    cap: Mapped['Cap'] = relationship('Cap', back_populates='nec')


class Nor(db.Model):
    __tablename__ = 'nor'
    __table_args__ = (
        ForeignKeyConstraint(['NORTPO'], ['tpo.IDETPO'], ondelete='CASCADE', onupdate='CASCADE', name='FK_NOR'),
        Index('FK_NOR', 'NORTPO')
    )

    IDENOR: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    NOMNOR: Mapped[str] = mapped_column(Text, nullable=False)
    NORTPO: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    tpo: Mapped['Tpo'] = relationship('Tpo', back_populates='nor')


class Nro(db.Model):
    __tablename__ = 'nro'
    __table_args__ = (
        ForeignKeyConstraint(['NROCAP'], ['cap.IDECAP'], ondelete='CASCADE', onupdate='CASCADE', name='FK_NRO'),
        Index('FK_NRO', 'NROCAP')
    )

    IDENRO: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    NOMNRO: Mapped[str] = mapped_column(Text, nullable=False)
    NROCAP: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    cap: Mapped['Cap'] = relationship('Cap', back_populates='nro')


class Obj(db.Model):
    __tablename__ = 'obj'
    __table_args__ = (
        ForeignKeyConstraint(['OBJCAP'], ['cap.IDECAP'], ondelete='CASCADE', onupdate='CASCADE', name='FK_OBJ'),
        Index('FK_OBJ', 'OBJCAP')
    )

    IDEOBJ: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    TIPOBJ: Mapped[str] = mapped_column(String(40), nullable=False)
    OBJCAP: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    DESOBJ: Mapped[Optional[str]] = mapped_column(Text)

    cap: Mapped['Cap'] = relationship('Cap', back_populates='obj')


class Pub(db.Model):
    __tablename__ = 'pub'
    __table_args__ = (
        ForeignKeyConstraint(['MEDPUB'], ['med.IDEMED'], ondelete='CASCADE', name='FK_PUB'),
        Index('FK_PUB', 'MEDPUB')
    )

    IDEPUB: Mapped[int] = mapped_column(INTEGER(8), primary_key=True)
    FECPUB: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    NOMPUB: Mapped[str] = mapped_column(String(100), nullable=False)
    NOPPUB: Mapped[str] = mapped_column(String(50), nullable=False)
    MEDPUB: Mapped[int] = mapped_column(INTEGER(2), nullable=False)
    CONPUB: Mapped[Optional[str]] = mapped_column(Text)
    DOCPUB: Mapped[Optional[str]] = mapped_column(String(150))

    med: Mapped['Med'] = relationship('Med', back_populates='pub')
    vis: Mapped[list['Vis']] = relationship('Vis', back_populates='pub')


class Tac(db.Model):
    __tablename__ = 'tac'
    __table_args__ = (
        ForeignKeyConstraint(['TACTOP'], ['top.IDETOP'], name='FK_TAC'),
        Index('FK_TAC', 'TACTOP')
    )

    IDETAC: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    DESTAC: Mapped[str] = mapped_column(String(80), nullable=False)
    TACTOP: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    top: Mapped['Top'] = relationship('Top', back_populates='tac')
    ejm: Mapped[list['Ejm']] = relationship('Ejm', back_populates='tac')


class Teccap(db.Model):
    __tablename__ = 'teccap'
    __table_args__ = (
        ForeignKeyConstraint(['TECCAPCAP'], ['cap.IDECAP'], ondelete='CASCADE', onupdate='CASCADE', name='FK_TECCAP'),
        ForeignKeyConstraint(['TECCAPTEC'], ['tec.IDETEC'], ondelete='CASCADE', onupdate='CASCADE', name='FK2_TECCAP'),
        Index('FK2_TECCAP', 'TECCAPTEC'),
        Index('FK_TECCAP', 'TECCAPCAP')
    )

    IDETECCAP: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    TECCAPCAP: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    TECCAPTEC: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    cap: Mapped['Cap'] = relationship('Cap', back_populates='teccap')
    tec: Mapped['Tec'] = relationship('Tec', back_populates='teccap')


class Tem(db.Model):
    __tablename__ = 'tem'
    __table_args__ = (
        ForeignKeyConstraint(['TEMCAP'], ['cap.IDECAP'], ondelete='CASCADE', onupdate='CASCADE', name='FK_TEM'),
        Index('FK_TEM', 'TEMCAP')
    )

    IDETEM: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    TEMCAP: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    DESTEM: Mapped[Optional[str]] = mapped_column(Text)

    cap: Mapped['Cap'] = relationship('Cap', back_populates='tem')


class TemJc(db.Model):
    __tablename__ = 'tem_jc'
    __table_args__ = (
        ForeignKeyConstraint(['JUNTEM'], ['jun.IDEJUN'], ondelete='CASCADE', onupdate='CASCADE', name='FK_TEM_JC'),
        Index('FK_TEM_JC', 'JUNTEM')
    )

    IDETEM: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    DESTEM: Mapped[str] = mapped_column(Text, nullable=False)
    JUNTEM: Mapped[int] = mapped_column(INTEGER(4), nullable=False)

    jun: Mapped['Jun'] = relationship('Jun', back_populates='tem_jc')
    pro_jc: Mapped[list['ProJc']] = relationship('ProJc', back_populates='tem_jc')


class Ejm(db.Model):
    __tablename__ = 'ejm'
    __table_args__ = (
        ForeignKeyConstraint(['EJMTAC'], ['tac.IDETAC'], name='FK_EJM'),
        Index('FK_EJM', 'EJMTAC')
    )

    IDEEJM: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    DESEJM: Mapped[str] = mapped_column(Text, nullable=False)
    EJMTAC: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    tac: Mapped['Tac'] = relationship('Tac', back_populates='ejm')


class Per(db.Model):
    __tablename__ = 'per'
    __table_args__ = (
        ForeignKeyConstraint(['CARPER'], ['car.IDECAR'], ondelete='CASCADE', onupdate='CASCADE', name='FK2_PER'),
        ForeignKeyConstraint(['EMPPER'], ['emp.IDEEMP'], ondelete='CASCADE', onupdate='CASCADE', name='FK_PER'),
        Index('FK2_PER', 'CARPER'),
        Index('FK_PER', 'EMPPER')
    )

    IDEPER: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    EMPPER: Mapped[int] = mapped_column(INTEGER(3), nullable=False)
    CARPER: Mapped[int] = mapped_column(INTEGER(2), nullable=False)
    FECFIN: Mapped[Optional[datetime.date]] = mapped_column(Date)

    car: Mapped['Car'] = relationship('Car', back_populates='per')
    emp: Mapped['Emp'] = relationship('Emp', back_populates='per')
    pro_jc: Mapped[list['ProJc']] = relationship('ProJc', back_populates='per')
    rep: Mapped[list['Rep']] = relationship('Rep', back_populates='per')
    sugerencias: Mapped[list['Sugerencias']] = relationship('Sugerencias', back_populates='per')
    val: Mapped[list['Val']] = relationship('Val', back_populates='per')
    vis: Mapped[list['Vis']] = relationship('Vis', back_populates='per')
    pro: Mapped[list['Pro']] = relationship('Pro', back_populates='per')
    res: Mapped[list['Res']] = relationship('Res', back_populates='per')


class ProJc(db.Model):
    __tablename__ = 'pro_jc'
    __table_args__ = (
        ForeignKeyConstraint(['RESPRO'], ['per.IDEPER'], ondelete='CASCADE', onupdate='CASCADE', name='FK_PRO_JC'),
        ForeignKeyConstraint(['TEMPRO'], ['tem_jc.IDETEM'], ondelete='CASCADE', onupdate='CASCADE', name='FK_PRO_JC1'),
        Index('FK_PRO_JC', 'RESPRO'),
        Index('FK_PRO_JC1', 'TEMPRO')
    )

    IDEPRO: Mapped[int] = mapped_column(INTEGER(8), primary_key=True)
    DESPRO: Mapped[str] = mapped_column(Text, nullable=False)
    TIEPRO: Mapped[int] = mapped_column(INTEGER(3), nullable=False)
    ESTPRO: Mapped[str] = mapped_column(String(100), nullable=False)
    RESPRO: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    TEMPRO: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    per: Mapped['Per'] = relationship('Per', back_populates='pro_jc')
    tem_jc: Mapped['TemJc'] = relationship('TemJc', back_populates='pro_jc')


class Rep(db.Model):
    __tablename__ = 'rep'
    __table_args__ = (
        ForeignKeyConstraint(['LUGREP'], ['lug.IDELUG'], ondelete='CASCADE', onupdate='CASCADE', name='FK1_REP'),
        ForeignKeyConstraint(['PERREP'], ['per.IDEPER'], ondelete='CASCADE', onupdate='CASCADE', name='FK2_REP'),
        Index('FK1_REP', 'LUGREP'),
        Index('FK2_REP', 'PERREP')
    )

    IDEREP: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    CONREP: Mapped[int] = mapped_column(TINYINT(1), nullable=False)
    FECEVE: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    FECREP: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    FREREP: Mapped[str] = mapped_column(String(25), nullable=False)
    LUGREP: Mapped[int] = mapped_column(INTEGER(3), nullable=False)
    CANREP: Mapped[int] = mapped_column(INTEGER(1), nullable=False)
    PERREP: Mapped[int] = mapped_column(INTEGER(3), nullable=False)
    OBSREP: Mapped[Optional[str]] = mapped_column(String(300))

    lug: Mapped['Lug'] = relationship('Lug', back_populates='rep')
    per: Mapped['Per'] = relationship('Per', back_populates='rep')
    evi: Mapped[list['Evi']] = relationship('Evi', back_populates='rep')


class Ses(Per):
    __tablename__ = 'ses'
    __table_args__ = (
        ForeignKeyConstraint(['IDESES'], ['per.IDEPER'], ondelete='CASCADE', onupdate='CASCADE', name='FK2_SES'),
        ForeignKeyConstraint(['PRISES'], ['pri.IDEPRI'], ondelete='CASCADE', onupdate='CASCADE', name='FK_SES'),
        Index('FK2_SES', 'IDESES'),
        Index('FK_SES', 'PRISES')
    )

    IDESES: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    PRISES: Mapped[int] = mapped_column(INTEGER(2), nullable=False)
    PASSES: Mapped[str] = mapped_column(String(20), nullable=False)

    pri: Mapped['Pri'] = relationship('Pri', back_populates='ses')


class Sugerencias(db.Model):
    __tablename__ = 'sugerencias'
    __table_args__ = (
        ForeignKeyConstraint(['PERSUG'], ['per.IDEPER'], ondelete='CASCADE', onupdate='CASCADE', name='fk_sug'),
        Index('fk_sug', 'PERSUG')
    )

    IDESUG: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    DESSUG: Mapped[str] = mapped_column(Text, nullable=False)
    PERSUG: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    FECSUG: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    RESSUG: Mapped[Optional[str]] = mapped_column(Text)

    per: Mapped['Per'] = relationship('Per', back_populates='sugerencias')


class Val(db.Model):
    __tablename__ = 'val'
    __table_args__ = (
        ForeignKeyConstraint(['DIAVAL'], ['dia.IDEDIA'], ondelete='CASCADE', onupdate='CASCADE', name='FK2_VAL'),
        ForeignKeyConstraint(['PERVAL'], ['per.IDEPER'], ondelete='CASCADE', onupdate='CASCADE', name='FK_VAL'),
        Index('FK2_VAL', 'DIAVAL'),
        Index('FK_VAL', 'PERVAL')
    )

    IDEVAL: Mapped[int] = mapped_column(INTEGER(9), primary_key=True)
    PERVAL: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    DIAVAL: Mapped[int] = mapped_column(INTEGER(4), nullable=False)
    HORINI: Mapped[Optional[datetime.time]] = mapped_column(Time)
    FECVAL: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    CALVAL: Mapped[Optional[int]] = mapped_column(INTEGER(2))
    DIAEXT: Mapped[Optional[int]] = mapped_column(INTEGER(2))

    dia: Mapped['Dia'] = relationship('Dia', back_populates='val')
    per: Mapped['Per'] = relationship('Per', back_populates='val')


class Vis(db.Model):
    __tablename__ = 'vis'
    __table_args__ = (
        ForeignKeyConstraint(['EMCVIS'], ['per.IDEPER'], ondelete='CASCADE', name='FK1_VIS'),
        ForeignKeyConstraint(['PUBVIS'], ['pub.IDEPUB'], ondelete='CASCADE', name='FK_VIS'),
        Index('FK1_VIS', 'EMCVIS'),
        Index('FK_VIS', 'PUBVIS')
    )

    IDEVIS: Mapped[int] = mapped_column(INTEGER(12), primary_key=True)
    PUBVIS: Mapped[int] = mapped_column(INTEGER(8), nullable=False)
    EMCVIS: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    FECVIS: Mapped[Optional[datetime.date]] = mapped_column(Date)

    per: Mapped['Per'] = relationship('Per', back_populates='vis')
    pub: Mapped['Pub'] = relationship('Pub', back_populates='vis')


class Evi(db.Model):
    __tablename__ = 'evi'
    __table_args__ = (
        ForeignKeyConstraint(['REPEVI'], ['rep.IDEREP'], ondelete='CASCADE', onupdate='CASCADE', name='FK_EVI'),
        Index('FK_EVI', 'REPEVI')
    )

    IDEEVI: Mapped[int] = mapped_column(INTEGER(8), primary_key=True)
    NOMEVI: Mapped[str] = mapped_column(String(40), nullable=False)
    FILEVI: Mapped[str] = mapped_column(String(150), nullable=False)
    RUTEVI: Mapped[str] = mapped_column(String(150), nullable=False)
    TIPEVI: Mapped[str] = mapped_column(String(11), nullable=False)
    REPEVI: Mapped[int] = mapped_column(INTEGER(5), nullable=False)

    rep: Mapped['Rep'] = relationship('Rep', back_populates='evi')


class Pel(Rep):
    __tablename__ = 'pel'
    __table_args__ = (
        ForeignKeyConstraint(['REPPEL'], ['rep.IDEREP'], ondelete='CASCADE', onupdate='CASCADE', name='FK_PEL'),
    )

    REPPEL: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    FECPEL: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    OBJPEL: Mapped[str] = mapped_column(String(100), nullable=False)
    ACTPEL: Mapped[str] = mapped_column(String(100), nullable=False)
    CONPEL: Mapped[str] = mapped_column(String(100), nullable=False)
    CATEPEL: Mapped[str] = mapped_column(String(10), nullable=False)
    RIEOPEPEL: Mapped[str] = mapped_column(String(2), nullable=False)
    GENPEL: Mapped[str] = mapped_column(Text, nullable=False)
    METIDEPEL: Mapped[str] = mapped_column(String(10), nullable=False)
    NOMGESPEL: Mapped[str] = mapped_column(String(40), nullable=False)

    rie: Mapped[list['Rie']] = relationship('Rie', back_populates='pel')


class Mon(Pel):
    __tablename__ = 'mon'
    __table_args__ = (
        ForeignKeyConstraint(['PELMON'], ['pel.REPPEL'], ondelete='CASCADE', name='FK_MON'),
    )

    PELMON: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    DIFMON: Mapped[str] = mapped_column(Text, nullable=False)
    MITMON: Mapped[str] = mapped_column(Text, nullable=False)
    MSMMON: Mapped[Optional[str]] = mapped_column(Text)
    PSMMON: Mapped[Optional[str]] = mapped_column(Text)
    PSOMON: Mapped[Optional[str]] = mapped_column(Text)
    ESTMON: Mapped[Optional[str]] = mapped_column(String(9))
    FECCIE: Mapped[Optional[datetime.date]] = mapped_column(Date)


class Rie(db.Model):
    __tablename__ = 'rie'
    __table_args__ = (
        ForeignKeyConstraint(['PELRIE'], ['pel.REPPEL'], ondelete='CASCADE', name='FK_RIE'),
        Index('FK_RIE', 'PELRIE')
    )

    IDERIE: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    DESRIE: Mapped[str] = mapped_column(Text, nullable=False)
    CESPRIE: Mapped[str] = mapped_column(Text, nullable=False)
    CONRIE: Mapped[str] = mapped_column(Text, nullable=False)
    PROBRIE: Mapped[int] = mapped_column(INTEGER(1), nullable=False)
    GRARIE: Mapped[str] = mapped_column(String(1), nullable=False)
    PELRIE: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    PROREV: Mapped[Optional[int]] = mapped_column(INTEGER(1))
    GRAREV: Mapped[Optional[str]] = mapped_column(String(1))

    pel: Mapped['Pel'] = relationship('Pel', back_populates='rie')
    ten: Mapped[list['Ten']] = relationship('Ten', secondary='inc', back_populates='rie')
    cau: Mapped[list['Cau']] = relationship('Cau', back_populates='rie')
    pro: Mapped[list['Pro']] = relationship('Pro', back_populates='rie')


class Cau(db.Model):
    __tablename__ = 'cau'
    __table_args__ = (
        ForeignKeyConstraint(['iderie'], ['rie.IDERIE'], name='cau_ibfk_1'),
        Index('iderie', 'iderie')
    )

    idecau: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    nomcau: Mapped[Optional[str]] = mapped_column(String(255))
    descau: Mapped[Optional[str]] = mapped_column(Text)
    iderie: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    rie: Mapped[Optional['Rie']] = relationship('Rie', back_populates='cau')
    acc: Mapped[list['Acc']] = relationship('Acc', back_populates='cau')


t_inc = Table(
    'inc', db.Model.metadata,
    Column('RIEINC', INTEGER(5), primary_key=True),
    Column('TENINC', INTEGER(3), nullable=False),
    ForeignKeyConstraint(['RIEINC'], ['rie.IDERIE'], ondelete='CASCADE', onupdate='CASCADE', name='INC_IBFK_1'),
    ForeignKeyConstraint(['TENINC'], ['ten.IDETEN'], ondelete='CASCADE', onupdate='CASCADE', name='INC_IBFK_2'),
    Index('FK1_INC', 'TENINC'),
    Index('FK_INC', 'RIEINC')
)


class Pro(db.Model):
    __tablename__ = 'pro'
    __table_args__ = (
        ForeignKeyConstraint(['RESPRO'], ['per.IDEPER'], ondelete='CASCADE', onupdate='CASCADE', name='FK1_PRO'),
        ForeignKeyConstraint(['RIEPRO'], ['rie.IDERIE'], ondelete='CASCADE', onupdate='CASCADE', name='FK_PRO'),
        Index('FK1_PRO', 'RESPRO'),
        Index('FK_PRO', 'RIEPRO')
    )

    IDEPRO: Mapped[int] = mapped_column(INTEGER(8), primary_key=True)
    PRIPRO: Mapped[str] = mapped_column(Text, nullable=False)
    DESPRO: Mapped[str] = mapped_column(Text, nullable=False)
    RIEPRO: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    FINPRO: Mapped[Optional[datetime.date]] = mapped_column(Date)
    RESPRO: Mapped[Optional[int]] = mapped_column(INTEGER(5))
    NOTPRO: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ESTPRO: Mapped[Optional[str]] = mapped_column(String(50))

    per: Mapped[Optional['Per']] = relationship('Per', back_populates='pro')
    rie: Mapped['Rie'] = relationship('Rie', back_populates='pro')
    com: Mapped[list['Com']] = relationship('Com', back_populates='pro')
    res: Mapped[list['Res']] = relationship('Res', back_populates='pro')


class Acc(db.Model):
    __tablename__ = 'acc'
    __table_args__ = (
        ForeignKeyConstraint(['idecau'], ['cau.idecau'], name='acc_ibfk_1'),
        Index('idecau', 'idecau')
    )

    ideacc: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    nomacc: Mapped[Optional[str]] = mapped_column(String(255))
    desacc: Mapped[Optional[str]] = mapped_column(Text)
    fecacc: Mapped[Optional[datetime.date]] = mapped_column(Date)
    idecau: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    cau: Mapped[Optional['Cau']] = relationship('Cau', back_populates='acc')


class Com(db.Model):
    __tablename__ = 'com'
    __table_args__ = (
        ForeignKeyConstraint(['PROCOM'], ['pro.IDEPRO'], ondelete='CASCADE', name='FK_COM'),
        Index('FK_COM', 'PROCOM')
    )

    IDECOM: Mapped[int] = mapped_column(INTEGER(12), primary_key=True)
    PROCOM: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    FECCOM: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    NOMCOM: Mapped[str] = mapped_column(String(60), nullable=False)
    COMCOM: Mapped[Optional[str]] = mapped_column(Text)

    pro: Mapped['Pro'] = relationship('Pro', back_populates='com')


class Monpro(Pro):
    __tablename__ = 'monpro'
    __table_args__ = (
        ForeignKeyConstraint(['MONPRO'], ['pro.IDEPRO'], ondelete='CASCADE', name='FK_MONPRO'),
        Index('FK_MONPRO', 'MONPRO')
    )

    MONPRO: Mapped[int] = mapped_column(INTEGER(8), primary_key=True)
    MEDMON: Mapped[str] = mapped_column(String(254), nullable=False)
    ESTMON: Mapped[str] = mapped_column(String(40), nullable=False)
    DESEST: Mapped[str] = mapped_column(Text, nullable=False)
    FECMON: Mapped[Optional[datetime.date]] = mapped_column(Date)
    POREST: Mapped[Optional[int]] = mapped_column(INTEGER(3))

    cic: Mapped[list['Cic']] = relationship('Cic', back_populates='monpro')
    docmon: Mapped[list['Docmon']] = relationship('Docmon', back_populates='monpro')


class Res(db.Model):
    __tablename__ = 'res'
    __table_args__ = (
        ForeignKeyConstraint(['EMPRES'], ['per.IDEPER'], ondelete='CASCADE', name='FK1_RES'),
        ForeignKeyConstraint(['PRORES'], ['pro.IDEPRO'], ondelete='CASCADE', name='FK_RES'),
        Index('FK1_RES', 'EMPRES'),
        Index('FK_RES', 'PRORES')
    )

    IDERES: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    EMPRES: Mapped[int] = mapped_column(INTEGER(5), nullable=False)
    PRORES: Mapped[int] = mapped_column(INTEGER(8), nullable=False)
    FECNOT: Mapped[Optional[datetime.date]] = mapped_column(Date)
    FECLIM: Mapped[Optional[datetime.date]] = mapped_column(Date)

    per: Mapped['Per'] = relationship('Per', back_populates='res')
    pro: Mapped['Pro'] = relationship('Pro', back_populates='res')
    doc: Mapped[list['Doc']] = relationship('Doc', back_populates='res')


class Cic(db.Model):
    __tablename__ = 'cic'
    __table_args__ = (
        ForeignKeyConstraint(['MONCIC'], ['monpro.MONPRO'], ondelete='CASCADE', onupdate='CASCADE', name='FK_CIC'),
        Index('FK_CIC', 'MONCIC')
    )

    IDECIC: Mapped[int] = mapped_column(INTEGER(5), primary_key=True)
    CAUCIC: Mapped[str] = mapped_column(Text, nullable=False)
    OBJCIC: Mapped[str] = mapped_column(Text, nullable=False)
    PLACIC: Mapped[str] = mapped_column(Text, nullable=False)
    VERCIC: Mapped[str] = mapped_column(Text, nullable=False)
    LOGCIC: Mapped[str] = mapped_column(String(2), nullable=False)
    ACTCIC: Mapped[str] = mapped_column(Text, nullable=False)
    MONCIC: Mapped[int] = mapped_column(INTEGER(8), nullable=False)
    FECINI: Mapped[Optional[datetime.date]] = mapped_column(Date)
    FECENT: Mapped[Optional[datetime.date]] = mapped_column(Date)

    monpro: Mapped['Monpro'] = relationship('Monpro', back_populates='cic')


class Doc(db.Model):
    __tablename__ = 'doc'
    __table_args__ = (
        ForeignKeyConstraint(['RESDOC'], ['res.IDERES'], ondelete='CASCADE', name='FK_DOC'),
        Index('FK_DOC', 'RESDOC')
    )

    IDEDOC: Mapped[int] = mapped_column(INTEGER(12), primary_key=True)
    RESDOC: Mapped[int] = mapped_column(INTEGER(8), nullable=False)
    NOMDOC: Mapped[str] = mapped_column(String(250), nullable=False)
    DIRDOC: Mapped[str] = mapped_column(String(250), nullable=False)
    FECDOC: Mapped[Optional[datetime.date]] = mapped_column(Date)
    VERDOC: Mapped[Optional[str]] = mapped_column(String(250))
    FECVERDOC: Mapped[Optional[datetime.date]] = mapped_column(Date)

    res: Mapped['Res'] = relationship('Res', back_populates='doc')


class Docmon(db.Model):
    __tablename__ = 'docmon'
    __table_args__ = (
        ForeignKeyConstraint(['MONDOC'], ['monpro.MONPRO'], ondelete='CASCADE', name='FK_DOCMON'),
        Index('FK_DOCMON', 'MONDOC')
    )

    IDEDOC: Mapped[int] = mapped_column(INTEGER(12), primary_key=True)
    MONDOC: Mapped[int] = mapped_column(INTEGER(8), nullable=False)
    NOMDOC: Mapped[str] = mapped_column(String(250), nullable=False)
    DIRDOC: Mapped[str] = mapped_column(String(250), nullable=False)
    FECDOC: Mapped[Optional[datetime.date]] = mapped_column(Date)

    monpro: Mapped['Monpro'] = relationship('Monpro', back_populates='docmon')


