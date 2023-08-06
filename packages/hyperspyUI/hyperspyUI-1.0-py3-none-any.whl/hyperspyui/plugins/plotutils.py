from hyperspyui.plugins.plugin import Plugin

from hyperspy.utils.plot import plot_images, plot_spectra


class PlotUtils(Plugin):
    name = "Plot utils"

    def create_actions(self):
        self.add_action(self.name + '.plot_images', "Plot images",
                        self.plot_images,
                        tip="Plots several images together in one figure.")
        self.add_action(self.name + '.plot_spectra', "Plot spectra",
                        self.plot_spectra,
                        tip="Plots several spectra together in one figure.")

    def create_menu(self):
        self.add_menuitem('Image',
                          self.ui.actions[self.name + '.plot_images'])
        self.add_menuitem('Spectrum',
                          self.ui.actions[self.name + '.plot_spectra'])

    def plot_images(self, images=None):
        if images is None:
            images = self.ui.get_selected_signals()
        plot_images(images, colorbar=None, axes_decor=None)

    def plot_spectra(self, spectra=None):
        if spectra is None:
            spectra = self.ui.get_selected_signals()
            if len(spectra) == 1:
                spectra = spectra[0]

        plot_spectra(spectra)
