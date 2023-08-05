from dateutil.parser import parse as parse_timestamp
from .utils import ElementTree


def node_for_tagname(tag):
	for k, v in globals().items():
		if k.endswith("Node") and v.tagname == tag:
			return v


class Node(object):
	attributes = ()
	tagname = None

	def __init__(self, *args):
		self._attributes = {}
		self.nodes = []
		for k, arg in zip(("ts", ) + self.attributes, args):
			setattr(self, k, arg)

	def __repr__(self):
		return "<%s>" % (self.__class__.__name__)

	@classmethod
	def from_xml(cls, xml):
		if xml.tag != cls.tagname:
			raise ValueError("%s.from_xml() called with %r, not %r" % (
				cls.__name__, xml.tag, cls.tagname
			))
		ts = xml.attrib.get("ts")
		if ts:
			ts = parse_timestamp(ts)
		ret = cls(ts)
		for element in xml:
			ecls = node_for_tagname(element.tag)
			node = ecls.from_xml(element)
			for attrname in ecls.attributes:
				setattr(node, attrname, element.attrib.get(attrname))
			ret.nodes.append(node)
		return ret

	def append(self, node):
		self.nodes.append(node)

	def xml(self):
		element = ElementTree.Element(self.tagname)
		for node in self.nodes:
			element.append(node.xml())
		for attr in self.attributes:
			attrib = getattr(self, attr, None)
			if attrib is not None:
				if isinstance(attrib, bool):
					attrib = str(attrib).lower()
				elif isinstance(attrib, int):
					# Check for enums
					attrib = str(int(attrib))
				element.attrib[attr] = attrib
		if self.timestamp and self.ts:
			element.attrib["ts"] = self.ts.isoformat()

		for k, v in self._attributes.items():
			element.attrib[k] = v

		return element


class GameNode(Node):
	tagname = "Game"
	attributes = ("id", "reconnecting")
	timestamp = True

	@property
	def players(self):
		return self.nodes[1:3]


class GameEntityNode(Node):
	tagname = "GameEntity"
	attributes = ("id", )
	timestamp = False


class PlayerNode(Node):
	tagname = "Player"
	attributes = (
		"id", "playerID", "accountHi", "accountLo", "name",
		"rank", "legendRank", "cardback"
	)
	timestamp = False

	def xml(self):
		ret = super(PlayerNode, self).xml()
		deck = getattr(self, "deck", None)
		if deck is not None:
			element = ElementTree.Element("Deck")
			ret.append(element)
			for card in deck:
				e = ElementTree.Element("Card")
				e.attrib["id"] = card
				element.append(e)

		return ret


class FullEntityNode(Node):
	tagname = "FullEntity"
	attributes = ("id", "cardID")
	timestamp = False


class ShowEntityNode(Node):
	tagname = "ShowEntity"
	attributes = ("entity", "cardID")
	timestamp = False


class BlockNode(Node):
	tagname = "Block"
	attributes = ("entity", "type", "index", "target")
	timestamp = True


class MetaDataNode(Node):
	tagname = "MetaData"
	attributes = ("meta", "data", "info")
	timestamp = False


class MetaDataInfoNode(Node):
	tagname = "Info"
	attributes = ("index", "entity")
	timestamp = False


class TagNode(Node):
	tagname = "Tag"
	attributes = ("tag", "value")
	timestamp = False


class TagChangeNode(Node):
	tagname = "TagChange"
	attributes = ("entity", "tag", "value")
	timestamp = False


class HideEntityNode(Node):
	tagname = "HideEntity"
	attributes = ("entity", "zone")
	timestamp = True


class ChangeEntityNode(Node):
	tagname = "ChangeEntity"
	attributes = ("entity", "cardID")
	timestamp = True


##
# Choices

class ChoicesNode(Node):
	tagname = "Choices"
	attributes = ("entity", "id", "taskList", "type", "min", "max", "source")
	timestamp = True


class ChoiceNode(Node):
	tagname = "Choice"
	attributes = ("index", "entity")
	timestamp = False


class ChosenEntitiesNode(Node):
	tagname = "ChosenEntities"
	attributes = ("entity", "id")
	timestamp = True


class SendChoicesNode(Node):
	tagname = "SendChoices"
	attributes = ("id", "type")
	timestamp = True


##
# Options

class OptionsNode(Node):
	tagname = "Options"
	attributes = ("id", )
	timestamp = True


class OptionNode(Node):
	tagname = "Option"
	attributes = ("index", "entity", "type")
	timestamp = False


class SubOptionNode(Node):
	tagname = "SubOption"
	attributes = ("index", "entity")
	timestamp = False


class OptionTargetNode(Node):
	tagname = "Target"
	attributes = ("index", "entity")
	timestamp = False


class SendOptionNode(Node):
	tagname = "SendOption"
	attributes = ("option", "subOption", "target", "position")
	timestamp = True
