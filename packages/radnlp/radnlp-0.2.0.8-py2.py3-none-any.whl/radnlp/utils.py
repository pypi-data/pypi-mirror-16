import pyConTextNLP.pyConTextGraph as pyConText
import networkx as nx

def modifies(g, n, modifiers):
    """
    Tests whether any of the modifiers of node n are in
    any of the categories listed in 'modifiers'
    """
    pred = g.predecessors(n)
    if not pred:
        return False
    pcats = []
    for p in pred:
        pcats.extend(p.getCategory())
    return bool(set(pcats).intersection([m.lower() for m in modifiers]))


def matched_modifiers(g, n, modifiers):
    """
    returns the set of predecessors of node 'n' that are of a
    category contained in 'modifiers'
    """
    pred = g.predecessors(n)
    if not pred:
        return False
    pcats = []
    for p in pred:
        pcats.extend(p.getCategory())

    return set(pcats).intersection([m.lower() for m in modifiers])


def return_matched_modifiers(g, n, modifiers):
    """
    """
    pred = g.predecessors(n)
    if not pred:
        return []
    mods = [m.lower() for m in modifiers]
    mmods = [p for p in pred if p.isA(mods)]
    return mmods


def markup_sentence(s, modifiers, targets):
    """
    """
    markup = pyConText.ConTextMarkup()
    markup.setRawText(s)
    markup.cleanText()
    markup.markItems(modifiers, mode="modifier")
    markup.markItems(targets, mode="target")
    markup.pruneMarks()
    markup.dropMarks('Exclusion')
    # apply modifiers to any targets within the modifiers scope
    markup.applyModifiers()
    markup.pruneSelfModifyingRelationships()
    markup.dropInactiveModifiers()
    return markup

def _merge_markups(rmarkups):
    if rmarkups:
        raw_text = " ".join([r.graph["__rawTxt"] for r in rmarkups])
        text = " ".join([r.graph["__txt"] for r in rmarkups])
        newgraph = nx.compose_all(rmarkups)
        newgraph.graph["__rawTxt"] = raw_text
        newgraph.graph["__txt"] = text
        return newgraph
    else:
        return nx.DiGraph()
def mark_report(report, modifiers, targets):
    context = pyConText.ConTextDocument()
    for m in [markup_sentence(s,
                              modifiers,
                              targets) for s in report]:
        context.addMarkup(m)
    return context
    # return _merge_markups([markup_sentence(s,
    #                                       modifiers,
    #                                       targets) for s in report])


def get_severity(g, t, severity_rule):
    """
    """
    if not t.isA(severity_rule[0]):
        return []
    smods = return_matched_modifiers(g, t, severity_rule[1])
    if smods:
        severity_results = []
        for m in smods:
            mgd = m.getMatchedGroupDictionary()
            val = mgd.get('value')
            units = mgd.get('unit')
            phrase = m.getPhrase()
        severity_results.append((phrase, val, units))
        return severity_results
    else:
        return []


def anatomy_recategorize(g, t, category_rule):
    """
    create a new category based on category_rule
    g: a graph containing a markup
    t: a target (???)
    category_rule: the rule to apply for the recateogrization

    """
    if not t.isA(category_rule[0]):
        return

    mods = g.predecessors(t)

    if mods:
        mmods = matched_modifiers(g, t, category_rule[1])
        if mmods:
            new_category = []
            for m in mmods:
                nc = "_".join((m.lower(), category_rule[0]))
                new_category.append(nc)
            t.replaceCategory(category_rule[0], new_category)


def generic_classifier(g, t, rule):
    """
    based on the modifiers of the target 't' and the provide rule
    in 'rule' classify the target node
    """
    mods = g.predecessors(t)
    if not mods:
        return rule["DEFAULT"]
    for r in rule["RULES"]:
        if modifies(g, t, r[1]):
            return r[0]
    return rule["DEFAULT"]

def process_report(report, modifier, target,
                   classification_rules,
                   category_rules,
                   _schema,
                   **kwargs):
    """
    """
    markup = mark_report(split.get_sentences(report),
                         modifier,
                         target)
    return  classify_document_targets(markup,
                                          classification_rules,
                                          category_rules,
                                          severity_rules,
                                          _schema,
                                          kwargs)
