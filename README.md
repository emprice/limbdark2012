Limb darkening coefficients from stellar atmosphere models
==========================================================

This small package contains a script for processing the limb darkening
parameter tables produced by Claret et al. (2012) using the PHOENIX/1D
stellar atmosphere models. The tables and associated publications are
available at the links below. **Please note that I have not modified the data
in any way and it does not belong to me. The script simply parses and
stores the data in a binary (HDF5) format for easier use.**

[Paper I tables](https://cdsarc.u-strasbg.fr/ftp/J/A+A/546/A14/)
[Paper II tables](https://cdsarc.u-strasbg.fr/ftp/J/A+A/552/A16/)

```bib
@ARTICLE{2012A&A...546A..14C,
       author = {{Claret}, A. and {Hauschildt}, P.~H. and {Witte}, S.},
        title = "{New limb-darkening coefficients for PHOENIX/1D model atmospheres. I. Calculations for 1500 K {\ensuremath{\leq}} T$_{eff}$ {\ensuremath{\leq}} 4800 K Kepler, CoRot, Spitzer, uvby, UBVRIJHK, Sloan, and 2MASS photometric systems}",
      journal = {\aap},
     keywords = {stars: atmospheres, binaries: eclipsing, brown dwarfs, planetary systems, stars: late-type},
         year = 2012,
        month = oct,
       volume = {546},
          eid = {A14},
        pages = {A14},
          doi = {10.1051/0004-6361/201219849},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2012A&A...546A..14C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2013A&A...552A..16C,
       author = {{Claret}, A. and {Hauschildt}, P.~H. and {Witte}, S.},
        title = "{New limb-darkening coefficients for Phoenix/1d model atmospheres. II. Calculations for 5000 K {\ensuremath{\leq}} T$_{eff}$ {\ensuremath{\leq}} 10 000 K Kepler, CoRot, Spitzer, uvby, UBVRIJHK, Sloan, and 2MASS photometric systems}",
      journal = {\aap},
     keywords = {stars: atmospheres, binaries: eclipsing, planetary systems},
         year = 2013,
        month = apr,
       volume = {552},
          eid = {A16},
        pages = {A16},
          doi = {10.1051/0004-6361/201220942},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2013A&A...552A..16C},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@dataset{vizier:J/A+A/546/A14,
  author={Claret A., Hauschildt P.H., Witte S.},
  title = {Limb-darkening for CoRoT, Kepler, Spitzer},
  year={2012},
  publisher = { Centre de Donnees astronomique de Strasbourg (CDS) },
  version = { Version 26-Jun-2017 (last modified) },
  doi = {https://doi.org/10.26093/cds/vizier.35460014}
}

@dataset{vizier:J/A+A/552/A16,
  author={Claret, A., Hauschildt, P.H., Witte, S.},
  title = {Limb-darkening for CoRoT, Kepler, Spitzer. II.},
  year={2013},
  publisher = { Centre de Donnees astronomique de Strasbourg (CDS) },
  version = { Version 30-Jun-2017 (last modified) },
  doi = {https://doi.org/10.26093/cds/vizier.35520016}
}

@MISC{vizier,
  author = { Ochsenbein F. et. al},
  title = "{ The VizieR database of astronomical catalogues }",
  publisher = "{ Centre de Donnees astronomique de Strasbourg (CDS) }",
  doi = {https://doi.org/10.26093/cds/vizier}
}
```

This research has made use of the VizieR catalogue access tool, CDS,
Strasbourg, France (DOI : 10.26093/cds/vizier). The original description
of the VizieR service was published in 2000, A&AS 143, 23

<!-- vim: set ft=markdown: -->
