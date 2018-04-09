import * as React from 'react';
import * as Hammer from 'hammerjs';

export interface ImageGalleryState {
  current: string;
  length: number;
  images: Array<string>;
  show: boolean;
}

export const ImageGallery = (WrappedComponent: React.ComponentType) =>
    class WrapperComponent extends React.Component<{}, ImageGalleryState> {
      private selector: HTMLDivElement;
      private imgSrcAttr: string;
      private imageContainer: HTMLImageElement;
      private hammer: HammerManager;

      constructor(props: {}) {
        super(props);
        this.state = {
          length: 0,
          current: '',
          images: [],
          show: false,
        };
        this.setSelector = this.setSelector.bind(this);
        this.handleClose = this.handleClose.bind(this);
        this.prev = this.prev.bind(this);
        this.next = this.next.bind(this);
      }

      componentDidMount() {
        this.hammer = new Hammer(this.imageContainer);
        this.hammer.on('swipeleft', this.next);
        this.hammer.on('swiperight', this.prev);
        document.addEventListener('keydown', this.keyEvent.bind(this), false);
      }

      setSelector(selector: HTMLDivElement, attr: string) {
        this.selector = selector;
        this.imgSrcAttr = attr;
        if (selector) {
          this.getImages();
        }
      }

      handleClose() {
        this.setState({show: false});
      }

      keyEvent(event: React.KeyboardEvent<HTMLDivElement>) {
        if (event.key === 'Escape') {
          this.handleClose();
        } else if (event.key === 'ArrowLeft') {
          this.prev();
        } else if (event.key === 'ArrowRight') {
          this.next();
        }
      }

      next() {
        const length = this.state.length;
        if (length < 2) {
          return;
        }
        const index = this.state.images.indexOf(this.state.current);
        const current = this.state.images[(index + 1) % length];
        this.setState({current});
      }

      prev() {
        const length = this.state.length;
        if (length < 2) {
          return;
        }
        const index = this.state.images.indexOf(this.state.current);
        let nextIndex = index - 1;
        if (nextIndex < 0) {
          nextIndex = length - 1;
        }
        const current = this.state.images[nextIndex];
        this.setState({current});
      }

      getImages() {
        var images = [];
        const img = this.selector.getElementsByTagName('img');
        for (var i = 0; i < img.length; i++) {
          images.push(img[i].getAttribute(this.imgSrcAttr) || '');

          img[i].onclick = (e) => {  // handle image click
            const target = e.srcElement as HTMLElement;
            this.setState({
              show: true,
              current: target.getAttribute(this.imgSrcAttr) || '',
            });
          };
        }
        this.setState({
          images,
          length: images.length,
        });
      }

      render() {
        const props = Object.assign(
          {}, this.props, {setSelector: this.setSelector}
        );
        return (
          <>
          <div
            className="ig-model"
            style={{display: this.state.show ? 'block' : 'none'}}
          >
            <div className="ig-bg" onClick={this.handleClose} />
            <div className="ig-content">
              <img
                src={this.state.current}
                alt=""
                ref={ref => this.imageContainer = ref as HTMLImageElement}
                // onClick={this.next}
              />
              <p>
                {this.state.images.indexOf(this.state.current) + 1} / {this.state.length}
              </p>
              <a className="origin" href={this.state.current} target="_blank">查看原图</a>
            </div>
          </div>
          <WrappedComponent {...props} />
          </>
        );
      }
    };
