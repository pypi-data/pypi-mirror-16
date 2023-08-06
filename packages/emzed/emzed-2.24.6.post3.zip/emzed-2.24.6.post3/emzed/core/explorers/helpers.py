import datetime
import functools
import new

from PyQt4.Qwt5 import QwtScaleDraw, QwtText

def widthOfTableWidget(tw):

    width = 0
    for i in range(tw.columnCount()):
        width += tw.columnWidth(i)

    width += tw.verticalHeader().sizeHint().width()
    width += tw.verticalScrollBar().sizeHint().width()
    width += tw.frameWidth()*2
    return width


def protect_signal_handler(fun):
    @functools.wraps(fun)
    def wrapped(*a, **kw):
        try:
            return fun(*a, **kw)
        except:
            import traceback
            traceback.print_exc()
    return wrapped


def formatSeconds(seconds):
    return "%.2fm" % (seconds / 60.0)


def set_rt_formatting_on_x_axis(plot):
    def label(self, v):
        return QwtText(formatSeconds(v))
    a = QwtScaleDraw()
    a.label = new.instancemethod(label, plot, QwtScaleDraw)
    plot.setAxisScaleDraw(plot.xBottom, a)


def set_datetime_formating_on_x_axis(plot):
    def label(self, float_val):
        if float_val < 1.0:
            return QwtText("")
        dt = datetime.datetime.fromordinal(int(float_val))
        txt = str(dt).split(" ")[0]
        return QwtText(txt)
    a = QwtScaleDraw()
    a.label = new.instancemethod(label, plot, QwtScaleDraw)
    plot.setAxisScaleDraw(plot.xBottom, a)
